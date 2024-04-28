import customtkinter as ctk
from PIL import Image

from telas.barraNavegacao import criar_barra_navegacao

def configurar_janela(aplicacao):
    aplicacao.geometry("700x600")
    aplicacao.grid_rowconfigure(4, weight=1)
    aplicacao.grid_columnconfigure(2, weight=1)
    aplicacao.minsize(600, 400)
    aplicacao.resizable(True,True)
    aplicacao.update_idletasks()  # Atualizar tarefas pendentes
    largura_aplicacao = aplicacao.winfo_width()
    altura_aplicacao = aplicacao.winfo_height()

    largura_tela = aplicacao.winfo_screenwidth()
    altura_tela = aplicacao.winfo_screenheight()

    posicao_x = (largura_tela - largura_aplicacao) // 3
    posicao_y = (altura_tela - altura_aplicacao) // 3

    aplicacao.geometry(f"+{posicao_x}+{posicao_y}")

def tela_principal(aplicacao):
    configurar_janela(aplicacao)
    tela_principal = ctk.CTkFrame(aplicacao, fg_color="transparent")
    tela_principal.grid(row=0, column=1)
    
    
    
    
    return tela_principal
    
    
    
    
    