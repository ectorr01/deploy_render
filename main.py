from fastapi import FastAPI

app = FastAPI()

@app.get("/") #metodo api (path api)
def homepage():
    return "Ciao, questa è l'homepage"



@app.get("/ciao") #metodo api (path api)
def homepage():

    a = 10
    a += 5
    return "Ciao, sono nel path ciao"

@app.get("/ciao") #metodo api (path api)
def homepage(nome: str, eta:int):
    return "ciao" + nome