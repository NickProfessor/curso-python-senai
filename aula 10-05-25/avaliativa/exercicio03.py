# Atividade 3 – Conversor de unidades (com entrada e cálculo)
# Descrição:
#  Crie um programa que:
# Peça ao usuário uma distância em quilômetros


# Converta para metros, centímetros e milímetros


# Mostre todos os resultados


# Objetivos avaliados:
# Conversão e operações matemáticas


# Manipulação de entrada com float()

try:
    distancia_em_km = float(input('Insira uma distância em quilômetros: '))
    distancia_em_metros = distancia_em_km * 1000
    distancia_em_centimetros = distancia_em_metros * 100
    distancia_em_milimetros = distancia_em_centimetros * 10
    print(f'''
          Atenção para as medidas!
          {distancia_em_km} Km
          {distancia_em_metros} Metros
          {distancia_em_centimetros} Cm
          {distancia_em_milimetros} Milímetros 
          ''')
except ValueError:
    print('INSIRA SOMENTE NÚMEROS')