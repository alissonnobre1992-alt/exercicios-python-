valores = []

for i in range(5):
    valores.append(int(input(f"Digite o {i+1}º valor: ")))
    

maior = max(valores)
menor = min(valores)

pos_maior = valores.index(maior)
pos_menor = valores.index(menor)

print(f"\nLista: {valores}")
print(f"Maior valor: {maior} → posição {pos_maior}")
print(f"Menor valor: {menor} → posição {pos_menor}")
