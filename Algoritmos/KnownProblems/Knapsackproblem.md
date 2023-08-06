# Problema da mochila / Knapsack 

Dada um mochileiro que pode carregar até $W$ de peso, e $N$ itens com um peso $W_i$ e um valor $V_i$, qual é o máximo de valor que o mochileiro consegue carregar.

Algumas regras:
 - Um item não pode ser dividido em pedaços
 - O mochileiro não pode carregar mais que $W$ de peso. Seja $S$ o conjunto de itens solução e $W_i\in S$ então $\sum{W_i}<=W$


# Solução para INTEIROS

Abaixo a solução para o problema quando todos os pesos inteiros. Todas as soluções apresentam o peso da mochila como multiplicador do custo de memória (Ex: $O(N*W)$), então essas soluções podem não ser ideais para quando se tem um peso máximo muito alto.

## Ideia base 
Solução baseada em programação dinamica. O objetivo é tentar cobrir todas as soluções disponiveis, dessa forma existem duas hipoteses, de o item estar no conjunto solução, e do item não estar no conjunto solução. As duas ramificações são calculadas e a partir de um algoritmo usando recursão podemos encontrar o seguinte código:
```python
def encontraSolucao(itens,pesoDisponivel,i)
    if i >= len(itens):
        return 0
    valor, peso = itens[i]
    return max(
        encontraSolucao(itens,pesoDisponivel,i+1),
        encontraSolucao(itens,pesoDisponivel-peso,i+1)+valor if pesoDisponivel-peso >= 0 else 0
    )
```

Claro que o algoritmo acima apresenta muitos problemas de eficiencia, mas é um bom código para exemplificar como resolver esse problema, agora abaixo um algoritmo que já implementa algum nivel de otimização na execução mas que o principio de resolução é o mesmo do anterior.

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
        mat[i][x] = max(mat[i-1][x],(mat[i-1][x-weightItem] if x-weightItem > 0 else 0) + val if x >= weightItem else 0)

print('Maximo peso:',mat[-1][weight])
```
Complexidade: $O(N*W)$ $N=$ Número de itens $W=$ Peso máximo carregado


Na matriz declarada os valores são calculados apenas na primeira passada por aquela coluna. O resultado da casa $M[X][Y]$ pode ser lido como o valor máximo que é possivel carregar considerando até o $X$ item com peso máximo $Y$.

## Backtrace

Algumas vezes queremos saber quais são os itens que vão ser levados na mochila se escolhermos a solução que maximize o valor, então temos o seguinte techo de código que resolve esse problema para nós:

```python
#Backpropagate to get the itens of max choise
def backtrackItensMaxChoise(mat,itens,weight):
    itensSelected = []
    currentWeight = weight
    for i in range(len(itens)-1,-1,-1):
        if mat[i+1][currentWeight] != mat[i][currentWeight]:
            val,peso = itens[i]
            itensSelected.append((val,peso))
            currentWeight -= peso
    return itensSelected

print(backtrackItensMaxChoise(mat,itens,weight))
```
Complexidade: $O(N)$ $N=$ Número de itens 

Esse algoritmo obviamente depende do código anterior para gerar a matriz de valores, porém executa em tempo ótimo e retorna uma lista de itens para a solução maximizada.


## Otimização de espaço

Como pode ser percebido, o código apresenta custo de memória de $O(M*N)$ o que pode crescer extremamente rápido, para isso existe uma versão do algoritmo que consegue fazer a implementação do mesmo código com custo de memoria $O(M)$. 

Obs: Nessa versão de algoritmo o sistema de backtrace **não funciona**. 

A ideia por traz dessa solução é que ao invez de precisar manter uma matriz das soluções de todos os itens anteriores calculada, é necessário apenas manter a ultima coluna calculada em memória, e o resto dos dados podem ser descartados. Segue um exemplo de código:


```python
weight, n = map(int,input().split())
itens  = []

for _ in range(n):
    val,peso = map(int,input().split())
    itens.append((val,peso))

#Compute matrix of max choises

lastColumn = [0] * (weight+1)
currentColumn = [0] * (weight+1)

for i, (val,peso) in enumerate(itens,1):
    for x in range(weight+1):
        currentColumn[x] = max(lastColumn[x],(lastColumn[x-peso] if x-peso > 0 else 0) + val if x >= peso else 0)
    lastColumn,currentColumn = currentColumn,lastColumn

print('Maximo peso:',lastColumn[weight])
```

# Melhor Solução 

Melhor solução para o problema independente de tudo o que foi dito.

```python
import sys
sys.setrecursionlimit(2500)

weight, n = map(int,input().split())
itens  = []

for _ in range(n):
    val,peso = map(int,input().split())
    itens.append((val,peso))

cache = {}
def knapsack_optimal(currentWeight,i):
    if i < 0:
        return 0
    key = (i,currentWeight)
    if key in cache:
        return cache[key]
    val,weight = itens[i]

    cache[key] = max(
        (knapsack_optimal(currentWeight-weight,i-1)+val) if currentWeight > weight else 0,
        knapsack_optimal(currentWeight,i-1)
    )
    return cache[key]
```


# Variações do problema

## Dois sacos

Agora imaginando que no problema existam dois recimentes que carreguem itens, quero preencher o máximo deles que no final eu tenha o maior valor possivel. Essa é uma variação bem ardilosa pensando inicialmente, mas quando se pega o algoritmo base inicial e pensa numa adpatação é possivel chega ao seguinte código:

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

Todas as técnicas de otmizações são aplicaveis, então a partir daqui deixo com você o código perfeito.


## N sacos

Esse é um caso realmente mais complicado, porém se você conseguiu entender as mudanças que acontecem quando vamos de 1 saco para 2 sacos, da para ter uma ideia da estrutura que vamos aplicar para calcular com numero $N$ de sacos. Deixo esse para você também.


