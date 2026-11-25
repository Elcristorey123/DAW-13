# Práctica Semana 13 - API RESTful con DRF

API RESTful para gestión de tareas desarrollada con Django y Django REST Framework.

## Requisitos
- Python 3.11+
- Django 6.x
- Django REST Framework

## Instalación
1. Clonar el repositorio
2. Crear entorno virtual: `python -m venv venv`
3. Activar entorno: `venv\Scripts\activate` (Windows)
4. Instalar dependencias: `pip install -r requirements.txt`
5. Migrar base de datos: `python manage.py migrate`
6. Correr servidor: `python manage.py runserver`

## Endpoints
- `GET /api/tareas/` - Listar tareas (paginado, filtrable, ordenable)
- `POST /api/tareas/` - Crear tarea
- `GET /api/tareas/{id}/` - Detalle de tarea
- `PUT /api/tareas/{id}/` - Actualizar tarea
- `DELETE /api/tareas/{id}/` - Eliminar tarea
- `GET /api/tareas/completadas/` - Tareas completadas
- `POST /api/tareas/{id}/completar/` - Marcar como completada
- `GET /api/docs/` - Documentación Swagger UI

<img width="886" height="498" alt="image" src="https://github.com/user-attachments/assets/b07f3fad-93a8-4fa1-92da-7e1467170bd9" />
