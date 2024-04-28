import sys

sys.dont_write_bytecode = True

import tkinter as tk
from telas.telaLogin import criar_tela_login
from telas.telaPrincipal import tela_principal

class Aplicacao(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configurar_janela()
        self.tela_login, self.entry_usuario, self.entry_senha, self.mensagem_erro = criar_tela_login(self)

    def configurar_janela(self):
        self.title("aplicação de login")
        self.geometry("800x700")
        self.resizable(False, False)
        self.configure(background="#000000", padx=0, pady=0)
    
    def efetuar_login(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()
        
        # Verificar as credenciais do usuário (exemplo: usuário: admin, senha: admin)
        if usuario == "admin" and senha == "admin":
            # Chamar a função para carregar a nova tela
            self.tela_principal = tela_principal(aplicacao=self)
            # Destruir a tela de login
            self.tela_login.destroy()
        else:
            self.mensagem_erro.config(text="Usuário ou senha incorretos",foreground="red")
    
    def fazer_logout(self):
        # Destruir a nova tela
        self.tela_principal.destroy()
        # Recriar a tela de login
        self.tela_login, self.entry_usuario, self.entry_senha, self.mensagem_erro = criar_tela_login(self)

def main():
    app = Aplicacao()
    app.mainloop()

if __name__ == "__main__":
    main()
