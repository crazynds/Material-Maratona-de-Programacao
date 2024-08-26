# Área de Polígono (Fórmula de Surveyor) #

Dados os pontos no plano cartesiano que formam um polígono, pode-se calcular a sua área.

## Explicação

Para calcular a área, deve-se somar os determinantes dos vetores formados por pontos adjacentes e dividir por 2. Para facilitar
o cálculo, pode-se considerar um polígono de $n$ lados como uma matriz de $n+1$ linhas e 2 colunas ($x$ e $y$). $n+1$ linhas são
necessárias, pois deve-se colocar uma cópia do primeiro ponto no fim da matriz. Deve-se calcular o determinante de todos os pares
de pontos adjacentes, somá-los e dividir por dois. É necessário utilizar o valor absoluto, pois, dependendo da ordem dos pontos (sentido
horário ou anti-horário), o resultado pode ser negativo.

**OBS:**
 - O polígono não precisa estar centralizado na origem (nem conter a origem);
 - O polígono não precisa ser convexo;
 - Os pontos precisam estar "em ordem", ou seja, no vetor, os pontos vizinhos são adjacentes.
 - Para o cálculo, é necessário duplicar o primeiro ponto no fim do vetor (a função abaixo já faz isso).

## O Algoritmo

`points` contém todos os pontos ($x$, $y$) que formam o polígono "em ordem".

```cpp
double orderedPointsArea(vector<pair<double, double>> points)
{
    points.push_back(points.front());

    double p = 0, n = 0;

    for(int i = 0; i < points.size() - 1; i++)
    {
        p += points[i].first * points[i + 1].second;
        n += points[i].second * points[i + 1].first;
    }

    return abs(p - n) / 2;
}
```

## E se os pontos não estiverem ordenados?

**Provavelmente**, deve-se aplicar a ordenação dos pontos que é feita no `Algoritmo de Graham`.



