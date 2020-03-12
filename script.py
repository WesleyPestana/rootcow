from database import con
import sqlite3
from contextlib import closing


sql_clientes = '''INSERT INTO clientes (nome, cpf, rg, telefone, email, endereco)
VALUES
    ('Wesley', '11111', '11111', '1111-1111', 'wes@wes.com', 'Rua Wes'),
    ('Daniel', '22222', '22222', '2222-2222', 'dan@dan.com', 'Rua Dan'),
    ('Bruno', '33333', '33333', '3333-3333', 'bruno@bruno.com', 'Rua Bruno'),
    ('Jonathan', '44444', '44444', '4444-4444', 'jhow@jhow.com', 'Rua Jonathan'),
    ('Marcelo', '55555', '55555', '5555-5555', 'marcelo@marcelo.com', 'Rua Marcelo');
'''

sql_fornecedores = '''INSERT INTO fornecedores (nome, telefone, email, endereco)
VALUES
    ('Joao', '1111-1111', 'joao@joao.com', 'Rua Joao'),
    ('Maria', '2222-2222', 'maria@maria.com', 'Rua Maria'),
    ('Jose', '3333-3333', 'jose@jose.com', 'Rua Jose'),
    ('Marcela', '4444-4444', 'marcela@marcela.com', 'Rua Marcela'),
    ('Jorge', '5555-5555', 'jorge@jorge.com', 'Rua Jorge');
'''

sql_instituicoes = '''INSERT INTO instituicoes (nome, telefone, email, endereco)
VALUES
    ('Ar', '1111-1111', 'ar@ar.com', 'Rua Ar'),
    ('Água', '2222-2222', 'agua@agua.com', 'Rua Água'),
    ('Éter', '3333-3333', 'eter@eter.com', 'Rua Éter'),
    ('Fogo', '4444-4444', 'fogo@fogo.com', 'Rua Fogo'),
    ('Terra', '5555-5555', 'terra@terra.com', 'Rua Terra');
'''

sql_categorias = '''INSERT INTO categorias (nome, descricao)
VALUES
    ('Doce', 'Alimentos doces'),
    ('Salgado', 'Alimentos salgados'),
    ('Acidos', 'Alimentos acidos'),
    ('Cosméticos P', 'Cosméticos em pó'),
    ('Cosméticos L', 'Cosméticos liquídos');
'''

sql_produtos = '''INSERT INTO produtos (nome, quantidade, valorcompra, valorvenda, descricao, fk_id_categoria, fk_id_fornecedor)
VALUES
    ('Banana', 10, '10.00', '100.00', 'Banana', 1, 1),
    ('Feijão', 20, '20.00', '200.00', 'Feijão', 2, 2),
    ('Laranja', 30, '30.00', '300.00', 'Laranja', 3, 3),
    ('Base', 40, '40.00', '400.00', 'Base', 4, 4),
    ('Asepxia', 50, '50.00', '500.00', 'Asepxia', 5, 5);
'''

with closing(con()) as connection, closing(connection.cursor()) as cursor:
    for query in [sql_clientes, sql_fornecedores, sql_instituicoes, sql_categorias, sql_produtos]:    
        cursor.execute(query)
        connection.commit()
        
