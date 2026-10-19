from fastapi import FastAPI

app = FastAPI(
    title = "Book'App",
    description = "API de gestion de livres",
    version = "1.0.0"
)

@app.get("/", tags=["Accueil"])
def accueil():
    return {"message":"Bienvenu dans la Bibliothèque"}