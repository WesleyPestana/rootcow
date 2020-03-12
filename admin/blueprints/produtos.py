from admin.services import produto_service, categoria_service, fornecedor_service
from flask import Blueprint, render_template, redirect, request, flash

produto_bp = Blueprint('produto_bp', __name__)

@produto_bp.route('/produtos/', methods=['GET'])
def listar_produtos():
    produtos = produto_service.listar()
    return render_template('admin/produtos/listar.html', produtos=produtos), 200


@produto_bp.route('/produtos/novo/', methods=['GET', 'POST'])
def cadastrar_produto():
    if request.method == 'GET':
        categorias = categoria_service.listar()
        fornecedores = fornecedor_service.listar()
        return render_template('admin/produtos/form_produto.html', categorias=categorias, fornecedores=fornecedores, botao='Incluir'), 200
    
    if request.method == 'POST':
        dados_form = request.form.to_dict()
        criado = produto_service.criar(**dados_form)
        flash(f'Produto {criado.id_produto} cadastrado com sucesso!', 'success')
        return redirect('/produtos/')


@produto_bp.route('/produtos/<int:id_produto>/', methods=['GET', 'POST'])
def editar_produto(id_produto):
    if request.method == 'GET': 
        produto = produto_service.localizar(id_produto)
        categorias = filter(lambda categoria: categoria.id_categoria != produto.categoria.id_categoria, categoria_service.listar())
        fornecedores = filter(lambda fornecedor: fornecedor.id_fornecedor != produto.fornecedor.id_fornecedor, fornecedor_service.listar())

        return render_template('admin/produtos/form_produto.html', nome=produto.nome, quantidade=produto.quantidade, 
                valor_compra=produto.valor_compra, valor_venda=produto.valor_venda, descricao=produto.descricao,
                categoria_bd=produto.categoria, fornecedor_bd=produto.fornecedor, categorias=categorias, fornecedores=fornecedores, botao='Alterar'), 200
    
    if request.method == 'POST':
        dados_form = request.form.to_dict()
        atualizado = produto_service.atualizar(id_produto, **dados_form)
        flash(f'Produto {atualizado.id_produto} alterado com sucesso!', 'success')
        return redirect('/produtos/')


@produto_bp.route('/produtos/<int:id_produto>/', methods=['DELETE'])
def deletar_produto(id_produto):
    deletado = produto_service.deletar(id_produto)
    flash(f'Produto {deletado.id_produto} excluido com sucesso!', 'success')
    return redirect('/produtos/', 200)
