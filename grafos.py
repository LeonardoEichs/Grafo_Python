# Importando de Bibliotecas

from collections import defaultdict
from random import randint

# Classe
class Grafo(object):

    # Construtor
    def __init__(self, conexoes, direcionado = False):
        self._grafo = defaultdict(set)
        self._direcionado = direcionado
        self.conectaArestas(conexoes)

    # Muda apenas como a informação é mostrada
    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._grafo))

    # Adiciona Vertice, caso já exista algum com mesmo nome é feito um aviso
    # e não é criado.
    def adicionaVertice(self, nodo):
        for x in self._grafo.keys():
            if (x == nodo):
                print("ESSE NODO JÁ EXISTE \n")
                return;
        self._grafo[nodo].add(None)
        self._grafo[nodo].remove(None)

    # Conecta multiplas arestas recebendo um argumento chamado conexoes, que tem
    # forma de lista contendo tuplas que representam os nodos a serem conctados
    def conectaArestas(self, conexoes):
        for nodo1, nodo2 in conexoes:
            self.conecta(nodo1, nodo2)

    # Cria uma aresta que liga nodo1 com nodo2, leva em consideracao se o Grafo
    # é direcionado ou não
    def conecta(self, nodo1, nodo2):
            self._grafo[nodo1].add(nodo2)
            if not self._direcionado:
                self._grafo[nodo2].add(nodo1)

    # Remove um vertice, primeiro remove as "arestas" que contém esse nodo e
    # depois apaga o nodo em si
    def removeVertice(self, nodo):
        for x, conj in self._grafo.items():
            try:
                conj.remove(nodo)
            except KeyError:
                pass
        try:
            del self._grafo[nodo]
        except KeyError:
            pass

    # Remove a aresta que liga o nodo1 com o nodo2
    def desconecta(self, nodo1, nodo2):
        self._grafo[nodo1].remove(nodo2)
        self._grafo[nodo2].remove(nodo1)

    # Retorna o número de vértices do Grafo
    def ordem(self):
	     return len(list(self._grafo))

    # Retorna um conjunto contendo os vértices do Grafo
    def vertice(self):
        return self._grafo.keys()

    # Retorna um vértice aleatório do Grafo
    def umVertice(self):
        tamanho = self.ordem()
        vertices = self.vertice()
        randomNum = randint(0, tamanho - 1)
        return vertices[randomNum]

    # Retorna um conjunto contendo os vértices adjacentes ao nodo no Grafo
    def adjacentes(self, nodo):
        return self._grafo[nodo]

    # Retorna o número de vértices adjacentes ao nodo no Grafo
    def grau(self, nodo):
        adjacentes = self.adjacentes(nodo)
        if (adjacentes != None):
            return len(adjacentes)
        return;

    # Encontra o menor caminho entre o nodo1 e nodo2
    def shortestPath(self, inicio, fim, caminho=[]):
        caminho = caminho + [inicio]
        if inicio == fim:
            return caminho
        if not self.hasKey(inicio):
            return None
        menor = None
        for nodo in self._grafo[inicio]:
            if nodo not in caminho:
                novoCaminho = self.shortestPath(nodo, fim, caminho)
                if novoCaminho:
                    if not menor or len(novoCaminho) < len(menor):
                        menor = novoCaminho
        return menor

    # Método de suporte para shortestPath, verifica se exista "key"
    def hasKey(self, key):
        for x, conj in self._grafo.items():
            if(key == x):
                return True;
        return False;

    # Depth First Search, usa recursividade
    def depthFirstSearch(self, inicio, caminho = []):
        caminho = caminho + [inicio]
        for nodo in self._grafo[inicio]:
            if not nodo in caminho:
                caminho = self.depthFirstSearch(nodo, caminho)
        return caminho

    # Breadth First Search, iterativo
    def breadthFirstSearch(self, inicio, caminho = []):
        stack = [inicio]
        while stack:
            v = stack.pop(0)
            if not v in caminho:
                caminho = caminho + [v]
                stack = stack + list(self._grafo[v])
        return caminho



################################################################################


conexoes = [('A', 'B'), ('A', 'S'),
               ('S', 'G'), ('S', 'C'),
               ('G', 'F'), ('G', 'H'),
               ('C', 'F'), ('C', 'D'), ('C', 'E'),
               ('E', 'H')]


g = Grafo(conexoes)
print(g._grafo)
print("\n")
print("\n")

print(g.shortestPath('A','F'))
print(g.depthFirstSearch('A'))
print(g.breadthFirstSearch('A'))
