from pydantic import BaseModel, Field
from .answer import Answer
from typing import List


class QuestionBase(BaseModel):
    category_id: int = Field(...)
    question: str = Field(...)


class Question(QuestionBase):
    id: int = Field(...)

    @staticmethod
    def parse(db_question):
        return Question.parse_obj(db_question.__dict__)

    @staticmethod
    def parse_all(db_questions):
        measurements = []
        for db_question in db_questions:
            measurements.append(Question.parse(db_question))

        return measurements

    @staticmethod
    def from_base(_id: int, base: QuestionBase):
        d = base.dict()
        d['id'] = _id
        return Question.parse_obj(d)


class SuperQuestion(QuestionBase):
    id: int = Field(...)
    answers: List[Answer] = []
    is_category_description: bool = False
    is_multiple_choice: bool = False
    category: str = ""

    class Config:
        orm_mode = True

    @staticmethod
    def parse(db_question):
        return Question.parse_obj(db_question.__dict__)

    @staticmethod
    def parse_all(db_questions):
        measurements = []
        for db_question in db_questions:
            measurements.append(Question.parse(db_question))

        return measurements
