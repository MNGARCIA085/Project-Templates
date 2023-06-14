from sqlalchemy.orm import Session
from schemas.movie import MovieCreate
from models import movies



def get_movies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(movies.Movie).offset(skip).limit(limit).all()


def create_movie(db: Session, movie: MovieCreate):
    db_user = movies.Movie(title=movie.title, description=movie.description)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user









