from fastapi import FastAPI

app = FastAPI()

@app.get("/") #metodo api (path api)
def homepage():
    return "Ciao, questa è l'homepage"

@app.get("/ciao") #metodo api (path api)
def homepage():
    return "Ciao, sono nel path ciao"

@app.get("/ciao")
def saluto(nome: str, cognome: str):
    return "ciao " + nome + cognome
