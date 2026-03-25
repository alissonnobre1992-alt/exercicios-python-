n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
n4 = int(input('Digite o último número: '))

total = (n1, n2, n3, n4)
print(total)

print(f'O valor 9 apareceu {total.count(9)} vez(es)')

if 3 in total:
    print(f'O primeiro valor 3 foi digitado na posição {total.index(3) + 1}')
else:
    print('O valor 3 não foi digitado em nenhuma posição')

if any(n % 2 == 0 for n in total):
    print('Os valores pares digitados foram: ', end='')
    for n in total:
        if n % 2 == 0:
            print(n, end=' ')
    print()
else:
    print('Não foi digitado nenhum valor par!')
