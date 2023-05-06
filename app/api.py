
from fastapi import FastAPI

import app.models as models
from .routes.question import question_router
from .routes.result import results_router
from .database import engine
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# This needs to change! its your CORS access

origins = ["http://localhost:7137", "http://localhost:3000",
           "https://aquamarine-otter-164c0e.netlify.app"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Content-Type"],
)


route = "/api"
app.include_router(question_router, prefix=f"{route}/questions")
app.include_router(results_router, prefix=f"{route}/results")


# Testroute to see if api is running
@app.get("/")
async def root():
    return {"message": "API running"}
