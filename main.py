from fastapi import FastAPI, HTTPException

ma_liste_courses = {}

app = FastAPI()

@app.get("/liste")
def get_list():
    return {"content": ma_liste_courses}

@app.post("/liste")
def add_to_list(produit: str, quantite: float, unite: str):
    ma_liste_courses[produit] = {"quantite": quantite, "unite": unite}
    return {"content": ma_liste_courses}

@app.delete("/liste")
def remove_from_list(produit: str, quantite: float, unite: str):
    try:
        ma_liste_courses.remove({"produit": produit, "quantite": quantite, "unite": unite})
        return {"content": ma_liste_courses}
    except ValueError:
        raise HTTPException(status_code=404, detail="Element not found in the list")

#  uvicorn main:app --reload