maior = 0
homens = 0
mulheres = 0
while True: 
    print('-' * 30)
    print(' CADASTRO DE USUÁRIOS'.center(30))
    print('-' * 30)
    
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo [ F / M ]: ').strip().upper()
    print('USUÁRIO CADASTRADO COM SUCESSO')
    continuar = input('Quer continuar ?  [S / N]: ' ).strip().upper()

    if idade > 18:
        maior += 1
    if idade < 20:
        if sexo == 'F':
             mulheres += 1
    if sexo == 'M':
        homens += 1
    if continuar == 'N':
        break
print(f' Usuários com mais de 18 anos: {maior}')
print(f' Homens cadastrados: {homens}')
print(f'Mulheres com menos de 20 anos: {mulheres}')
