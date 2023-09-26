# Algoritmo de Kadane

Nesse algoritmo O(n), retornará o valor da maior soma de um subarray contíguo que está contido no array original.

Ou seja: `subarray_sum([1,-2,3,-1,4]) -> 6` pois a maior soma está em [3, -1, 4].

Este algoritmo utiliza técnicas de programação dinâmica para resolução do problema.

## Python

```python
def subarray_sum(arr):
    # valores iniciais
    max_ = arr[0]
    max_end = 0
    
    for i in range(len(arr)):
        max_end = max_end + arr[i]
        if max_end < 0: # resetar contador
            max_end = 0
        
        elif max_ < max_end: # atualizar máximo
            max_ = max_end

    return max_
```

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

# Problema da mochila / Knapsack 

```python
weight, n = map(int,input().split())
itens  = []

for _ in range(n):
    val,weightItem = map(int,input().split())
    itens.append((val,weightItem))

#Compute matrix of max choises
mat = [[0]*(weight+1) for _ in range(n+1)]
for i, (val,weightItem) in enumerate(itens,1):
    for x in range(weight+1):
        mat[i][x] = max(mat[i-1][x],(mat[i-1][x-weightItem] + val) if x >= weightItem else 0)

print('Maximo peso:',mat[-1][weight])
```
Complexidade: $O(N*W)$ $N=$ Número de itens $W=$ Peso máximo carregado

# Solução ótima 


```python
import sys
# If some recursion error apear, increase this number
sys.setrecursionlimit(2500)

weight, n = map(int,input().split())
itens  = []

for _ in range(n):
    val,peso = map(int,input().split())
    itens.append((val,peso))

def knapsack_optimal(itens,cache,currentWeight,i):
    if i < 0:
        return 0
    key = (i,currentWeight)
    if key in cache:
        return cache[key]
    val,weight = itens[i]

    cache[key] = max(
        (knapsack_optimal(itens,cache,currentWeight-weight,i-1)+val) if currentWeight >= weight else 0,
        knapsack_optimal(itens,cache,currentWeight,i-1)
    )
    return cache[key]

cache = {}
solve = knapsack_optimal(itens,cache,weight,len(itens)-1)
```

## BackTrace da solução otima


```python

def knapsack_optimal_with_backtrace(itens,maxWeight):
    currentWeight = maxWeight
    solution = []
    cache = {}
    totalValue = knapsack_optimal(itens,cache,maxWeight,len(itens)-1)
    currentValue = totalValue
    
    # Executa todos menos o item na casa 0
    for i in range(len(itens)-1,0,-1):
        # se o valor do passo anterior for diferente do valor atual, então foi adicionado o item ao valor atual
        if cache[(i-1,currentWeight)] != cache[(i,currentWeight)]:
            # inclui o iten no conjunto solução
            val,weight = itens[i]
            currentWeight -= weight
            currentValue -= val
            solution.append(itens[i])
    else:
        # Depois que executou tudo
        # Se ainda tem valor sobrando, então inclui o ultimo
        if currentValue > 0:
            solution.append(itens[0])
    
    return solution,totalValue

```

# Variações do problema

## Dois sacos

```python
# mudança nos parametros
def encontraSolucao(itens,pesoDispA,pesoDispB,i)
    if i >= len(itens):
        return 0
    valor, peso = itens[i]
    return max(
        encontraSolucao(itens,pesoDispA,i+1),
        encontraSolucao(itens,pesoDispA-peso,i+1)+valor if pesoDispA-peso >= 0 else 0
        # nova linha
        encontraSolucao(itens,pesoDispA,pesoDispB-peso,i+1)+valor if pesoDispB-peso >= 0 else 0
    )
```

# Combinatória em Python

Se quiser uma lista de todas as combinações de um item em Python utilize a função `combinations` da biblioteca `ìtertools`:
```python

# onde iterável é qualquer iterável
# e quantidade remete a quantos itens cada combinação terá
# combinations(iterável, quantidade)

from itertools import combinations

itens = [1,2,3]

print(list(combinations(itens,2)))
# [(1, 2), (1, 3), (2, 3)]

print(list(combinations(itens, 3)))
# [(1, 2, 3)]
```

Caso seja desejado uma combinação com repetição de elementos individuais, temos a `combinations_with_replacement`:

```python
from itertools import combinations_with_replacement

itens = [1,2,3]

print(list(combinations_with_replacement(itens, 2)))
# [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]

print(list(combinations_with_replacement(itens, 3)))
# [(1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 2, 2), (1, 2, 3), (1, 3, 3), (2, 2, 2), (2, 2, 3), (2, 3, 3), (3, 3, 3)]
```

Para permutações, utilize `permutations`:

```python
from itertools import permutations

# onde iterável é qualquer iterável
# e quantidade remete a quantos itens cada permutação terá
# permutations(iterável, quantidade)

itens = [1,2,3]

print(list(permutations(itens)))
# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]


print(list(permutations(itens, 2)))
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
```

De forma similar, pode ser feito combinações parecido com produto cartesiano em Python de forma rápida com `product`:


```python
from itertools import product

itens1 = 'abc'
itens2 = 'def'

print(list(product(itens1, itens2)))
[('a', 'd'), ('a', 'e'), ('a', 'f'), ('b', 'd'), ('b', 'e'), ('b', 'f'), ('c', 'd'), ('c', 'e'), ('c', 'f')]

```

Caso se queira C<sub>i</sub> sem computar toda a lista pode-se usar o código a seguir:


```python
# função da biblioteca more_itertools
def nth_combination(iterable, r, index):
    "Equivalent to list(combinations(iterable, r))[index]"
    pool = tuple(iterable)
    n = len(pool)
    c = math.comb(n, r)
    if index < 0:
        index += c
    if index < 0 or index >= c:
        raise IndexError
    result = []
    while r:
        c, n, r = c*r//n, n-1, r-1
        while index >= c:
            index -= c
            c, n = c*(n-r)//n, n-1
        result.append(pool[-1-n])
    return tuple(result)

itens = [1,2,3]

print(list(combinations(itens, 2)))
# [(1, 2), (1, 3), (2, 3)]

print(nth_combination([1,2,3], 2, 1))
# (1, 3)

# benchmarks com pequeno N:

timeit.timeit(lambda: nth_combination([1,2,3], 2, 2))
# 0.4471917999908328

timeit.timeit(lambda: list(combinations([1,2,3], 2))[2])
# 0.25818079998134635

# Note que para pequeno N vale mais a pena utilizar o método padrão

timeit.timeit(lambda: list(combinations(range(50), 2))[2])
# 24.647441400011303

timeit.timeit(lambda: nth_combination(range(50), 2, 2))
# 0.742395299981581

# nos meus testes, com o número total de combinações > 15 já é vantajoso utilizar a função nth_combination
```

# Apenas quantidades

Caso queria apenas a quantidade de combinações, invés de utilizar len() pode se utilizar as funções prontas da `math`:

```python
from math import comb, perm

# número de maneiras de combinar n itens em k posições 
# comb(n,k)

# equivalente a len(combinations([1,2,3], 2))
print(comb(3,2))
# 3

# equivalente a len(permutations([1,2,3], 2))
print(perm(3,2))
# 6
```

