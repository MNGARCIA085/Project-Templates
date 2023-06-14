from fastapi import  APIRouter,Depends

router = APIRouter(
    prefix="/prueba",
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def read_users_me():
    return {'bla':7}




from sqlalchemy.orm import Session

from .deps import get_db

from . import schemas,crud


@router.post("/movies/", response_model=schemas.Movie)
def create_user(movie: schemas.MovieCreate, db: Session = Depends(get_db)):
    crud.create_movie(db=db, movie=movie)


@router.get("/movies/", response_model=list[schemas.Movie])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_movies(db, skip=skip, limit=limit)
    return users