# Remover ciclos

O código abaixo remove ciclos de um grafo direcionado. A forma que ele faz isso é transformar todos os nós pertencentes a um ciclo em um único nó, dessa forma facilita quando se calcula o _In-degree_ e o _Out-Degree_ e não se quer um ciclo.

De uma olhada no seguinte exercício para mais detalhes de onde usar:
- [3431 - Habilitando a Movimentação](https://www.beecrowd.com.br/judge/pt/runs/code/35267180)

```python

n,m = map(int,input().split())

nodes = [set() for _ in range(n)]

for _ in range(m):
    r,s = map(lambda a:int(a)-1,input().split())
    nodes[r].add(s)

def recursivaRemoveCiclo(nodeId,nodes:list[set],nodeStack: set,nodesVisited:list):
    # check if this node is in cicle
    if nodeId in nodeStack:
        return nodeId
    # check if this node already was visited
    if nodesVisited[nodeId]:
        return None

    # mark this node in stack and visited
    nodeStack.add(nodeId)
    nodesVisited[nodeId] = True

    for child in nodes[nodeId].copy():
        newNodeId = recursivaRemoveCiclo(child,nodes,nodeStack,nodesVisited)
        if newNodeId != None:
            if newNodeId != nodeId:
                nodes[nodeId].remove(child)
                nodes[newNodeId] |= nodes[nodeId]
                if nodeId in nodes[newNodeId]:
                    nodes[newNodeId].remove(nodeId)
                nodes[nodeId] = nodes[newNodeId]
                nodesVisited[nodeId] = 2 # Mark to destroy this node later
                return newNodeId
            else:
                nodesVisited[nodeId] = False
                
            
    # remove node of stack
    nodeStack.remove(nodeId)
    return None

def removeCiclo(nodes:list[set]):
    nodesVisited = [False] * len(nodes)
    for node in range(len(nodes)):
        if not nodesVisited[node]:
            recursivaRemoveCiclo(node,nodes,set(),nodesVisited)
    
    print(nodes)
    nodes = [nodes[node] for node in range(len(nodes)) if nodesVisited[node]!=2]
    return nodes

```
