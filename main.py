from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.product import product_router
from routers.auth import auth_router
from routers.user import user_router


# Estamos creando una instancia de la clase FastAPI
app = FastAPI()
app.title = "API para bares" 
app.version = "3.0.0"

app.add_middleware(ErrorHandler)
app.include_router(product_router)
app.include_router(user_router)
app.include_router(auth_router)
Base.metadata.create_all(bind=engine)

# Ahora crearemos nuestro primer endpoint 
@app.get("/", tags=['home']) # Aqui se agrega la ruta de inicio
def message():
    return HTMLResponse(content="<h1> Y a beber!! </h1>")