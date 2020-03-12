from admin.models.instituicao import Instituicao
from admin.dao import instituicao_dao


def listar():
    instituicoes = []
    instituicoes_bd = instituicao_dao.listar()
    for instituicao_bd in instituicoes_bd:
        instituicoes.append(Instituicao(instituicao_bd['nome'], instituicao_bd['telefone'], instituicao_bd['email'], instituicao_bd['endereco'], 
                                        instituicao_bd['id_instituicao']))
    return instituicoes


def localizar(id_instituicao):
    instituicao_bd = instituicao_dao.localizar(id_instituicao)
    return Instituicao(instituicao_bd['nome'], instituicao_bd['telefone'], instituicao_bd['email'], instituicao_bd['endereco'], 
                        instituicao_bd['id_instituicao'])

 
def criar(nome, telefone, email, endereco):
    nova_instituicao = Instituicao(nome, telefone, email, endereco)
    nova_instituicao.id_instituicao = instituicao_dao.criar(nova_instituicao)
    return nova_instituicao


def atualizar(id_instituicao, nome, telefone, email, endereco):
    instituicao_atualizada = Instituicao(nome, telefone, email, endereco, id_instituicao)
    instituicao_dao.atualizar(instituicao_atualizada)
    return instituicao_atualizada


def deletar(id_instituicao):
    instituicao = localizar(id_instituicao)
    instituicao_dao.deletar(id_instituicao)
    return instituicao
