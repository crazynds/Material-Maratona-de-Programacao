# Busca em Profundidade


Segue a regra abaixo:

![](./buscaProfundidade.webp)


```python

import abc
from treelib import Node, Tree

class BuscaProfundidade(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self) -> None:
        pass

    @abc.abstractmethod
    def computaChave(self,estado):
        """This method should create a unique key for this state to prevent pass again in this state"""
        return 0

    @abc.abstractmethod
    def abreNovosEstados(self,estado):
        """This method should be a generator for all news states to navigate
            Remember, this Deep search don't need all states to be memory independente (you can reuse your object).
            You can process your object before the yield instruction (open) and after (close)."""
        return []
    
    @abc.abstractmethod
    def verificaCondicaoDeParada(self,estado):
        """Return false if you want to continue, return None if you want to discart this branch, return anything else if you find the solution"""
        return True

    def encontraSolucao(self,estadoAtual,generateTree = False):
        if generateTree:
            self.tree = Tree()
            chav = self.computaChave(estadoAtual)
            self.tree.create_node(str(chav),str(chav),data={'color':'gray'})
        return self.__executa(estadoAtual,set(),generateTree)
    
    def __executa(self,estadoAtual,visitados,generateTree):
        chave = self.computaChave(estadoAtual)
        if chave in visitados:
            return None
        visitados.add(chave)
        parada = self.verificaCondicaoDeParada(estadoAtual)
        if parada != False:
            return parada
        for novoEstado in self.abreNovosEstados(estadoAtual):
            if generateTree:
                chav = self.computaChave(novoEstado)
                if chav not in visitados:
                    self.tree.create_node(str(chav),str(chav),parent=str(chave))

            resultado = self.__executa(novoEstado,visitados,generateTree)
            if resultado != None:
                return resultado
        return None
```