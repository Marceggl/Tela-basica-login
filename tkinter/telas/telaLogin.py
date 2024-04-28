import tkinter as tk
from tkinter import ttk

def criar_tela_login(aplicacao):
    tela_login = ttk.Frame(aplicacao)
    tela_login.grid(row=0, column=0, sticky="nsew")
    aplicacao.title("Login")
    
    # Configuração para o frame preencher todo o espaço disponível na janela principal
    aplicacao.grid_rowconfigure(0, weight=1)
    aplicacao.grid_columnconfigure(0, weight=1)
    tela_login.grid(sticky="nsew") 
    
    # Adicionar imagem de fundo ao frame
    imagem_fundo = tk.PhotoImage(file="img/tela_login3.png")
    label_imagem_fundo = ttk.Label(tela_login, image=imagem_fundo)
    label_imagem_fundo.image = imagem_fundo
    label_imagem_fundo.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Criar um subframe para o formulário de login
    form_input = ttk.Frame(tela_login)
    form_input.place(relx=0.5, rely=0.5, anchor="center")
    
    paddy= 10
    paddx= 10
    
    # Definindo estilos para o texto
    estilo_texto = 'Arial 10 bold'
    cor_texto = 'white'
    
    label_usuario = ttk.Label(form_input, text="Usuário:", font=(estilo_texto, 10), foreground=cor_texto)
    label_usuario.grid(row=0, column=0, sticky="w", padx=paddx, pady=paddy)
    
    entry_usuario = ttk.Entry(form_input)
    entry_usuario.grid(row=0, column=1, padx=paddx, pady=paddy)
    
    label_senha = ttk.Label(form_input, text="Senha:", font=(estilo_texto, 10), foreground=cor_texto)
    label_senha.grid(row=1, column=0, sticky="w", padx=paddx, pady=paddy)
    
    entry_senha = ttk.Entry(form_input, show="*")
    entry_senha.grid(row=1, column=1, padx=paddx, pady=paddy)
    
    botao_login = ttk.Button(form_input, text="Login", command=aplicacao.efetuar_login)
    botao_login.grid(row=2, columnspan=2, padx=paddx, pady=paddy)
    
    mensagem_erro = ttk.Label(form_input, text="", font=(estilo_texto, 10), foreground=cor_texto)
    mensagem_erro.grid(row=3, columnspan=2, padx=paddx, pady=paddy)
    
    return tela_login, entry_usuario, entry_senha, mensagem_erro