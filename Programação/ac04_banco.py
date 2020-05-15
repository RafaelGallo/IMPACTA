# Linguagem de Programação II
# AC04 - Banco
#
# Nome: Bruno de Aguiar Becaleti RA: 1901506
# Nome: Rafael Henrique Gallo RA: 1901885


class Cliente():
    def __init__(self, nome: str, telefone: int, email: str):
        if "@" not in email:
            raise ValueError("Email Incorreto.")
        elif type(telefone) != int:
            raise TypeError("Telefone Incorreto.")
        else:
            self.__nome = nome
            self.__telefone = telefone
            self.__email = email

    def get_nome(self):
        return self.__nome

    def get_telefone(self):
        return self.__telefone

    def set_telefone(self, novo_telefone: int):
        if type(novo_telefone) != int:
            raise TypeError("Telefone Incorreto.")
        else:
            self.__telefone = novo_telefone

    def get_email(self):
        return self.__email

    def set_email(self, novo_email: str):
        if "@" not in novo_email:
            raise ValueError("Email Incorreto.")
        else:
            self.__email = novo_email


class Banco:
    def __init__(self, nome: str):
        self.__nome = nome
        self.__numero_conta = 1
        self.__lista_contas = []

    def get_nome(self):
        return self.__nome

    def abrir_conta(self, cliente: Cliente, saldo: float):
        if saldo < 0:
            raise ValueError("Saldo negativo! A conta nao pode ser aberta.")
        else:
            conta = Conta(cliente, self.__numero_conta, saldo)
            self.__numero_conta = self.__numero_conta + 1
            self.__lista_contas.append(conta)

    def listar_contas(self):
        return self.__lista_contas


class Conta:
    def __init__(self, cliente: Cliente, numero: int, saldo: float):
        if saldo < 0:
            raise ValueError
        else:
            self.__cliente = cliente
            self.__numero = numero
            self.__saldo = saldo
            self.__saldo_inicial = saldo
            self.__operacoes = [('saldo_inicial', saldo)]

    def get_cliente(self):
        return self.__cliente

    def get_saldo(self):
        return self.__saldo

    def get_numero(self):
        return self.__numero

    def sacar(self, valor: float):
        if valor > self.__saldo:
            raise ValueError("Saldo insuficiente! Valor Superior ao da conta.")
        else:
            self.__saldo = self.__saldo - valor
            self.__operacoes.append(('saque', valor))

    def depositar(self, valor: float):
        if valor < 0:
            raise ValueError("Valor inválido")
        else:
            self.__saldo = self.__saldo + valor
            self.__operacoes.append(('deposito', valor))

    def extrato(self):
        return self.__operacoes
