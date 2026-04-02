lista = []

while True:
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)

    resp = input('Quer continuar? [S/N] ').strip().upper()
    if resp == 'N':
        break

lista.sort()
print(f'Você digitou os valores {lista}')
