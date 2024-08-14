import json
import os
import argparse as arg
from datetime import datetime

ARCHIVO_TAREAS = 'tasks.json'

#Funcion para cargar el archivo json
def cargar_tareas():
    if not os.path.exists(ARCHIVO_TAREAS):
        print("El archivo no exite creando el archivo...")
        with open(ARCHIVO_TAREAS, 'w') as file:
            json.dump([],file)
        return []
    with open(ARCHIVO_TAREAS, 'r') as file:
        return json.load(file)

#Funcion para guardar las tareas en el json
def gruardar_tareas(tasks):
    with open(ARCHIVO_TAREAS, 'w') as file:
        json.dump(tasks, file, indent=2)

#Funcion para añadir una tarea
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

#Funcion para actualizar una tarea   
def update_tarea(task_id, new_description):
    tasks = cargar_tareas()
    for task in tasks:
        if task['id'] == task_id:
            task['descripcion'] = new_description
            task['actualizacion'] = datetime.now().isoformat()
            gruardar_tareas(tasks)
            print(f"Tarea {task_id} actualizada correctamente.")
            return
    print(f"Tarea con ID {task_id} no encontrada.")

#Funcion para borrar una tarea
def delete_tarea(task_id):
    tasks = cargar_tareas()
    original_length = len(tasks)
    tasks = [task for task in tasks if task['id'] != task_id] 
    if len(tasks) < original_length:
        gruardar_tareas(tasks)
        print(f"Tarea {task_id} eliminada correctamente.")
    else:
        print(f"Tarea con ID {task_id} no encontrada.")

#Funcion para actualizar una tarea a en progreso  
def progress_tarea(task_id):
    tasks = cargar_tareas()
    for task in tasks:
        if task['id'] == task_id:
            task['estado'] = "En progreso"
            task['actualizacion'] = datetime.now().isoformat()
            gruardar_tareas(tasks)
            print(f"Tarea {task_id} colocada en progreso.")
            return
    print(f"Tarea con ID {task_id} no encontrada.")

#Funcion para actualizar una tarea a realizado
def done_tarea(task_id):
    tasks = cargar_tareas()
    for task in tasks:
        if task['id'] == task_id:
            task['estado'] = "Realizado"
            task['actualizacion'] = datetime.now().isoformat()
            gruardar_tareas(tasks)
            print(f"Tarea {task_id} colocada en realizadas.")
            return
    print(f"Tarea con ID {task_id} no encontrada.")

#Funcion para listar las tareas
def list_tareas(status=None):
    tasks = cargar_tareas()
    if status:
        tasks = [task for task in tasks if task['estado'].lower() == status.lower()]
    if tasks:
        for task in tasks:
            print(f"ID: {task['id']}, Descripción: {task['descripcion']}, Estado: {task['estado']}, Creado: {task['creacion']}, Actualizado: {task['actualizacion']}")
    else:
        print("No hay tareas para mostrar.")    

#Comandos para trabajar por consola
parser = arg.ArgumentParser(description="Task Tracker CLI")
parser.add_argument('command', choices=['add', 'update', 'delete', 'mark-in-progress', 'mark-done', 'list'])
parser.add_argument('args', nargs='*')
args = parser.parse_args()

#Llamado a cada comando de la consola
if args.command == 'add':
    add_tarea(args.args[0])
if args.command == 'update':
    update_tarea(int(args.args[0]), " ".join(args.args[1:]))
if args.command == 'delete':
    delete_tarea(int(args.args[0]))
if args.command == 'mark-in-progress':
    progress_tarea(int(args.args[0]))
if args.command == 'mark-done':
    done_tarea(int(args.args[0]))
if args.command == 'list':
    list_tareas(args.args[0] if args.args else None)