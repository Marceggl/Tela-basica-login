from tkinter import ttk

def tela_principal(aplicacao):
    nova_tela = ttk.Frame(aplicacao, padding=10)
    nova_tela.grid(row=0, column=0, sticky="nsew")
    # Adicione widgets ou configure a nova tela conforme necessário
    label_bem_vindo = ttk.Label(nova_tela, text="Bem-vindo à nova tela!")
    label_bem_vindo.pack()
    
    # Adicione um botão de logout
    botao_logout = ttk.Button(nova_tela, text="Logout", command=aplicacao.fazer_logout)
    botao_logout.pack()
    
    return nova_tela
        