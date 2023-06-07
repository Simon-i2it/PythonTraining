from pydantic import BaseModel
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()


# Models
class User(BaseModel):
    username: str
    password: str


# Simulated database
USERS_DB = [
    User(username="user", password="pass"),
    User(username="simon", password="22299"),
]

# OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


def authenticate_user(token: str = Depends(oauth2_scheme)):
    current_user = None

    for user in USERS_DB:
        if user.username == token:
            current_user = User(
                username=user.username,  # TODO - Decrypt username from token
                password=user.password,
            )

    if not current_user:
        raise HTTPException(status_code=401, detail="Invalid token")
    # if user.password != password:  # TODO - Decrypt password from token
    #     raise HTTPException(status_code=401, detail="Invalid password")

    return current_user


@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid username or password")
    return {
        "access_token": user.username,  # TODO - Encrypt username and generate token
        "token_type": "bearer",
    }


@app.get("/")
def root(user: User = Depends(authenticate_user)):
    return {"message": f"Hi, {user.username}"}
