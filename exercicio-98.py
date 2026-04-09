from time import sleep

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1

    print("Contagem de {} até {} de {} em {}".format(inicio, fim, passo, passo))

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(cont , end=' ', flush=True)
            sleep(0.5)
            cont += passo
    else:
        cont = inicio
        while cont >= fim:
            print(cont , end=' ', flush=True)
            sleep(0.5)
            cont -= passo

    print()


contador(1, 10, 1)


contador(10, 0, 2)

print("Agora é sua vez de personalizar a contagem!")
ini = int(input("Início: "))
fim = int(input("Fim: "))
pas = int(input("Passo: "))

contador(ini, fim, pas)
