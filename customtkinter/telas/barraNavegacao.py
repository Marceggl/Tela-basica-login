import customtkinter as ctk
from PIL import Image
import os

def criar_barra_navegacao(aplicacao):
    barra_navegacao = ctk.CTkFrame(aplicacao, width=140, corner_radius=0)
    barra_navegacao.grid(row=0, column=0, rowspan=5, sticky="nsew")
    barra_navegacao.grid_rowconfigure(6, weight=1)
    
    fonte_btn = ctk.CTkFont(size=15, weight="bold")
    fonte_autor = ctk.CTkFont(size=12, weight="bold")
    
    image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../img")
    home_icon = ctk.CTkImage(Image.open(os.path.join(image_path, "home.png")), size=(26, 26))
    setting_icon = ctk.CTkImage(Image.open(os.path.join(image_path, "settings.png")), size=(26, 26))
    logout_icon = ctk.CTkImage(Image.open(os.path.join(image_path, "log-out.png")), size=(26, 26))
    
    botao1_navegacao = ctk.CTkButton(barra_navegacao, corner_radius=0,
            height=40,
            border_spacing=10,
            text="Página inicial",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            image=home_icon,
            anchor="w",
            # command=self.evento_btn_autenticar_navegacao,
            font=fonte_btn)
    botao1_navegacao.grid(row=0, column=0, sticky="new")
    
    botao2_navegacao = ctk.CTkButton(barra_navegacao, corner_radius=0,
            height=40,
            border_spacing=10,
            text="Configurações",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            image=setting_icon,
            anchor="w",
            # command=self.evento_btn_autenticar_navegacao,
            font=fonte_btn)
    botao2_navegacao.grid(row=1, column=0, sticky="new")
    
    botao_logout_navegacao = ctk.CTkButton(barra_navegacao, corner_radius=0,
            height=40,
            border_spacing=10,
            text="Sair",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            image=logout_icon,
            anchor="w",
            command=aplicacao.logout,
            font=fonte_btn)
    botao_logout_navegacao.grid(row=6, column=0, sticky="swe")
    
    author = ctk.CTkLabel(
        barra_navegacao,
        text="By Marcel Barreto",
        font=fonte_autor,
    )
    author.grid(row=7, column=0, padx=5, sticky="swe")
    
    return barra_navegacao

    
    
    