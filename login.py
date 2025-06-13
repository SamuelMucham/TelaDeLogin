from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox

co0 = "#000000"
co1 = "#01fed0"
co2 = "#4b7dfb"
co3 = "#60ffaf"
co4 = "#5ECCFF"

janela = Tk()
janela.title("")
janela.geometry('310x300')
janela.resizable(False, False)

Frame_cima = Frame(janela, width=301, height=50, bg=co1, relief="flat")
Frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

Frame_baixo = Frame(janela, width=310, height=300, bg=co1, relief="flat")
Frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

l_nome = Label(Frame_cima, text="LOGIN", height=1, anchor=NE, font=('Ivy 25'), bg=co1, fg=co4)
l_nome.place(x=5, y=5)

l_linha = Label(Frame_cima, width=275, text="", height=1, anchor=NW, font=('Ivy 1'), bg=co2)
l_linha.place(x=10, y=45)

credenciais = ['samuel', '12345']

def verificar_senha():
    nome = e_nome.get()
    senha = str(e_pass.get())

    if nome == 'admin' and senha == 'admin':
        messagebox.showinfo('Login', 'Seja muito bem-vindo(a), administrador(a). É uma honra contar com a sua presença')

    elif credenciais[0] == nome and credenciais[1] == senha:
        messagebox.showinfo('Login', 'Desejamos que aproveite ao máximo essa experiência. ' + credenciais[0])

        for widget in Frame_baixo.winfo_children():
            widget.destroy()

        for widget in Frame_cima.winfo_children():
            widget.destroy()

        nova_janela()
    else:
        messagebox.showwarning('Error', 'Verifique o nome de usuário ou a palavra passe')

def nova_janela():
    l_nome = Label(Frame_cima, text="Usuário " + credenciais[0], height=1, anchor=NE, font=('Ivy 20'), bg=co1, fg=co4)
    l_nome.place(x=5, y=5)

    l_linha = Label(Frame_cima, width=275, text="", height=1, anchor=NW, font=('Ivy 1'), bg=co2)
    l_linha.place(x=10, y=45)

    l_bemvindo = Label(Frame_baixo, text="Seja bem vindo " + credenciais[0], height=1, anchor=NE, font=('Ivy 20'), bg=co1, fg=co4)
    l_bemvindo.place(x=5, y=105)

l_nome = Label(Frame_baixo, text="Nome *", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome.place(x=10, y=20)

e_nome = Entry(Frame_baixo, width=25, justify='left', font=("", 15), highlightbackground=co1, relief="solid")
e_nome.place(x=14, y=50)

l_pass = Label(Frame_baixo, text="Senha *", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_pass.place(x=10, y=100)

e_pass = Entry(Frame_baixo, show='*', width=25, justify='left', font=("", 15), highlightbackground=co1, relief="solid")
e_pass.place(x=14, y=130)

botao_confimar = Button(Frame_baixo, text="Entrar", width=39, height=2, bg=co2, fg=co1, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE, command=verificar_senha)
botao_confimar.place(x=15, y=180)

janela.mainloop()