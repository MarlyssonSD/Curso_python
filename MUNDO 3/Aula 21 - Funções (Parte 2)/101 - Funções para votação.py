from datetime import datetime


def voto(idade_pessoa):
    if (idade_pessoa < 18 and idade_pessoa > 16) or idade_pessoa > 70:
        return "O voto é opcional."
    elif (idade_pessoa >= 18) and (idade_pessoa <= 70):
        return "O voto é obrigatório"
    else:
        return "Não vota"


ano_nasc = int(input("Digite o ano de nascimento:"))
ano_atual = datetime.now().year
idade = ano_atual - ano_nasc
print(f'Com {idade} anos: {voto(idade)}')
