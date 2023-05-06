from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey, Integer, DateTime
from datetime import datetime
from sqlalchemy.sql import func

Base = declarative_base()


class Category(Base):
    __tablename__ = 'category'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    desc: Mapped[str] = mapped_column(nullable=False)


class Resultaten(Base):
    __tablename__ = 'result'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    score: Mapped[int] = mapped_column(nullable=False)
    total_score: Mapped[int] = mapped_column(nullable=False)
    level_estimate: Mapped[int] = mapped_column(nullable=False)
    level: Mapped[int] = mapped_column(nullable=False)
    time_created: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now())


class Question(Base):
    __tablename__ = 'question'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    category_id: Mapped[int] = mapped_column(ForeignKey(
        'category.id', ondelete='CASCADE'))
    question: Mapped[str] = mapped_column(nullable=False)


class Antwoord(Base):
    __tablename__ = 'answer'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    question_id: Mapped[int] = mapped_column(ForeignKey(
        'question.id', ondelete='CASCADE'))
    img_url: Mapped[str] = mapped_column(nullable=True)
    text: Mapped[str] = mapped_column(nullable=False)
    correct: Mapped[bool] = mapped_column(nullable=False)
