import pandas as pd 
import statistics as sts

dados = pd.read_json('dados.json')

valor = dados.loc[dados['valor'] > 0 ]

media = sts.mean(valor['valor'])

contador = valor.loc[valor['valor'] > media].count()

minimo = valor.min(axis=0)
maximo = valor.max(axis=0)

print(f'O menor valor ocorrido em um dia do mes foi {float(minimo["valor"])} R$')
print(f'O maior valor ocorrido em um dia do mes foi {float(maximo["valor"])} R$')
print(f'O número de dias do mes em que o valor de faturamento diário foi superior a média mensal é de {contador["dia"]} dias')
