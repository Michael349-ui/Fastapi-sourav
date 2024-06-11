from fastapi import FastAPI
from . import models
from .database import engine
from .routers import posts, user, auth, vote
from fastapi.middleware.cors import CORSMiddleware


#models.Base.metadata.create_all(bind= engine)


origins = ['https://www.google.com']

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(posts.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
async def root():
    return {"message": "My Api5564"}


