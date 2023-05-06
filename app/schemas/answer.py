from pydantic import BaseModel, Field
from typing import Optional


class AnswerBase(BaseModel):
    question_id: int = Field(...)
    img_url: Optional[str] = Field(...)
    text: str = Field(...)
    correct: bool = Field(...)


class Answer(AnswerBase):
    id: int = Field(...)

    @staticmethod
    def parse(db_answer):
        return Answer.parse_obj(db_answer.__dict__)

    @staticmethod
    def parse_all(db_answers):
        answers = []
        for db_answer in db_answers:
            answers.append(Answer.parse(db_answer))

        return answers

    @staticmethod
    def from_base(_id: int, base: AnswerBase):
        d = base.dict()
        d['id'] = _id
        return Answer.parse_obj(d)


class IdkAnswer:
    def __init__(self, text, url):
        self.text = text
        self.imgUrl = url
