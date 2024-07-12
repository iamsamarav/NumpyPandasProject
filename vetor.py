import numpy as np

class Vetor:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.ultimo = -1
        self.elementos = np.empty(self.tamanho, dtype=int)

    def exibe_em_tela(self):
        if self.ultimo == -1:
            print('Vetor vazio!')
        else:
            for i in range(self.ultimo + 1):
                print(i, self.elementos[i])

    def insere_elemento(self, elemento):
        if self.ultimo == self.tamanho -1:
            print('Capacidade máxima atingida')
        else:
            self.ultimo += 1
            self.elementos[self.ultimo] = elemento

    def pesquisa_elemento(self, elemento):
        for i in range(self.ultimo+1):
            if self.elementos[i] == elemento:
                return i
        return -1

    def exclui_elemento(self, elemento):
        posicao = self.pesquisa_elemento(elemento)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao,self.ultimo):
                self.elementos[i] = self.elementos[i+1]
                self.ultimo -= 1