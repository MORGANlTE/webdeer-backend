from sqlalchemy.orm import Session
from ..models import Question as ModelQuestion
from ..models import Category as ModelCategory
from ..models import Antwoord as ModelAnswer
from ..schemas.question import QuestionBase as SchemaQuestionBase
from ..schemas.answer import IdkAnswer
from ..schemas.question import SuperQuestion as SchemaQuestion
from fastapi import APIRouter, HTTPException
from fastapi import Depends
from ..database import get_db
import random

question_router = APIRouter()


@question_router.get('/', response_model=list,
                     tags=['question'])
async def get_all_questions(db: Session = Depends(get_db)):

    db_q = db.query(ModelQuestion).all()
    db_categories = db.query(ModelCategory).all()
    returnwaarde = []
    for cat in db_categories:

        # Select all questions from this category
        db_questions = db.query(ModelQuestion).filter_by(
            category_id=cat.id).all()

        # Randomly select 5 questions from the list
        if len(db_questions) > 5:
            selected_questions = random.sample(db_questions, 5)
        else:
            selected_questions = db_questions

        # Convert the database objects to schema objects
        schema_questions = [SchemaQuestion.from_orm(
            q) for q in selected_questions]

        # Create a new list of questions for each category
        category_questions = []
        category_questions.extend(schema_questions)

        # Add the category description as a question

        for question in category_questions:
            db_answers = db.query(ModelAnswer.text, ModelAnswer.img_url, ModelAnswer.correct).filter_by(
                question_id=question.id).all()
            idk_answers = [{"text": text, "imgUrl": img_url, "correct": correct}
                           for text, img_url, correct in db_answers]
            question.answers = idk_answers
            if len(idk_answers) > 3:
                question.is_multiple_choice = True
            question.category = cat.name

        category_questions.insert(0,
                                  SchemaQuestion(
                                      category=cat.name,
                                      category_id=cat.id,
                                      question=cat.desc,
                                      id=0,
                                      is_category_description=True
                                  )
                                  )
        returnwaarde.append(category_questions)

    return returnwaarde
