import sqlite3
from sqlite3 import Error


#criar conexão com o banco
def ConexaoBanco():
    caminho = 'C:\\temp\\PY-VSCODE-2020\\SQLite\\Agenda.db'
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    else:
        return con

#criar tabela

vsql = """CREATE TABLE tb_contatos(
            N_IDCONTATO INTEGER PRIMARY KEY AUTOINCREMENT,
            T_NOMECONTATO VARCHAR(30),
            T_TELEFONECONTATO VARCHAR(14),
            T_EMAILCONTATO VARCHAR(30)
)"""

def criarTabela(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        print('tabela criada')
    except Error as ex:
        print(ex)

vcon = ConexaoBanco()
criarTabela(vcon,vsql)
vcon.close()
