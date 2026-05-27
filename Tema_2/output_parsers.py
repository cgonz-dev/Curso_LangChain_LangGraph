from pydantic import BaseModel

class Usuario(BaseModel):
    _id: int
    nombre: str
    activo: bool = True
    
data = {
    "_id": 123,
    "nombre": "Juan"}

usuario = Usuario(**data)

print(usuario.model_dump_json())