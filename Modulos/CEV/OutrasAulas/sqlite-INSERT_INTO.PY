import sqlite3
from sqlite3 import Error


def ConexaoBanco():
    caminho = 'C:\\temp\\PY-VSCODE-2020\\SQLite\\Agenda.db'
    con=None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    else:
        return con


def inserir(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print('Valor Inserido')
    except Error as ex:
        print(ex)


nome = input('Digite um nome:')
telefone = input('Digite o telefone:')
email = input('Digite o email:')

vsql = f'INSERT INTO tb_contatos(T_NOMECONTATO,T_TELEFONECONTATO,T_EMAILCONTATO) VALUES("{nome}","{telefone}","{email}")'
vcon = ConexaoBanco()
inserir(vcon, vsql)

