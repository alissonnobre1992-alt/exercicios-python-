## fiz uma pasta chamada moedas.py, fiz os módulos e depois criei outro arquivo, nesse outro arquivo eu importei os módulos dando um import moedas

def dobro (a):
    return a * 2
def metade (a):
    return a / 2
def porcentagem (a):
    return a * 0.10 + a

######OUTRO ARQUIVO
import moedas
n = float(input('Digite um valor R$:' ))
print(f'A metade de {n} é R${moeda.metade(n)}')
print(f'O dobro de {n} é R$ {moeda.dobro(n)}')
print(f'Aumentando 10% de {n} fica R$ {moeda.porcentagem(n,)}')
