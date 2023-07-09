# Espaçamento entre clusters

Esse algoritmo é bem confuso. Apesar o nome ser Maximum Spacing of k-clustering, ele quer a menor distancia entre clusters. O $K$ indica a quantidade de clusters que devem existir, e você que deve descobrir eles. Da pra usar o algoritmo de Kruskal para resolver a parte da geração de um cluster.

Um cluster deve ser gerado a partir da união dos vertices mais próximos. É ordenado de forma crescente pelo peso as arestas e iterado no qual o vertice $A$ se funde com o vertice $B$ formando um cluster, e assim até que sobrem apenas $K$ clusters. Se $A$ ou $B$ já fizerem parte de algum cluster, os clusters deles devem ser fundidos.

O que você quer no final é a menor distancia entre quaisquer 2 clusters. O algoritmo abaixo utiliza a estrutura de dados [DisjointSet](./../../Estrutura%20de%20Dados/DisjoinSet.md) adaptada para facilitar a contagem dos clusters, efetuando em tempo constante O(1) a contagem de clusters.

Esse algoritmo tem a mesma alma que o algoritmo de [Kruskal](./kruskalsmst.md) para encontrar MST.

```python
from collections import deque

class DisjointSetUnion:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.groups = set(self.parent)
 
    def find(self, x):
       if self.parent[x] != x:
           self.parent[x] = self.find(self.parent[x])
       return self.parent[x] 

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return

        if self.size[root_y] > self.size[root_x]:
            root_x, root_y = root_y, root_x
        elif self.size[root_y] == self.size[root_x]:
            self.size[root_x] += 1

        # delete root_y group
        self.groups.remove(root_y)
        self.parent[root_y] = root_x
    
    def num_groups(self):
        return len(self.groups)

def maxSpacingClustering(kClusters: int,nodes: int,edges: list):
    edges.sort(reverse=True,key=lambda e: e[2])
    union = DisjointSetUnion(nodes)
    # Une os vertices até que sobre apenas k clusters
    while len(edges)>0:
        # Note que a aresta é removida do array, sabe dizer porque?
        (a,b,_) = edges.pop()
        union.union(a,b)
        # Condição de parada
        if union.num_groups()<=kClusters:
            break
    # Procura a menor distancia entre 2 clusters
    minCost = float('inf')
    for (a,b,minCost) in reversed(edges):
        if union.find(a)!=union.find(b):
            break
    return minCost
```

Complexidade de tempo: O(M * alpha(n)) + sorting time (M * log M)