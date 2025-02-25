from fastapi import FastAPI
from typing import List

app = FastAPI()

resources = [
    {"id": 1, "title": "Curso de Python", "category": "Programação"},
    {"id": 2, "title": "Introdução ao Machine Learning", "category": "Machine Learning"},
    {"id": 3, "title": "Curso de Data Science", "category": "Data Science"},
    {"id": 4, "title": "Artigo sobre IA", "category": "Inteligência Artificial"},
    {"id": 5, "title": "Vídeo sobre Deep Learning", "category": "Machine Learning"},
]

@app.get("/")
def read_root():
    return {"message": resources}
