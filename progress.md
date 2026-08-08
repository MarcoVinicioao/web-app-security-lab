# Web Application Security Lab — Progreso

## Objetivo

Proyecto educativo basado en Web Application Fundamentals de HTB Academy.

Objetivo: construir una aplicación web funcional y estudiar vulnerabilidades,
pruebas de seguridad y mitigaciones en un entorno controlado.

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

### Aplicación

- [x] VM / servidor web
- [x] HTML
- [x] CSS
- [x] JavaScript
- [x] Backend Flask
- [x] API POST /api/tasks
- [x] API GET /api/tasks
- [x] CORS
- [x] SQLite
- [x] Tabla tasks
- [x] Guardar tareas con INSERT
- [x] Recuperar tareas desde SQLite
- [x] Conectar frontend con backend
- [x] Persistencia de datos

### Seguridad

- [x] Pruebas de validación de entrada
- [x] Rechazo de tareas vacías
- [x] Rechazo de tipos incorrectos
- [x] Manejo de JSON inválido
- [x] Prueba de SQL Injection
- [x] Consultas SQL parametrizadas
- [x] Prueba de XSS
- [x] Uso de textContent para evitar ejecución de HTML/JavaScript
- [x] Configuración de CORS
- [x] Revisión de debug=True para desarrollo
- [x] Hardening inicial

### Git / GitHub

- [x] Repositorio Git
- [x] SSH configurado con GitHub
- [x] Push del proyecto
- [x] Rama security/input-validation
- [x] Commit de corrección de seguridad
- [x] Pull Request #1
- [x] Merge de Pull Request a main

## Seguridad implementada

### Validación de entrada

La API valida que `task`:

- exista
- sea un string
- no esté vacío

Las entradas inválidas reciben HTTP 400.

### SQL Injection

Las consultas utilizan parámetros:

    INSERT INTO tasks (task) VALUES (?)

El contenido enviado por el usuario se trata como dato y no como parte de la consulta SQL.

### XSS

El frontend utiliza:

    textContent

para insertar las tareas en el DOM, evitando interpretar el contenido como HTML ejecutable.

### CORS

El backend permite solicitudes desde:

    http://localhost:8080

## Últimas pruebas realizadas

- [x] Crear tarea válida
- [x] Recuperar tareas mediante GET
- [x] Intentar crear una tarea vacía
- [x] Intentar enviar un número como tarea
- [x] Enviar JSON inválido
- [x] Probar payload de SQL Injection
- [x] Probar payload de XSS
- [x] Comprobar persistencia en SQLite

## Estado actual

La aplicación funciona correctamente y los datos se sincronizan entre:

Frontend → API Flask → SQLite

La primera corrección de seguridad fue implementada en una rama independiente,
revisada mediante Pull Request y fusionada a `main`.

## Siguiente paso

Continuar con pruebas de seguridad más avanzadas y documentar cada hallazgo
siguiendo el formato:

- ¿Qué es?
- Objetivo
- Funcionamiento
- Tipos
- Payloads comunes
- Ejemplos
- Impacto
- Mitigaciones
- Herramientas
- Notas
- Referencias

## Cómo iniciar el proyecto

### Terminal 1 — Backend

    cd ~/projects/web-app-security-lab/backend
    python3 app.py

### Terminal 2 — Frontend

    cd ~/projects/web-app-security-lab/frontend
    python3 -m http.server 8080

### Frontend

    http://localhost:8080

### Backend

    http://localhost:5000
