import datetime

class Funcionario:
    def __init__(self, id_num, sobrenome, nome, nascimento, admissao, salario):
        self.id_num = id_num  
        self.sobrenome = sobrenome
        self.nome = nome
        self.nascimento = nascimento  
        self.admissao = admissao  
        self.salario = salario  
    
    def idade(self):
        ano_atual = datetime.datetime.now().year
        return ano_atual - self.nascimento[2]
    
    def tempo_de_casa(self):
        ano_atual = datetime.datetime.now().year
        return ano_atual - self.admissao[2]
    
    def aumento_de_salario(self):
        tempo = self.tempo_de_casa()
        if tempo < 5:
            self.salario *= 1.02  
        elif tempo < 10:
            self.salario *= 1.05  
        else:
            self.salario *= 1.10 

    
    def mostrar_funcionario(self):
        print(f"Número pessoal: {self.id_num}")
        print(f"Sobrenome: {self.sobrenome}")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade()}")
        print(f"Tempo de casa: {self.tempo_de_casa()}")
        print(f"Salário em€: {self.salario:.2f}")