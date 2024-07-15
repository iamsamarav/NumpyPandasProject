import pandas as pd

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


