# Grafos

A teoria dos grafos ou de grafos é um ramo da matemática que estuda as relações entre os objetos de um determinado conjunto. 
Para tal são utilizadas estruturas chamadas de grafos, $G(V,E)$
, onde $V$ é um conjunto não vazio de objetos denominados vértices (ou nós) e 
$E$ (do inglês edges - arestas) é um subconjunto de pares não ordenados de $V$.

Diversas estruturas podem ser consideradas grafos, como listas encadeadas e arvores, por possuirem arestas e nós.


## Caracteristicas
### Direção
Na literatura, as definições básicas da teoria dos grafos variam bastante.



Um grafo não direcionado (ou simplesmente grafo) é dado por:
 - Uma aresta $E$ vincula um nó $V_{1}$ a um nó $V_{2}$, implica que a mesma aresta vincula $V_{2}$ a $V_{1}$;

Um grafo direcionado (também chamado dígrafo) consiste de:

 - Dada uma aresta $E$ que vincula um nó $V_{1}$ a um nó $V_{2}$, o inverso não pode ser aplicado usando a mesma aresta;

Em um digrafo, quando dizemos que uma aresta é incidente a um vértice queremos saber em que sentido, isto é, se a aresta é *convergente* ou *divergente* a este vértice. É natural dizer que uma aresta a associada ao par $(v_{i},v_{j})$ é convergente a $v_{j}$ e divergente de $v_{i}$.

Em relação ao grau de um vértice $v_{i}$ queremos também saber: 
 - o número de arestas convergentes, chamado grau de entrada; 
 - o número de arestas divergentes, chamado grau de saída$;

### Conectividade

Um grafo é dito **conexo** se existir pelo menos um caminho entre cada par de vértices do grafo. Caso contrário, o grafo é chamado de **desconexo**.

Um grafo é dito **completo** se todo vertice pertencente ao grafo for adjacente a todos os outros vértices.

Um grafo é **planar** se puder ser desenhado no plano sem que haja arestas se cruzando

