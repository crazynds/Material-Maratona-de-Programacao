# Funções conversoras

Aqui algumas funções que vão facilitar na conversão entre um tipo de estrutura de grafo para outra.

```python
def convertEdgesArrayToNonDirectedSimpleGraph(edges,vertices):
    simplegraph = [{} for _ in range(vertices)]

    for (a,b,cost) in edges:
        simplegraph[a][b] = cost
        simplegraph[b][a] = cost
    return simplegraph

def convertEdgesArrayToDirectedSimpleGraph(edges,vertices):
    simplegraph = [{} for _ in range(vertices)]

    for (a,b,cost) in edges:
        simplegraph[a][b] = cost
    return simplegraph

def convertSimpleGraphToEdgesArray(simplegraph):
    edges = []

    for a in range(len(simplegraph)):
        for b in simplegraph[a]:
            if a<b:
                edges.append((a,b,simplegraph[a][b]))
    return edges
```	


