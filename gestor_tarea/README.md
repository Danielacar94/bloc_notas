# Gestor de tareas

Aplicación web sencilla con **Flask** para agregar tareas y marcarlas como completadas. La interfaz usa plantillas **Jinja2**.

## Requisitos

- Python 3.10 o superior recomendado
- [Flask](https://flask.palletsprojects.com/)

## Instalación

Se recomienda usar un entorno virtual:

```bash
python -m venv .venv
```

Activación en Windows (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

Instalar dependencias:

```bash
pip install flask
```

## Cómo ejecutar

Desde esta carpeta (`gestor_tarea`):

```bash
python index.py
```

Abrí el navegador en [http://127.0.0.1:5000](http://127.0.0.1:5000).

El servidor arranca en modo **debug** (útil en desarrollo).

## Uso

- Escribí una tarea y pulsá **Agregar**.
- Para marcar como hecha, usá el enlace **\[Completar\]** de cada tarea.
- Las incompletas se listan antes que las completadas; las hechas se muestran tachadas (`<s>`) y con la leyenda “Hecha”.

## Rutas

| Ruta | Método | Descripción |
|------|--------|-------------|
| `/` | GET | Lista de tareas |
| `/agregar` | POST | Agrega una tarea (campo de formulario `texto_tarea`) |
| `/completar/<id>` | GET | Marca la tarea con ese `id` como hecha |

## Estructura del proyecto

```
gestor_tarea/
├── index.py              # App Flask y rutas
├── templates/
│   └── index.html        # Plantilla principal (Jinja2)
├── .gitignore
└── README.md
```

## Nota importante

Las tareas se guardan en una **lista en memoria**. Si reiniciás el proceso de Python, se pierden. Esto sirve como práctica de Flask y plantillas; para persistencia habría que sumar archivo, SQLite u otra base de datos.
