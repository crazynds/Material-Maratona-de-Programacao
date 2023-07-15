# Perfect matching Graph

>In graph theory, a perfect matching in a graph is a matching that covers every vertex of the graph. More formally, given a graph G = (V, E), a perfect matching in G is a subset M of edge set E, such that every vertex in the vertex set V is adjacent to exactly one edge in M.

Tem q escrever melhor isso ae

```python

def perfectMatchGraph(graph):
    '''
        Check if in one graph every vertice can be matched with other vertice.
            without any vertice stays alone.

        If a vertice is matched with other, it can't be matched with any other vertice.
    '''
    nodes = len(graph)
    vert = [len(graph[a]) for a in range(nodes)]
    hp = [(len(graph[a]),a) for a in range(nodes)]
    heapq.heapify(hp)
    
    revGraph = getReverseGraph(graph)
    
    while len(hp)>0:
        g,a = heapq.heappop(hp)
        if vert[a] != g or vert[a]<0:
            continue
        if g==0:
            return False
        
        for b in graph[a]:
            if vert[b]>0:
                vert[b] = -1
                vert[a] = -1
                for c in revGraph[a]:
                    if vert[c] != -1:
                        vert[c] -= 1
                        heapq.heappush(hp,(vert[c],c))
                for c in revGraph[b]:
                    if vert[c] != -1:
                        vert[c] -= 1
                        heapq.heappush(hp,(vert[c],c))
                break
    return max(vert)<0

```
