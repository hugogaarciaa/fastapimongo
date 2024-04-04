from http.client import HTTPException
from fastapi import APIRouter
from typing import List
from models.users import Users
from config.database import collectionUsers
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()

@router.post("/login")
async def login(username: str, email: str, password: str):
    # Buscar al usuario en la base de datos
    user = collectionUsers.find_one({"username": username})
    if user:
        # Verificar el email
        if user.get("email") == email:
            return {"message": "Login successful"}
        else:
            return {"message": "Incorrect email"}
    else:
        raise HTTPException(status_code=404, detail="User not found")

#Register
@router.post("/register")
async def register(user: Users):
    if collectionUsers.find_one({"username": user.username}):
        return {"message": "Username already exists"}
    else:
        new_user = {"name": user.name, "last_name": user.last_name, "username": user.username, "email": user.email, "password": user.password}
        collectionUsers.insert_one(new_user)
        return user
    
#Comprobar si el nombre de usuario ya existe
@router.get("/check/{username}")
async def check_username(username: str):
    if collectionUsers.find_one({"username": username}):
        return {"message": "OK"}
    else:
        return {"message": "KO"}
    
#Comprobar si el email ya existe
@router.get("/check/email/{email}")
async def check_email(email: str):
    if collectionUsers.find_one({"email": email}):
        return {"message": "OK"}
    else:
        return {"message": "KO"}
    
