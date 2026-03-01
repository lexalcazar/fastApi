# 🚀 FastAPI – API REST de Gestión de Usuarios

API REST desarrollada con **FastAPI** para la gestión de usuarios mediante operaciones CRUD y búsqueda por nombre.

Proyecto orientado a la práctica de desarrollo backend y diseño de servicios web con Python.

---

## 🛠️ Tecnologías

- Python 3.x
- FastAPI
- Uvicorn
- Base de datos relacional (SQLite / PostgreSQL)
- SQL
- Pydantic

> Los endpoints están implementados de forma síncrona.

---

## ✅ Funcionalidades

- Obtener todos los usuarios
- Obtener usuario por ID
- Buscar usuarios por nombre
- Crear nuevos usuarios
- Actualizar usuarios existentes
- Eliminar usuarios
- Validación de datos mediante modelos Pydantic
- Documentación automática con OpenAPI / Swagger

---

## 📌 Endpoints

| Método | Endpoint | Descripción |
|--------|---------|-------------|
| GET | `/usuarios` | Obtener todos los usuarios |
| GET | `/usuarios/{id}` | Obtener usuario por ID |
| GET | `/usuarios/buscar/{nombre}` | Buscar usuarios por nombre |
| POST | `/usuarios` | Crear un nuevo usuario |
| PUT | `/usuarios/{id}` | Actualizar un usuario |
| DELETE | `/usuarios/{id}` | Eliminar un usuario |

---
