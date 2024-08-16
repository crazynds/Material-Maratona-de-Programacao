# Caixeiro Viajante (Traveling Sailsman Problem - TSP)

## Algoritmo de Held-Karp

- Complexidade: O(n^2 * 2^n)
- Utiliza Programação Dinâmica

```c++

#include <iostream>
#include <vector>
#include <cmath>
#include <limits>

using namespace std;

int tspHeldKarp(const vector<vector<int>>& adjMatrix)
{
    int numCities = adjMatrix.size();
    int numSubsets = 1 << numCities; // 2^numCities
    vector<vector<int>> dp(numSubsets, vector<int>(numCities, numeric_limits<int>::max()));

    // Base case: o custo de visitar a cidade inicial é 0
    dp[1][0] = 0;

    // Iterar sobre todos os subconjuntos de cidades
    for (int subset = 1; subset < numSubsets; ++subset)
    {
        for (int last = 0; last < numCities; ++last)
        {
            // Verificar se a cidade 'last' está no subconjunto atual
            if (!(subset & (1 << last))) continue;

            // Tentar adicionar uma nova cidade ao caminho
            for (int next = 0; next < numCities; ++next)
            {
                // Verificar se a cidade 'next' não está no subconjunto atual
                if (subset & (1 << next)) continue;

                int nextSubset = subset | (1 << next);
                dp[nextSubset][next] = min(
                    dp[nextSubset][next],
                    dp[subset][last] + adjMatrix[last][next]
                );
            }
        }
    }

    // Retornar à cidade inicial, encontrando o custo mínimo
    int minCost = numeric_limits<int>::max();
    for (int last = 1; last < numCities; ++last)
    {
        minCost = min(minCost, dp[numSubsets - 1][last] + adjMatrix[last][0]);
    }

    return minCost;
}

```

**OBS:** Pode-se alterar o algoritmo para não se retornar à cidade de origem. Basta remover `adjMatrix[last][0]` quando se calcula o `minCost` no fim.




