from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.estado_normas import CrearEstadoNorma, EditarEstadoNorma
from app.crud.estado_normas import (
    crear_estado_norma, obtener_todas_normas, obtener_norma_por_id,
    actualizar_norma, eliminar_norma
)
from core.database import get_db

router = APIRouter(
    prefix="/estado_normas",
    tags=["Estado de Normas"]
)

@router.post("/crear")
def crear_norma(norma: CrearEstadoNorma, db: Session = Depends(get_db)):
    if crear_estado_norma(db, norma):
        return {"message": "Registro creado correctamente"}
    raise HTTPException(status_code=500, detail="Error al crear el registro")


@router.get("/listar")
def listar_normas(db: Session = Depends(get_db)):
    return obtener_todas_normas(db)


@router.get("/{cod_programa}")
def obtener_norma(cod_programa: int, db: Session = Depends(get_db)):
    result = obtener_norma_por_id(db, cod_programa)
    if not result:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return result


@router.put("/actualizar/{cod_programa}")
def actualizar(cod_programa: int, data: EditarEstadoNorma, db: Session = Depends(get_db)):
    if actualizar_norma(db, cod_programa, data):
        return {"message": "Registro actualizado correctamente"}
    raise HTTPException(status_code=400, detail="No se proporcionaron datos para actualizar")


@router.delete("/eliminar/{cod_programa}")
def eliminar(cod_programa: int, db: Session = Depends(get_db)):
    if eliminar_norma(db, cod_programa):
        return {"message": "Registro eliminado correctamente"}
    raise HTTPException(status_code=500, detail="Error al eliminar el registro")
