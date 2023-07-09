# Algoritmo A*

O algoritmo é quase identico ao algoritmo [Dijkstra](./dijkstra.md), porém ao invés de ordenar os nós na estrutura heap pelos pessos das arestas, ele atribui uma heuristica, dessa forma é possivel chegar a outros caminhos com condições mais complexas do que apenas o pesos das arestas.


```python

import abc
import heapq as hq


class BuscaA(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def computaChave(self,estado):
        """This method should create a unique key for this state to prevent pass again in this state"""
        return 0
    
    @abc.abstractmethod
    def abreNovosEstados(self,estado):
        """This method should be a generator for all news states to navigate.
            Remember, this Width search need all states to be memory independente (one state can not be same object of other state)
        """
        return []
    
    @abc.abstractmethod
    def verificaCondicaoDeParada(self,estado):
        """Return false if you want to continue, return None if you want to discart this branch, return anything else if you find the solution"""
        return True
    
    def computaPeso(self,estado):
        """This method should return a weight to place this state in the queue. Less weight meaning this will execute first
            This method is also called 'Heuristic'
            By default, this method call 'computaChave' and return the result
        """
        return self.computaChave(estado)

    def encontraSolucao(self,estadoInicial):
        return self.__executa(estadoInicial,set(),[])
    
    def __executa(self,estadoInicial,visitados,queue):
        hq.heappush(queue,(self.computaPeso(estadoInicial),0,estadoInicial))
        visitados.add(self.computaChave(estadoInicial))
        count = 1
        while len(queue)>0:
            _,_,estadoAtual = hq.heappop(queue)
            parada = self.verificaCondicaoDeParada(estadoAtual)
            if parada!=False:
                return parada
            for estado in self.abreNovosEstados(estadoAtual):
                chave = self.computaChave(estado)
                if chave not in visitados:
                    visitados.add(chave)
                    hq.heappush(queue,(self.computaPeso(estado),count,estado))
                    count += 1

        return None
```