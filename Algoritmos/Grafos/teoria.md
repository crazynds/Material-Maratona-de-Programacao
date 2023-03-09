# Teoria dos grafos

A teoria dos grafos ou de grafos é um ramo da matemática que estuda as relações entre os objetos de um determinado conjunto.  Para tal são utilizadas estruturas chamadas de grafos, $G(V,E)$ , onde $V$ é um conjunto não vazio de objetos denominados vértices (ou nós) e  $E$ (do inglês edges - arestas) é um subconjunto de pares não ordenados de $V$.

Diversas estruturas podem ser consideradas grafos, como listas encadeadas e arvores, por possuirem arestas e nós.

## Definição

Um grafo $G$ consiste de um conjunto finito e não vazio $V (G)$ de objetos chamados vértices, juntamente com um conjunto $E(G)$ de pares não ordenados de vértices; os elementos de $E(G)$ são chamados de arestas. Podemos representá-lo por $G = (V ; E)$, onde $V = V (G)$ e $E = E(G)$.


- Um **grafo trivial** é um grafo no qual $G = (V;\varnothing)$, ou seja, não contém arestas.

- Um **grafo completo** é um grafo no qual todo vertice possui uma aresta a qualquer vertice, sendo o número de vertices desse tipo de grafo sempre $n * (n-1)$. 

- Um **grafo regular** é um grafo no qual todos os vertices possuem um mesmo grau $r$.


## Direção

Um grafo não direcionado (ou simplesmente grafo) é dado por:
 - Uma aresta $E$ vincula um nó $V_{1}$ a um nó $V_{2}$, implica que a mesma aresta vincula $V_{2}$ a $V_{1}$;

Um grafo direcionado (também chamado dígrafo) consiste de:

 - Dada uma aresta $E$ que vincula um nó $V_{1}$ a um nó $V_{2}$, o inverso não pode ser aplicado usando a mesma aresta;

Em um digrafo, quando dizemos que uma aresta é incidente a um vértice queremos saber em que sentido, isto é, se a aresta é *convergente* ou *divergente* a este vértice. É natural dizer que uma aresta a associada ao par $(v_{i},v_{j})$ é convergente a $v_{j}$ e divergente de $v_{i}$.

Em relação ao grau de um vértice $v_{i}$ queremos também saber: 
 - o número de arestas convergentes, chamado grau de entrada; 
 - o número de arestas divergentes, chamado grau de saída$;

## Conectividade

Um passeio de comprimento $k ≥ 1$ em um grafo $G$ é uma sequência $P = (u0, u1, ..., uk)$ de vértices (não necessariamente distintos) de $G$ tal que $u_{i}−1$ é adjacente a $u_{i}$ para $1 ≤ i ≤ k$. O passeio $P$ acima é fechado se $u0 = uk$, podemos chamar o passeio fechado de circuito.

Um grafo é dito **conexo** se existir pelo menos um *passeio* entre cada par de vértices do grafo. Caso contrário, o grafo é chamado de **desconexo**.

Um grafo é **planar** se puder ser desenhado no plano sem que haja arestas se cruzando.

## Ideias Básicas

Um grafo é dito como *Euleriano* se contiver um [passeio euleriano](./konisgsberg.md).

[Ciclos Hamiltonianos](./hamiltonianos.md)


## Referencias

[Introdução à Teoria dos Grafos](https://github.com/UFSM-Maratona-de-Computacao/Material-Auxiliar/blob/main/livros/Teoria%20dos%20grafos.pdf)

[Wikepedia](https://pt.wikipedia.org/wiki/Teoria_dos_grafos)
