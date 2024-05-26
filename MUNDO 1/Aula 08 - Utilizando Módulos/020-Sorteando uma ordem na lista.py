import random
a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
alunos = [a1, a2, a3, a4]
random.shuffle(alunos)
print('A ordem de alunos é {}'.format(alunos))
