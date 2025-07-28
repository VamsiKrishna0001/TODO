from fastapi import FastAPI
from database.connection import engine, Base
from fastapi.middleware.cors import CORSMiddleware
from routes import todos, auth, admin, users

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Todo app", version="0.0.1")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(todos.todos_router)
app.include_router(auth.auth_router)
app.include_router(admin.router)
app.include_router(users.router)

@app.get("/")
async def read_main():
    return "OK"