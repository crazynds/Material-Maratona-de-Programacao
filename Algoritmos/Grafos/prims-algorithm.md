# Prim's Algorithm

O algoritmo de prim's se baseia em uma ideia muito parecida do algoritmo Dijkstra. Ele seleciona um nó aletório para começar a busca, e adiciona todas as arestas que ele está ligado a uma lista Heap, e sempre remove a menor. 

Se ambos os nós da aresta removida da Heap já está na MST, então a aresta é descartada, se todos os nós do grafo estão na MST, então o algoritmo finaliza. Prim's algoritmo é provado que consegue chegar sempre na MST em tempo O(m*log(n)), é possivel melhorar o desepenho se usado uma estrutura [heap com dicionário](./../../Estrutura%20de%20Dados/HeapDictionaried.md).


```python
def primAlgorithm(graph,initialNode = 0):
    '''
        complexity: O(m*log(n))
        m = edges
        n = nodes

        this function return a list of edges of MST

        can be faster if you replace s(set) to a array of True or False
            - code needs to be adapted to this change;
    '''
    s = set()
    s.add(initialNode)
    tree = []

    arr = []
    a = initialNode
    for b in graph[a]:
        heapq.heappush(arr,(graph[a][b],a,b))

    while len(s)!=len(graph) and len(arr)>0:
        (cost,a,b) = heapq.heappop(arr)
        if b in s:
            continue
        
        tree.append((a,b,cost))
        s.add(b)
        
        a = b
        for b in graph[a]:
            if b not in s:
                heapq.heappush(arr,(graph[a][b],a,b))

        pass
    return tree 
```