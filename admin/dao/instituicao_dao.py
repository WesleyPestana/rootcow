from contextlib import closing
from database import con
from admin.dao.utils.rows import rows_to_dict, row_to_dict


sql_listar = "SELECT id_instituicao, nome, telefone, email, endereco FROM instituicoes"

sql_localizar = "SELECT id_instituicao, nome, telefone, email, endereco FROM instituicoes WHERE id_instituicao = ?"

sql_criar = "INSERT INTO instituicoes(nome, telefone, email, endereco) VALUES (?, ?, ?, ?)"

sql_atualizar = "UPDATE instituicoes SET nome = ?, telefone = ?, email = ?, endereco = ? WHERE id_instituicao = ?"

sql_remover = "DELETE FROM instituicoes WHERE id_instituicao = ?"

sql_total = "SELECT count(*) total FROM instituicoes"


def listar():
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(sql_listar)
        return rows_to_dict(cursor.description, cursor.fetchall())


def localizar(id_instituicao):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(sql_localizar, (id_instituicao, ))
        return row_to_dict(cursor.description, cursor.fetchone())

 
def criar(instituicao):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(sql_criar, (instituicao.nome, instituicao.telefone, instituicao.email, instituicao.endereco))
        id_instituicao = cursor.lastrowid
        connection.commit()
        return id_instituicao


def atualizar(instituicao_atualizada):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(sql_atualizar, (instituicao_atualizada.nome, instituicao_atualizada.telefone, instituicao_atualizada.email,
                                        instituicao_atualizada.endereco, instituicao_atualizada.id_instituicao))
        connection.commit()


def deletar(id_instituicao):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(sql_remover, (id_instituicao, ))
        connection.commit()


def total_instituicoes():
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(sql_total)
        total = row_to_dict(cursor.description, cursor.fetchone())
        return total['total']