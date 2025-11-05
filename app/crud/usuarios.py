
from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import Optional
import logging

from app.schemas.usuarios import CrearUsuario
from core.security import get_hashed_password

logger = logging.getLogger(__name__)

def create_user(db: Session, user: CrearUsuario) -> Optional[bool]:
    try:
        dataUser = user.model_dump()
        contraOrigin = dataUser["contra_encript"]

        print(contraOrigin)

        contraEncript = get_hashed_password(dataUser["contra_encript"])



        dataUser

#        dataUser.contra_encript = get_hashed_password(dataUser.contra_encript)
        query = text("""
            INSERT INTO usuario (
                nombre_completo, num_documento,
                correo, contra_encript, id_rol,
                estado,
            ) VALUES (
                :nombre_completo, :num_documento,
                :correo, :contra_encript, :id_rol,
                :estado,
            )
        """)
        db.execute(query, user.model_dump())
        db.commit()
        return True
    except Exception as e:
        db.rollback()
        logger.error(f"Error al crear usuario: {e}")
        raise Exception("Error de base de datos al crear el usuario")
    
