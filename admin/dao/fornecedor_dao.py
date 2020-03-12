from contextlib import closing
from database import con
from admin.dao.utils.rows import rows_to_dict, row_to_dict


sql_listar = "SELECT id_fornecedor, nome, telefone, email, endereco FROM fornecedores"

sql_localizar = "SELECT id_fornecedor, nome, telefone, email, endereco FROM fornecedores WHERE id_fornecedor = ?"

sql_criar = "INSERT INTO fornecedores(nome, telefone, email, endereco) VALUES (?, ?, ?, ?)"

sql_atualizar = "UPDATE fornecedores SET nome = ?, telefone = ?, email = ?, endereco = ? WHERE id_fornecedor = ?"

sql_remover = "DELETE FROM fornecedores WHERE id_fornecedor = ?"

sql_total = "SELECT count(*) total FROM fornecedores"


def listar():
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(sql_listar)
        return rows_to_dict(cursor.description, cursor.fetchall())


def localizar(id_fornecedor):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(sql_localizar, (id_fornecedor, ))
        return row_to_dict(cursor.description, cursor.fetchone())

 
def criar(fornecedor):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(sql_criar, (fornecedor.nome, fornecedor.telefone, fornecedor.email, fornecedor.endereco))
        id_fornecedor = cursor.lastrowid
        connection.commit()
        return id_fornecedor


def atualizar(fornecedor_atualizado):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(sql_atualizar, (fornecedor_atualizado.nome, fornecedor_atualizado.telefone, fornecedor_atualizado.email,
                                        fornecedor_atualizado.endereco, fornecedor_atualizado.id_fornecedor))
        connection.commit()


def deletar(id_fornecedor):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(sql_remover, (id_fornecedor, ))
        connection.commit()


def total_fornecedores():
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(sql_total)
        total = row_to_dict(cursor.description, cursor.fetchone())
        return total['total']