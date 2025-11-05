from pydantic import BaseModel
from typing import Optional
from datetime import date

class CrearEstadoNorma(BaseModel):
    cod_programa: Optional[int] = None
    cod_version: str
    fecha_elaboracion: date
    anio: int
    red_conocimiento: str
    nombre_ncl: str
    cod_ncl: int
    ncl_version: int
    norma_corte_noviembre: str
    version: int
    norma_version: str
    mesa_sectorial: str
    tipo_norma: str
    tipo_competencia: str
    observacion: Optional[str] = None
    fecha_revision: Optional[date] = None
    vigencia: Optional[str] = None
    fecha_indice: Optional[str] = None


class EditarEstadoNorma(BaseModel):
    cod_version: Optional[str] = None
    fecha_elaboracion: Optional[date] = None
    anio: Optional[int] = None
    red_conocimiento: Optional[str] = None
    nombre_ncl: Optional[str] = None
    cod_ncl: Optional[int] = None
    ncl_version: Optional[int] = None
    norma_corte_noviembre: Optional[str] = None
    version: Optional[int] = None
    norma_version: Optional[str] = None
    mesa_sectorial: Optional[str] = None
    tipo_norma: Optional[str] = None
    tipo_competencia: Optional[str] = None
    observacion: Optional[str] = None
    fecha_revision: Optional[date] = None
    vigencia: Optional[str] = None
    fecha_indice: Optional[str] = None


class RetornoEstadoNorma(BaseModel):
    cod_programa: int
    cod_version: str
    fecha_elaboracion: date
    anio: int
    red_conocimiento: str
    nombre_ncl: str
    cod_ncl: int
    ncl_version: int
    norma_corte_noviembre: str
    version: int
    norma_version: str
    mesa_sectorial: str
    tipo_norma: str
    tipo_competencia: str
    observacion: Optional[str]
    fecha_revision: Optional[date]
    vigencia: Optional[str]
    fecha_indice: Optional[str]
