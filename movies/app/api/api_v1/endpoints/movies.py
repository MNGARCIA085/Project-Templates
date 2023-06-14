from fastapi import  APIRouter,Depends
from sqlalchemy.orm import Session
from api.deps import get_db
from crud import crud_movies
from schemas.movie import Movie,MovieCreate


router = APIRouter(
    prefix="/movies",
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=Movie)
def create_movie(movie: MovieCreate, db: Session = Depends(get_db)):
    return crud_movies.create_movie(db=db, movie=movie)


@router.get("/", response_model=list[Movie])
def read_movies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    movies = crud_movies.get_movies(db, skip=skip, limit=limit)
    return movies