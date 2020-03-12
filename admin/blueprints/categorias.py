from admin.services import categoria_service
from flask import Blueprint, render_template, redirect, request, flash

categoria_bp = Blueprint('categoria_bp', __name__)

@categoria_bp.route('/categorias/', methods=['GET'])
def listar_categorias():
    categorias = categoria_service.listar()
    return render_template('admin/categorias/listar.html', categorias=categorias), 200


@categoria_bp.route('/categorias/nova/', methods=['GET', 'POST'])
def cadastrar_categoria():
    if request.method == 'GET':
        return render_template('admin/categorias/form_categoria.html', botao='Incluir'), 200
    
    if request.method == 'POST':
        dados_form = request.form.to_dict()
        criada = categoria_service.criar(**dados_form)
        flash(f'Categoria {criada.id_categoria} cadastrada com sucesso!', 'success')
        return redirect('/categorias/')


@categoria_bp.route('/categorias/<int:id_categoria>/', methods=['GET', 'POST'])
def editar_categoria(id_categoria):
    if request.method == 'GET':
        categoria = categoria_service.localizar(id_categoria)
        return render_template('admin/categorias/form_categoria.html', nome=categoria.nome, descricao=categoria.descricao, botao='Alterar'), 200

    if request.method == 'POST':
        dados_form = request.form.to_dict()
        atualizada = categoria_service.atualizar(id_categoria, **dados_form)
        flash(f'Categoria {atualizada.id_categoria} alterada com sucesso!', 'success')
        return redirect('/categorias/')


@categoria_bp.route('/categorias/<int:id_categoria>/', methods=['DELETE'])
def deletar_categoria(id_categoria):
    deletada = categoria_service.deletar(id_categoria)
    flash(f'Categoria {deletada.id_categoria} excluida com sucesso!', 'success')
    return redirect('/categorias/', 200)
