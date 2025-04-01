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