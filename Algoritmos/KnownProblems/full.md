# Material de agendamento de tarefas

## Agendamento em um único computador O(n log n)

O primeiro problema a ser resolvido é em que ordem agendar N trabalhos de forma que o custo da função de penalidade final seja mínimo.

Para casos em que a função é linear, basta ordenar os trabalhos pela razão custo/tempo.

Se a função for exponencial, basta ordenar por (1 - e^a*tempo) / custo

## Agendamento em dois computadores O(n log n)

Esse problema a ser resolvido se resume em que ordem os os trabalhos devem ser ordenados para finalizar no menor tempo possível. Um trabalho só pode ser agendado no segundo computador depois de ser finalizado na primeira.

Esse algoritmo surge a partir da tentativa de minimizar o tempo ocioso do segundo computador. Assim como o problema anterior, a solução para esse é um ordenamento dos trabalhos.

## C++
```cpp
struct Job {
    int a, b, idx;

    bool operator<(Job o) const {
        return min(a, b) < min(o.a, o.b);
    }
};

vector<Job> johnsons_rule(vector<Job> jobs) {
    sort(jobs.begin(), jobs.end());
    vector<Job> a, b;
    for (Job j : jobs) {
        if (j.a < j.b)
            a.push_back(j);
        else
            b.push_back(j);
    }
    a.insert(a.end(), b.rbegin(), b.rend());
    return a;
}

pair<int, int> finish_times(vector<Job> const& jobs) {
    int t1 = 0, t2 = 0;
    for (Job j : jobs) {
        t1 += j.a;
        t2 = max(t2, t1) + j.b;
    }
    return make_pair(t1, t2);
}
```

## Agendamento de tarefas com deadline

Problema para agendar o máximo de tarefas em um espaço de tempo.

## C++
```cpp
struct Job {
    int deadline, duration, idx;

    bool operator<(Job o) const {
        return deadline < o.deadline;
    }
};

vector<int> compute_schedule(vector<Job> jobs) {
    sort(jobs.begin(), jobs.end());

    set<pair<int,int>> s;
    vector<int> schedule;
    for (int i = jobs.size()-1; i >= 0; i--) {
        int t = jobs[i].deadline - (i ? jobs[i-1].deadline : 0);
        s.insert(make_pair(jobs[i].duration, jobs[i].idx));
        while (t && !s.empty()) {
            auto it = s.begin();
            if (it->first <= t) {
                t -= it->first;
                schedule.push_back(it->second);
            } else {
                s.insert(make_pair(it->first - t, it->second));
                t = 0;
            }
            s.erase(it);
        }
    }
    return schedule;
}
```


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
        mat[i][x] = max(mat[i-1][x],(mat[i-1][x-weightItem] + val) if x >= weightItem else 0)

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

# Solução ótima 

Melhor solução para o problema independente de tudo o que foi dito.

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

Vou te entregar de bandeja o backtrace, então vc deve aprender como usar e fazer o resto. Essa função utiliza a solução ótima para o Knapsack problem, então deve ser usado com as duas funçoes.


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

Teste o que aprendeu com o problema abaixo.

- [Beecrowd 1767](https://www.beecrowd.com.br/judge/pt/problems/view/1767)


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

[1310 - Lucro](https://www.beecrowd.com.br/judge/pt/problems/view/1310)

# Variações do problema

## Maior somatorio de sub array que a soma seja menor que K

Queremos saber qual o maior somatório de um sub array do array original que o valor seja menor que K. O problema é bem simples de resolver usando a solução que temos anteriormente.

Adicionamos no algoritmo apenas uma verificação se o novo máximo é menor que K, então ele seta e retornamos ele depois.

```python
def subarray_sum_less_or_equal_than(arr,k):
    # valores iniciais
    max_ = 0
    max_end = 0
    
    for i in range(len(arr)):
        max_end = max_end + arr[i]
        if max_end < 0: # resetar contador
            max_end = 0
        
        elif max_ < max_end and max_end <= k: # atualizar máximo
            max_ = max_end

    return max_
```

Outra forma pode ser vista [aqui](https://www.geeksforgeeks.org/maximum-sum-subarray-having-sum-less-than-or-equal-to-given-sum-using-set/).

## Maior sub array que a soma seja menor que K

Diferente da questão acima, queremos o maior array que a soma seja menor que K, independente do somatorio.

```python
def length_subarrays_more_than_k(array, K):
    head, tail = 0, 0
    current_sum = 0
    while(tail<len(array)):
        if current_sum + array[tail]<=K:
            current_sum += array[tail]
            tail += 1
            yield tail - head
        else:
            current_sum -= array[head]
            head += 1

def max_subarray_more_than_k(array, k):
    return max(length_subarrays_more_than_k(array, K))

```

Graças a nossos [colegas de carreira (fonte)](https://codereview.stackexchange.com/questions/146524/find-the-longest-subarray-with-sum-less-than-k), temos uma solução elegante que roda O(N).

Devemos notar que funciona somente para arrays com valores positivos apenas, quando incluido valores negativos, temos diversos problemas que surgem no algoritmo acima. Você que é inteligente vai descobrir um algoritmo que funciona para qualquer número em O(N) e vai mandar um commit para esse repositório. 😉 



# Manacher

O algoritmo de Manacher é utilizado para encontrar todos os palíndromos de uma palavra em tempo O(n). 

O Manacher funciona somente com strings de tamanho ímpar, portanto, caso o a string tenha tamanho par, é necessário adicionar '.' entre cada caracter, para que dessa forma ela tenha um tamanho ímpar.

O Manacher utilizar propriedades dos palíndromos para descobrí-los todos em O(n). Ele funciona verificando qual o maior palíndromo que tenha centro em i. A propriedade principal que ele utiliza é que palíndromos dentro de palíndromos são espelhados. Ou seja, no caso 'abacaba', há um palíndromo maior com centro em 'c'. O algoritmo ao verificar qual o maior palíndromo em todos os caracteres que estão a direita de 'c', sabe que eles tem pelo menos o tamanho dos palíndromos que estão a esquerda de 'c', e assim evitam cálculos repetidos.

O retorno do algoritmo é uma lista que representa: para a posição i, o maior palíndromo é LPS[i]. A partir disso, todos os palíndromos podem ser recuperados da string.

## Python

```python
def PreProcessWord(word):
    return "." + "".join([c + "." for c in word])

def Manacher(string):
    string = PreProcessWord(string)
    LPS = [0 for _ in range(len(string))]
    C = 0
    R = 0

    for i in range(len(string)):
        iMirror = 2*C - i
        if R > i:
            LPS[i] = min(R-i, LPS[iMirror])
        else:
            LPS[i] = 0
        try:
            while string[i + 1 + LPS[i]] == string[i - 1 - LPS[i]]:
                LPS[i] += 1
        except:
            pass
        
        if i + LPS[i] > R:
            C = i
            R = i + LPS[i]
    
    return LPS
    r, c = max(LPS), LPS.index(max(LPS))
    result = string[c - r : c + r].replace(".","")

```

# Longest Common Substring

Esse algoritmo encontra a maior subsequência comum entre duas strings em O(n*m). Uma subsequência não exige que os caracteres sejam sequenciais.

## Top-Down

Essa primeira versão utiliza uma abordagem Top-Down através de recursão.

## Python

```python
def lcs(X, Y, m, n, dp):
    if (m == 0 or n == 0):
        return 0

    if (dp[m][n] != -1):
        return dp[m][n]

    if X[m - 1] == Y[n - 1]:
        dp[m][n] = 1 + lcs(X, Y, m - 1, n - 1, dp)
        return dp[m][n]

    dp[m][n] = max(lcs(X, Y, m, n - 1, dp), lcs(X, Y, m - 1, n, dp))
    return dp[m][n]
```

## C++

```cpp
#include <bits/stdc++.h>
using namespace std;

int lcs(char* X, char* Y, int m, int n, vector<vector<int> >& dp)
{
    if (m == 0 || n == 0)
        return 0;
    if (X[m - 1] == Y[n - 1])
        return dp[m][n] = 1 + lcs(X, Y, m - 1, n - 1, dp);

    if (dp[m][n] != -1)
        return dp[m][n];

    return dp[m][n] = max(lcs(X, Y, m, n - 1, dp), lcs(X, Y, m - 1, n, dp));
}
```

## Bottom-Up

Já essa segunda implementação utiliza uma abordagem Bottom-Up, já com otimização de espaço.

## Python

```python
def longestCommonSubsequence(text1, text2):
    n = len(text1)
    m = len(text2)

    prev = [0] * (m + 1)
    cur = [0] * (m + 1)

    for idx1 in range(1, n + 1):
        for idx2 in range(1, m + 1):
            if text1[idx1 - 1] == text2[idx2 - 1]:
                cur[idx2] = 1 + prev[idx2 - 1]
            else:
                cur[idx2] = max(cur[idx2 - 1], prev[idx2])

        prev = cur.copy()

    return cur[m]
```

## C++

```cpp
#include <bits/stdc++.h>
using namespace std;

int longestCommonSubsequence(string& text1, string& text2)
{
    int n = text1.size();
    int m = text2.size();

    vector<int> prev(m + 1, 0), cur(m + 1, 0);

    for (int idx2 = 0; idx2 < m + 1; idx2++)
        cur[idx2] = 0;

    for (int idx1 = 1; idx1 < n + 1; idx1++) {
        for (int idx2 = 1; idx2 < m + 1; idx2++) {
            if (text1[idx1 - 1] == text2[idx2 - 1])
                cur[idx2] = 1 + prev[idx2 - 1];
            else
                cur[idx2] = 0 + max(cur[idx2 - 1], prev[idx2]);
        }
        prev = cur;
    }

    return cur[m];
}
```


