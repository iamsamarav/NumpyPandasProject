import pandas as pd
import numpy as np

#Estrutura de Series

base = [1,2,3,4,5,6,7,8,9,10]
data = pd.Series(base)
print(data)
print(type(data))

#Outra forma de criar uma Serie

data = pd.Series([1,2,3,4,5,6,7,8,9,10])
print(data)

data = pd.Series(['Ana', 'Carlos', 'Diego', 'Fernando', 'Maria', 'Paulo'])
print(data)

nomes = data

data3 = pd.Series(data = nomes)
print(data3)

#DataFrames

base = {'Nomes':['Hanna', 'Samara', 'Valquiria'],'Fones':[81934459087, 81990909191, 81995959090]}
print(base)
data = pd.DataFrame(base)
print(data)

#Visualizando o cabeçalho

print(data3.head())

#Indice personalizado

indice = [1,2,3,4,5,6,7,8,9]
data4 = pd.Series(data = nomes,
                  index = indice)

print(data4)

# Array Numpy em uma Serie

nomes_mod = np.array(nomes)
data5 = pd.Series(data = nomes_mod)
print(data5)

#Qualquer estrutura em uma Serie

funcoes = [input, print]
data6 = pd.Series(data = funcoes)

print(data6)

#Integrando funções com Series

paises = ['Argentina', 'Brasil', 'Canadá', 'Estados Unidos', 'Itália', 'México']
data7 = pd.Series(data = paises,
                  index = np.arange(0,6))

print(data7)

#Tamanho de uma Serie

print(data.index)
print(data7.index)

#Série de um dicionário

dicionario = {'Nome': 'Fernando', 'Idade': 33, 'Altura': 1.90}
serie_dicio = pd.Series(dicionario)
print(serie_dicio)

#Unindo elementos de duas Series

nomes2 = ['Ana', 'Alberto', 'Maria', 'Paulo', 'Tania']
nomes1 = ['Ana', 'Carlos', 'Betina', 'Maria', 'Rafael']
data_1 = pd.Series([1,2,3,4,5], index = nomes1)
data_2 = pd.Series([1,2,3,4,5], index = nomes2)

data_3 = data_1 + data_2
print(data_3)

#Criando um DataFrame

data = pd.DataFrame(base)
print(data)
print(data.info())
print(data.describe())