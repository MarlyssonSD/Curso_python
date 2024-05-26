
print("Digite uma expressão: ")
expressao = str(input())
contaParenteses = 0
for x in range (0 , len(expressao)):
    if expressao[x] == '(':
        contaParenteses+=1
    elif expressao[x] == ')':
        contaParenteses-=1

if not contaParenteses:
    print("A expressão é válida")
else:
    print("A expressão não é válida")
