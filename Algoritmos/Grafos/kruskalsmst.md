# Kruskal's MST

O algoritmo de Kruskal se baseia no conceito ordenar as arestas e ir iterando sobre elas em ordem crescente de peso. Dessa forma se a aresta que está sendo consultada não vai gerar um ciclo dentro do novo grafo, então insere essa aresta no grafo. 

Para verificar se existe ciclos no grafo, é usado uma estrutura de [DisjoinSet](./../../Estrutura%20de%20Dados/DisjoinSet.md). A ideia por tras disso é que se uma aresta $X$ que liga o vertice $A$ com o vertice $B$ e se os vertices pertencessem ao mesmo cluster, então um ciclo vai ser criado se adicionar essa aresta ao novo grafo. 


```python
def kruskalsMST(nodes: int,edges: list):
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


