# Algoritmo de Dijkstra

Esse algoritmo serve para determinar o menor caminho entre dois vértices de um grafo, desde que o peso das arestas
não seja negativo.

```python
import heapq

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
        
        for child in nodes[node]['child']:
            if visited[child]:
                continue
            heigth = nodes[node]['child'][child]
            aux = dist[node] + heigth
            if aux < dist[child]:
                dist[child] = aux
                heapq.heappush(queue,(aux,child))
    return dist
```
