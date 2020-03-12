from admin.models.cliente import Cliente
from admin.dao import cliente_dao


def listar():
    clientes = []
    clientes_bd = cliente_dao.listar()
    for cliente_bd in clientes_bd:
        clientes.append(Cliente(cliente_bd['nome'], cliente_bd['cpf'], cliente_bd['rg'], cliente_bd['telefone'], cliente_bd['email'], 
                                cliente_bd['endereco'], cliente_bd['id_cliente']))
    return clientes


def localizar(id_cliente):
    cliente_bd = cliente_dao.localizar(id_cliente)
    return Cliente(cliente_bd['nome'], cliente_bd['cpf'], cliente_bd['rg'], cliente_bd['telefone'], cliente_bd['email'], cliente_bd['endereco'], 
                    cliente_bd['id_cliente'])

 
def criar(nome, cpf, rg, telefone, email, endereco):
    novo_cliente = Cliente(nome, cpf, rg, telefone, email, endereco)
    novo_cliente.id_cliente = cliente_dao.criar(novo_cliente)
    return novo_cliente


def atualizar(id_cliente, nome, cpf, rg, telefone, email, endereco):
    cliente_atualizado = Cliente(nome, cpf, rg, telefone, email, endereco, id_cliente)
    cliente_dao.atualizar(cliente_atualizado)
    return cliente_atualizado


def deletar(id_cliente):
    cliente = localizar(id_cliente)
    cliente_dao.deletar(id_cliente)
    return cliente
