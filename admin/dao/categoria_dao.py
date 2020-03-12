from contextlib import closing
from database import con
from admin.dao.utils.rows import rows_to_dict, row_to_dict

sql_listar = "SELECT id_categoria, nome, descricao FROM categorias"

sql_localizar = "SELECT id_categoria, nome, descricao FROM categorias WHERE id_categoria = ?"

sql_criar = "INSERT INTO categorias(nome, descricao) VALUES (?, ?)"

sql_atualizar = "UPDATE categorias SET nome = ?, descricao = ? WHERE id_categoria = ?"

sql_remover = "DELETE FROM categorias WHERE id_categoria = ?"

sql_total = "SELECT count(*) total FROM categorias"


def listar():
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(sql_listar)
        return rows_to_dict(cursor.description, cursor.fetchall())


def localizar(id_categoria):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(sql_localizar, (id_categoria, ))
        return row_to_dict(cursor.description, cursor.fetchone())

 
def criar(categoria):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(sql_criar, (categoria.nome, categoria.descricao))
        id_categoria = cursor.lastrowid
        connection.commit()
        return id_categoria


def atualizar(categoria_atualizada):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(sql_atualizar, (categoria_atualizada.nome, categoria_atualizada.descricao, categoria_atualizada.id_categoria))
        connection.commit()


def deletar(id_categoria):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(sql_remover, (id_categoria, ))
        connection.commit()


def total_categorias():
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(sql_total)
        total = row_to_dict(cursor.description, cursor.fetchone())
        return total['total']