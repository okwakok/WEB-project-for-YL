from fastapi import FastAPI
from app.api.routes import auth
from app.db.session import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "API работает"}