# Kruskal's MST

O algoritmo de Kruskal se baseia no conceito ordenar as arestas e ir iterando sobre elas em ordem crescente de peso. Dessa forma se a aresta que está sendo consultada não vai gerar um ciclo dentro do novo grafo, então insere essa aresta no grafo. 

Para verificar se existe ciclos no grafo, é usado uma estrutura de [DisjoinSet](./../../Estrutura%20de%20Dados/DisjoinSet.md). A ideia por tras disso é que se uma aresta $X$ que liga o vertice $A$ com o vertice $B$ e se os vertices pertencessem ao mesmo cluster, então um ciclo vai ser criado se adicionar essa aresta ao novo grafo. 


```python
def kruskalsMST(edges: list,nodes: int):
    '''
        complexity: O(m*alpha(n)) + (sort operation)
        m = edges
        n = nodes

        this function return a list of edges of MST

        can be faster if yout implementation of SetUnion are better
    '''
    union = DisjointSetUnion(nodes)
    nEdges = []
    edges.sort(key=lambda e: e[2])
    for (a,b,cost) in edges:
        # Check if 'a' and 'b' already are in the same cluster
        if union.find(a) != union.find(b):
            union.union(a,b)
            nEdges.append((a,b,cost))
    return nEdges
```

## Algoritmo em C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Estrutura para representar uma aresta
struct Edge
{
    int u, v, weight;
    bool operator<(const Edge& other) const
    {
        return weight < other.weight;
    }
};

// Função para encontrar o representante (ou "pai") de um conjunto
int findSet(int v, vector<int>& parent)
{
    if (v == parent[v])
        return v;
    return parent[v] = findSet(parent[v], parent);
}

// Função para unir dois subconjuntos
void unionSets(int a, int b, vector<int>& parent, vector<int>& rank)
{
    a = findSet(a, parent);
    b = findSet(b, parent);
    if (a != b)
    {
        if (rank[a] < rank[b])
            swap(a, b);
        parent[b] = a;
        if (rank[a] == rank[b])
            rank[a]++;
    }
}

// n = número de vértices
// Função principal do algoritmo de Kruskal
int kruskal(int n, vector<Edge>& edges)
{
    sort(edges.begin(), edges.end());  // Ordena as arestas por peso
    vector<int> parent(n);
    vector<int> rank(n, 0);
    for (int i = 0; i < n; i++)
        parent[i] = i;

    int mstWeight = 0;
    for (Edge& edge : edges)
    {
        if (findSet(edge.u, parent) != findSet(edge.v, parent))
        {
            mstWeight += edge.weight;
            unionSets(edge.u, edge.v, parent, rank);
        }
    }

    return mstWeight;
}
```


