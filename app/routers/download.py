from sqlalchemy.orm import Session
from fastapi import status, Depends

from app.configs.db_config import get_db
from app.entity.entities import Uploads
from app.utils import UPLOADS_DIR
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

router = APIRouter(tags=['File download'], prefix="/download")


def get(id: int, db: Session):
    upload = db.query(Uploads).filter(Uploads.id == id).first()
    if not upload:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"File not found with id : '{id}'")
    return FileResponse(f"{UPLOADS_DIR}/{upload.generated_name}", media_type=upload.content_type,
                        filename=upload.original_name)


@router.get('/{id}')
async def download_file(id: int, db: Session = Depends(get_db)):
    return get(id=id, db=db)
