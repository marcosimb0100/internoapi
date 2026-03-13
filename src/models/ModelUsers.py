from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional
from datetime import datetime


class UsuarioModel(BaseModel):

    correo_electronico: str
    nombre_completo: str
    clave: str
    foto_perfil: Optional[str] = None

    idUsuarioCreo: Optional[int] = None
    idUsuarioModifico: Optional[int] = None
    
    activo: bool = True

    fecha_creacion: datetime = Field(default_factory=datetime.utcnow)
    fecha_actualizacion: Optional[datetime] = None
    fecha_inactivo: Optional[datetime] = None

    class Config:
        json_encoders = {ObjectId: str}
        populate_by_name = True
