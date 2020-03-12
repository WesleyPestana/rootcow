class Cliente:
    def __init__(self, nome, cpf, rg, telefone, email, endereco, id_cliente=None):
        self.__nome = nome
        self.__cpf = cpf
        self.__rg = rg
        self.__telefone = telefone
        self.__email = email
        self.__endereco = endereco
        self.__id_cliente = id_cliente

    def __repr__(self):
        return f'Cliente({self.nome}, {self.cpf}, {self.rg}, {self.telefone}, {self.email}, {self.endereco}, {self.id_cliente})'

    @property
    def nome(self):
        return self.__nome
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def rg(self):
        return self.__rg
    
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
    def id_cliente(self):
        return self.__id_cliente

    @id_cliente.setter
    def id_cliente(self, id):
        self.__id_cliente = id