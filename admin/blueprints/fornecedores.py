from admin.services import fornecedor_service
from flask import Blueprint, render_template, redirect, request, flash


fornecedor_bp = Blueprint('fornecedor_bp', __name__)

@fornecedor_bp.route('/fornecedores/', methods=['GET'])
def listar_fornecedores():
    fornecedores = fornecedor_service.listar()
    return render_template('admin/fornecedores/listar.html', fornecedores=fornecedores), 200


@fornecedor_bp.route('/fornecedores/novo/', methods=['GET', 'POST'])
def cadastrar_fornecedor():
    if request.method == 'GET':
        return render_template('admin/fornecedores/form_fornecedor.html', botao='Incluir'), 200
    
    if request.method == 'POST':
        dados_form = request.form.to_dict()
        criado = fornecedor_service.criar(**dados_form)
        flash(f'Fornecedor {criado.id_fornecedor} cadastrado com sucesso!', 'success')
        return redirect('/fornecedores/')


@fornecedor_bp.route('/fornecedores/<int:id_fornecedor>/', methods=['GET', 'POST'])
def editar_fornecedor(id_fornecedor):
    if request.method == 'GET':
        fornecedor = fornecedor_service.localizar(id_fornecedor)
        return render_template('admin/fornecedores/form_fornecedor.html', nome=fornecedor.nome, telefone=fornecedor.telefone,
                email=fornecedor.email, endereco=fornecedor.endereco, botao='Alterar'), 200

    if request.method == 'POST':
        dados_form = request.form.to_dict()
        atualizado = fornecedor_service.atualizar(id_fornecedor, **dados_form)
        flash(f'Fornecedor {atualizado.id_fornecedor} alterado com sucesso!', 'success')
        return redirect('/fornecedores/')


@fornecedor_bp.route('/fornecedores/<int:id_fornecedor>/', methods=['DELETE'])
def deletar_fornecedor(id_fornecedor):
    deletado = fornecedor_service.deletar(id_fornecedor)
    flash(f'Fornecedor {deletado.id_fornecedor} excluido com sucesso!', 'success')
    return redirect('/fornecedores/', 200)
