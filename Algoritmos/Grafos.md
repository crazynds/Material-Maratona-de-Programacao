# Algoritmos de Grafo

## Floyd Warshall

Calcula distâncias entre todos os nodos do grafo.

Entradas:
 - dist é uma matrix de adjacência do grafo, logo: dist[i][j] é o custo de ir de i até j.
 - Se não existe aresta entre i e j, o valor de dist[i][j] é igual a INFINITY.
 - Se i e j forem iguais, deve-se setar o dist[i][j] para zero.
 - Max_n é o número máximo de vértices (variável de acordo com o problema proposto)

Saidas:
 - dist[i][j]: Custo do menor caminho de i até j.
 - detour_path[i][j]: Para qual nodo ir partindo de i para se aproximar de j ou -1 se não 
existe caminho.

OBS: O algoritmo começa verificando na posição zero e vai até o valor < n, ou seja, se o grafo tiver 5 vértices, eles estarão na posição 0, 1, 2, 3, 4.

```C++
static const int max_n = 101;
#define INFINITY 1.0/0.0
float dist[max_n][max_n];
int detour_path[max_n][max_n];

void floyd_warshall(int n) {
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            detour_path[i][j] = -1;

    for (int k = 0; k < n; ++k) {
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                float new_dist = dist[i][k] + dist[k][j];
                if (new_dist < dist[i][j]) {
                    dist[i][j] = new_dist;
                    detour_path[i][j] = k;
                }
            }
        }
    }
}
```

## Ford-Fulkerson
Função Ford-Fulkerson(G, s, t) [Achar o fluxo máximo de um grafo]
- para cada (u, v) em E[G]
    - fluxo(u, v) := 0
    - fluxo(v, u) := 0
    - enquanto existir caminho de aumento p de s para t na rede residual
        - Cf(p) := capacidade do arco de menor capacidade em p
        - para cada (u, v) em p
            - fluxo(u, v) := fluxo(u, v) + Cf(p)
            - fluxo(v, u) := fluxo(v, u) - Cf(p)

setar as variáveis em:
- memset(FLOW, 0, sizeof(FLOW));
- memset(queue, 0, sizeof(queue));
- memset(F, 0, sizeof(F));
    
Basta apenas configurar a variável FLOW sendo:
- FLOW[A][B] = o fluxo máximo da aresta de A pra B.

Depois basta chamar maxflow, fTotal é o fluxo total do grafo.

```C++
#include<stdio.h>
#include<stdbool.h>
#define MAX 102

int FLOW[MAX][MAX];
int queue[MAX];
int head, tail;
int parent[MAX];
int V, E;
int s, t, fTotal;
int F[MAX][MAX];

bool reachable(int s, int t) {
   bool found = false;
   int vq;
   head = tail = 0;
   memset(parent, 255, sizeof(parent));
   queue[tail++] = s;
   parent[s] = s;

   while(head < tail && !found) {
      vq = queue[head++];
      int i;
      for(i=0; i<V; i++) {
         if(FLOW[vq][i] && parent[i] == -1) {
            queue[tail++] = i;
            parent[i] = vq;

            if(i == t) {
               found = true;
               break;
            }
         }
      }
   }
   return found;
}

void maxflow() {
   int vj, min;
   fTotal = 0;
   while(reachable(s, t)) {
       min = FLOW[parent[t]][t];
       vj = t;
       while(parent[vj] != vj) {
          if(FLOW[parent[vj]][vj] < min)
             min = FLOW[parent[vj]][vj];
             vj = parent[vj];
       }

       vj = t;
       while(parent[vj] != vj) {
          FLOW[parent[vj]][vj] -= min;
          FLOW[vj][parent[vj]] += min;
          F[parent[vj]][vj] += min;
          vj = parent[vj];
       }
       fTotal += min;
   }
}

int main () {
    /*Inicio do programa*/
    /*While para repetição dependendo do problema*/
    memset(FLOW, 0, sizeof(FLOW));
    memset(queue, 0, sizeof(queue));
    memset(F, 0, sizeof(F));
    /*Setar o FLOW (fluxo entre vértices*/
    maxflow();
    printf("O Fluxo total é %d.\n",++cases,fTotal);
    scanf("%d",&V);
    return 0;
}
```

## Bellman-Ford

BELLMAN-FORD - O Algoritmo de Bellman-Ford é um algoritmo de busca de caminho mínimo em um dígrafo ( ou Grafo direcionado) ponderado, ou seja, cujas arestas têm peso, inclusive negativo. 

**O(VxA)**

- edgecount – número de arestas do grafo.

- nodecount – número de nodos(vértices) do grafo.

- edges[MAX] – vetor que contém as arestas, com o peso de cada.

- MAX – Quantidade máxima de arestas.

Obs: dentro do algoritmo, a variável distance[] computa a distância mais curta encontrada entre cada um dos nodos.

```C++
#include <iostream>
#define INFINITY 99999999
#define MAX 10000
using namespace std;

typedef struct {
    int source;
    int dest;
    int weight;
} Edge;

Edge edges[MAX];
int edgecount;
int nodecount;

void bellman_ford(int source) {
    int i, j;
    int *distance = new int [nodecount];
    for(i = 0; i < nodecount; i++) {
        distance[i] = INFINITY;
    }
    distance[source] = 0;
    for (i = 0; i < nodecount; i++) {
        bool change = false;
        for (j = 0; j < edgecount; j++) {
            if (distance[edges[j].dest] > distance[edges[j].source] + edges[j].weight) {
                distance[edges[j].dest] = distance[edges[j].source] + edges[j].weight;
                change = true;
            }
        }
        if(change == false) break;
    }
    for (i = 0; i < edgecount; i++) {
        if (distance[edges[i].dest] > distance[edges[i].source] + edges[i].weight) {
            //cout << "Negative cycle." << endl;
            break;
        }
    }
    /*for (i = 0; i < nodecount; i++) {
       cout << "A distancia mais curta entre os nodos " 
       << source << " e " << i <<" eh " << distance[i] << endl;
    }*/
}
```

## Topological Sort
Utilizado com grafos direcionados.

O algoritmo só pode ser utilizado se o grafo não possuir ciclos direcionados. Topological sorting é útil para definir a ordem que “coisas” devem ser feitas (ou visitadas). Gerar uma ordem para os vértices.

Entrada:
- graph[][] – Matriz de adjacência do grafo ( o algoritmo começa a contar na posição 1  dos nodos (diferente dos outros que começa em 0).
- N – número de nodos do grafo
- indegree[] – vetor que diz para cada nodo, quantas arestas chegam nesse nodo (como é um grafo direcionado). Ex: se tivermos uma aresta 1 2, ou seja de 1 para 2, faça indegree[2]++; (aumenta o número de arestas incidentes em 2).

```C++
#define MAX 105
#include <cstdio>
#include <iostream>
#include <queue>
using namespace std;
int N;
int graph[MAX][MAX];
int indegree[MAX];
int top_sort[MAX];
void topological_sorting() {
   queue<int> Q;
   for(int i = 1; i <= N; i++) {
      if(indegree[i] == 0) {
         Q.push(i);
      }
   }

   int counter_sort = 1;

   while(!Q.empty()){
      int v = Q.front();
      Q.pop();
      top_sort[counter_sort] = v;
      counter_sort++;

      for(int i = 1; i <= N; i++) {
         if(graph[v][i] != 0) {
            indegree[i]--;
            if(indegree[i] == 0) {
               Q.push(i);
            }
         }
      }
   }
   for(int i = 1 ; i <= N; i++)
   {
      if(i == 1)
      {
         printf("%d", top_sort[i]);
      }else{
         printf(" %d", top_sort[i]);
      }
   }
   printf("\n");
}

int main () {
    /*Inicio do programa*/
    /*While para repetição dependendo do problema*/
    for(int i = 0 ; i < n ; i++)
      {
         for(int j = 0 ; j < n ; j++)
         {
            graph[i][j] = 0;
         }
         indegree[i] = 0;
      }
    /*Setar o graph e o indegree (configuração do grafo)*/
    topological_sorting();
    return 0;
}
```
