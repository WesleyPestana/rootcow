from admin.models.fornecedor import Fornecedor
from admin.dao import fornecedor_dao


def listar():
    fornecedores = []
    fornecedores_bd = fornecedor_dao.listar()
    for fornecedor_bd in fornecedores_bd:
        fornecedores.append(Fornecedor(fornecedor_bd['nome'], fornecedor_bd['telefone'], fornecedor_bd['email'], fornecedor_bd['endereco'], 
                                        fornecedor_bd['id_fornecedor']))
    return fornecedores


def localizar(id_fornecedor):
    fornecedor_bd = fornecedor_dao.localizar(id_fornecedor)
    return Fornecedor(fornecedor_bd['nome'], fornecedor_bd['telefone'], fornecedor_bd['email'], fornecedor_bd['endereco'], 
                        fornecedor_bd['id_fornecedor'])

 
def criar(nome, telefone, email, endereco):
    novo_fornecedor = Fornecedor(nome, telefone, email, endereco)
    novo_fornecedor.id_fornecedor = fornecedor_dao.criar(novo_fornecedor)
    return novo_fornecedor


def atualizar(id_fornecedor, nome, telefone, email, endereco):
    fornecedor_atualizado = Fornecedor(nome, telefone, email, endereco, id_fornecedor)
    fornecedor_dao.atualizar(fornecedor_atualizado)
    return fornecedor_atualizado


def deletar(id_fornecedor):
    fornecedor = localizar(id_fornecedor)
    fornecedor_dao.deletar(id_fornecedor)
    return fornecedor
