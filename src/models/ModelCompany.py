# // Company

from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional
from datetime import datetime

class EmpresasRPModel(BaseModel):

    razonSocial: Optional[str] = None
    rfc: Optional[str] = None
    siglas: Optional[str] = None
    nombreCorto: Optional[str] = None
    calle: Optional[str] = None
    numExt: Optional[str] = None
    numInt: Optional[str] = None
    colonia: Optional[str] = None
    poblacion: Optional[str] = None
    municipio: Optional[str] = None
    estado: Optional[str] = None
    pais: Optional[str] = None
    codigoPostal: Optional[str] = None
    telefono1: Optional[str] = None
    telefono2: Optional[str] = None
    representanteLegal: Optional[str] = None
    
    idUsuarioCreo: Optional[int] = None
    idUsuarioModifico: Optional[int] = None
    
    activo: bool = True

    fecha_creacion: datetime = Field(default_factory=datetime.utcnow)
    fecha_actualizacion: Optional[datetime] = None
    fecha_inactivo: Optional[datetime] = None

    class Config:
        json_encoders = {ObjectId: str}
        populate_by_name = True