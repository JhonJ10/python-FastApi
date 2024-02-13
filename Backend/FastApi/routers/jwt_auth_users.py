from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta


ALGORITM = "HS256"
ACCESS_TOKEN_DURATION = 1
SECRET = "122166dd9e2d617246da9af9d7d3cd6f"


router = APIRouter()


OAuth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt =CryptContext(schemes=["bcrypt"])

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
        "password": "$2a$12$ifegTFbCCbBb2hK7rTg48OdOdEM1X5Mv2BZluTt4L.Jo47FjLK2W."
        },

        "jhoncito2":{
        "username" : "jhoncito2",
        "full_name": "jhon jairo 2",
        "email" : "jhoncito2@gmail.com",
        "disabled" : True,
        "password": "$2a$12$4pzpYgR0NpLjaV3MQNc5auPuRSh0jQRbwwGzG7OHlf119BmLwRsoO"
        }
}
def search_user_db(username: str):
        if username in users_db:
                return UserDB(**users_db[username])
        
def search_user(username: str):
        if username in users_db:
                return User(**users_db[username])
        
async def auth_user(token: str= Depends(OAuth2)):
    exception = HTTPException(
        status_code=401,
        detail="credenciales de autenticacion invalidas",
        headers={"www-Authenticate": "Bearer"})
       
    try:
        username= jwt.decode(token, SECRET, algorithms=[ALGORITM]).get("sub")
        if username is  None: 
            raise  exception
        
    except JWTError:
        raise  exception
    return search_user(username)

async def current_user(user: User = Depends(auth_user)):    
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

        

        if not crypt.verify(form.password, user.password):
               raise  HTTPException(
                   status_code=400, detail="la contraseña no es correcta")
        
  
        
        #expire= datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)

        access_token= {"sub":user.username,
                       "exp":datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)}


        return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITM), "token_type": "bearer"}


@router.get("/users/me")
async def me(user:User = Depends(current_user)):
       return user
       
