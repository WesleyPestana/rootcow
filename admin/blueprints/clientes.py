from admin.services import cliente_service
from flask import Blueprint, render_template, redirect, request, flash


cliente_bp = Blueprint('cliente_bp', __name__)

@cliente_bp.route('/clientes/', methods=['GET'])
def listar_clientes():
    clientes = cliente_service.listar()
    return render_template('admin/clientes/listar.html', clientes=clientes), 200


@cliente_bp.route('/clientes/novo/', methods=['GET', 'POST'])
def cadastrar_cliente():
    if request.method == 'GET':
        return render_template('admin/clientes/form_cliente.html', botao='Incluir'), 200
    
    if request.method == 'POST':
        dados_form = request.form.to_dict()
        criado = cliente_service.criar(**dados_form)
        flash(f'Cliente {criado.id_cliente} cadastrado com sucesso!', 'success')
        return redirect('/clientes/')


@cliente_bp.route('/clientes/<int:id_cliente>/', methods=['GET', 'POST'])
def editar_cliente(id_cliente):
    if request.method == 'GET':
        cliente = cliente_service.localizar(id_cliente)
        return render_template('admin/clientes/form_cliente.html', nome=cliente.nome, email=cliente.email,
                cpf=cliente.cpf, rg=cliente.rg, telefone=cliente.telefone, endereco=cliente.endereco, botao='Alterar'), 200

    if request.method == 'POST':
        dados_form = request.form.to_dict()
        atualizado = cliente_service.atualizar(id_cliente, **dados_form)
        flash(f'Cliente {atualizado.id_cliente} alterado com sucesso!', 'success')
        return redirect('/clientes/')


@cliente_bp.route('/clientes/<int:id_cliente>/', methods=['DELETE'])
def deletar_cliente(id_cliente):
    deletado = cliente_service.deletar(id_cliente)
    flash(f'Cliente {deletado.id_cliente} excluido com sucesso!', 'success')
    return redirect('/clientes/', 200)
