import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def gerar_pdf(produtos, imagens):
    if not os.path.exists("output"):
        os.makedirs("output")

    for i, produto in enumerate(produtos):
        nome_pdf = f"output/etiqueta_{i}.pdf"
        c = canvas.Canvas(nome_pdf, pagesize=letter)
        
        # Aqui supõe-se que 'produto' é um dict ou pd.Series com chave 'nome'
        nome_produto = produto['nome'] if isinstance(produto, dict) else str(produto)
        
        c.drawString(100, 750, f"Produto: {nome_produto}")
        c.drawImage(imagens[i], 100, 600, width=200, height=200)
        c.save()
