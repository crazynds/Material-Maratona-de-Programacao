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