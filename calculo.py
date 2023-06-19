# Bibliotecas
import csv

import pandas as pd
from pandas import *

# ler arquivo de navios atracados
data1 = read_csv("navios_atracados.csv")

# buscar no arquivo os dados necessários para o cálculo e transformar as colunas em listas
navios = data1["Navio"].tolist()
dwt = data1["DWT"].tolist()
qtd_carga = data1["Qtd.Carga"].tolist()
code = data1["IMO"].tolist()

# cálculo do deslastre estimado e transformação do resultado em t para m³
contador = 0
deslastre = []
nome = []
imo = []

for n in navios:
    deslastre.append(round(((dwt[contador] - qtd_carga[contador]) * 0.3) * 1000, 3))
    nome.append(navios[contador])
    imo.append(code[contador])
    contador += 1

# Análise para o nível de risco
contador = 0
pontos = []
nivel = []

for valor in deslastre:
    if valor < 1500:
        pontos.append(0.5)
        nivel.append("BAIXO")
    elif valor <= 5000:
        pontos.append(1)
        nivel.append("BAIXO")
    else:
        pontos.append(2)
        nivel.append("MÉDIO")

# Concatena as listas
resultado = []
resultado.append(
    ["Navio", "Deslastre Estimado", "Pontos por Faixa", "Nível de Risco", "IMO"]
)
for i in range(len(navios)):
    resultado.append([nome[i], deslastre[i], pontos[i], nivel[i], imo[i]])

# Cria um arquivo CSV para armazenar os resultados
with open("resultado.csv", "a", newline="", encoding="utf-8") as resultado_file:
    natemp = csv.writer(resultado_file)
    natemp.writerows(resultado)

# ler arquivo de navios esperando
data2 = read_csv("navios_esperados.csv")

# buscar no arquivo os dados necessários para o cálculo e transformar as colunas em listas
navios = data2["Navio"].tolist()
dwt = data2["DWT"].tolist()
qtd_carga = data2["Qtd.Carga"].tolist()
code = data2["IMO"].tolist()

# cálculo do deslastre estimado e transformação do resultado em t para m³
contador = 0
deslastre = []
nome = []
imo = []

for n in navios:
    deslastre.append(round(((dwt[contador] - qtd_carga[contador]) * 0.3) * 1000, 3))
    nome.append(navios[contador])
    imo.append(code[contador])
    contador += 1

# Análise para o nível de risco
contador = 0
pontos = []
nivel = []

for valor in deslastre:
    if valor < 1500:
        pontos.append(0.5)
        nivel.append("BAIXO")
    elif valor <= 5000:
        pontos.append(1)
        nivel.append("BAIXO")
    else:
        pontos.append(2)
        nivel.append("MÉDIO")

# Concatena as listas
resultado = []
for i in range(len(navios)):
    resultado.append([nome[i], deslastre[i], pontos[i], nivel[i], imo[i]])

# Cria um arquivo CSV para armazenar os resultados
with open("resultado.csv", "a", newline="", encoding="utf-8") as resultado_file:
    natemp = csv.writer(resultado_file)
    natemp.writerows(resultado)

# ler arquivo de navios atracados
data3 = read_csv("navios_fundeados.csv")

# buscar no arquivo os dados necessários para o cálculo e transformar as colunas em listas
navios = data3["Navio"].tolist()
dwt = data3["DWT"].tolist()
qtd_carga = data3["Qtd.Carga"].tolist()
code = data3["IMO"].tolist()

# cálculo do deslastre estimado e transformação do resultado em t para m³
contador = 0
deslastre = []
nome = []
imo = []

for n in navios:
    deslastre.append(round(((dwt[contador] - qtd_carga[contador]) * 0.3) * 1000, 3))
    nome.append(navios[contador])
    imo.append(code[contador])
    contador += 1

# Análise para o nível de risco
contador = 0
pontos = []
nivel = []

for valor in deslastre:
    if valor < 1500:
        pontos.append(0.5)
        nivel.append("BAIXO")
    elif valor <= 5000:
        pontos.append(1)
        nivel.append("BAIXO")
    else:
        pontos.append(2)
        nivel.append("MÉDIO")

# Concatena as listas
resultado = []
for i in range(len(navios)):
    resultado.append([nome[i], deslastre[i], pontos[i], nivel[i], imo[i]])

# Cria um arquivo CSV para armazenar os resultados
with open("resultado.csv", "a", newline="", encoding="utf-8") as resultado_file:
    natemp = csv.writer(resultado_file)
    natemp.writerows(resultado)

# lê o arquivo CSV atualizado e mostra na tela
try:
    resultado_updated = pd.read_csv("resultado.csv", encoding="utf-8")
    print(resultado_updated)
except FileNotFoundError:
    print("Arquivo CSV não encontrado.")
