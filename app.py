import admin.blueprints.clientes as clientes
import admin.blueprints.fornecedores as fornecedores
import admin.blueprints.instituicoes as instituicoes
import admin.blueprints.categorias as categorias
import admin.blueprints.produtos as produtos
from database import criar_bd
from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cdd9946cbe9640409de21e1623fae502'
app.register_blueprint(clientes.cliente_bp)
app.register_blueprint(fornecedores.fornecedor_bp)
app.register_blueprint(instituicoes.instituicao_bp)
app.register_blueprint(categorias.categoria_bp)
app.register_blueprint(produtos.produto_bp)


@app.route('/')
def index():
    from admin.dao.cliente_dao import total_clientes
    from admin.dao.fornecedor_dao import total_fornecedores
    from admin.dao.instituicao_dao import total_instituicoes
    from admin.dao.categoria_dao import total_categorias
    from admin.dao.produto_dao import total_produtos

    return render_template('admin/index.html', clientes=total_clientes(), fornecedores=total_fornecedores(), 
                            instituicoes=total_instituicoes(), categorias=total_categorias(), produtos=total_produtos())


if __name__ == "__main__":
    criar_bd()
    app.run(debug=True)
