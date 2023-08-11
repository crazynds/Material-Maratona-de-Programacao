# Algoritmo de Dijkstra

Esse algoritmo serve para determinar o menor caminho entre dois vértices de um grafo, desde que o peso das arestas
não seja negativo.

```python
def dijkstra(nodes,src):
    """
        complexity: O(m*log(n))
        m = edges
        n = nodes

        this function return a list of distances from src

        can be faster if you implement heapDictionary (maybe?, in C++ using heapDictionary is faster, but in python i dont think...)
    """
    inf = float('inf')
    queue = []
    dist = [inf] * len(nodes)

    heapq.heappush(queue,(0,src))
    dist[src] = 0

    while queue:
        d,node = heapq.heappop(queue)
        if d > dist[node]:
            continue
        
        for child in nodes[node]:
            weigth = nodes[node][child]
            aux = dist[node] + weigth
            if dist[child] > aux:
                dist[child] = aux
                heapq.heappush(queue,(aux,child))
    return dist
```


## Implementação usando [HeapDictionary](./../../Estrutura%20de%20Dados/HeapDictionaried.md)

Abaixo a implementação usando a biblioteca de Heap + Dictionary. Recomendo em python usar a versão normal do dijkstra, mas se for traduzir para C++ acredito que tenha um ganho.

```python
def dijkstra(nodes,src):
    inf = float('inf')
    queue = HeapDictionary([(0,src)],key= lambda a:a[1])
    dist = [inf] * len(nodes)
    dist[src] = 0
    while queue.len()>0:
        d,node = queue.pop()
        
        for child in nodes[node]:
            newDist = dist[node] + nodes[node][child]
            if dist[child] > newDist:
                dist[child] = newDist
                queue.push((newDist,child))
    return dist
```