# Task Tracker CLI

Este es un sencillo administrador de tareas basado en la línea de comandos (CLI) escrito en Python. Permite añadir, actualizar, eliminar y listar tareas, así como cambiar el estado de una tarea a "En progreso" o "Realizado".

## Características

- **Añadir Tarea**: Permite añadir una nueva tarea con una descripción.
- **Actualizar Tarea**: Permite actualizar la descripción de una tarea existente.
- **Eliminar Tarea**: Permite eliminar una tarea por su ID.
- **Marcar como En Progreso**: Cambia el estado de una tarea a "En progreso".
- **Marcar como Realizado**: Cambia el estado de una tarea a "Realizado".
- **Listar Tareas**: Muestra todas las tareas o filtra por estado ("Por hacer", "En progreso", "Realizado").

## Requisitos

- Python 3.x

## Instalación

1. Clona este repositorio o descarga los archivos.

git clone https://github.com/tu_usuario/task-tracker-cli.git

Navega al directorio del proyecto.

cd task-tracker-cli

## Uso

El script puede ser ejecutado desde la línea de comandos utilizando el intérprete de Python. Aquí tienes ejemplos de cómo usar cada uno de los comandos disponibles:

**Añadir una Tarea**

python task_tracker.py add "Descripción de la tarea"

**Actualizar una Tarea**

python task_tracker.py update <id> "Nueva descripción de la tarea"

**Eliminar una Tarea**

python task_tracker.py delete <id>

**Marcar una Tarea como En Progreso**

python task_tracker.py mark-in-progress <id>

**Marcar una Tarea como Realizado**

python task_tracker.py mark-done <id>

**Listar Tareas**

Para listar todas las tareas:

python task_tracker.py list

Para listar tareas por estado (ejemplo: "Por hacer"):

python task_tracker.py list "Por hacer"