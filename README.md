# Etiquetas_Pro

Aplicativo gráfico que:
- Lê um arquivo CSV com produtos
- Gera etiquetas com código de barras ou QR Code
- Exporta em PDF e compacta em ZIP

## Tecnologias
- Python 3.11+
- Tkinter (interface gráfica)
- Pandas (leitura CSV)
- python-barcode (códigos de barras)
- qrcode + Pillow (QR Codes)
- reportlab (PDF)
- zipfile (compactação)
- PDM (gerenciador de dependências)

## Estrutura
- `data/`: arquivos de entrada
- `output/`: etiquetas geradas
- `src/`: código-fonte do app

## Como usar
1. Instale o PDM: `pip install pdm`
2. Instale as dependências: `pdm install`
3. Execute o app: `pdm run python src/main.py`
