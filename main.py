import numpy as np

data = np.array([2, 4, 6, 8, 10])

print(data)
print(type(data))
print(data.shape) # Tamanho do array

data = np.arange(15)

print(data)

data = np.random.rand(15) # Números float aleatórios entre 0 e 1
print(data)

data = np.random.randint(15, size = 10) # Números int aleatórios
print(data)

data = np.random.random([2,2])
print(data)

data = np.zeros([3,4])
print(data)

data = np.ones([3, 4])
print(data)

data = np.empty([3, 4])
print(data)

data = np.arange(10) * -1
print(data)

tamanho = 10
data6 = np.random.permutation(tamanho)
print(data6)

#unidimensional

data = np.random.randint(5, size = 10)

print(data)
print(data.shape)

#bimensional

data = np.random.randint(5, size = (3,4))
print(data)

#tridimensional

data = np.random.randint(5, size = (5, 3, 4))
print(data)
print(data.shape)

#possíveis verificações

print(data.ndim)
print(data.size)
print(data.shape)

print(f'Cada elemento possui {data.itemsize} bytes')
print(f'Toda a matriz possui {data.nbytes} bytes')

print(data.max())

#Consulta dentro de um intervalo

print(data[:5])
print(data[])
