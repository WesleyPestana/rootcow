class Produto:
    def __init__(self, nome, quantidade, valor_compra, valor_venda, descricao, categoria, fornecedor, id_produto=None):
        self.__nome = nome
        self.__quantidade = quantidade
        self.__valor_compra = valor_compra
        self.__valor_venda = valor_venda
        self.__descricao = descricao
        self.__categoria = categoria
        self.__fornecedor = fornecedor
        self.__id_produto = id_produto

    def __repr__(self):
        return f'Produto({self.nome}, {self.quantidade}, {self.valor_compra}, {self.valor_venda}, {self.descricao}, {self.categoria.nome}, \
                            {self.fornecedor.nome}, {self.id_produto})'

    @property
    def nome(self):
        return self.__nome

    @property
    def quantidade(self):
        return self.__quantidade
    
    @property
    def valor_compra(self):
        return self.__valor_compra
    
    @property
    def valor_venda(self):
        return self.__valor_venda

    @property
    def descricao(self):
        return self.__descricao

    @property
    def categoria(self):
        return self.__categoria
    
    @property
    def fornecedor(self):
        return self.__fornecedor

    @property
    def id_produto(self):
        return self.__id_produto

    @id_produto.setter
    def id_produto(self, id):
        self.__id_produto = id
