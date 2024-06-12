from fastapi import FastAPI, HTTPException
import pandas as pd
from typing import List, Dict, Union

app = FastAPI()


liste_de_course = [{"item": "Pomme", "qte": 25, "type": "kg"},
    {"item": "Farine", "qte": 2, "type": "kg"},
    {"item": "Yaourt", "qte": 25, "type": "unité"}]




@app.get("/")
def welcome():
    print("bonjour bienvenu sur l'API liste de course")

@app.get("/get_list", response_model=List[Dict])
def show_list():
    if len(liste_de_course) == 0:
        return {"message": "Bienvenue sur la liste de course"}
    else:
        return liste_de_course

# accepte un élément simple avec sa quantité ou un dictionnaire, élément quantité. Quand l’élément est déja dans la liste de course, les quantités s’ajoute. Les quantités peuvent être de type unité/gramme ou litre

@app.post("/add_to_list", response_model=List[Dict])
def add_list(item: dict):
    if isinstance(item, dict):
        for dictionary in liste_de_course:
            if dictionary["item"] == item["item"]:
               dictionary["qte"] += item["qte"]
               return liste_de_course
            else:
                liste_de_course.append(item)
                return liste_de_course

@app.delete("/remove_from_liste", response_model=List[Dict])
def remove_item(name_item):
    for dictionary in liste_de_course:
        if dictionary["item"] == name_item:
            liste_de_course.remove(dictionary)
            return liste_de_course
        else:
            return {"message" : "nothing to delete"}
               


