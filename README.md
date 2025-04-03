# Convertisseur PDF en Images

Ce script permet de convertir toutes les pages des fichiers PDF d'un dossier en images PNG.

## Prérequis

Avant d'exécuter le script, assurez-vous d'avoir installé les bibliothèques nécessaires. Vous pouvez les installer avec la commande suivante :

```bash
pip install pymupdf
```

## Utilisation

1. Exécutez le script Python :

```bash
py main.py
```

2. Entrez le chemin absolu du dossier contenant les fichiers PDF lorsque demandé.

3. Le script va parcourir tous les fichiers PDF du dossier et les convertir en images PNG. Chaque page d'un PDF sera enregistrée sous la forme :
   
   ```
   images/nom_du_fichier_page_X.png
   ```
   dans un sous-dossier `images` du dossier contenant les PDF.

4. Une fois terminé, le script affichera la liste des fichiers convertis.

## Exemple de sortie

```
=======================================
Fichier(s) convertie:
exemple.pdf
rapport.pdf
=======================================
```

## Remarque
- Assurez-vous que le dossier contient bien des fichiers PDF avant de lancer le script.
- Un sous-dossier `images` sera créé automatiquement pour stocker les fichiers convertis.
- Le script utilise la bibliothèque `PyMuPDF` (`fitz`) pour l'extraction des images.
- Les images seront enregistrées au format PNG dans le dossier `images`.
