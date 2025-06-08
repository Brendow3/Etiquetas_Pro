import zipfile
import os

def compactar_pdfs():
    if not os.path.exists("output"):
        os.makedirs("output")  # Cria a pasta se não existir

    with zipfile.ZipFile("output/etiquetas.zip", "w") as zipf:
        for arquivo in os.listdir("output"):
            if arquivo.endswith(".pdf"):
                zipf.write(os.path.join("output", arquivo), arcname=arquivo)