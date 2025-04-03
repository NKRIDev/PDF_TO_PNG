# Libs
import fitz
import os

# Dossier ou sont stocké les PDF
folder_path = input("Entrer le chemin absolu oû se trouvent vos PDF : ")

# Dossier image
image_folder = os.path.join(folder_path, "images")
os.makedirs(image_folder, exist_ok=True)

# Fichier qui se sont correctement convertie
file_convert = []

# Récupération de tout les fichiers dans le dossier
for file in os.listdir(folder_path):
    if file.lower().endswith(".pdf"):
        pdf_path = os.path.join(folder_path, file)
        doc = fitz.open(pdf_path)

        for i, page in enumerate(doc):
            pix = page.get_pixmap()
            img_path = os.path.join(image_folder, f"{file[:-4]}_page_{i + 1}.png")
            pix.save(img_path)
            file_convert.append(file)

# Succès
print("=======================================")
print("Fichier(s) convertie: ")
for file in file_convert:
    print(file)
print("=======================================")
