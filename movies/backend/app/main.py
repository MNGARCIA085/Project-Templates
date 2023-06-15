from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from api.api_v1.api import api_router


app = FastAPI()



origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



router = APIRouter()

app.include_router(api_router, prefix='/API')




"""

#models.Base.metadata.create_all(bind=engine); migrar sin usar alembic (en main)


alembic.ini
sqlalchemy.url = "sqlite:///./sql_app.db"


.env de alembic:

config.set_main_option("sqlalchemy.url", "sqlite:///./sql_app.db")
from db.base import Base  # noqa
target_metadata = Base.metadata




migraciones

alembic revision --autogenerate -m "Initial migration"
alembic upgrade head


----> https://medium.com/@julgq/migraciones-en-fastapi-usando-alembic-19379607db70


"""