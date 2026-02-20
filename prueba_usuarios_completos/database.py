import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Cargar las variables de entorno desde el archivo .env
load_dotenv()
# Obtener la URL de la base de datos desde las variables de entorno
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL no esta definido en el archivo .env")
# Configurar la conexión a la base de datos y la sesión
engine = create_engine(DATABASE_URL)
# Crear una clase de sesión para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Crear una clase base para los modelos de la base de datos
Base = declarative_base()
