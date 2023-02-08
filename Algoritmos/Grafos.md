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

## Depth-First Search
Realiza uma busca em profundidade no grafo.
- N – O número de nodos.
- v – Nodo inicial.

Para realizar o algoritmo:
- setar a variável graph[MAX][MAX] com a matriz de adjacência do grafo.
- setar todos os discovered[MAX] para false.


```C++
#define MAX 101
bool discovered[MAX];
int parent[MAX];
int graph[MAX][MAX];

void dfs(int v, int N) {
   discovered[v] = true;   
   for (int i = 1; i <= N; i++) {
      if(graph[v][i] != 0 && discovered[i] == false) { 
         parent[i] = v;
         dfs(i);
      }
   }
}
```

## Dijkstra
O algoritmo de Dijkstra soluciona o problema do caminho mais curto num grafo dirigido ou não dirigido com arestas de peso não negativo, em tempo computacional O([m+n]log n).

Deve-se setar a variável graph[MAX][MAX], sendo que esta matriz representa o peso/custo de cada aresta.
- em graph[][], tendo i e j, se i == j, graph[i][j] == 0. Se i != j, graph[i][j] = custo dele.
- Se não existir aresta entre i e j ( ou no caso no grafo direcionado de i para j), então o  custo é graph[i][j] = INF; (setado abaixo);

fazendo um for simples:
- graph[i][j] = (i == j ? 0 : INF);

OBS: Os nodos começam em ZERO (na matriz graph[][] no caso).

vCost corresponde ao caminho pra chegar até o nodo (partindo do nodo inicial dado quando foi chamada a função dijkstra).

Ex: se chamdou dijkstra(START = 0, END = 4)
vCost[4] é o vector com os índices dos nodos que foram visitados para chegar de 0 até 4.(ex 0 2 3 4).

```C++
#define MAX 1000
#define INF 999999999
int N;
int graph[MAX][MAX];
int visited[MAX],cost[MAX];
vector<int> vCost[MAX];

int dijkstra(int START, int END){
   int i, k, aux = 1,min=0;

   for(i=0 ; i<N ; i++) { /* inicializa foi e custo */
      visited[i] = 0;
      cost[i] = INF;
   }

   cost[START] = 0; /* a menor distância de INI já conhecida */
   visited[START] = 1;
   k = START;
   vCost[START].clear();
   vCost[START].push_back(START);

   while(!visited[END] && min!=INF){
      min = INF;

      for(i=0 ; i<N ; i++)
         if(!visited[i]){
            if(cost[i]>cost[k]+graph[k][i]) /* relaxamento */
            {
               cost[i]=cost[k]+graph[k][i];
               vCost[i] = vCost[k];
               vCost[i].push_back(i);
            }

            if(cost[i]<min){
               min=cost[i];
               aux=i;
            }
         }

         visited[aux]=1;
         k = aux;
   }

   if(visited[END]) return cost[END];
   else return -1;
}
```

## Dijkstra - Sem Memória Adicional
Mesmas instruções do algoritmo anterior, PORÉM nesse caso o algoritmo não guarda o vCost[], ou seja, os nodos percorridos para chegar de um nodo “ini” para um nodo “fim”.

No algoritmo abaixo foram comentadas linhas de impressão, onde é dito o nodo em questão e os nodos percorridos.

```C++
#include <cstring>
#include <iostream>
using namespace std;
#define MAX 100
#define INF 999999999
int N;
int graph[MAX][MAX];
int foi[MAX],custo[MAX];
int dijkstra(int INI, int FIM){
    int i, k, aux = 1,minimo=0;
    for(i=0 ; i<N ; i++) {
        foi[i] = 0;
        custo[i] = INF;
    }
    custo[INI] = 0;
    foi[INI] = 1;
    k = INI;
    int counter = 0;
    while(!foi[FIM] && minimo!=INF){
        //cout << counter << endl;
        counter++;
        minimo = INF;
        for(i=0 ; i<N ; i++) {
            //cout << "i: " << i << endl;
            if(!foi[i]){
                if(custo[i]>custo[k]+graph[k][i])
                    custo[i]=custo[k]+graph[k][i];
                if(custo[i]<minimo){
                    minimo=custo[i];
                    aux=i;
                }
            }
        }
        foi[aux]=1;
        k = aux;
    }

    if(foi[FIM]) return custo[FIM];
    else return -1;
}
```

## Simple Path entre dois vértices

O Algoritmo foi pego do problema hedge mazes da prova da maratona de 2011 – nacional, este algoritmo recebe um grafo com suas arestas e seta “componentes” para cada nodo do grafo.

Dois nodos tem a mesma componente quando: entre um nodo inicial e final há APENAS UM simple path possível.

    Simple Path – sequencia de nodos distintos que chegam de um nodo inicial a um final (sem repetição de nodos no caso). 

Seguindo o algoritmo abaixo, o teste das componentes eh realizado pela variável vis[MAX].


```C++
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#define MAX 10005
using namespace std;
vector <int> l[MAX];
int vis[MAX], viu[MAX], pai[MAX];
bool paiponte[MAX];
int cnt;

void dfs(int x){
   vis[x] = cnt++;
   viu[x] = vis[x];
   for (int i = 0; i < (int)l[x].size(); i++){
      if(l[x][i] != pai[x]){
         if(vis[l[x][i]] == -1){
            pai[l[x][i]] = x;
            dfs(l[x][i]);
            viu[x] = min(viu[x], viu[l[x][i]]);
         }
         viu[x] = min(viu[x], vis[l[x][i]]);
      }
   }
   for (int i = 0; i < (int)l[x].size(); i++){
      if(l[x][i] != pai[x] && viu[l[x][i]] > vis[x])
         paiponte[l[x][i]] = true;
   }
}

void dfsp(int x){
   vis[x] = cnt;
   for (int i = 0; i < (int)l[x].size(); i++){
      if(vis[l[x][i]] == -1 && ((pai[l[x][i]] == x && paiponte[l[x][i]]) || (pai[x] == l[x][i] && paiponte[x])) ){
         dfsp(l[x][i]);
      }
   }
}

/* função main para fins de exemplificação.
 */
int main(){
      /*Realizar a leitura da entrada.*/
      for (int i = 0; i < NUMERO_DE_VERTICES_DO_ATUAL_GRAFO; i++){
         pai[i] = vis[i] = viu[i] = -1;
         paiponte[i] = false;
         l[i].clear();
      }
      int x, y;
      for (int i = 0; i < QUANTIDADE_DE_ARESTAS_DO_GRAFO; i++){
         /*ler os dois vértices que pertencem a aresta*/
  /*No caso abaixo, o grafo é bidirecional*/
         l[x-1].push_back(y-1);
         l[y-1].push_back(x-1);
      }
      for (int i = 0; i < NUMERO_DE_VERTICES_DO_ATUAL_GRAFO; i++)
         if(vis[i] == -1){
            cnt = 0;
            dfs(i);
         }
      for (int i = 0; i < NUMERO_DE_VERTICES_DO_ATUAL_GRAFO; i++)
         vis[i] = -1;
      cnt = 0;

      for (int i = 0; i < NUMERO_DE_VERTICES_DO_ATUAL_GRAFO; i++)
         if (vis[i] == -1){
            dfsp(i);
            cnt++;
         }
      /*Ao final, basta fazer a seguinte comparação:*/
      if(vis[x] == vis[y])
         printf("Há uma Bridge entre X e Y (ou simple path).\n");
      else
         printf("Não há uma Bridge entre X e Y (ou simple path).\n");
      /*Se for um loop, volta em realizar a leitura de entrada:*/
  
   return 0;
}
```


## **(NÃO TESTADO)** Longest or Min Path in DAG

LONGEST OR MIM PATH IN DAG - Directed Acyclic Graphs

O(V + E)

```C++
void longest_path(int source) {
   for(int i = 1; i <= N; i++) {
      l_dist[i] = -90000000;
   }
   l_dist[source] = 0;

   for(int j = 1; j <= N; j++) {
      int v = top_sort[j];
      for(int i = 1; i <= N; i++) {
         if(graph[v][i] != 0) {
            if(l_dist[i] < l_dist[v] + graph[v][i]) {
               l_dist[i] = l_dist[v] + graph[v][i];
            }            
         }
      }
   }
}
```

## **(NÃO TESTADO)** Connected Components
CONNECTED COMPONENTES - Connected component of an undirected graph is a subgraph in which any two vertices are connected to each other by paths, and which is connected to no additional vertices.
```C++
void connected_components() { 
   int count_cc = 0;
   for(int i = 1; i <= N; i++) {
      if(discovered[i] == false) {
         count_cc++;
         dfs(i);
      }
   }
   cout << count_cc << endl;
}
```

## **(NÃO TESTADO)** Strongly Connected Components
STRONGLY CONNECTED COMPONENTES - Kosaraju's algorithm finds strongly-connected components in a directed graph. 
A directed graph is called strongly connected if there is a path from each vertex in the graph to every other vertex. In particular, this means paths in each direction; a path from a to b and also a path from b to a.
```C++
int N;
vector<int> SortNodes;
typedef struct {
   list<int> to;
} graph;
graph G[MAX];
graph Gt[MAX];
int component[MAX];
int visited[MAX];
int counter_scc;

void search(int v) {
   visited[v] = true;   

   for(list<int>::iterator it = G[v].to.begin(); it != G[v].to.end(); ++it){
      if(!visited[*it]) {
         search(*it);
      }
   }
   SortNodes.push_back(v);
}
void searchT(int v, int counter) {
   visited[v] = false; 
   component[v] = counter;

   for(list<int>::iterator it = Gt[v].to.begin(); it != Gt[v].to.end(); ++it){
      if(visited[*it]) {
         searchT(*it, counter);
      }
   }
}
void kosaraju(){
   for(int i = 1; i <= N; i++) {
      if(!visited[i]) {
         search(i);   
      }
   }
   for(int i = SortNodes.size() - 1; i >= 0; i--) {
      if(visited[ SortNodes[i] ]) {
         searchT(SortNodes[i], ++counter_scc);
      }
   }
}
```

## **(NÃO TESTADO)** Bridge
BRIDGE -  Bridge (also known as a cut-edge or cut arc or an isthmus) is an edge whose deletion increases the number of connected components
```C++
vector<bool> visited;
vector<int> prev, low, d;
vector<vector<int> > g;
vector<vector<bool> > is_bridge;
int N, counter;
counter = 0;

visited.assign(n, false);
prev.assign(n, -1);
low.resize(n);
d.resize(n);
g.assign(n, vector<int>());
is_bridge.assign(n, vector<bool>(n, false));

for (int i=0; i<n; ++i){
   if (!visited[i]){
      dfs(i);
   }
}

void dfs(int u){
   visited[u] = true;
   d[u] = low[u] = counter++;
   for (int i=0; i< (int)g[u].size(); ++i){
      int v = g[u][i];
      if (prev[u] != v){
         if(!visited[v]){
            prev[v] = u;
            dfs(v);
            if (d[u] < low[v]){
               is_bridge[u][v] = is_bridge[v][u] = true;
            }
            low[u] = min(low[u], low[v]);
         }else{
            low[u] = min(low[u], d[v]);
         }
      }
   }
}
```

## **(NÃO TESTADO)** Articulation Points
ARTICULATION POINTS - Vértice de corte ou ponto de articulação é um vértice de um grafo tal que a remoção deste vértice provoca um aumento no número de componentes conectados.
```C++
int N;
int graph[MAX][MAX];
int low[MAX];
int un[MAX];
int counter;
int art_points[MAX];
void find_art_points(int v, int u){
   low[v] = un[v] = counter++;
   for(int w = 1; w <= N; w++){
      if(graph[v][w] == 1 && w != u) {
         if(un[w] == 0) {
            find_art_points(w, v);
            low[v] = min(low[v], low[w]);
            if(un[v] == 1 && un[w] != 2) {
               art_points[v] = 1;
            }
            if(un[v] != 1 && low[w] >= un[v]){
               art_points[v] = 1;
            }
         } else {
            low[v] = min(low[v], un[w]);
         }
      }   
   }
}


for (int i = 1; i <= N; i++){
   if (un[i] == 0){
      find_art_points(i, -1);
   }
}
```


## Prim's Algorithm

Algoritmo O(n log n) para encontrar em um grafo com pesos não direcionado a arvore que conecte todos os nós e tenha o menor somatório de pesos.

[Mais informações...](https://cp-algorithms.com/graph/mst_prim.html)
[Algoritmo de mesmo propósito mais simples](https://cp-algorithms.com/graph/mst_kruskal.html)

No exemplo abaixo, o algoritmo encontra a menor arvore e retorna a soma dos pesos da aresta.

```C++
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

const int INF = 1000000000;
struct Edge {
    int w = INF, to = -1;
    bool operator<(Edge const& other) const {
        return make_pair(w, to) < make_pair(other.w, other.to);
    }
};

int prim(vector<vector<Edge>> adj, int n) {
    int total_weight = 0;
    vector<Edge> min_e(n);
    min_e[0].w = 0;
    set<Edge> q;
    q.insert({0, 0});
    vector<bool> selected(n, false);
    for (int i = 0; i < n; ++i) {
        if (q.empty()) {
            return 0;
        }

        int v = q.begin()->to;
        selected[v] = true;
        total_weight += q.begin()->w;
        q.erase(q.begin());

        for (Edge e : adj[v]) {
            if (!selected[e.to] && e.w < min_e[e.to].w) {
                q.erase({min_e[e.to].w, e.to});
                min_e[e.to] = {e.w, v};
                q.insert({e.w, e.to});
            }
        }
    }

    return total_weight;
}
```