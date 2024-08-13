import json
import os
import argparse as arg
from datetime import datetime

ARCHIVO_TAREAS = 'tasks.json'

def cargar_tareas():
    if not os.path.exists(ARCHIVO_TAREAS):
        print("El archivo no exite creando el archivo...")
        with open(ARCHIVO_TAREAS, 'w') as file:
            json.dump([],file)
        return []
    with open(ARCHIVO_TAREAS, 'r') as file:
        return json.load(file)

def gruardar_tareas(tasks):
    with open(ARCHIVO_TAREAS, 'w') as file:
        json.dump(tasks, file, indent=2)


def add_tarea(description):
    tasks = cargar_tareas()
    new_id = max(task['id'] for task in tasks) + 1 if tasks else 1
    new_task = {
        "id": new_id,
        "descripcion": description,
        "estado": "Por hacer",
        "creacion": datetime.now().isoformat(),
        "actualizacion": datetime.now().isoformat()
    }
    tasks.append(new_task)
    gruardar_tareas(tasks)
    print(f"Tarea añadida correctamente (ID: {new_id})")

        


parser = arg.ArgumentParser(description="Task Tracker CLI")
parser.add_argument('command', choices=['add', 'update', 'delete', 'mark-in-progress', 'mark-done', 'list'])
parser.add_argument('args', nargs='*')
args = parser.parse_args()

if args.command == 'add':
    add_tarea(args.args[0])