from fastapi import APIRouter, Depends, status
from app.services import universities as service
from app.dto import universities as schema
from sqlalchemy.orm import Session
from app.configs.db_config import get_db
from app import _http

router = APIRouter(tags=['University Router'], prefix="/universities")


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(dto: schema.UniversityCreateDto, db: Session = Depends(get_db)):
    return service.create(dto, db)


@router.get("/")
def get_all(db: Session = Depends(get_db)):
    return service.get_all(db)


@router.get("/{id}", response_model=schema.UniversityDto, responses=_http.get_university)
def get(id: int, db: Session = Depends(get_db)):
    return service.get(id, db)


@router.put("/")
def update(dto: schema.UniversityUpdateDto, db: Session = Depends(get_db)):
    return service.update(dto, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def get(id: int, db: Session = Depends(get_db)):
    return service.delete(id, db)
