import tkinter as tk
from tkinter import filedialog, messagebox
from leitor_CSV import ler_csv_completo, obter_categorias, filtrar_por_categoria
from gerador_codigo import gerar_codigos
from gerador_pdf import gerar_pdf
from exportador_zip import compactar_pdfs

arquivo_csv = None
df_csv = None

def selecionar_arquivo():
    global arquivo_csv, df_csv
    caminho = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if not caminho:
        return

    try:
        df_csv = ler_csv_completo(caminho)
        categorias = obter_categorias(df_csv)
        if not categorias:
            raise ValueError("Nenhuma categoria encontrada no arquivo.")

        arquivo_csv = caminho
        categoria_var.set(categorias[0])  # Seleciona a primeira categoria
        menu_categoria['menu'].delete(0, 'end')
        for c in categorias:
            menu_categoria['menu'].add_command(label=c, command=tk._setit(categoria_var, c))

        messagebox.showinfo("Arquivo carregado", f"{len(df_csv)} produtos encontrados.")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

def gerar_etiquetas():
    try:
        if df_csv is None:
            raise ValueError("Nenhum CSV carregado.")
        categoria = categoria_var.get()
        produtos_filtrados = filtrar_por_categoria(df_csv, categoria)
        if produtos_filtrados.empty:
            raise ValueError("Nenhum produto encontrado para a categoria selecionada.")

        tipo = tipo_codigo.get()
        arquivos = gerar_codigos(produtos_filtrados, tipo)
        gerar_pdf(produtos_filtrados, arquivos)
        compactar_pdfs()
        messagebox.showinfo("Sucesso", "Etiquetas geradas com sucesso!")

    except Exception as e:
        messagebox.showerror("Erro", str(e))

def criar_janela():
    global tipo_codigo, categoria_var, menu_categoria

    root = tk.Tk()
    root.title("EtiquetasPro")

    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack()

    # Botão para carregar CSV
    tk.Button(frame, text="Selecionar CSV", command=selecionar_arquivo).pack(pady=5)

    # Dropdown de categoria
    categoria_var = tk.StringVar()
    tk.Label(frame, text="Categoria:").pack()
    menu_categoria = tk.OptionMenu(frame, categoria_var, '')
    menu_categoria.pack(pady=5)

    # Tipo de código
    tipo_codigo = tk.StringVar(value="barcode")
    tk.Radiobutton(frame, text="Código de Barras", variable=tipo_codigo, value="barcode").pack()
    tk.Radiobutton(frame, text="QR Code", variable=tipo_codigo, value="qrcode").pack()

    # Botão para gerar etiquetas
    tk.Button(frame, text="Gerar Etiquetas", command=gerar_etiquetas).pack(pady=10)

    root.mainloop()

def editar_produto(produto, atualizar_callback):
    janela_edicao = tk.Toplevel()
    janela_edicao.title("Editar Produto")

    tk.Label(janela_edicao, text="Nome:").grid(row=0, column=0)
    nome_entry = tk.Entry(janela_edicao)
    nome_entry.insert(0, produto["nome"])
    nome_entry.grid(row=0, column=1)

    tk.Label(janela_edicao, text="Categoria:").grid(row=1, column=0)
    categoria_entry = tk.Entry(janela_edicao)
    categoria_entry.insert(0, produto["categoria"])
    categoria_entry.grid(row=1, column=1)

    tk.Label(janela_edicao, text="Preço:").grid(row=2, column=0)
    preco_entry = tk.Entry(janela_edicao)
    preco_entry.insert(0, produto["preco"])
    preco_entry.grid(row=2, column=1)

    def salvar_alteracoes():
        produto["nome"] = nome_entry.get()
        produto["categoria"] = categoria_entry.get()
        produto["preco"] = preco_entry.get()
        atualizar_callback()
        janela_edicao.destroy()

    tk.Button(janela_edicao, text="Salvar", command=salvar_alteracoes).grid(row=3, column=0, columnspan=2)
