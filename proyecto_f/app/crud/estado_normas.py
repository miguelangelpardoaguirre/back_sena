from sqlalchemy.orm import Session
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
import logging
from typing import Optional, List

from app.schemas.estado_normas import CrearEstadoNorma, EditarEstadoNorma

logger = logging.getLogger(__name__)

def crear_estado_norma(db: Session, norma: CrearEstadoNorma) -> bool:
    try:
        data = norma.model_dump()
        query = text("""
            INSERT INTO estado_de_normas (
                cod_version, fecha_elaboracion, anio, red_conocimiento,
                nombre_ncl, cod_ncl, ncl_version, norma_corte_noviembre,
                version, norma_version, mesa_sectorial, tipo_norma,
                tipo_competencia, observacion, fecha_revision, vigencia, fecha_indice
            ) VALUES (
                :cod_version, :fecha_elaboracion, :anio, :red_conocimiento,
                :nombre_ncl, :cod_ncl, :ncl_version, :norma_corte_noviembre,
                :version, :norma_version, :mesa_sectorial, :tipo_norma,
                :tipo_competencia, :observacion, :fecha_revision, :vigencia, :fecha_indice
            )
        """)
        db.execute(query, data)
        db.commit()
        return True
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error al crear registro en estado_de_normas: {e}")
        raise Exception("Error de base de datos al crear el registro")


def obtener_todas_normas(db: Session):
    try:
        query = text("SELECT * FROM estado_de_normas ORDER BY cod_programa ASC")
        result = db.execute(query).mappings().all()
        return result
    except SQLAlchemyError as e:
        logger.error(f"Error al obtener registros: {e}")
        raise Exception("Error de base de datos al obtener registros")


def obtener_norma_por_id(db: Session, cod_programa: int):
    try:
        query = text("SELECT * FROM estado_de_normas WHERE cod_programa = :id")
        result = db.execute(query, {"id": cod_programa}).mappings().first()
        return result
    except SQLAlchemyError as e:
        logger.error(f"Error al obtener registro: {e}")
        raise Exception("Error de base de datos al obtener el registro")


def actualizar_norma(db: Session, cod_programa: int, data_update: EditarEstadoNorma) -> bool:
    try:
        fields = data_update.model_dump(exclude_unset=True)
        if not fields:
            return False
        set_clause = ", ".join([f"{key} = :{key}" for key in fields])
        fields["id"] = cod_programa

        query = text(f"UPDATE estado_de_normas SET {set_clause} WHERE cod_programa = :id")
        db.execute(query, fields)
        db.commit()
        return True
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error al actualizar estado_de_normas: {e}")
        raise Exception("Error de base de datos al actualizar el registro")


def eliminar_norma(db: Session, cod_programa: int) -> bool:
    try:
        query = text("DELETE FROM estado_de_normas WHERE cod_programa = :id")
        db.execute(query, {"id": cod_programa})
        db.commit()
        return True
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error al eliminar registro: {e}")
        raise Exception("Error de base de datos al eliminar el registro")
