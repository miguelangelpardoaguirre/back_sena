
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.usuarios import CrearUsuario
from core.database import get_db
from app.crud import usuarios as crud_users  # (as) alias para especificar


router = APIRouter()

@router.post("/registrar", status_code=status.HTTP_201_CREATED)  # decorador (@funcion en este caso router) crea una ruta tipo post,get('api') para ser consumida
def create_user(user: CrearUsuario, db: Session = Depends(get_db)):
    try:
        crud_users.create_user(db, user)
        return {"message": "Usuario creado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    