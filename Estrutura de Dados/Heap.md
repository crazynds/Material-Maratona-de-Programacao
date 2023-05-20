# Heap (Arvore binaria em array)

O heap simula uma arvore binária em um array. Ele é muito eficiente para remover o elemento de menor prioridado e adicionar elementos e manter a arvore ordenada.

Aplicações:
 - Dijkstra
 - Priority Queue (fila)

## Python - [Heap](https://docs.python.org/3/library/heapq.html)

O python tem filas utilizando a biblioteca _heapq_ que já vem por padrão com o python nas versões mais recentes. (>=3.7)

As funções utilizados no heap são citadas abaixo:


### Modificadores:
 - heappush(): adiciona um elemento ao array heap;
 - heappop(): remove o menor elemento do array heap;
 - heappushpop(): adiciona um elemento ao array heap e remove o menor elemento, é mais eficiente que executar as duas funções em separado;
 - heapify(): transforma um array em um array heap;


Exemplo:
```python
import heapq

arr = [5,17,0,3,7,9]

arr = heapq.heapify(arr)  # transform unsorted array in heapified array

heapq.heappush(arr,6) # add 6 to heap array
heapq.heappush(arr,17) # add 17 to heap array
v1 = heapq.heappop(arr) # return the smallest element from heap array

v2 = heapq.heappushpop(arr,4) # return the smallest elemento and push 4 to heap array

```





