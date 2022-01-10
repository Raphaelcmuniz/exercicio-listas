
from operator import itemgetter
from time import sleep

lista = [{'nome':'Geladeira', 'volume': 0.751, 'preço': 999.90}, {'nome': 'Notbook Dell', 'volume': 0.00350, 'preço': 2499.90},
         {'nome': 'Microondas X', 'volume': 0.0319, 'preço': 299.29}, {'nome': 'Notbook Asus', 'volume': 0.527, 'preço': 3999.90},
         {'nome': 'Iphone 8', 'volume': 0.000089, 'preço': 2199.12}, {'nome': 'Ventilador Gelado', 'volume': 0.496, 'preço': 199.90},
         {'nome': 'Freezer', 'volume': 0.635, 'preço': 849.00}, {'nome': 'Tv 55', 'volume': 0.400, 'preço': 4346.99},
         {'nome': 'Tv 50', 'volume': 0.290, 'preço': 3999.90}, {'nome': 'Tv 42', 'volume': 0.200, 'preço': 2999.90},
         {'nome': 'Notbook Lenovo', 'volume': 0.498, 'preço': 1999.90},{'nome': 'Microondas Y', 'volume': 0.0544, 'preço': 429.90},
         {'nome': 'Microodas Z', 'volume': 0.0424, 'preço': 429.90},{'nome': 'Geladeira faz frio', 'volume': 0.870, 'preço': 1199.98}]

# Geladeira [0]                 # Tv 55 [7]
# Notbook Dell [1]              # Tv 50 [8]
# Microondas X [2]              # Tv 42 [9]
# Notbook Azus [3]              # Notbook Lenovo [10]
# Iphone 8 [4]                  # Microondas Y [11]
# Ventilador Gelado [5]         # Microondas Z [12]
# Freezer [6]                   # Geladeira faz frio [13]

caminhao = []
lista_ordenada_volume = sorted(lista, key=itemgetter('volume'))
soma = 0
soma_preco = 0

for e in lista_ordenada_volume:
    for k, v in e.items():
        print(f"{k}: {v}")
    print("-" * 30)

for c in lista_ordenada_volume:
    v = c.get('volume')
    soma += v
    if soma < 3:
        print(f"{c['nome']} >> Adicionado ao caminhão")
        caminhao.append(c['nome'])
        soma_preco += c.get('preço')
        sleep(1)
        print(".", end=''), sleep(0.6)
        print(".", end=''), sleep(0.6)
        print(".", end=''), sleep(0.6)
        print()

print("~~ PRODUTOS-CAMINHÃO ~~")
cont = 0
for p in caminhao:
    print(f"-{p}")
    cont += 1
print("=-=" * 12)
print(f"Total de produtos: {cont}")
print(f"Valor do frete: {soma_preco:,.2f}")
print()
print("~~ FIM ~~")
