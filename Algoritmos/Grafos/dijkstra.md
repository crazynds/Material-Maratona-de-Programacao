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

        can be faster if you implement heapDictionary
    """
    inf = float('inf')
    queue = []
    dist = [float('inf')] * len(nodes)
    visited = [False] * len(nodes)

    heapq.heappush(queue,(0,src))
    dist[src] = 0

    while len(queue)>0:
        _,node = heapq.heappop(queue)
        if visited[node]:
            continue
        visited[node] = True
        
        for child in nodes[node]:
            if visited[child]:
                continue
            heigth = nodes[node][child]
            aux = dist[node] + heigth
            if aux < dist[child]:
                dist[child] = aux
                heapq.heappush(queue,(aux,child))
    return dist
```


## Implementação usando [HeapDictionary](./../../Estrutura%20de%20Dados/HeapDictionaried.md)

Abaixo a implementação usando a biblioteca de Heap + Dictionary.

```python
def dijkstra(nodes,src):
    inf = float('inf')
    queue = HeapDictionary([(0,src)],key= lambda a:a[1])
    dist = [float('inf')] * len(nodes)
    visited = [False] * len(nodes)

    dist[src] = 0

    while queue.len()>0:
        _,node = queue.pop()
        if visited[node]:
            continue
        visited[node] = True
        
        for child in nodes[node]['child']:
            if visited[child]:
                continue
            heigth = nodes[node]['child'][child]
            aux = dist[node] + heigth
            if aux < dist[child]:
                dist[child] = aux
                queue.push((aux,child))
    return dist
```