from dotenv import load_dotenv
from fastapi import FastAPI
from routers.routers import router
from database.database import Base, engine

load_dotenv()

app = FastAPI(title = "Instagram Insights")

app.include_router(router, prefix='/api')
Base.metadata.create_all(bind=engine)