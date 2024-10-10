import tkinter as tk 

from tkinter import messagebox 

janela = tk.Tk()
janela.title("Interface Gráfica com Imagem")

imagem = tk.PhotoImage(file="imagem.gif")

rotulo = tk.Label(janela, image=imagem)
rotulo.pack()
rotulo1 = tk.Label(janela, text= "Essa é uma interface gráfica com imagem!")
rotulo1.pack()

def mostrar_mensagem():
    messagebox.showinfo("Informação","Botão Clicado!")

botaoimg = tk.PhotoImage(file="botao1.png")
botao = tk.Button(janela, image=botaoimg, command=mostrar_mensagem)
botao.pack()

janela.mainloop()