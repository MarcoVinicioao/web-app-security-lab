# Web Application Security Lab — Progreso

## Objetivo
Proyecto educativo basado en Web Application Fundamentals de HTB Academy.
Objetivo: construir una aplicación web y posteriormente estudiar vulnerabilidades y mitigaciones.

## Entorno
- Kali Linux
- Python 3.11.4
- Flask 2.2.2
- Werkzeug 2.2.2
- Flask-CORS 6.0.5
- SQLite 3.42.0
- Git + GitHub
- Frontend servido en puerto 8080
- Backend Flask servido en puerto 5000

## Estructura actual

web-app-security-lab/
├── README.md
├── PROGRESS.md
├── frontend/
│   ├── index.html
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── app.js
└── backend/
    ├── app.py
    ├── database.py
    └── tasks.db

## Progreso

- [x] VM / servidor web
- [x] HTML
- [x] CSS
- [x] JavaScript
- [x] Backend Flask
- [x] API POST /api/tasks
- [x] CORS
- [x] SQLite
- [x] Tabla tasks
- [x] Guardar tareas con INSERT
- [ ] GET /api/tasks
- [ ] Cargar tareas desde SQLite al frontend
- [ ] APIs
- [ ] Pruebas de seguridad
- [ ] Vulnerabilidades controladas
- [ ] Mitigaciones / hardening

## Último punto

POST /api/tasks funciona correctamente.

La tarea se guarda en SQLite y fue comprobada con:

SELECT * FROM tasks;

## Siguiente paso

Crear GET /api/tasks para recuperar las tareas desde SQLite y después conectar esa ruta con JavaScript.

## Cómo iniciar el proyecto

Terminal 1:

cd ~/projects/web-app-security-lab/backend
python3 app.py

Terminal 2:

cd ~/projects/web-app-security-lab/frontend
python3 -m http.server 8080

Frontend:
http://localhost:8080

Backend:
http://localhost:5000
