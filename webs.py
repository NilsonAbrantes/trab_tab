# bibliotecas utilizadas
import csv

import pandas as pd
import requests
from bs4 import BeautifulSoup

# webscrap do site
html = requests.get("http://www.portodoitaqui.com/porto-agora/navios").content
soup = BeautifulSoup(html, "html.parser")

# procura no site a tabela dos navios atracados
atracados = soup.find(id="atracados")
atracados_tab = atracados.find_all("tr")

# filtra os dados da tabela de navios atracados
n1 = []
for row in atracados_tab:
    cols = row.findChildren(recursive=False)
    cols = [element.text.strip() for element in cols]
    n1.append(cols)

# abre o arquivo em modo de escrita, escreve os novos dados e fecha o arquivo
with open(
    "navios_atracados_temp.csv", "a", newline="", encoding="utf-8"
) as navios_atracados_file:
    natemp = csv.writer(navios_atracados_file)
    natemp.writerows(n1)


# lê o arquivo CSV atualizado e mostra na tela
try:
    navios_atracados_updated = pd.read_csv(
        "navios_atracados_temp.csv", encoding="utf-8"
    )
    print(navios_atracados_updated)
except FileNotFoundError:
    print("Arquivo CSV não encontrado.")

# procura no site a tabela dos navios fundeados
fundeados = soup.find(id="fundeados")
fundeados_tab = fundeados.find_all("tr")

# filtra os dados da tabela de navios fundeados
n2 = []
for row in fundeados_tab:
    cols = row.findChildren(recursive=False)
    cols = [element.text.strip() for element in cols]
    n2.append(cols)

# abre o arquivo em modo de escrita, escreve os novos dados e fecha o arquivo
with open(
    "navios_fundeados_temp.csv", "a", newline="", encoding="utf-8"
) as navios_fundeados_file:
    natemp = csv.writer(navios_fundeados_file)
    natemp.writerows(n2)

# lê o arquivo CSV atualizado e mostra na tela
try:
    navios_fundeados_updated = pd.read_csv(
        "navios_fundeados_temp.csv", encoding="utf-8"
    )
    print(navios_fundeados_updated)
except FileNotFoundError:
    print("Arquivo CSV não encontrado.")

# procura no site a tabela dos navios esperados
esperados = soup.find(id="esperados")
esperados_tab = esperados.find_all("tr")

# filtra os dados da tabela de navios esperados
n3 = []
for row in esperados_tab:
    cols = row.findChildren(recursive=False)
    cols = [element.text.strip() for element in cols]
    n3.append(cols)

# abre o arquivo em modo de escrita, escreve os novos dados e fecha o arquivo
with open(
    "navios_esperados_temp.csv", "a", newline="", encoding="utf-8"
) as navios_esperados_file:
    natemp = csv.writer(navios_esperados_file)
    natemp.writerows(n3)

# lê o arquivo CSV atualizado e mostra na tela
try:
    navios_esperados_updated = pd.read_csv(
        "navios_esperados_temp.csv", encoding="utf-8"
    )
    print(navios_esperados_updated)
except FileNotFoundError:
    print("Arquivo CSV não encontrado.")
