from fastapi import APIRouter

router = APIRouter(tags=['Likes Router'], prefix="/likes")


@router.post("/")
def create():
    pass


@router.get("/")
def get_all():
    pass


@router.get("/{id}")
def get(id: int):
    pass



@router.put("/{id}")
def get(id: int):
    pass


@router.delete("/{id}")
def get(id: int):
    pass







