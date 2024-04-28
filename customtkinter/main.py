import sys

sys.dont_write_bytecode = True

import customtkinter
from telas.telaLogin import telaLogin
from telas.telaPrincipal import tela_principal
from telas.barraNavegacao import criar_barra_navegacao

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.configurar_janela()
        # Tela de login
        self.tela_login, self.input_user, self.input_password, self.label_info = telaLogin(self)
        
        #Bypass pra próxima
        # tela_principal(self)
        
    def configurar_janela(self):
        self.geometry("800x700")
        
    def logout(self):
        self.tela_principal.destroy()
        self.barra_navegacao.destroy()
        self.tela_login, self.input_user, self.input_password, self.label_info = telaLogin(self)
    
    def autenticar(self):
        if self.input_user.get() == 'admin' and self.input_password.get() == 'admin':
            self.tela_login.destroy()
            self.tela_principal = tela_principal(self)
            self.barra_navegacao = criar_barra_navegacao(self)
            
        elif self.input_user.get() == '' and self.input_password.get() == '':
            self.label_info.configure(text="preencha os campos")
        else:
            self.label_info.configure(text="Erro de autenticação")
            

if __name__ == "__main__":
    app = App()
    app.mainloop()