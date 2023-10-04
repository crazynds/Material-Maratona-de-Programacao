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


