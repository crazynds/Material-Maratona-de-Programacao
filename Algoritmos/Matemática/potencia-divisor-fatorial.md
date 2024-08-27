# Encontrando a potência de um divisor de fatorial (Fórmula de Legendre)

Algoritmo para encontrar o maior $x$ tal que $k ^ x$ divide $n!$.

**Complexidade:** $O(log n)$

## Caso $k$ seja primo

```cpp
int fact_pow (int n, int k)
{
    int res = 0;
    while (n)
    {
        n /= k;
        res += n;
    }

    return res;
}
```

## Caso $k$ não seja primo ($k$ composto)

No algoritmo abaixo, `factors` é um vetor que guarda os fatores primos que formam $k$. Ele guarda um par, pois o primeiro
é o fator em si, e o segundo, a potência a ele associada.

Para exemplificar: $60 = 2^2 * 3 * 5$

Logo, para representar 60, seria necessário montar um vetor com os seguintes valores:
 - {2, 2}
 - {3, 1}
 - {5, 1}

**OBS:** os primos não precisam estar em ordem.

```cpp
int fact_pow(int n, vector<pair<int, int>> factors)
{
    int resp = 1000000;
    int aux;
    for(auto p : factors)
    {
        aux = fact_pow(n, p.first);
        aux /= p.second;

        if(resp > aux)
        {
            resp = aux;
        }
    }

    return resp;
}
```
