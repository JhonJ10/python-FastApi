from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


# Inicia el server: uvicorn users:app --reload

#entidad users
class User(BaseModel):
        id: int
        name: str
        surname:str
        url: str
        age:int

users_list = [User(id=1, name="jhon", surname="galvis", url="https://mouredev.com/python", age=19 ),
              User(id=2, name="jairo", surname="rodriguez", url="https://rodriguez.com", age=25 ),
              User(id=3, name="haakon", surname="dalberg", url="https://haakon.com", age=35 )]


@router.get("/usersjson")
async def usersjson():
    return [{"name": "jhon", "surname":"galvis", "url":"https://mouredev.com/python", "age": 19},
            {"name": "jairo", "surname":"rodriguez", "url":"https://rodriguez.com", "age": 25},
            {"name": "haakon", "surname":"dalberg", "url":"https://haakon.com", "age": 35}]

@router.get("/users")
async def users():
      return users_list

# paht
@router.get("/user/{id}")
async def user(id:int):
        return search_user(id)
#query
@router.get("/user/")
async def user(id:int):
      return search_user(id)



@router.post("/user/", status_code=201)
async def user(user: User):
      if type(search_user(user.id)) == User:
          raise  HTTPException(status_code=404, detail="el usuario ya existe")
      

      else: 
            users_list.append(user)
            return user


@router.put("/user/")
async def user(user: User):

      found =False


      for index, saved_user in enumerate(users_list):
            if saved_user.id== user.id:
                  users_list[index] =user
                  found =True

      if not found:
            return {"error": "nose ha actualizado el usuario"}

      else:
            return user


@router.delete("/user/{id}")
async def user(id:int):
      found =False

      for index, saved_user in enumerate(users_list):
            if saved_user.id== id:
                 del users_list[index] 
                 found= True

      if not found:
            return {"error": "nose ha eliminado el usuario"}


            
               


def search_user(id:int):
      users= filter(lambda user: user.id == id, users_list)
      try: 
            return list(users)[0]
      except: 
            return {"error": "nose ha encontrado el usuario"}


