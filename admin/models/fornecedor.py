class Fornecedor:
    def __init__(self, nome, telefone, email, endereco, id_fornecedor=None):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email
        self.__endereco = endereco
        self.__id_fornecedor = id_fornecedor

    def __repr__(self):
        return f'Fornecedor({self.nome}, {self.telefone}, {self.email}, {self.endereco}, {self.id_fornecedor})'

    @property
    def nome(self):
        return self.__nome
    
    @property
    def telefone(self):
        return self.__telefone
    
    @property
    def email(self):
        return self.__email
    
    @property
    def endereco(self):
        return self.__endereco

    @property
    def id_fornecedor(self):
        return self.__id_fornecedor

    @id_fornecedor.setter
    def id_fornecedor(self, id):
        self.__id_fornecedor = id