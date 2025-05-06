import json
from pydantic import BaseModel
from typing import Type, List, Optional

class GestorArchivos:
    def __init__(self, archivo: str, modelo: Type[BaseModel]):
        self.archivo = archivo
        self.modelo = modelo

    def _leer_datos(self) -> List[dict]:
        try:
            with open(self.archivo, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def _escribir_datos(self, datos: List[dict]):
        with open(self.archivo, 'w') as f:
            json.dump(datos, f, indent=4)

    def get_all(self) -> List[BaseModel]:
        datos = self._leer_datos()
        return [self.modelo(**item) for item in datos]

    def get_by_id(self, id: int) -> Optional[BaseModel]:
        datos = self._leer_datos()
        for item in datos:
            if item['id'] == id:
                return self.modelo(**item)
        return None

    def add(self, objeto: BaseModel):
        datos = self._leer_datos()
        datos.append(objeto.dict())
        self._escribir_datos(datos)

    def update(self, id: int, datos_actualizados: dict):
        datos = self._leer_datos()
        for item in datos:
            if item['id'] == id:
                item.update(datos_actualizados)
                self._escribir_datos(datos)
                return
        raise ValueError("ID no encontrado")

    def delete(self, id: int):
        datos = self._leer_datos()
        datos = [item for item in datos if item['id'] != id]
        self._escribir_datos(datos)