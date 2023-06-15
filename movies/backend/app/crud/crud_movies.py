from sqlalchemy.orm import Session
from schemas.movie import MovieCreate
from models import movies



def get_movies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(movies.Movie).offset(skip).limit(limit).all()


def create_movie(db: Session, movie: MovieCreate):
    db_movie = movies.Movie(title=movie.title, description=movie.description)
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie









