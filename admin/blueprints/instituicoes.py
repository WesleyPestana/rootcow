from admin.services import instituicao_service
from flask import Blueprint, render_template, redirect, request, flash


instituicao_bp = Blueprint('instituicao_bp', __name__)

@instituicao_bp.route('/instituicoes/', methods=['GET'])
def listar_instituicoes():
    instituicoes = instituicao_service.listar()
    return render_template('admin/instituicoes/listar.html', instituicoes=instituicoes), 200


@instituicao_bp.route('/instituicoes/nova/', methods=['GET', 'POST'])
def cadastrar_instituicao():
    if request.method == 'GET':
        return render_template('admin/instituicoes/form_instituicao.html', botao='Incluir'), 200
    
    if request.method == 'POST':
        dados_form = request.form.to_dict()
        criada = instituicao_service.criar(**dados_form)
        flash(f'Instituição {criada.id_instituicao} cadastrada com sucesso!', 'success')
        return redirect('/instituicoes/')


@instituicao_bp.route('/instituicoes/<int:id_instituicao>/', methods=['GET', 'POST'])
def editar_instituicao(id_instituicao):
    if request.method == 'GET':
        instituicao = instituicao_service.localizar(id_instituicao)
        return render_template('admin/instituicoes/form_instituicao.html', nome=instituicao.nome, telefone=instituicao.telefone,
                email=instituicao.email, endereco=instituicao.endereco, botao='Alterar'), 200

    if request.method == 'POST':
        dados_form = request.form.to_dict()
        atualizada = instituicao_service.atualizar(id_instituicao, **dados_form)
        flash(f'Instituição {atualizada.id_instituicao} alterada com sucesso!', 'success')
        return redirect('/instituicoes/')


@instituicao_bp.route('/instituicoes/<int:id_instituicao>/', methods=['DELETE'])
def deletar_instituicao(id_instituicao):
    deletada = instituicao_service.deletar(id_instituicao)
    flash(f'Instituição {deletada.id_instituicao} excluida com sucesso!', 'success')
    return redirect('/instituicoes/', 200)
