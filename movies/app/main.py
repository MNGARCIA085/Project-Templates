from fastapi import FastAPI, APIRouter
from prueba import router as prueba_routes


#models.Base.metadata.create_all(bind=engine); migrar sin usar alembic

app = FastAPI()


router = APIRouter()


app.include_router(prueba_routes.router,tags=['prueba'])





from api.api_v1.api import api_router


app.include_router(api_router, prefix='/API')




"""


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