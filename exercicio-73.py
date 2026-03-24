times = (
    'Flamengo',
    'Chapecoense',
    'Palmeiras',
    'Vitória',
    'Corinthians',
    'Remo',
    'São Paulo',
    'Bahia',
    'Cruzeiro',
    'Santos',
    'Botafogo',
    'Grêmio',
    'Athletico Paranaense',
    'Mirassol',
    'Vasco da Gama',
    'Internacional',
    'Coritiba',
    'Atlético Mineiro',
    'Fluminense',
    'Red Bull Bragantino'
)

print(f'Os 5 primeiros são: {times[:5]}')
print(f'Os 4 últimos são: {times[-4:]}')
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'A Chapecoense está na posição: {times.index("Chapecoense") + 1}')
