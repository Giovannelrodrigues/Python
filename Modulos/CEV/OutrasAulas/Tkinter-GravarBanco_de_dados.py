from tkinter import *

programa =Tk()
programa.title('Meu Programa')
programa.geometry('500x300')
programa.configure(background="gray69")

#anchor N=NORTE, S=SUL, E=LESTE, W=OESTE, 
#NE=NORDESTE, SE=SUDESTE, SO=SUDOESTE, NO=NOROESTE
#entry
Label(programa,text="Nome",background="snow",foreground="Blue", anchor=W).place(x=10,y=10,width=100,height=20)
vnome = Entry(programa)
vnome.place(x=150,y=10,width=250,height=20)

Label(programa,text="Email",background="snow",foreground="Blue", anchor=W).place(x=10,y=40,width=100,height=20)
vemail = Entry(programa)
vemail.place(x=150,y=40,width=250,height=20)

Label(programa,text="Telefone",background="snow",foreground="blue", anchor=W).place(x=10,y=70,width=100,height=20)
vtelefone = Entry(programa)
vtelefone.place(x=150,y=70,width=100,height=20)

#text usase para texto com mais de uma linha
Label(programa,text="OBS:",background="snow",foreground="blue", anchor=W).place(x=10,y=110,width=100,height=20)
vobs = Text(programa)
vobs.place(x=10,y=140,width=200,height=50)

programa.mainloop()