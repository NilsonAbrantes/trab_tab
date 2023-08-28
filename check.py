import csv

import pandas as pd

data1 = pd.read_csv("navios_atracados_temp.csv")
dwt = data1["DWT"].tolist()
qtd_carga = data1["Qtd.Carga"].tolist()

with open("navios_atracados.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    nova = float
    for nova in dwt:
        for row in reader:
            if nova in row["DWT"]:
                print("ss")
    # Após percorrer todas as linhas do arquivo CSV com cada valor de dwt,
    # o ponteiro de leitura estará no final do arquivo. Se você precisar
    # ler novamente o arquivo, é necessário voltar ao início.
