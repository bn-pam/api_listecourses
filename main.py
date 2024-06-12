from fastapi import FastAPI, HTTPException

ma_liste_courses = {}

app = FastAPI()

@app.get("/liste") #un dictionnaire de dictionnaires
def get_list():
    return {"content": ma_liste_courses}

@app.post("/liste")
def add_to_list(produit: str, quantite: float, unite: str):
    # vérifier si l'élément est déjà dans le dictionnaire
    if produit in ma_liste_courses : #vérifier que la clé qui est présentée, correspond à une clé du dico, pour parcourir un dictionnaire 
        # s'il est dans le dico, vérifier que l'unité est la même 
            if unite:
                if unite == ma_liste_courses[produit][1]: #on fait matcher unité cherchée et unité du produit donné plus haut
                #pour obtenir le dico : on donne la clé et on obtient la valeur
                # si l'unité est la même on ajoute les unités
                    ma_liste_courses[produit][0]+=quantite
                    return {produit:ma_liste_courses[produit]} #renvoyer le produit et sa quantité cad la valeur correspondant à la clé produit
                else :  # si l'unité est pas la même, on renvoie un message d'erreur
                    raise HTTPException(
                        status_code=400,
                        detail=f"Not the good unit for the product, {produit} is in {ma_liste_courses[produit]}"
                    ) 
                # pas d'unité fournie, j'ajoute par défault
            else:
                ma_liste_courses[produit][0]+=quantite
                return {produit:ma_liste_courses[produit]}
    # si non, on ajoute l'élément au dictionnaire
    else : 
        ma_liste_courses[produit] = [quantite, unite]
        return {produit:ma_liste_courses[produit]}


@app.delete("/liste")
def remove_from_list(produit: str, quantite: float, unite: str):
    try:
        ma_liste_courses.remove({"produit": produit, "quantite": quantite, "unite": unite})
        return {"content": ma_liste_courses}
    except ValueError:
        raise HTTPException(status_code=404, detail="Element not found in the list")

#  uvicorn main:app --reload