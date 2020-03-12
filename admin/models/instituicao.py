class Instituicao:
    def __init__(self, nome, telefone, email, endereco, id_instituicao=None):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email
        self.__endereco = endereco
        self.__id_instituicao = id_instituicao

    def __repr__(self):
        return f'Instituicao({self.nome}, {self.telefone}, {self.email}, {self.endereco}, {self.id_instituicao})'

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
    def id_instituicao(self):
        return self.__id_instituicao

    @id_instituicao.setter
    def id_instituicao(self, id):
        self.__id_instituicao = id