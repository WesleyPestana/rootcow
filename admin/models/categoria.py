class Categoria:
    def __init__(self, nome, descricao, id_categoria=None):
        self.__nome = nome
        self.__descricao = descricao
        self.__id_categoria = id_categoria

    def __repr__(self):
        return f'Categoria({self.nome}, {self.descricao}, {self.id_categoria})'

    @property
    def nome(self):
        return self.__nome

    @property
    def descricao(self):
        return self.__descricao

    @property
    def id_categoria(self):
        return self.__id_categoria

    @id_categoria.setter
    def id_categoria(self, id):
        self.__id_categoria = id