# Bellman-Ford

Esse algoritmo serve para encontrar o menor caminho entre dois vértices em um grafo com arestas com peso negativo.
Não somente isso, ele também é o algoritmo usado para o roteamento de pacotes na internet, já que ele possibilita o processamento descentralizado de grafos, onde cada vertice precisa calcular apenas as arestas que ele está conectado, e propagar o seu valor para os vertices vizinhos.

```python

def bellmanford(edges: list,src):
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
    current = [inf]*n
    last = [inf]*n
    last[src] = 0

    ## Optional, only for backtrace
    trace = [i for i in range(n)]

    for _ in range(1,n): # run n-1 times
        change = False # premature optimization
        for s,d,w in edges:
            current[d] = min(current[d],last[d],last[s] + w)
            change |= current[d] != last[d] # check if some change ocurr at all

            ## Optional, only for backtrace
            if current[d] == last[s] + w:
                trace[d] = s

        current,last = last,current
        if not change: # if any change in array ocurr, then already got the final result
            break
    else: # Run one more to check infinit loops
        # the path between 2 vertices has at max n-1 edges without negative loops, 
        # if the path has more than n-1 edges, so it has a negative loop in the graph 
        for s,d,w in edges:
            if last[s] + w < last[d]:
                ## 2nd return value is optional, only for backtrace
                return [float('-inf')]*n,trace

    ## 2nd return value is optional, only for backtrace
    return last,trace

```