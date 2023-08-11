# Bellman-Ford

Esse algoritmo serve para encontrar o menor caminho entre dois vértices em um grafo com arestas com peso negativo.
Não somente isso, ele também é o algoritmo usado para o roteamento de pacotes na internet, já que ele possibilita o processamento descentralizado de grafos, onde cada vertice precisa calcular apenas as arestas que ele está conectado, e propagar o seu valor para os vertices vizinhos.

```python

def bellmanford(edges: list,vertices,src):
    """
        complexity: O(m*n)
        m = edges
        n = nodes

        this function return a list of distances from src
        different than dijkstra, the bellman ford can compute correct distances over negative edges
        work in directed graphs, there is no sense a non directed graph with negative edges (think about)

    """
    # In theory, sort the edges array can make the code fast because of the sequential reading of the array, but in reality this is over engineering
    # edges.sort()
    inf = float('inf')
    current = [inf]*vertices
    current[src] = 0

    ## Optional, only for backtrace
    trace = [i for i in range(vertices)]

    for _ in range(1,vertices): # run n-1 times
        change = False # premature optimization
        for s,d,w in edges:
            if current[s]!=inf and current[s] + w < current[d]:
                change = True
                current[d] = current[s] + w
                ## Optional, only for backtrace
                trace[d] = s

        if not change: # if any change in array ocurr, then already got the final result
            break
    else: # Run one more to check infinit loops
        # the path between 2 vertices has at max n-1 edges without negative loops, 
        # if the path has more than n-1 edges, so it has a negative loop in the graph 
        for s,d,w in edges:
            if last[s] + w < last[d]:
                ## 2nd return value is optional, only for backtrace
                return [float('-inf')]*vertices,trace

    ## 2nd return value is optional, only for backtrace
    return last,trace

```

# ASAP

Existe uma variação do algoritmo no qual é possivel calcular a distancia entre todos os pares de vertices do grafo, o algoritmo é semelhante a executar o algoritmo original N vezes, sendo cada vez uma origem diferente, porém a implementação abaixo ela possibilita o uso de instruções SIMD.


```python
def bellmanford_asap(edges: list,vertices):
    """
        complexity: O(m*n^2)
        m = edges
        n = nodes

        this function return a list of distances from every pair of nodes
        this is a variation of the original bellmanford algorithm that execute N * belmanford for every vertice

    """
    # In theory, sort the edges array can make the code fast because of the sequential reading of the array, but in reality this is over engineering
    # edges.sort()
    inf = float('inf')
    current = [[inf]*vertices  for _ in range(vertices)]
    for i in range(vertices):
        current[i][i] = 0

    ## Optional, only for backtrace
    trace = [[i for i in range(vertices)] for _ in range(vertices)]

    for _ in range(1,vertices): # run n-1 times
        change = False # premature optimization
        for s,d,w in edges:

            # this for loop can be boosted if implemented using SIMD instructions
            for i in range(vertices):
                if current[s][i]!=inf and current[s][i] + w < current[d][i]:
                    change = True
                    current[d][i] = current[s][i] + w
                    ## Optional, only for backtrace
                    trace[d][i] = s

        if not change: # if any change in array ocurr, then already got the final result
            break
    else: # Run one more to check infinit loops
        # the path between 2 vertices has at max n-1 edges without negative loops, 
        # if the path has more than n-1 edges, so it has a negative loop in the graph 
        for s,d,w in edges:
            for i in range(vertices):
                if current[s][i] + w < current[d][i]:
                    ## 2nd return value is optional, only for backtrace
                    return [float('-inf')]*n,trace

    # You need to rotate the array, so the src is the first index, and the dst is the second,
    # You can skip this if you wish, but the index are reversed, like: result[dst][src] = ShortestPath(src,dst)
    result = list(zip(*current))

    ## 2nd return value is optional, only for backtrace
    return result,trace

```

É preferivel usar qualquer outro algoritmo para resolver esse problema, esse algoritmo é muiiiito lento, procure usar [Johnson](./johnson-algorithm.md) para resolver esse problema.



