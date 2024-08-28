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

## Topological Sorting

Usando DFS é possivel ordenar os nós de um gráfico direcionado aciclíco de forma que se tenha uma ordem de modo que cada aresta va do vértice com um índice menor a um vértice com um índice maior.



```C++
int n; // number of vertices
vector<vector<int>> adj; // adjacency list of graph
vector<bool> visited;
vector<int> ans;

void dfs(int v) {
    visited[v] = true;
    for (int u : adj[v]) {
        if (!visited[u])
            dfs(u);
    }
    ans.push_back(v);
}

void topological_sort() {
    visited.assign(n, false);
    ans.clear();
    for (int i = 0; i < n; ++i) {
        if (!visited[i]) {
            dfs(i);
        }
    }
    reverse(ans.begin(), ans.end());
}
```

