times = ('Atlético-MG', 'Bahia', 'Botafogo', 'Ceará SC', 'Corinthians', 'Cruzeiro', 'Flamengo', 'Fluminense', 'Fortaleza', 'Grêmio', 'Internacional',
         'Juventude', 'Mirassol', 'Palmeiras', 'Bragantino', 'Santos', 'Sport Recife', 'São Paulo', 'Vasco da Gama', 'EC Vitória')

print('A Lista de times do Brasileirão:', times)
print(70 * "==-")
print('Cinco Primeiros Colocados (2025):', times[:5])
print(70 * "==-")
print('Quatro Últimos Colocados(2025):', times[16:])
print(70 * "==-")
print('A Lista de times do Brasileirão (em ordem alfabética):', sorted(times))
print(70 * "==-")
print('O time do Palmeiras está na {}° colocação'.format(times.index('Palmeiras') + 1))