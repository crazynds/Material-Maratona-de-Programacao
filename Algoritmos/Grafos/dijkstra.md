# Algoritmo de Dijkstra

Esse algoritmo serve para determinar o menor caminho entre dois vértices de um grafo, desde que o peso das arestas
não seja negativo por conta que o Dijkstra não é capaz de detectar ciclos negativos. Caso o grafo em questão não 
contenha ciclos negativos, do algoritmo Dijkstra pode ser usado.

Nota:É possivel detectar ciclos negativos em O(N).


### Python
```python
def dijkstra(nodes,src):
    """
        complexity: O(m*log(n))
        m = edges
        n = nodes

        this function return a list of distances from src

        can be faster if you implement heapDictionary (maybe?, in C++ using heapDictionary is faster, but in python i dont think so...)
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


### C++

```C++
#define INF_INT (((unsigned int)-1) >> 1)
 
// List of adj Obs: acredito que está funcionando. Confia! 😉 
vector<ll> dijkstra(vector<vector<pair<ll, ll>>> &graph, int src)
{
    priority_queue<pair<ll, ll>, vector<pair<ll, ll>>, greater<pair<ll, ll>>> pq;
    vector<ll> resp(graph.size());
    for (int x = 0; x < n; x++)
    {
        resp[x] = (x != src) ? INF : 0;
    }
    pq.emplace(0, 0);
    while (!pq.empty())
    {
        auto [du, u] = pq.top();
        pq.pop();
        if (du > dist[u])
            continue;
        for (auto &[v, dv] : graph[u])
        {
            if (dist[v] > dist[u] + dv)
            {
                pq.emplace(dist[u] + dv, v);
                dist[v] = dist[u] + dv;
            }
        }
    }
    return resp;
}

// Outra implementação que roubei de: João Henrique Alves dos Santos hehehe!
vector<ll> dijkstra(vector<vector<pair<ll, ll>>> graph, int src)
{
    priority_queue<pair<ll, ll>, vector<pair<ll, ll>>, greater<pair<ll, ll>>> pq;
    vector<ll> resp(graph.size());
    for (int x = 0; x < n; x++)
    {
        resp[x] = (x != src) ? INF : 0;
    }
    pq.emplace(0, 0);
    while (!pq.empty())
    {
        auto [du, u] = pq.top();
        pq.pop();
        if (du > dist[u])
            continue;
        for (auto &[v, dv] : graph[u])
        {
            if (dist[v] > dist[u] + dv)
            {
                pq.emplace(dist[u] + dv, v);
                dist[v] = dist[u] + dv;
            }
        }
    }
    return resp;
}
```


## APSP


Implementação de _All Pairs Shortest Path_ usando Dijkstra para grafos direcionados com pesos não negativos.
Ele apenas repete o Dijkstra para cada nó $i$ como inicial e armazena numa matriz os resultados.

```python
def dijkstra_apsp(nodes):
    """
        complexity: O(n*m*log(n))
        m = edges
        n = nodes


        this function recive a list of nodes from a graph that can be directed or not
        this function return a matriz of shortest path from every node to other node
    """
    return [dijkstra(nodes,i) for i in range(len(nodes))]

```
