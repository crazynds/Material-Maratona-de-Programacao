# Johnson Algorithm

Ele tenta adaptar o algoritmo de [Dijkstra](./dijkstra.md) para grafos com pesos negativos. Esse algoritmo aplica um _shift_ (incremento) dos valores das arestas do grafo para que não haja arestas com valores negavitos.

Esse algoritmo usa o algoritmo de [Bellman-Ford] no primeiro passo para calcular o valor $P_v$ para cada vertice. Usando esses valores $P_v$ de cada vertice, é aplicado o seguinte calculo para fazer o incremento de cada aresta:
$$
    Edge=(i,j,w)
$$
$$
    w' = w + P_i - P_j
$$

Após aplicada a formula, todas as arestas devem estar com pesos não negativos. Então é aplicado o algoritmo de Dijkstra para encontrar o menor caminho.

Agora a prova do porque e como que funciona fica com você, boa sorte. Saiba que funciona.


O algoritmo abaixo depende dessas seguintes funções:
 - [bellmanford](./Bellman-Ford.md)
 - [convertEdgesArrayToDirectedSimpleGraph](./GrafosCrazynds/conversao_estruturas.md)
 - [dijkstra](./dijkstra.md)

```python
def johnson(edges: list, vertices):
    """
        complexity: O(n + m*n + m + n*m log n + n^2) = O(n*m log n)
        m = edges
        n = nodes

        this function return a list of distances from every pair of nodes

    """
    # Add a new Vertice and add an edge from this vertice to every other vertice with weight zero
    newVertice = vertices
    edges.extend([(newVertice,i,0) for i in range(vertices)])

    # Compute a P_v for every vertice
    vW,_ = bellmanford(edges,vertices+1,newVertice)

    # Remove the edges previously added
    del edges[-vertices:]

    if vW[0] == float('-inf'):
        return [[float('-inf')]*vertices for _ in range(vertices)]

    # Apply the function to every edge
    newEdges = [(s,d,w+vW[s]-vW[d]) for s,d,w in edges]

    # Convert the new edges to a grahp
    nodes = convertEdgesArrayToDirectedSimpleGraph(newEdges,vertices)

    # Compute dijkstra to get the ASAP
    bestPaths = [dijkstra(nodes,i) for i in range(vertices)]

    # Correct the values of the paths
    for i in range(vertices):
        for j in range(vertices):
            bestPaths[i][j] = bestPaths[i][j] - vW[i] + vW[j]

    return bestPaths
```
