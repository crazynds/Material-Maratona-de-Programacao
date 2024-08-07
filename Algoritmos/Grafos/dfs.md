# Depth First Search

A DFS ou busca em profudidade realiza uma busca iterativa sempre no próximo nó encontrado. Ela ignora nós já passados e quando a busca é completa no nó ela retorna para o seu pai. Ela é executada de forma recursiva.



## Python

```python
import sys
# Sempre bom aumentar o número de recursões
sys.setrecursionlimit(1000)


def dfs(graph: list[set], node: int, visited: list[bool]):
    visited[node] = True
    for child in list[node]:
        if not visited[child]:
            dfs(graph,child,visited)

```

Note que esse algoritmo em python não é tão eficiente, e quando se deparar com um problema grande o suficiente é melhor fazer a solução em C/C++. Python não trabalha muito bem com recursões e gasta muita memoria para aumentar o limite de recursão.

## C++


```c++
#include <bits/stdc++.h>

using namespace std;
void dfs(vector<unordered_set<int>> &graph, int node, vector<bool> &visited)
{
    visited[node] = true;
    for (auto child : graph[node])
    {
        if (!visited[child])
            dfs(graph, child, visited);
    }
}

```