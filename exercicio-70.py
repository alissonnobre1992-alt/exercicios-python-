print('-' * 30)
print(' LOJA DO ALISSON'.center(30))
print('-' * 30)

total = 0
menor_preco = 0
mais_de_1000 = 0
produto_barato = ''
quantidade = 0

while True:
    produto = input('Digite o nome do produto: ')
    valor = float(input('Digite o valor do produto: '))

    if valor < 0:
        print('Valor inválido! Digite um valor positivo.')
    else:
        total += valor
        quantidade += 1

        if valor > 1000:
            mais_de_1000 += 1

        if menor_preco == 0 or valor < menor_preco:
            menor_preco = valor
            produto_barato = produto

        resp = input('Quer continuar? [S/N] ').strip().upper()
        if resp == 'N':
            break

print('-' * 30)
print(' RESUMO DA COMPRA'.center(30))
print('-' * 30)
print(f'Quantidade de produtos: {quantidade}')
print(f'Total da compra: R${total:.2f}')
if quantidade > 0:
    print(f'Média por produto: R${total / quantidade:.2f}')
    print(f'Produtos acima de R$1000: {mais_de_1000}')
    print(f'Produto mais barato: {produto_barato} (R${menor_preco:.2f})')
print('-' * 30)
