from admin.models.produto import Produto
from admin.services.categoria_service import localizar as localizar_categoria
from admin.services.fornecedor_service import localizar as localizar_fornecedor
from admin.dao import produto_dao


def listar():
    produtos = []
    produtos_bd = produto_dao.listar()
    for produto_bd in produtos_bd:
        categoria = localizar_categoria(produto_bd['fk_id_categoria'])
        fornecedor = localizar_fornecedor(produto_bd['fk_id_fornecedor'])
        produtos.append(Produto(produto_bd['nome'], produto_bd['quantidade'], produto_bd['valorcompra'], produto_bd['valorvenda'], produto_bd['descricao'],
                                categoria, fornecedor, produto_bd['id_produto']))
    return produtos


def localizar(id_produto):
    produto_bd = produto_dao.localizar(id_produto)
    categoria = localizar_categoria(produto_bd['fk_id_categoria'])
    fornecedor = localizar_fornecedor(produto_bd['fk_id_fornecedor'])
    return Produto(produto_bd['nome'], produto_bd['quantidade'], produto_bd['valorcompra'], produto_bd['valorvenda'], produto_bd['descricao'],
                    categoria, fornecedor, produto_bd['id_produto'])

 
def criar(nome, quantidade, valor_compra, valor_venda, descricao, id_categoria, id_fornecedor):
    categoria = localizar_categoria(id_categoria)
    fornecedor = localizar_fornecedor(id_fornecedor)
    novo_produto = Produto(nome, quantidade, valor_compra, valor_venda, descricao, categoria, fornecedor)
    novo_produto.id_produto = produto_dao.criar(novo_produto)
    return novo_produto


def atualizar(id_produto, nome, quantidade, valor_compra, valor_venda, descricao, id_categoria, id_fornecedor):
    categoria = localizar_categoria(id_categoria)
    fornecedor = localizar_fornecedor(id_fornecedor)
    produto_atualizado = Produto(nome, quantidade, valor_compra, valor_venda, descricao, categoria, fornecedor, id_produto)
    produto_dao.atualizar(produto_atualizado)
    return produto_atualizado


def deletar(id_produto):
    produto = localizar(id_produto)
    produto_dao.deletar(id_produto)
    return produto
