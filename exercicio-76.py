listagem = (
    'Arroz', 22.50,
    'Feijão', 8.90,
    'Macarrão', 6.75,
    'Óleo', 7.40,
    'Açúcar', 5.60,
    'Café', 14.30,
    'Leite', 4.99,
    'Pão', 12.00,
    'Manteiga', 9.50
)

print('-' * 40)
print('LISTAGEM DE PREÇOS')
print('-' * 40)

for pos in range(0, len(listagem), 2):
    print(f'{listagem[pos]:.<30}R$ {listagem[pos + 1]:>7.2f}')

print('-' * 40)
