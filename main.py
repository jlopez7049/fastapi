from fastapi import FastAPI, HTTPException
from models import Usuario, Producto, Pedido
from gestor_archivos import GestorArchivos

app = FastAPI()

gestor_usuarios = GestorArchivos('usuarios.json', Usuario)
gestor_productos = GestorArchivos('productos.json', Producto)
gestor_pedidos = GestorArchivos('pedidos.json', Pedido)

@app.get("/usuarios")
def mostrar_usuarios():
    return gestor_usuarios.get_all()

@app.get("/usuarios/{id}")
def optener_usuario_id(id: int):
    usuario = gestor_usuarios.get_by_id(id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@app.post("/usuarios")
def añadir_usuario(usuario: Usuario):
    gestor_usuarios.add(usuario)
    return {"mensaje": "Usuario agregado"}

@app.put("/usuarios/{id}")
def actualizar_usuario(id: int, usuario: Usuario):
    try:
        gestor_usuarios.update(id, usuario.dict())
        return {"mensaje": "Usuario actualizado"}
    except ValueError:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

@app.delete("/usuarios/{id}")
def borrar_usuario(id: int):
    gestor_usuarios.delete(id)
    return {"mensaje": "Usuario eliminado"}

@app.get("/productos")
def mostrar_productos():
    return gestor_productos.get_all()

@app.get("/productos/{id}")
def optener_producto_id(id: int):
    producto = gestor_productos.get_by_id(id)
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@app.post("/productos")
def añadir_producto(producto: Producto):
    gestor_productos.add(producto)
    return {"mensaje": "Producto agregado"}

@app.put("/productos/{id}")
def actualizar_producto(id: int, producto: Producto):
    try:
        gestor_productos.update(id, producto.dict())
        return {"mensaje": "Producto actualizado"}
    except ValueError:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

@app.delete("/productos/{id}")
def eliminar_producto(id: int):
    gestor_productos.delete(id)
    return {"mensaje": "Producto eliminado"}

# Endpoints para Pedidos
@app.get("/pedidos")
def mostrar_pedidos():
    return gestor_pedidos.get_all()

@app.get("/pedidos/{id}")
def obtener_pedido(id: int):
    pedido = gestor_pedidos.get_by_id(id)
    if pedido is None:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return pedido

@app.post("/pedidos")
def añadir_pedido(pedido: Pedido):
    gestor_pedidos.add(pedido)
    return {"mensaje": "Pedido agregado"}

@app.put("/pedidos/{id}")
def actualizar_pedido(id: int, pedido: Pedido):
    try:
        gestor_pedidos.update(id, pedido.dict())
        return {"mensaje": "Pedido actualizado"}
    except ValueError:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")

@app.delete("/pedidos/{id}")
def borrar_pedido(id: int):
    gestor_pedidos.delete(id)
    return {"mensaje": "Pedido eliminado"}