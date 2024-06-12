
liste_de_course = [{"item": "Pomme", "qte": 25, "type": "kg"},
    {"item": "Farine", "qte": 2, "type": "kg"},
    {"item": "Yaourt", "qte": 25, "type": "unité"}]

def add_list(item: dict):
    if isinstance(item, dict):
        for dictionary in liste_de_course:
            if dictionary["item"] == item["item"]:
               dictionary["qte"] += item["qte"]
               return print(f"Quantitée mise à jour {liste_de_course}")
            else:
                liste_de_course.append(item)
                return print(f"liste mise à jour {liste_de_course}")
            
add_list({"item": "Pomme", "qte": 25, "type": "kg"})