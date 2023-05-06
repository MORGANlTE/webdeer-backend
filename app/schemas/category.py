from typing import Optional, List

from pydantic import BaseModel, Field


class CategoryBase(BaseModel):
    name: str = Field(...)
    desc: str = Field(...)


class Category(CategoryBase):
    id: int = Field(...)

    @staticmethod
    def parse(db_category):
        return Category.parse_obj(db_category.__dict__)

    @staticmethod
    def parse_all(db_categorys):
        categories = []
        for db_category in db_categorys:
            categories.append(Category.parse(db_category))

        return categories

    @staticmethod
    def from_base(_id: int, base: CategoryBase):
        d = base.dict()
        d['id'] = _id
        return Category.parse_obj(d)
