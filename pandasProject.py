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

data = pd.DataFrame(data = np.random.randn(6,5),
                    index= [1,2,3,4,5,6],
                    columns= ['a', 'b', 'c', 'd', 'e'])
print(data)
print(data.columns)
print(data.index)
print(data['c'])
print(type(data['c']))
print(data.d)

#Extração de + de 1 coluna

print(data[['a', 'e']])
data['f'] = data['d'] + data['e']
print(data)

#Removendo colunas manualmente

data = data.drop('f', axis = 1)
print(data)

#Em arquivos ipynb

#data = data.drop('a', axis=1, inplace=True)

del data['b']
print(data)

#Ordenar uma coluna

dataf = pd.DataFrame(data= np.random.randn(6,5),
                     index= [1,2,3,4,5,6],
                     columns= ['a', 'b', 'c', 'd', 'e'])
print(dataf)
dataf.sort_values(by = 'b', inplace=True)
print(dataf)

#Extraindo dados de uma linha específica

print(dataf.loc[3])
print(dataf.loc[2,'b']) #elemento específico
print(dataf.loc[[2,3], ['a','b','c']]) #um intervalo
print(dataf.iloc[1:3,0:3]) #um intervalo

#Buscando elementos via condição

print(dataf > 0)

#Operações Matemáticas

data = pd.DataFrame(data = np.random.randn(6,5),
                    index = [1,2,3,4,5,6],
                    columns= ['a', 'b', 'c', 'd', 'e'])

print(data)
print(data['b'].sum())
print(data.sum()) #Retorna em série

data = data + 1
print(data)

#Funções matemáticas personalizadas

def soma(x):
    return x + x

print(data['b'].apply(soma))

def ao_quadrado(num):
    return num ** 2

print(data['a'].apply(ao_quadrado))
print(data.iloc[0:1, 1:2].apply(ao_quadrado))

#Expressão lambda

print(data['d'].apply(lambda x: x ** 2))

#Estruturas condicionais

data2 = data[data['d'] > 0]
print(data2)
print(data[data['d'] > 0]['e']) #Aqui também altera de forma permanente

#Condicionais compostas

print(data[(data['a'] > 0) & (data['e'] < 0)]) #Operador and
print(data[(data['a'] > 0) | (data['b'] < 0)]) #Operador or

#Atualizando um DataFrame de acordo com uma condicional

data_positivos = data > 0
data = data[data_positivos]

print(data)



