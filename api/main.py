from fastapi import FastAPI
from mangum import Mangum
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI()

# Configuración de CORS
origins = [
    "http://localhost",  
    "http://localhost:3000",
    "https://testapimanu.pages.dev" 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Datos
datos = [
    {"id": 1, "nombre": "EL PONCHO", "edad": 25, "pais": "GUACOCHE", "imagen": "https://media.istockphoto.com/id/2231666998/es/foto/avatar-masculino-silueta-de-un-joven-icono-de-las-redes-sociales-silueta-en-blanco-y-negro.jpg?s=1024x1024&w=is&k=20&c=rXtDWlTOH9583qgexZN_nQeJiZTZG4kg_FYzgMhUNWg="},
    {"id": 2, "nombre": "EL PEPO", "edad": 30, "pais": "EL TOTUMO", "imagen": "https://media.istockphoto.com/id/2231666998/es/foto/avatar-masculino-silueta-de-un-joven-icono-de-las-redes-sociales-silueta-en-blanco-y-negro.jpg?s=1024x1024&w=is&k=20&c=rXtDWlTOH9583qgexZN_nQeJiZTZG4kg_FYzgMhUNWg="},
    {"id": 3, "nombre": "EL MENBER", "edad": 22, "pais": "TOCAINA", "imagen": "https://media.istockphoto.com/id/2231666998/es/foto/avatar-masculino-silueta-de-un-joven-icono-de-las-redes-sociales-silueta-en-blanco-y-negro.jpg?s=1024x1024&w=is&k=20&c=rXtDWlTOH9583qgexZN_nQeJiZTZG4kg_FYzgMhUNWg="},
    {"id": 4, "nombre": "LA MARIA", "edad": 28, "pais": "MOROCHOA", "imagen": "https://media.istockphoto.com/id/2231666998/es/foto/avatar-masculino-silueta-de-un-joven-icono-de-las-redes-sociales-silueta-en-blanco-y-negro.jpg?s=1024x1024&w=is&k=20&c=rXtDWlTOH9583qgexZN_nQeJiZTZG4kg_FYzgMhUNWg="},
    {"id": 5, "nombre": "LUCHO", "edad": 35, "pais": "LA PAZ", "imagen": "https://media.istockphoto.com/id/2231666998/es/foto/avatar-masculino-silueta-de-un-joven-icono-de-las-redes-sociales-silueta-en-blanco-y-negro.jpg?s=1024x1024&w=is&k=20&c=rXtDWlTOH9583qgexZN_nQeJiZTZG4kg_FYzgMhUNWg="},
    {"id": 6, "nombre": "Sofía", "edad": 27, "pais": "LA NEVADA", "imagen": "https://media.istockphoto.com/id/2231666998/es/foto/avatar-masculino-silueta-de-un-joven-icono-de-las-redes-sociales-silueta-en-blanco-y-negro.jpg?s=1024x1024&w=is&k=20&c=rXtDWlTOH9583qgexZN_nQeJiZTZG4kg_FYzgMhUNWg="},
    {"id": 7, "nombre": "Pedro", "edad": 40, "pais": "LOS HATICOS", "imagen": "https://media.istockphoto.com/id/2231666998/es/foto/avatar-masculino-silueta-de-un-joven-icono-de-las-redes-sociales-silueta-en-blanco-y-negro.jpg?s=1024x1024&w=is&k=20&c=rXtDWlTOH9583qgexZN_nQeJiZTZG4kg_FYzgMhUNWg="},
    {"id": 8, "nombre": "Lucía", "edad": 19, "pais": "SOLONDRIA", "imagen": "https://media.istockphoto.com/id/2231666998/es/foto/avatar-masculino-silueta-de-un-joven-icono-de-las-redes-sociales-silueta-en-blanco-y-negro.jpg?s=1024x1024&w=is&k=20&c=rXtDWlTOH9583qgexZN_nQeJiZTZG4kg_FYzgMhUNWg="},
    {"id": 9, "nombre": "Carlos", "edad": 33, "pais": "VALLEDUPAR", "imagen": "https://media.istockphoto.com/id/2231666998/es/foto/avatar-masculino-silueta-de-un-joven-icono-de-las-redes-sociales-silueta-en-blanco-y-negro.jpg?s=1024x1024&w=is&k=20&c=rXtDWlTOH9583qgexZN_nQeJiZTZG4kg_FYzgMhUNWg="},
    {"id": 10, "nombre": "Ana", "edad": 24, "pais": "BARRANQUILLA", "imagen": "https://media.istockphoto.com/id/2231666998/es/foto/avatar-masculino-silueta-de-un-joven-icono-de-las-redes-sociales-silueta-en-blanco-y-negro.jpg?s=1024x1024&w=is&k=20&c=rXtDWlTOH9583qgexZN_nQeJiZTZG4kg_FYzgMhUNWg="},
    {"id": 11, "nombre": "Manuel", "edad": 29, "pais": "CARTAGENA", "imagen": "https://media.istockphoto.com/id/2231666998/es/foto/avatar-masculino-silueta-de-un-joven-icono-de-las-redes-sociales-silueta-en-blanco-y-negro.jpg?s=1024x1024&w=is&k=20&c=rXtDWlTOH9583qgexZN_nQeJiZTZG4kg_FYzgMhUNWg="},
    {"id": 12, "nombre": "Marta", "edad": 31, "pais": "SANTA MARTA", "imagen": "https://media.istockphoto.com/id/2231666998/es/foto/avatar-masculino-silueta-de-un-joven-icono-de-las-redes-sociales-silueta-en-blanco-y-negro.jpg?s=1024x1024&w=is&k=20&c=rXtDWlTOH9583qgexZN_nQeJiZTZG4kg_FYzgMhUNWg="},
    {"id": 13, "nombre": "Luis", "edad": 45, "pais": "RIOHACHA", "imagen": "https://media.istockphoto.com/id/2231666998/es/foto/avatar-masculino-silueta-de-un-joven-icono-de-las-redes-sociales-silueta-en-blanco-y-negro.jpg?s=1024x1024&w=is&k=20&c=rXtDWlTOH9583qgexZN_nQeJiZTZG4kg_FYzgMhUNWg="},
    {"id": 14, "nombre": "Camila", "edad": 26, "pais": "MAICAO", "imagen": "https://media.istockphoto.com/id/2231666998/es/foto/avatar-masculino-silueta-de-un-joven-icono-de-las-redes-sociales-silueta-en-blanco-y-negro.jpg?s=1024x1024&w=is&k=20&c=rXtDWlTOH9583qgexZN_nQeJiZTZG4kg_FYzgMhUNWg="},
    {"id": 15, "nombre": "Andrés", "edad": 38, "pais": "FONSECA", "imagen": "https://media.istockphoto.com/id/2231666998/es/foto/avatar-masculino-silueta-de-un-joven-icono-de-las-redes-sociales-silueta-en-blanco-y-negro.jpg?s=1024x1024&w=is&k=20&c=rXtDWlTOH9583qgexZN_nQeJiZTZG4kg_FYzgMhUNWg="},
    {"id": 16, "nombre": "Paula", "edad": 21, "pais": "SAN JUAN", "imagen": "https://media.istockphoto.com/id/2231666998/es/foto/avatar-masculino-silueta-de-un-joven-icono-de-las-redes-sociales-silueta-en-blanco-y-negro.jpg?s=1024x1024&w=is&k=20&c=rXtDWlTOH9583qgexZN_nQeJiZTZG4kg_FYzgMhUNWg="},
    {"id": 17, "nombre": "Diego", "edad": 34, "pais": "VILLANUEVA", "imagen": "https://media.istockphoto.com/id/2231666998/es/foto/avatar-masculino-silueta-de-un-joven-icono-de-las-redes-sociales-silueta-en-blanco-y-negro.jpg?s=1024x1024&w=is&k=20&c=rXtDWlTOH9583qgexZN_nQeJiZTZG4kg_FYzgMhUNWg="},
    {"id": 18, "nombre": "Valentina", "edad": 23, "pais": "URUMITA", "imagen": "https://media.istockphoto.com/id/2231666998/es/foto/avatar-masculino-silueta-de-un-joven-icono-de-las-redes-sociales-silueta-en-blanco-y-negro.jpg?s=1024x1024&w=is&k=20&c=rXtDWlTOH9583qgexZN_nQeJiZTZG4kg_FYzgMhUNWg="},
    {"id": 19, "nombre": "Fernando", "edad": 41, "pais": "DIBULLA", "imagen": "https://media.istockphoto.com/id/2231666998/es/foto/avatar-masculino-silueta-de-un-joven-icono-de-las-redes-sociales-silueta-en-blanco-y-negro.jpg?s=1024x1024&w=is&k=20&c=rXtDWlTOH9583qgexZN_nQeJiZTZG4kg_FYzgMhUNWg=  "},
    {"id": 20, "nombre": "Daniela", "edad": 28, "pais": "ALBANIA", "imagen": "https://media.istockphoto.com/id/2231666998/es/foto/avatar-masculino-silueta-de-un-joven-icono-de-las-redes-sociales-silueta-en-blanco-y-negro.jpg?s=1024x1024&w=is&k=20&c=rXtDWlTOH9583qgexZN_nQeJiZTZG4kg_FYzgMhUNWg="},
    {"id": 21, "nombre": "Ricardo", "edad": 36, "pais": "HATONUEVO", "imagen": "https://media.istockphoto.com/id/2231666998/es/foto/avatar-masculino-silueta-de-un-joven-icono-de-las-redes-sociales-silueta-en-blanco-y-negro.jpg?s=1024x1024&w=is&k=20&c=rXtDWlTOH9583qgexZN_nQeJiZTZG4kg_FYzgMhUNWg="},
    {"id": 22, "nombre": "Natalia", "edad": 27, "pais": "BOSCONIA", "imagen": "https://media.istockphoto.com/id/2231666998/es/foto/avatar-masculino-silueta-de-un-joven-icono-de-las-redes-sociales-silueta-en-blanco-y-negro.jpg?s=1024x1024&w=is&k=20&c=rXtDWlTOH9583qgexZN_nQeJiZTZG4kg_FYzgMhUNWg="},
    {"id": 23, "nombre": "Héctor", "edad": 39, "pais": "AGUACHICA", "imagen": "https://media.istockphoto.com/id/2231666998/es/foto/avatar-masculino-silueta-de-un-joven-icono-de-las-redes-sociales-silueta-en-blanco-y-negro.jpg?s=1024x1024&w=is&k=20&c=rXtDWlTOH9583qgexZN_nQeJiZTZG4kg_FYzgMhUNWg="},
    {"id": 24, "nombre": "Laura", "edad": 22, "pais": "CODAZZI", "imagen": "https://media.istockphoto.com/id/2231666998/es/foto/avatar-masculino-silueta-de-un-joven-icono-de-las-redes-sociales-silueta-en-blanco-y-negro.jpg?s=1024x1024&w=is&k=20&c=rXtDWlTOH9583qgexZN_nQeJiZTZG4kg_FYzgMhUNWg="},
    {"id": 25, "nombre": "Oscar", "edad": 20, "pais": "CHIRIGUANA", "imagen": "https://media.istockphoto.com/id/2231666998/es/foto/avatar-masculino-silueta-de-un-joven-icono-de-las-redes-sociales-silueta-en-blanco-y -negro.jpg?s=1024x1024&w=is&k=20&c=rXtDWlTOH9583qgexZN_nQeJiZTZG4kg_FYzgMhUNWg="},
    {"id": 26, "nombre": "Karol", "edad": 20, "pais": "Valledupar", "imagen": "https://media.istockphoto.com/id/2231666998/es/foto/avatar-masculino-silueta-de-un-joven-icono-de-las-redes-sociales-silueta-en-blanco-y-negro.jpg?s=1024x1024&w=is&k=20&c=rXtDWlTOH9583qgexZN_nQeJiZTZG4kg_FYzgMhUNWg="}
]

@app.get("/")
def get_datos():
    return {
        "fecha": datetime.now().strftime("%Y-%m-%d"),
        "total": len(datos),
        "datos": datos
    }

# handler para serverless
handler = Mangum(app)