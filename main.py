from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
import uuid

app = FastAPI(
    title="APIs en clase 5",
    version="0.0.1"
)

@app.post("/api/v1/users/")
async def create_user(username: str, name: str):
    return {
        "username": username,
        "name": name,
        "id": str(uuid.uuid4()),
        "message": "The user was created",
        "status_code": 201
    }

@app.get("/api/v1/[{user_id}/")
async def get_user(user_id: str):
    users = {
        "hola_test": {
            "username": "test_a",
            "name": "test_b"
        },
        "ide-67": {
            "username": "test_c",
            "name": "test_d"
        }
    }

    if user_id in users:
        user = users[user_id]

        return JSONResponse(
            content = user,
            status_code = status.HTTP_200_OK
        )
    else:
        return JSONResponse(
            content="No existe el usuario",
            status_code = status.HTTP_404_NOT_FOUND
        )