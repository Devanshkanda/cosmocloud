from fastapi import FastAPI
from db.db_conn import get_db_connection
from config import EnvConfigSettings

app = FastAPI()
env = EnvConfigSettings()

db = get_db_connection(env.mongodb_uri, env.db_name)

from routers import students, author_routes
app.include_router(students.router)
app.include_router(author_routes.router)

print(env.mongodb_uri, env.db_name, env.test_name)
print("world")
print(db)


@app.get("/")
def root():
    return {
        "message": "heello bigger application"
    }