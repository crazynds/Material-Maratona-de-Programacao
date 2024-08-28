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

## Algoritmo para calcular a quantidade de combinações

No algoritmo abaixo, $n$ é o total de elementos e $k$ o tamanho dos conjuntos a serem formados.

```cpp
int comb(int n, int k)
{
    int resp = 1;

    for (int i = n - k + 1; i <= n; i++)
    {
        resp *= i;
    }

    for (int i = 2; i <= k; i++)
    {
        resp /= i;
    }

    return resp;
}
```

## Triângulo de Pascal

Pode-se pré-computar os coeficientes binomiais com o Triângulo de Pascal.

No algoritmo abaixo, `maxn` é o maior valor possível para $n$.

```cpp
const int maxn = 100;
int pascal[maxn + 1][maxn + 1];

void makePascal()
{
    pascal[0][0] = 1;
    for (int n = 1; n <= maxn; n++)
    {
        pascal[n][0] = pascal[n][n] = 1;
        for (int k = 1; k < n; k++)
        {
            pascal[n][k] = pascal[n - 1][k - 1] + pascal[n - 1][k];
        }
    }
}
```

Para acessar a combinatória de $n$ em $k$, basta utilizar `pascal[n][k]`.

## Algumas Propriedades

 - $C_{n, k} = C_{n, n - k}$
 - $C_{n, k} = (n / k) * C_{n-1, k-1}$
 - $C_{n, 0} + C_{n, 1} + ... + C_{n, n} = 2 ^ n$
