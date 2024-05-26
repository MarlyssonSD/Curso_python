def fatorial(num, show=False):
    fat = 1
    print(f'Fatorial de {num}: ', end='')

    if show:
        for x in range(1, num + 1):
            fat *= x
            if x != num:
                print(x, end=' * ')
            else:
                print(x, end=' = ')
    else:
        for x in range(1, num+1):
            fat *= x

    print(fat)

fatorial(5, True)
