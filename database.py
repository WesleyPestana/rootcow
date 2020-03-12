import sqlite3
from contextlib import closing

sql_create = '''CREATE TABLE IF NOT EXISTS clientes (
id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
nome VARCHAR(80) NOT NULL,
cpf VARCHAR(15) NOT NULL,
rg VARCHAR(15) NOT NULL,
telefone VARCHAR(15) NOT NULL,
email VARCHAR(60) NOT NULL,
endereco VARCHAR(80) NOT NULL
);

CREATE TABLE IF NOT EXISTS fornecedores (
id_fornecedor INTEGER PRIMARY KEY AUTOINCREMENT,
nome VARCHAR(80) NOT NULL,
telefone VARCHAR(50) NOT NULL,
email VARCHAR(60) NOT NULL,
endereco VARCHAR(80) NOT NULL
);

CREATE TABLE IF NOT EXISTS instituicoes (
id_instituicao INTEGER PRIMARY KEY AUTOINCREMENT,
nome VARCHAR(80) NOT NULL,
telefone VARCHAR(50) NOT NULL,
email VARCHAR(60) NOT NULL,
endereco VARCHAR(80) NOT NULL
);

CREATE TABLE IF NOT EXISTS categorias (
id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
nome VARCHAR(20) NOT NULL,
descricao VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS produtos (
id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
fk_id_categoria INTEGER NOT NULL,
fk_id_fornecedor INTEGER NOT NULL,
nome VARCHAR(60) NOT NULL,
quantidade INTEGER NOT NULL,
valorcompra VARCHAR(10) NOT NULL,
valorvenda VARCHAR(10) NOT NULL,
descricao VARCHAR(100) NOT NULL,
FOREIGN KEY(fk_id_categoria) REFERENCES Categorias(id_categoria),
FOREIGN KEY(fk_id_fornecedor) REFERENCES Fornecedores(id_fornecedor)
);
'''

def con():
    return sqlite3.connect('rootcow.db')


def criar_bd():
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.executescript(sql_create)
        connection.commit()
