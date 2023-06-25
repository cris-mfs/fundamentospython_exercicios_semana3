#Exercício Ficha de Trabalho semana 4 - Cristiano Silva

import pandas as pd

def ler_dados_excel(caminho_do_ficheiro):
    return pd.read_excel(caminho_do_ficheiro)

def filtra_dados_por_paiís(dados, nome_país):
    return dados[dados["Country Name"]==nome_país]

def calcular_variação_percentual(valor_inicial, valor_final):
    return (valor_final-valor_inicial)/valor_inicial * 100

dados = ler_dados_excel("P_Data_Extract_From_World_Development_Indicators.xlsx")
dados = dados[["Country Name", "1990 [YR1990]", "2000 [YR2000]"]]

dados_portugal = filtra_dados_por_paiís(dados, "Portugal")
consumo_inicial = dados_portugal["1990 [YR1990]"].values[0]
consumo_final = dados_portugal["2000 [YR2000]"].values[0]
variacao = calcular_variação_percentual(consumo_inicial, consumo_final)

print(f'A Variação percentual no consumo de energia elétrica em Portugal entre 1990 e 2000 foi de: {variacao:.2f}%')

#Gráfico de Barras

import matplotlib.pyplot as plt

categorias = ["Ano 1990", "Ano 2000"]
valores = [consumo_inicial,consumo_final]

plt.bar(categorias, valores, color="blue")
plt.ylabel("Consumo em kWh")
plt.title("Variação de consumo de energia elétrica em Portugal entre 1990 e 2000\n")
plt.show()