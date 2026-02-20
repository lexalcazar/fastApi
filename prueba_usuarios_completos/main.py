from datetime import date
from fastapi import FastAPI, HTTPException, HTTPException
from pydantic import BaseModel
from database import Base, SessionLocal, engine
from models import Usuario as Usuariodb
from fastapi import Depends

#definir la función de dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Crear la base de datos y las tablas
Base.metadata.create_all(bind=engine)
# Crear la aplicación FastAPI
app = FastAPI()
# Definir el modelo de datos para la entrada de usuario
class UsuarioIn(BaseModel):
    nombre: str
    apellidos: str
    email: str
    fecha_nacimiento: date

#----------------------------------Endpoints-------------------------------------

#- Endpoint para crear un nuevo usuario
@app.post("/usuarios/")
def crear_usuario(usuario: UsuarioIn, db = Depends(get_db)):
    # Crear una instancia del modelo de base de datos con los datos del usuario
    nuevo_usuario = Usuariodb(
        name=usuario.nombre,
        apellidos=usuario.apellidos,
        email=usuario.email,
        fecha_nacimiento=usuario.fecha_nacimiento
    )
    # Agregar el nuevo usuario a la sesión y guardar los cambios en la base de datos
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    if nuevo_usuario is None:
        raise HTTPException(status_code=400, detail="Error al crear el usuario")
    return {"id": nuevo_usuario.id, "nombre": nuevo_usuario.name, "apellidos": nuevo_usuario.apellidos, "email": nuevo_usuario.email, "fecha_nacimiento": nuevo_usuario.fecha_nacimiento}


#- Endpoint para obtener la lista de usuarios
@app.get("/usuarios/")
def obtener_usuarios(db = Depends(get_db)):
    usuarios = db.query(Usuariodb).all()
    return [{"id": usuario.id, "nombre": usuario.name, "apellidos": usuario.apellidos, "email": usuario.email, "fecha_nacimiento": usuario.fecha_nacimiento} for usuario in usuarios]


#- Endpoint para obtener un usuario por su ID
@app.get("/usuarios/{usuario_id}")
def obtener_usuario(usuario_id: int, db = Depends(get_db)):
    usuario = db.query(Usuariodb).filter(Usuariodb.id == usuario_id).first()
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"id": usuario.id, "nombre": usuario.name, "apellidos": usuario.apellidos, "email": usuario.email, "fecha_nacimiento": usuario.fecha_nacimiento}

#- Endpoint para eliminar un usuario por su ID
@app.delete("/usuarios/{usuario_id}")
def eliminar_usuario(usuario_id: int, db = Depends(get_db)):
    usuario = db.query(Usuariodb).filter(Usuariodb.id == usuario_id).first()
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db.delete(usuario)
    db.commit()
    return {"message": "Usuario eliminado exitosamente"}


#- Endpoint para actualizar un usuario por su ID
@app.put("/usuarios/{usuario_id}")
def actualizar_usuario(usuario_id: int, usuario: UsuarioIn, db = Depends(get_db)):
    usuario_db = db.query(Usuariodb).filter(Usuariodb.id == usuario_id).first()
    if usuario_db is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    usuario_db.name = usuario.nombre
    usuario_db.apellidos = usuario.apellidos
    usuario_db.email = usuario.email
    usuario_db.fecha_nacimiento = usuario.fecha_nacimiento
    db.commit()
    db.refresh(usuario_db)
    return {"id": usuario_db.id, "nombre": usuario_db.name, "apellidos": usuario_db.apellidos, "email": usuario_db.email, "fecha_nacimiento": usuario_db.fecha_nacimiento}


#- Endpoint para buscar usuarios por nombre
@app.get("/usuarios/buscar/")
def buscar_usuarios(nombre: str, db = Depends(get_db)):
    usuarios = db.query(Usuariodb).filter(Usuariodb.name.ilike(f"%{nombre}%")).all()
    if not usuarios:
        raise HTTPException(status_code=404, detail="No se encontraron usuarios con ese nombre")
    return [{"id": usuario.id, "nombre": usuario.name, "apellidos": usuario.apellidos, "email": usuario.email, "fecha_nacimiento": usuario.fecha_nacimiento} for usuario in usuarios]