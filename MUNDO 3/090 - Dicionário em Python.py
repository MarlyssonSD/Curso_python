alunos = {}


alunos['nome'] = input("Digite o nome: ")
alunos['media'] = float(input("Digite a média: "))
if alunos['media'] >= 7:
    alunos['situação'] = 'aprovado(a)'
else:
    alunos['situação'] = 'Reprovado(a)'

print(f'Aluno(a) {alunos["nome"]} com média {alunos["media"]} está {alunos["situação"]}')