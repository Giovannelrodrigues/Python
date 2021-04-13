import sqlite3
from sqlite3 import Error
import os
from tkinter import *
try: 
    import tkinter as tk
except:
    import tkinter as tk

class Agenda():
    def __init__(self):
        self.a = 0
        self.programa = tk.Tk()
        self.programa.geometry('150x230')
        self.programa.title('Agenda')
        self.programa.configure(background='black')
        #botoes
        Label(self.programa,text='Banco de Dados',background='Cyan', foreground='Black').place(x=25,y=10,width=100,height=20)
        Button(self.programa,text='Inserir Registro',command=self.MenuInserir).place(x=25,y=50,width=100,height=20)
        Button(self.programa,text='Deletar Registro',command=self.MenuDeletar).place(x=25,y=80,width=100,height=20)
        Button(self.programa,text='Atualizar Registro',command=self.MenuAtualizar).place(x=25,y=110,width=100,height=20)
        Button(self.programa,text='Consultar IDs',command=self.MenuConsultar).place(x=25,y=140,width=100,height=20)
        Button(self.programa,text='Sair do Programa',command=self.SairDoPrograma).place(x=25,y=170,width=100,height=20)
        self.programa.mainloop()

    def MenuInserir(self):
        self.programa.destroy()
        self.MenuInserir = tk.Tk()
        self.MenuInserir.geometry('500x300')
        self.MenuInserir.title('Inserir')
        self.MenuInserir.configure(background='black')

        Label(self.MenuInserir,text='Nome:',background='Cyan', foreground='Black').place(x=10,y=10,width=70,height=20)
        Label(self.MenuInserir,text='Email:',background='Cyan', foreground='Black').place(x=10,y=40,width=70,height=20)
        Label(self.MenuInserir,text='Telefone:',background='Cyan', foreground='Black').place(x=10,y=70,width=70,height=20)
        Label(self.MenuInserir,text='OBS:',background='Cyan', foreground='Black').place(x=10, y=100, width=70, height=20)
        
        self.nome = Entry(self.MenuInserir)
        self.nome.place(x=110,y=10, width=150, height=19)

        self.email = Entry(self.MenuInserir)
        self.email.place(x=110,y=40, width=150, height=19)

        self.telefone = Entry(self.MenuInserir)
        self.telefone.place(x=110,y=70, width=150, height=19)
        
        self.obs = Text(self.MenuInserir)
        self.obs.place(x=110,y=100, width=300, height=60)

        Button(self.MenuInserir,text='Voltar',command=self.Voltar).place(x=10,y=250,width=180,height=40)
        Button(self.MenuInserir,text='Confirmar',command=self.InserirBanco).place(x=10,y=200,width=180,height=40)
        self.MenuInserir.mainloop()

    def MenuDeletar(self):
        self.programa.destroy()
        self.MenuDeletar = tk.Tk()
        self.MenuDeletar.geometry('300x150')
        self.MenuDeletar.title('Deletar')
        self.MenuDeletar.configure(background='black')

        Label(self.MenuDeletar,text='Digite O Id Que deseja deletar:').place(x=10,y=10,width=170,height=19)
        self.num = Entry(self.MenuDeletar)
        self.num.place(x=200,y=10,width=50,height=19)

        Button(self.MenuDeletar,text='Voltar',command=self.Voltar).place(x=10,y=70,width=135,height=40)
        Button(self.MenuDeletar,text='Deletar',command=self.DeletarBanco).place(x=155,y=70,width=135,height=40)

    def MenuAtualizar(self):
        self.programa.destroy()
        self.MenuAtualizar = tk.Tk()
        self.MenuAtualizar.geometry('400x300')
        self.MenuAtualizar.title('Atualizar')
        self.MenuAtualizar.configure(background='Blue')

        Label(self.MenuAtualizar,text='ID').place(x=10,y=10,width=50,height=19)
        Label(self.MenuAtualizar,text='Atualizar Nome').place(x=10,y=40,width=100,height=19)
        Label(self.MenuAtualizar,text='Atualizar Email').place(x=10,y=70,width=100,height=19)
        Label(self.MenuAtualizar,text='Atualizar Telefone').place(x=10,y=100,width=100,height=19)
        Label(self.MenuAtualizar,text='Atualizar OBS').place(x=10,y=130,width=100,height=19)

        Button(self.MenuAtualizar,text='Voltar',command=self.Voltar).place(x=15,y=220,width=135,height=50)
        Button(self.MenuAtualizar,text='Atualizar',command=self.AtualizarBanco).place(x=250,y=220,width=135,height=50)

        self.ind = Entry(self.MenuAtualizar)
        self.ind.place(x=120,y=10,width=50, height=19)

        self.nome = Entry(self.MenuAtualizar)
        self.nome.place(x=120,y=40, width=130, height=19)

        self.email = Entry(self.MenuAtualizar)
        self.email.place(x=120,y=70, width=130, height=19)

        self.telefone = Entry(self.MenuAtualizar)
        self.telefone.place(x=120,y=100, width=130, height=19)

        self.obs = Text(self.MenuAtualizar)
        self.obs.place(x=120,y=130, width=250, height=60)

        self.MenuAtualizar.mainloop()

    def MenuConsultar(self):
        self.programa.destroy()
        self.MenuConsultar = tk.Tk()
        self.MenuConsultar.geometry('450x700')
        self.MenuConsultar.title('Consultar')
        self.MenuConsultar.configure(background='Blue')

        Button(self.MenuConsultar,text='Voltar',command=self.Voltar).place(x=10,y=620,width=135,height=50)

        self.caminho = 'C:\\temp\\PY-VSCODE-2020\\Python\\Modulos\\CEV\Agenda\\AgendaPython.db'
        self.con=None
        
        try:
            self.con=sqlite3.connect(self.caminho)
        except Error as ex:
            print(ex)

        sql = f'SELECT * FROM TB_CONTATOS'
        c=self.con.cursor()
        c.execute(sql)
        res = c.fetchall()
        for r in res:
            self.a += 30
            Label(self.MenuConsultar,text=f'ID:{r[0]}     Nome:{r[1]}     Email:{r[2]}    Número:{r[3]}').place(x=10, y=self.a, width=400, height=25)


    def SairDoPrograma(self):
        self.programa.destroy()
    
    def Voltar(self):
        try:
            self.MenuInserir.destroy()
        except:
            pass
        else:
            Agenda()
        
        try:
            self.MenuDeletar.destroy()
        except:
            pass
        else:
            Agenda()
        
        try:
            self.MenuAtualizar.destroy()
        except:
            pass
        else:
            Agenda()
        
        try:
            self.MenuConsultar.destroy()
        except:
            pass
        else:
            Agenda()

    def InserirBanco(self):
        self.caminho = 'C:\\temp\\PY-VSCODE-2020\\Python\\Modulos\\CEV\Agenda\\AgendaPython.db'
        self.con=None

        try:
            self.con=sqlite3.connect(self.caminho)
        except Error as ex:
            print(ex)

        sql= f'INSERT INTO TB_CONTATOS(NOME_CONTATO,EMAIL_CONTATO,TELEFONE_CONTATO, TB_OBS) VALUES("{self.nome.get()}","{self.email.get()}","{self.telefone.get()}","{self.obs.get("1.0", END)}")'
        
        try:
            c=self.con.cursor()
            c.execute(sql)
            self.con.commit()
        except Error as ex:
            print(ex)
        
        self.Voltar()
        
            
    def DeletarBanco(self):
        self.caminho = 'C:\\temp\\PY-VSCODE-2020\\Python\\Modulos\\CEV\Agenda\\AgendaPython.db'
        self.con=None

        try:
            self.con=sqlite3.connect(self.caminho)
        except Error as ex:
            print(ex)
        
        sql = f'DELETE FROM TB_CONTATOS WHERE ID_CONTATO={self.num.get()}'
        try:
            c=self.con.cursor()
            c.execute(sql)
            self.con.commit()
        except Error as ex:
            print(ex)
        self.Voltar()

    def AtualizarBanco(self):
        self.caminho = 'C:\\temp\\PY-VSCODE-2020\\Python\\Modulos\\CEV\Agenda\\AgendaPython.db'
        self.con=None

        try:
            self.con=sqlite3.connect(self.caminho)
        except Error as ex:
            print(ex)
        
        sql = f'UPDATE TB_CONTATOS SET NOME_CONTATO="{self.nome.get()}", EMAIL_CONTATO="{self.email.get()}", TELEFONE_CONTATO="{self.telefone.get()}", TB_OBS="{self.obs.get("1.0", END)}" WHERE ID_CONTATO={self.ind.get()}'

        try:
            c=self.con.cursor()
            c.execute(sql)
            self.con.commit()
        except Error as ex:
            print(ex)
        
        self.Voltar()

Agenda()
