# Números de Catalan

Números de Catalan são usados para resolver alguns problemas de combinatória.

O enésimo número de Catalan ($C_{n}$) é resultado dos seguintes problemas:
 - Número total de sequências de parênteses corretas (abrindo $n$ e fechando $n$). Ex: ()(());
 - Número de formas para colocar parênteses em $n+1$ fatores.

**OBS:** Existem MUITAS outras aplicações, mas envolvem assuntos mais complexos.

```cpp
int catalan[maxn];

void precomputeCatalan()
{
    catalan[0] = catalan[1] = 1;
    for (int i = 2; i <= maxn; i++)
    {
        catalan[i] = 0;
        for (int j = 0; j < i; j++)
        {
            catalan[i] += (catalan[j] * catalan[i-j-1]) % mod;
            catalan[i] = catalan[i] % mod;
        }
    }
}
```

Para acessar $C_{n}$, utilizar `catalan[n]`.