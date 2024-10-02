from tkinter import *

cor1 = "#3b3b3b"
cor2 = "#feffff"
cor3 = "#38576b"
cor4 = "#eceff1"
cor5 = "#ffab40"

janela = Tk()

janela.title("Calculadora")
janela.geometry("310x450")
janela.config(bg=cor1)

frame_tela = Frame(janela, width=310, height=100, bg = cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=310, height=350)
frame_corpo.grid(row=1, column=0)


valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height= 3, padx = 7, relief = FLAT, anchor="e", justify=RIGHT, font = ("Ivy 23"), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)
app_label.place(x=10, y=0)



def calcular():
    resultado = eval(valor_texto.get()) 

    valor_texto.set(resultado)


def entrar_valores(valor):
    valor_texto.set(valor_texto.get() + valor)

def limpar():
    valor_texto.set("")



b1 = Button(frame_corpo, command=lambda: limpar() ,text="C", width=15, height=3, bg = cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b1.place(x=0, y=0)

b2 = Button(frame_corpo, command= lambda: entrar_valores("%"),text="%", width=7, height=3, bg = cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b2.place(x=155, y=0)

b3 = Button(frame_corpo, command= lambda: entrar_valores("/"), text="/", width=7, height=3, bg = cor5, fg=cor2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b3.place(x=235, y=0)



b4 = Button(frame_corpo, command= lambda: entrar_valores("7"), text="7", width=7, height=3, bg = cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b4.place(x=0, y=70)

b5 = Button(frame_corpo, command= lambda: entrar_valores("8"), text="8", width=7, height=3, bg = cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b5.place(x=77, y=70)

b6 = Button(frame_corpo, command= lambda: entrar_valores("9") ,text="9", width=7, height=3, bg = cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b6.place(x=155, y=70)

b7 = Button(frame_corpo, command= lambda: entrar_valores("*") ,text="*", width=7, height=3, bg = cor5, fg=cor2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b7.place(x=235, y=70)



b8 = Button(frame_corpo, command= lambda: entrar_valores("4") ,text="4", width=7, height=3, bg = cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b8.place(x=0, y=140)

b9 = Button(frame_corpo, command= lambda: entrar_valores("5") ,text="5", width=7, height=3, bg = cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b9.place(x=77, y=140)

b10 = Button(frame_corpo, command= lambda: entrar_valores("6") ,text="6", width=7, height=3, bg = cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b10.place(x=155, y=140)

b11 = Button(frame_corpo, command= lambda: entrar_valores("-") ,text="-", width=7, height=3, bg = cor5, fg=cor2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b11.place(x=235, y=140)



b12 = Button(frame_corpo, command= lambda: entrar_valores("1") ,text="1", width=7, height=3, bg = cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b12.place(x=0, y=210)

b13 = Button(frame_corpo, command= lambda: entrar_valores("2") ,text="2", width=7, height=3, bg = cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b13.place(x=77, y=210)

b14 = Button(frame_corpo, command= lambda: entrar_valores("3") ,text="3", width=7, height=3, bg = cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b14.place(x=155, y=210)

b15 = Button(frame_corpo, command= lambda: entrar_valores("+") , text="+", width=7, height=3, bg = cor5, fg=cor2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b15.place(x=235, y=210)



b16 = Button(frame_corpo, command= lambda: entrar_valores("0") ,text="0", width=15, height=3, bg = cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b16.place(x=0, y=280)

b17 = Button(frame_corpo, command= lambda: entrar_valores(".") , text=".", width=7, height=3, bg = cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b17.place(x=155, y=280)

b18 = Button(frame_corpo, command= lambda: calcular() ,text="=", width=7, height=3, bg = cor5, fg=cor2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b18.place(x=235, y=280)



janela.mainloop()
