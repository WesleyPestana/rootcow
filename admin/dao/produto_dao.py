from contextlib import closing
from database import con
from admin.dao.utils.rows import rows_to_dict, row_to_dict
from admin.models.produto import Produto


sql_listar = "SELECT p.id_produto, p.nome, p.quantidade, p.valorcompra, p.valorvenda, p.descricao, \
            c.id_categoria fk_id_categoria, f.id_fornecedor fk_id_fornecedor \
            FROM produtos as p\
            INNER JOIN categorias as c on p.fk_id_categoria = c.id_categoria \
            INNER JOIN fornecedores as f on p.fk_id_fornecedor = f.id_fornecedor"

sql_localizar = "SELECT id_produto, nome, descricao, valorcompra, valorvenda, quantidade, fk_id_categoria, fk_id_fornecedor \
                FROM produtos WHERE id_produto = ?"

sql_criar = "INSERT INTO produtos (nome, quantidade, valorcompra, valorvenda, descricao, fk_id_categoria, fk_id_fornecedor) VALUES (?, ?, ?, ?, ?, ?, ?)"

sql_atualizar = "UPDATE produtos SET nome = ?, quantidade = ?, valorcompra = ?, valorvenda = ?, descricao = ?, fk_id_categoria = ?, \
                fk_id_fornecedor = ? WHERE id_produto = ?"

sql_remover = "DELETE FROM produtos WHERE id_produto = ?"

sql_total = "SELECT count(*) total FROM produtos"


def listar():
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(sql_listar)
        return rows_to_dict(cursor.description, cursor.fetchall())


def localizar(id_produto):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(sql_localizar, (id_produto, ))
        return row_to_dict(cursor.description, cursor.fetchone())

 
def criar(produto):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        print(produto)
        cursor.execute(sql_criar, (produto.nome, produto.quantidade, produto.valor_compra, produto.valor_venda, produto.descricao, 
                                    produto.categoria.id_categoria, produto.fornecedor.id_fornecedor))
        id_produto = cursor.lastrowid
        connection.commit()
        return id_produto


def atualizar(produto_atualizado):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(sql_atualizar, (produto_atualizado.nome, produto_atualizado.quantidade, produto_atualizado.valor_compra, 
                                        produto_atualizado.valor_venda, produto_atualizado.descricao, produto_atualizado.categoria.id_categoria, 
                                        produto_atualizado.fornecedor.id_fornecedor, produto_atualizado.id_produto))
        connection.commit()


def deletar(id_produto):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(sql_remover, (id_produto, ))
        connection.commit()


def total_produtos():
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(sql_total)
        total = row_to_dict(cursor.description, cursor.fetchone())
        return total['total']