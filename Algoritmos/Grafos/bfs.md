# Breadth First Search
O BFS ou busca em largura, para cada nó, ele adiciona todos os filhos a uma fila, e sempre o próximo nó a ser executado é o primeiro da fila. Dessa forma consome mais memória, porém não depende de recursão e consegue se espalhar de maneira igual a partir do primeiro nó.


## Python

```python

from collections import deque

def bfs(graph: list[set], node: int):
    visited = [False] * len(graph)
    stack = deque([node])
    # check if is not empty
    while stack:
        node = stack.popleft()
        #  You need this check
        if visited[node]:
            continue
        visited[node] = True
        for child in list[node]:
            #  You need this check too
            if not visited[child]:
                stack.append(child)



```

## C++

```c++
#include <bits/stdc++.h>

using namespace std;

void bfs(vector<unordered_set<int>> &graph, int node){
    deque<int> stack;
    vector<bool> visited(graph.size());
    stack.push_back(node);
    while (!stack.empty()) {
        int currentNode = stack.top();
        stack.pop_front();
        // You need this check
        if (visited[current]) continue;
        visited[current] = true;
        for (auto child : graph[node])
        {
            // You need this check too
            if (!visited[child])
                stack.push_back(child);
        }
    }
}

```


# Problemas

## Nós mais distantes

Esse é um algoritmo para encontrar quais são os dois nós mais distantes entre si em um grafo conexo sem pesos. Note que não é para encontrar o maior caminho no grafo, e sim os dois nós mais distantes entre si.

```python
def bfs_adapted(graph: list[set], node: int):
    visited = [-1] * len(graph)
    stack = deque([(node,0)])
    maxDist = node
    # check if is not empty
    while stack:
        node,dist = stack.popleft()
        if visited[node] >= 0:
            continue
        visited[node] = dist
        if dist > visited[maxDist]:
            maxDist = node
        for child in list[node]:
            if visited[child] < 0:
                stack.append((child,dist+1))
    return (node,maxDist)

def resolve(graph: list[set]):
    ponta1,dist = bfs_adapted(graph,0)
    ponta2,dist = bfs_adapted(graph,ponta1)
    # No1 - No2 e a distancia entre eles
    return (ponta1,ponta2,dist)
```

Comentário: É possivel adaptar para usar uma heapq e fazer ele encontrar o maior caminho entre dois nós, sem ficar infinitamente em um ciclo.


