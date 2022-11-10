from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return "Mi primera Api Con python"

@app.get("/usuarios/{user_id]")
def read_user(user_id: int):
    return {"user_id" : user_id} 

cursos = [{"Curso1":"Software"},
          {"curso2":"Programacion Basica"},
          {"curso3":"Sistemas"},
          {"Curso4":"Desarrollo web"}]

@app.get("/cursos")
def leer_cursos(skip: int =0, limit: int =10):
    return cursos[skip: skip + limit]

@app.post("/estudiantes/")
def crear_estudiante (nombre: str, apellido: str):
    return f"Estudiante {nombre} {apellido} guardado!"
