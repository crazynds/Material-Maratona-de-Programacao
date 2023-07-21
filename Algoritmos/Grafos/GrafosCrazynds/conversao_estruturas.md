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

def convertEdgesArrayToTreeGraph(edges,vertices):
    FATHER = 0
    CHILD = 1
    treeGraph = [[None,[]] for _ in range(vertices)]
    simpleGraph = convertEdgesArrayToNonDirectedSimpleGraph(edges,vertices)
    def iterOverGraph(currentNode,father):
        treeGraph[currentNode][FATHER] = father
        for node in simpleGraph[currentNode]:
            if node!=father:
                treeGraph[currentNode][CHILD].append(iterOverGraph(node,currentNode))
        return currentNode
    root = iterOverGraph(0,None)
    return (treeGraph,root)

def getReverseGraph(graph):
    reverse = [{} for _ in range(len(graph))]
    for a in range(len(graph)):
        for b in graph[a]:
            reverse[b][a] = graph[a][b]
    return reverse

```	




