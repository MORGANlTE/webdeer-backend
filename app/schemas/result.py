from pydantic import BaseModel, Field


class Result(BaseModel):
    # id: int = Field(...)
    score: int = Field(...)
    total_score: int = Field(...)
    level_estimate: int = Field(...)
    level: int = Field(...)

    @staticmethod
    def parse(db_result):
        return Result.parse_obj(db_result.__dict__)

    @staticmethod
    def parse_all(db_results):
        res = []
        for db_result in db_results:
            res.append(Result.parse(db_result))

        return res


class SuperResult(Result):
    id: int = Field(...)

    @staticmethod
    def parse(db_result):
        return SuperResult.parse_obj(db_result.__dict__)

    @staticmethod
    def parse_all(db_results):
        res = []
        for db_result in db_results:
            res.append(Result.parse(db_result))

        return res
