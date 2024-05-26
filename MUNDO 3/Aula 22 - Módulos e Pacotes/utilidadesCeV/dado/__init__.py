def leiadinheiro():
    flag = True
    while flag:
        valor = str(input("Digite um valor: ")).replace(',','.').strip()
        if valor.isalpha() or valor.strip('') == '':
            print('\033[0;31mEsse valor é inválido!\033[m')
        else:
            flag = False
            return float(valor)

