print ("-" * 30) 
print('ÁREA DO TERRENO'.center(30))
print ("-" * 30)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
def area (largura, comprimento):
    a = largura * comprimento
print (f'A área do terreno {largura} x {comprimento} é de {a}m²')
area(largura, comprimento)
print ("-" * 30) 
