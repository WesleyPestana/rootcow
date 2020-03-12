from admin.models.categoria import Categoria
from admin.dao import categoria_dao


def listar():
    categorias = []
    categorias_bd = categoria_dao.listar()
    for categoria_bd in categorias_bd:
        categorias.append(Categoria(categoria_bd['nome'], categoria_bd['descricao'], categoria_bd['id_categoria']))
    return categorias


def localizar(id_categoria):
    categoria_bd = categoria_dao.localizar(id_categoria)
    return Categoria(categoria_bd['nome'], categoria_bd['descricao'], categoria_bd['id_categoria'])

 
def criar(nome, descricao):
    nova_categoria = Categoria(nome, descricao)
    nova_categoria.id_categoria = categoria_dao.criar(nova_categoria)
    return nova_categoria


def atualizar(id_categoria, nome, descricao):
    categoria_atualizada = Categoria(nome, descricao, id_categoria)
    categoria_dao.atualizar(categoria_atualizada)
    return categoria_atualizada


def deletar(id_categoria):
    categoria = localizar(id_categoria)
    categoria_dao.deletar(id_categoria)
    return categoria
