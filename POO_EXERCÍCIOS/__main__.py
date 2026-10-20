from rich import print,inspect
from EX_04_Heranca_cursoemvideo import Aluno, Professor, Funcionario

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