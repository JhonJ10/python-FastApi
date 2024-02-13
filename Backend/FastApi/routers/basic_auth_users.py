from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# Inicia el server: uvicorn basic_auth_users:app --reload

router = APIRouter()

OAuth2 = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
        username: str
        full_name: str
        email: str
        disabled:bool

class UserDB(User):
        password: str

users_db ={
        "jhoncito":{
        "username" : "jhoncito",
        "full_name": "jhon jairo",
        "email" : "jhoncito@gmail.com",
        "disabled" : False,
        "password": "123456"
        },

        "jhoncito2":{
        "username" : "jhoncito2",
        "full_name": "jhon jairo 2",
        "email" : "jhoncito2@gmail.com",
        "disabled" : True,
        "password": "654321"
        }
}

def search_user_db(username: str):
        if username in users_db:
                return UserDB(**users_db[username])

def search_user(username: str):
        if username in users_db:
                return User(**users_db[username])
        
async def current_user(token: str = Depends(OAuth2)):
       user = search_user(token)
       if not user:
            raise  HTTPException(
                status_code=401,
                detail="credenciales de autenticacion invalidas",
                headers={"www-Authenticate": "Bearer"})
       
       if user.disabled:
                raise  HTTPException(
                status_code=400,
                detail="usuario inactivo")
              
       return user
       


        
@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
        user_db = users_db.get(form.username)
        if not user_db:
            raise  HTTPException(
                   status_code=400, detail="el usuario no es correcto")

        user= search_user_db(form.username)
        if not form.password== user.password:
               raise  HTTPException(
                   status_code=400, detail="la contraseña no es correcta")
        return {"access_token": user.username, "token_type": "bearer"}

@router.get("/users/me")
async def me(user:User = Depends(current_user)):
       return user
       
