# Utiliser l'image officielle Python
FROM python:3.10

#définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copie le fichier requirements dans le conteneur
COPY requirements.txt /app/requirements.txt

# installer les bibliothèques (ici bibliothèques Python) néecassaire au fonctionnement 
RUN pip install -r requirements.txt 

# Copie le fichier Python dans le conteneur
COPY . /app

# lorsque le conteneur Docker sera démarré, il exécutera le serveur Uvicorn 
# avec l'application spécifiée dans le fichier main.py sous forme de module Python main et objet app, 
# écoutant sur l'adresse IP 0.0.0.0 et le port 8000,
# avec l'option --reload qui permet de recharger automatiquement le serveur lorsqu'un changement est détecté dans le code source.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]