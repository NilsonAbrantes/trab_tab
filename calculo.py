import csv

import pandas as pd


def process_ships(data, situacao):
    deslastre = []
    nome = data["Navio"].tolist()
    imo = data["IMO"].tolist()
    pontos = []
    nivel = []

    for index, row in data.iterrows():
        row["DWT"] = float(row["DWT"])
        d = round(((row["DWT"] - row["Qtd.Carga"]) * 0.3) * 1000, 3)
        deslastre.append(d)

        if d < 1500:
            pontos.append(0.5)
            nivel.append("BAIXO")
        elif d <= 5000:
            pontos.append(1)
            nivel.append("BAIXO")
        else:
            pontos.append(2)
            nivel.append("MÉDIO")

    resultado = []
    resultado.append(
        [
            "Situacao",
            "Navio",
            "Deslastre Estimado",
            "Pontos por Faixa",
            "Nível de Risco",
            "IMO",
        ]
    )

    for i in range(len(nome)):
        resultado.append([situacao, nome[i], deslastre[i], pontos[i], nivel[i], imo[i]])

    return resultado


# ler arquivo de navios atracados
data1 = pd.read_csv("navios_atracados_temp.csv")
resultado_atracados = process_ships(data1, "ATRACADOS")

# ler arquivo de navios esperando
data2 = pd.read_csv("navios_esperados_temp.csv")
resultado_esperando = process_ships(data2, "ESPERANDO")

# ler arquivo de navios fundeados
data3 = pd.read_csv("navios_fundeados_temp.csv")
resultado_fundeados = process_ships(data3, "FUNDEADOS")

# Juntar todos os resultados
resultado_total = resultado_atracados + resultado_esperando + resultado_fundeados

# Escreve os resultados em um arquivo CSV
with open("resultado_new.csv", "w", newline="", encoding="utf-8") as resultado_file:
    natemp = csv.writer(resultado_file)
    natemp.writerows(resultado_total)

# lê o arquivo CSV atualizado e mostra na tela
try:
    resultado_updated = pd.read_csv("resultado_new.csv", encoding="utf-8")
    print(resultado_updated)
except FileNotFoundError:
    print("Arquivo CSV não encontrado.")
