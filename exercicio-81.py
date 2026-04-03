lista = []
while True:
    r = int(input('Digite um número: '))
    lista.append(r)

    resp = input('Quer continuar ? [S/N] ').upper()
    if resp == 'N':
        break

print(f'Você digitou {len(lista)} números.')
print(f'Os valores em ordem decrescente são {sorted(lista, reverse=True)}')
print(f'O número 5 apareceu {lista.count(5)} vezes.')
