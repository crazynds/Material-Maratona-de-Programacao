# The Floyd Warshall Algorithm

Esse algoritmo resolve o problema APSP (All pairs shortest path), ele se traz uma ideia semelhante em alguns aspectos ao [bellman-ford](./Bellman-Ford.md) porém ao invez de iterar sobre as arestas, ele itera apenas sobre os vertices, sendo cada vez para uma origem diferente, e retorna uma matriz com a relação de $A[i][j] = ShortestPath(i,j)$.

Complexidade desse algoritmo é $O(N^3)$

Ele também traz as vantagens do algoritmo de bellman-ford, como encontrar o menor caminho em um grafo com pesos negativos, e pode ser executado de forma distribuida.



O funcionamento desse algoritmo usa uma matriz, no qual a posição $(i,j)$ contém o menor caminho do vertice $i$ até o vertice $j$. Para cada iteração de $k$, o algoritmo verifica se existe um caminho de $i$ até $j$ que passe por $k$, e se ele for menor, substitui na posição da matriz. Os valores iniciais da matriz são definidos como:

 - Defini-se zero quando $i=j$;
 - Defini-se $w_{i,j}$ quando existir uma aresta de $i$ para $j$;
 - Defini-se $+inf$ para todos os outros casos;

```python


def floydwarshall(edges: list, vertices):
    """
        complexity: O(n^3 + m)
        m = edges
        n = nodes

        this function return a list of distances from every pair of nodes

    """
    inf = float('inf')
    last = [[0 if j==i else inf for j in range(vertices)] for i in range(vertices)]
    current = [[inf for j in range(vertices)] for i in range(vertices)]

    for s,d,w in edges:
        last[s][d] = w

    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                current[i][j] = min(
                    current[i][j],
                    last[i][j],
                    last[i][k]+last[k][j] )
                
        last, current = current,last #swap
    
    # check if exists a negative cycle
    for i in range(vertices):
        if last[i][i] < 0:
            return [[float('-inf')]*vertices for _ in range (vertices)]

    return last

```

## Vantagens

A grande vantagem de se usar esse algoritmo ao invez de executar o [bellman-ford](./Bellman-Ford.md) $N$ vezes, uma para cada vertice como origem, é no tempo de execução. O tempo de execução do bellman-ford tem como um de seus parametros o número de arestas $M$ no qual todos os grafos conexos não arvores vão ter a seguinte equação verdadeira $M >= N$.

Dessa forma, é possivel deduzir que a complexidade do bellman-ford sempre será igual ou maior ao da execução desse algoritmo, e quanto mais denso do grafo for (maior o numero de arestas) maior será a eficiencia do uso desse algoritmo ao invez do bellman-ford.

Para $M >= N$ então $O(M*N^2) >= O(N^3)$


## Reconstruindo o caminho

É possivel reconstruir o caminho. Não entendi a explicação, mas você que é esperto, vai descobrir e adicionar um commit nesse repositório. 😉