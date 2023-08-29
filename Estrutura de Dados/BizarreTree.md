# BizarreTree

É uma criação minha que implementa as funcionalidades de uma arvore sem uma árvore.

Isso é util em python que implementar uma árvore pode ser muito demorado além da arvore ser extremamente lenta na execução. Tem também o problema de balanceamento que deve se levar em conta dependendo do problema.

A _BizarreTree_ não é uma árvore de fato, ela utiliza um _dictionary_ e duas _heap_ para simular as funções principais de uma árvore, podendo assim pegar o menor valor, o maior e iterar sobre ela de maneira crescente e decrescente.

Os custos das operações seguem abaixo:

 - Inserção: O(log n) _heap push_
 - Remoção: O(1) _dictionary acess_
 - Find: O(1) _dictionary acess_
 - Min: O(k log n) k* _heap pop_
 - Max: O(k log n) k* _heap pop_

Para k sendo a quantidade de elementos que foram removidos da árvore entre as chamadas de _min_ e _max_.

- [Crazynds](https://github.com/crazynds)

## Python

Como eu fiz ela especialmente para resolver as funções de árvores em python, só faz sentido a implementação em python. Mas é possivel adaptar em qualquer outra linguagem. 

```python
import heapq
from collections import defaultdict

class BizarreTree:

    def __init__(self) -> None:
        self.minArr = []
        self.maxArr = []
        self.size = 0
        self.data = defaultdict(int)
        pass

    def find(self,val):
        return self.data[val] > 0

    def insert(self,val):
        self.data[val] += 1
        self.size += 1
        heapq.heappush(self.minArr,val)
        heapq.heappush(self.maxArr,-val)

    def delete(self,val):
        if self.data[val] > 0:
            self.size -= 1
            self.data[val] -= 1
    
    def min(self):
        while self.data[self.minArr[0]] == 0:
            heapq.heappop(self.minArr)
        return self.minArr[0]

    def max(self):
        while self.data[-self.maxArr[0]] == 0:
            heapq.heappop(self.maxArr)
        return -self.maxArr[0]
```


É possivel fazer a iteração dessa árvore de forma crescente, mas deixo com você essa parte. Só por ter lido até aqui sei que você é uma pessoa esperta. 