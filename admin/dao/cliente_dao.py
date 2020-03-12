from contextlib import closing
from database import con
from admin.dao.utils.rows import rows_to_dict, row_to_dict


sql_listar = "SELECT id_cliente, nome, cpf, rg, telefone, email, endereco FROM clientes"

sql_localizar = "SELECT id_cliente, nome, cpf, rg, telefone, email, endereco FROM clientes WHERE id_cliente = ?"

sql_criar = "INSERT INTO clientes(nome, cpf, rg, telefone, email, endereco) VALUES (?, ?, ?, ?, ?, ?)"

sql_atualizar = "UPDATE clientes SET nome = ?, cpf = ?, rg = ?, telefone = ?, email = ?, endereco = ? WHERE id_cliente = ?"

sql_remover = "DELETE FROM clientes WHERE id_cliente = ?"

sql_total = "SELECT count(*) total FROM clientes"


def listar():
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(sql_listar)
        return rows_to_dict(cursor.description, cursor.fetchall())


def localizar(id_cliente):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(sql_localizar, (id_cliente, ))
        return row_to_dict(cursor.description, cursor.fetchone())

 
def criar(cliente):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(sql_criar, (cliente.nome, cliente.cpf, cliente.rg, cliente.telefone, cliente.email, cliente.endereco))
        id_cliente = cursor.lastrowid
        connection.commit()
        return id_cliente


def atualizar(cliente_atualizado):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(sql_atualizar, (cliente_atualizado.nome, cliente_atualizado.cpf, cliente_atualizado.rg,
                                        cliente_atualizado.telefone, cliente_atualizado.email,
                                        cliente_atualizado.endereco, cliente_atualizado.id_cliente))
        connection.commit()


def deletar(id_cliente):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(sql_remover, (id_cliente, ))
        connection.commit()


def total_clientes():
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(sql_total)
        total = row_to_dict(cursor.description, cursor.fetchone())
        return total['total']