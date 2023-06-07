from jinja2 import Environment, FileSystemLoader


# Création de l'environnement Jinja2
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('templates/exercises_template.html')

# Définition de la valeur de la variable Python
title = "Fiche d'exercice"

# Rendu du modèle HTML avec la valeur de la variable
result = template.render(title=title)

# Affichage du résultat
print(result)