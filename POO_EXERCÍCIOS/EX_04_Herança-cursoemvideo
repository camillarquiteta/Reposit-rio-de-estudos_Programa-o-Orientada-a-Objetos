from rich import print,inspect
class Pessoa:
    def __init__(self,nome = '',idade = 0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade+= 1


class Aluno(Pessoa):
    def __init__(self,nome,idade,curso,turma):
        super().__init__(nome,idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print (f'Aluno(a) {self.nome} fez matrícula!')


class Professor(Pessoa):
    def __init__(self,nome,idade,especialidade,nivel):
        super().__init__(nome,idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print (f'Prof. {self.nome} começou a dar aula!')


class Funcionario(Pessoa):
    def __init__(self,nome,idade,cargo,setor):
        super().__init__(nome,idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print (f'{self.nome} bateu o ponto!')


a1=Aluno('camilla',25,'engenharia de software','t01')
a1.fazer_aniversario()
inspect(a1)
p1=Professor('Elvira',45,'Veterinária','Doutorado')
f1=Funcionario('Minio',37,'Zelador','Limpeza')
inspect(f1)
inspect(a1)
inspect(p1)
a1.fazer_matricula()
p1.dar_aula()
f1.bater_ponto()