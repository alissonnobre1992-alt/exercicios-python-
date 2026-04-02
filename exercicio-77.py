palavras = ('Alisson', 'Marcela', 'Software', 'Expresso', 'Faculdade')

for palavra in palavras: 
    print(f'\nNa palavra {palavra} temos as vogais: ',end = ' ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end = ' ')
