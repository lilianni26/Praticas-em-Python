#Autor: Lilianni Nayara
#Data: 11/10/2024
#código: Exemplo de interfce no Tkinter

from tkinder import*

root = Tk()


class Application():
    def __init__ (self):
        self.root = root
        self.tela()

    def tela(self):
         self.root.title("Cadastro FMF de Clientes")
         self.root.configure(backgound= 'purple')
         self.root.geometry('900x500')
         self.root.resizable(True,True)
         self.root.maxsize(width=1000, height=650)
         self.root.sinsize(width=300, height=200)
    def frame_da_tela(self):
         self.frames_1 = Frame(self,root, bd=4, bg='yellow', highlightbackground='#FF1493',highlightthickness='3')
         self.frames_1.place(relx=0.02, relwidth=0.96, relheight=0.46)

         self.frame_2 = Frame(self.root, bd=4,bg='#dfe3ee', highlightbackground='3')

Application()