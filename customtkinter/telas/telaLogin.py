import customtkinter as ctk
from PIL import Image
import os

def configurar_janela(aplicacao):
    aplicacao.geometry("500x300")
    aplicacao.grid_rowconfigure(4, weight=1)
    aplicacao.grid_columnconfigure(2, weight=1)
    aplicacao.resizable(False, False)
    largura_janela = aplicacao.winfo_width()
    altura_janela = aplicacao.winfo_height()

    largura_tela = aplicacao.winfo_screenwidth()
    altura_tela = aplicacao.winfo_screenheight()

    posicao_x = (largura_tela - largura_janela) // 2
    posicao_y = (altura_tela - altura_janela) // 2

    aplicacao.geometry(f"+{posicao_x}+{posicao_y}")
        

def telaLogin(aplicacao):
    tela_login = ctk.CTkFrame(aplicacao)
    tela_login.place(relx=0.5, rely=0.5, anchor="center")
    configurar_janela(aplicacao=aplicacao)
    
    paddx = 20
    paddy = 10
    tamanho_input = 300
    
    image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../img")
    user_icon = ctk.CTkImage(Image.open(os.path.join(image_path, "user.png")), size=(26, 26))
    lock_icon = ctk.CTkImage(Image.open(os.path.join(image_path, "lock.png")), size=(26, 26))
    
    label_info = ctk.CTkLabel(tela_login, text="Bem vindo !\nFaça a autenticação para entrar", font=ctk.CTkFont(size=15, weight="bold"))
    label_info.grid(row=0, column=0, columnspan=2, padx=paddx, pady=paddy)
    
    label_user = ctk.CTkLabel(tela_login, image=user_icon, text="")
    label_user.grid(row=1, column=0, padx=paddx, pady=paddy)
    
    input_user = ctk.CTkEntry(tela_login, placeholder_text="Usuário", width=tamanho_input)
    input_user.grid(row=1, column=1, padx=paddx, pady=paddy)
    
    label_password = ctk.CTkLabel(tela_login, image=lock_icon, text="")
    label_password.grid(row=2, column=0, padx=paddx, pady=paddy)
    
    input_password = ctk.CTkEntry(tela_login, placeholder_text="Senha", width=tamanho_input, show="*")
    input_password.grid(row=2, column=1, padx=paddx, pady=paddy)
    
    autenticar_btn = ctk.CTkButton(tela_login, text="Autenticar", command=aplicacao.autenticar, font=ctk.CTkFont(size=15, weight="bold"))
    autenticar_btn.grid(row=3, column=0, columnspan=2, padx=paddx, pady=paddy)
    
    label_info = ctk.CTkLabel(tela_login, text="", font=ctk.CTkFont(size=15, weight="bold"))
    label_info.grid(row=4, column=0, columnspan=2, padx=paddx,pady=paddy)
    
    input_user.bind("<Return>", lambda event: aplicacao.autenticar())
    input_password.bind("<Return>", lambda event: aplicacao.autenticar()) 
    
    return tela_login, input_user, input_password, label_info