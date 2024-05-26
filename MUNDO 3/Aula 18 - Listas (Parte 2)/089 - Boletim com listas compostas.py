alunos = []
notas = []
media = 0.0
nome = ''

while True:
    nome = input('Digite o nome do aluno (FLAG: 0): ')
    if nome == '0':
        break
    notas.append(float(input('Digite a primeira nota: ')))
    notas.append(float(input('Digite a segunda nota: ')))
    media = (notas[0]+notas[1])/2
    alunos.append([nome, notas[:], media])
    notas.clear()

for x in alunos:
    print(f'{x[0]}:\nMédia: {x[2]}')

num_aluno = 0
while True:
    print('=-='*10)
    num_aluno = int(input(f'Deseja ver a nota de qual aluno? (sair: numero < 0 '))
    if num_aluno < 0 or num_aluno > len(alunos):
        break
    else:
        print(f'Notas de {alunos[num_aluno][0]}: {alunos[num_aluno][1][0]} e {alunos[num_aluno][1][1]}')


