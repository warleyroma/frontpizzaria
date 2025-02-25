import tkinter as tk
from tkinter import ttk

def create_interface():
    root = tk.Tk()
    root.title("CMS - Loja Virtual Visão Geral")

    # Barra lateral
    sidebar = tk.Frame(root, width=200, bg="#f0f0f0")
    sidebar.pack(side=tk.LEFT, fill=tk.Y)

    # Logo e título
    logo_label = tk.Label(sidebar, text="CMS", font=("Arial", 20, "bold"), bg="#f0f0f0")
    logo_label.pack(pady=20)
    title_label = tk.Label(sidebar, text="2RS Soluções em TI", font=("Arial", 12), bg="#f0f0f0")
    title_label.pack()

    # Botões da barra lateral
    buttons = ["Abrir o Site", "Dashboard", "Conteúdo", "Pedidos", "Aparência", "Produtos", "Menu", "Banner", "Cadastro", "Configurações", "? Central de ajuda", "Layout Antigo"]
    for button_text in buttons:
        button = tk.Button(sidebar, text=button_text, anchor=tk.W, padx=10, bg="#f0f0f0")
        button.pack(fill=tk.X, pady=5)

    # Conteúdo principal
    main_content = tk.Frame(root)
    main_content.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Barra superior
    top_bar = tk.Frame(main_content, height=50, bg="#e0e0e0")
    top_bar.pack(fill=tk.X)

    # Botões da barra superior
    top_buttons = ["Pesquisar", "Meus Dados", "Configurações", "Sair"]
    for button_text in top_buttons:
        button = tk.Button(top_bar, text=button_text, padx=10, bg="#e0e0e0")
        button.pack(side=tk.RIGHT, padx=5)

    # Título da página
    page_title = tk.Label(main_content, text="Loja Virtual » Visão Geral", font=("Arial", 14, "bold"), padx=20, pady=10)
    page_title.pack(anchor=tk.W)

    # Botão "Acessar Relatórios"
    reports_button = tk.Button(main_content, text="Acessar Relatórios", padx=10)
    reports_button.pack(anchor=tk.NE, padx=20, pady=10)

    # Tabela de últimos pedidos
    orders_frame = tk.Frame(main_content, padx=20, pady=10)
    orders_frame.pack(fill=tk.X)

    orders_title = tk.Label(orders_frame, text="Últimos pedidos realizados", font=("Arial", 12, "bold"))
    orders_title.pack(anchor=tk.W)

    table = ttk.Treeview(orders_frame, columns=("Pedido", "Data", "Itens", "Valor Total", "Situação"), show="headings")
    table.heading("Pedido", text="Pedido")
    table.heading("Data", text="Data")
    table.heading("Itens", text="Itens")
    table.heading("Valor Total", text="Valor Total")
    table.heading("Situação", text="Situação")
    table.pack(fill=tk.X, pady=10)

    # Dados de exemplo para a tabela
    orders = [
        ("#130520220434", "06/06/2017", "2", "R$68,30", "Confirmado"),
        ("#130520220433", "06/06/2017", "1", "R$38,71", "Confirmado"),
        ("#130520220432", "06/06/2017", "1", "R$28,61", "Pendente"),
        ("#130520220430", "30/03/2017", "3", "R$56,43", "Confirmado"),
        ("#130520220428", "21/03/2017", "10", "R$79,46", "Confirmado"),
    ]

    for order in orders:
        table.insert("", tk.END, values=order)

    # Informações e gráfico de vendas (áreas vazias)
    info_frame = tk.Frame(main_content, padx=20, pady=10)
    info_frame.pack(fill=tk.X)

    info_title = tk.Label(info_frame, text="Informações", font=("Arial", 12, "bold"))
    info_title.pack(anchor=tk.W)

    sales_graph_frame = tk.Frame(main_content, padx=20, pady=10)
    sales_graph_frame.pack(fill=tk.X)

    sales_graph_title = tk.Label(sales_graph_frame, text="Gráfico de vendas", font=("Arial", 12, "bold"))
    sales_graph_title.pack(anchor=tk.W)

    root.mainloop()

if __name__ == "__main__":
    create_interface()
