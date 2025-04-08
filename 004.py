import math
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if valor > self.__saldo:
            print("Erro: Saldo insuficiente!")
        else:
            self.__saldo -= valor
    