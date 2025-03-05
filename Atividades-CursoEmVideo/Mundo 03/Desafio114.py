import urllib
import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br')
except urllib.error.URLError:
    print(f'Erro! Site do pudim indisponível no momento')
else:
    print('Site do pudim acessado com sucesso')