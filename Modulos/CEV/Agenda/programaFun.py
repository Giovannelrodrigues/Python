import sqlite3
from sqlite3 import Error
import os

def mostrar_tela():
    os.system('cls')
    print('======================')
    print('======SUA AGENDA======')
    print('======================')
    print('1 =   Inserir Registro')
    print('2 -   Deletar Registro')
    print('3 = Atualizar Registro')
    print('4 -       Consultar ID')
    print('5 =    Consultar Nomes')
    print('6 -   Sair do Programa')
    escolha = int(input('Digite um dos valores correspondente:'))
    while escolha > 6:
        escolha = int(input('Digite um dos valores correspondente:'))

    return escolha

def conexao():
    caminho = 'C:\\temp\\PY-VSCODE-2020\\Python\\Modulos\\CEV\Agenda\\AgendaPython.db'
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    else:
        return con

def Inserir(conexao):

    nome = str(input('Digite o nome:'))
    while len(nome) > 30:
        nome = str(input('Abaixo de 30 caractere,Digite o nome:'))

    email = str(input('Digite um email:'))
    while len(email) > 30:
        email = str(input('Abaixo de 30 caractere,Digite o email:'))

    telefone = str(input('Digite o telefone:'))
    while len(telefone) > 14:
        telefone = str(input('Abaixo de 14 caractere,Digite o telefone:'))
    
    sql= f'INSERT INTO TB_CONTATOS(NOME_CONTATO,EMAIL_CONTATO,TELEFONE_CONTATO) VALUES("{nome}","{email}","{telefone}")'

    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    else:
        print('Registro Inserido')

def deletar(conexao):
    num = int(input('Digite o Id que deseja deletar: [0]Listar'))
    if num == 0:
            consulta(conexao)
    while True:
        sql = f'DELETE FROM TB_CONTATOS WHERE ID_CONTATO="{num}"'
        try:
            c=conexao.cursor()
            c.execute(sql)
            conexao.commit()
        except Error as ex:
            print(ex)
        finally:
            break
    

def atualizar(conexao):
    var = 0
    sql=''
    while var != 6:
        os.system('cls')
        print('1 =     Mudar nome')
        print('2 -    Mudar email')
        print('3 = Mudar telefone')
        print('4 -           Tudo')
        print('5 =         listar')
        print('6 -         Voltar')

        var = int(input('Digite o valor correspondente:'))
        if var == 1:
            num = int(input('Digite o id que deseja atualizar:[0]voltar:'))
            if num == 0:
                break
            nome = input('Digite o novo nome:')
            while len(nome) > 30:
                 nome = input('Nome maior que 30 letras, Digite o novo nome:')
                
            sql = f'UPDATE TB_CONTATOS SET NOME_CONTATO="{nome}" WHERE ID_CONTATO={num}'    

        if var == 2:
            num = int(input('Digite o id que deseja excluir:[0]voltar:'))
            if num == 0:
               break
            email = input('Digite o novo email:')
            while len(email) > 30:
                email = input('Email maior que 30 letras, Digite o novo email:')

            sql = f'UPDATE TB_CONTATOS SET EMAIL_CONTATO="{email}" WHERE ID_CONTATO={num}'
            
        if var == 3:
            num = int(input('Digite o id que deseja excluir:[0]voltar:'))
            if num == 0:
                break
            telefone = input('Digite o novo telefone:')
            while len(telefone) > 14:
                telefone = input('Telefone maior que 14 numeros, Digite o novo telefone:')

            sql = f'UPDATE TB_CONTATOS SET TELEFONE_CONTATO="{telefone}" WHERE ID_CONTATO={num}'
            
        if var == 4:
            num = int(input('Digite o id que deseja excluir:[0]voltar:'))
            if num == 0:
                break
            nome = input('Digite o novo nome:')
            while len(nome) > 30:
                nome = input('Nome maior que 30 letras, Digite o novo nome:')
                
            email = input('Digite o novo email:')
            while len(email) > 30:
                email = input('Email maior que 30 letras, Digite o novo email:')
                
            telefone = input('Digite o novo telefone:')
            while len(telefone) > 14:
                 telefone = input('Telefone maior que 14 numeros, Digite o novo telefone:')
                
            sql = f'UPDATE TB_CONTATOS SET NOME_CONTATO="{nome}", EMAIL_CONTATO="{email}", TELEFONE_CONTATO="{telefone}" WHERE ID_CONTATO={num}'


        if var ==5:
            consulta(conexao)

        if sql != '':
            try:
                c=conexao.cursor()
                c.execute(sql)
                conexao.commit()
            except Error as ex:
                print(ex)
            
def consulta(conexao):
    sql = f'SELECT * FROM TB_CONTATOS'
    c=conexao.cursor()
    c.execute(sql)
    res = c.fetchall()
    print('======================================================')
    for r in res:
        print(f'ID:{r[0]} Nome:{r[1]} Email:{r[2]} Número:{r[3]}')
    print('======================================================')
    enter = input('Digite enter para continuar')

def consultaNome(conexao):
    con = input('Digite o nome que deseja consultar:')
    sql = f'SELECT * FROM TB_CONTATOS WHERE NOME_CONTATO LIKE "%{con}%"'
    c=conexao.cursor()
    c.execute(sql)
    res = c.fetchall()
    print('======================================================')
    for r in res:
        print(f'ID:{r[0]} Nome:{r[1]} Email:{r[2]} Número:{r[3]}')
    print('======================================================')
    enter = input('Digite enter para continuar')