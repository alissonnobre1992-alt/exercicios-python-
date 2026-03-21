computador = randint(0, 10)
total = jogador + computador

print('-' * 30)
print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')

if total % 2 == 0:
    print('Deu PAR')
    resultado = 'P'
else:
    print('Deu ÍMPAR')
    resultado = 'I'

if escolha == resultado:
    print('Você VENCEU!')
    vitorias += 1
    print('Vamos jogar novamente...')
else:
    print('Você PERDEU!')
    break

print('-' * 30)
