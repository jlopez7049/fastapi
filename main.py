import json
from typing import Union
from fastapi import FastAPI

app = FastAPI()

nombres = []

@app.get("/personas/{personas_id}")
def obetener_persona(personas_id: str):
    with open("personas.json", "r") as file:
        texto= file.read()
        personas_json = json.loads(texto)
        print(personas_json[personas_id])
    return personas_json[personas_id]

@app.post("/personas")
def crear_persona(personas_id: str,edad: str):
    with open("personas.json", "r") as file:
        texto= file.read()
        personas_json = json.loads(texto)
    with open("personas.json", "w") as file:
        personas_json.append({
        "nombre": personas_id,
        "edad": edad,
            })
        json.dump(personas_json, file, indent= 4)
    return personas_json


@app.put("/personas/{personas_id}")
def actualizar_persona(personas_id: str, edad: str):
    with open("personas.json", "r") as file:
        texto = file.read()
        personas_json = json.loads(texto)
    for persona in personas_json:
        if persona["nombre"] == personas_id:
            persona["edad"] = edad
            break
    with open("personas.json", "w") as file:
        json.dump(personas_json, file, indent=4)
    return personas_json

@app.delete("/personas/{personas_id}")
def borrar_persona(persona_id:str):
    with open("frutas.json", "r") as file:
        texto= file.read()
        personas_json =json.loads(texto)
        personas_json = [persona for persona in personas_json if persona["nombre"] != persona_id]
    with open("frutas.json", "w") as file:
        json.dump(personas_json, file, indent=4)
    return personas_json