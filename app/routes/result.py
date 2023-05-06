from sqlalchemy.orm import Session
from ..models import Resultaten as ModelResult
from ..schemas.result import Result as SchemaResult
from ..schemas.result import SuperResult as SchemaSuperResult
from fastapi import APIRouter
from fastapi import Depends
from ..database import get_db

results_router = APIRouter()


@results_router.post('/', response_model=SchemaSuperResult,
                     tags=['result'])
async def add_result(result: SchemaResult, db: Session = Depends(get_db)):
    db_result = ModelResult(**result.dict())

    db.add(db_result)
    db.commit()
    db.refresh(db_result)

    return SchemaSuperResult.parse_obj(db_result.__dict__)
