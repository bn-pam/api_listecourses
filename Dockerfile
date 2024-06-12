# Utiliser l'image officielle Python
FROM python:3.10

# installer la bibliothèque néecassaire au fonctionnement 
RUN pip install pandas

#définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copie le fichier Python dans le conteneur
COPY courses.py /app/courses.py

# exécuter le script python lors du démarrage du conteneur
CMD ["python", "courses.py"]