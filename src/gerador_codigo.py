import os
import barcode
from barcode.writer import ImageWriter
import qrcode

def gerar_codigos(lista_produtos, tipo):
    if not os.path.exists("output"):
        os.makedirs("output")  # Cria a pasta se não existir

    nomes_arquivos = []
    for i, item in enumerate(lista_produtos):
        nome = f"output/codigo_{i}.png"
        if tipo == "barcode":
            ean = barcode.get('ean13', str(100000000000 + i), writer=ImageWriter())
            ean.save(nome[:-4])  # Salva sem extensão para barcode lib
        else:
            img = qrcode.make(item)
            img.save(nome)
        nomes_arquivos.append(nome)
    return nomes_arquivos
