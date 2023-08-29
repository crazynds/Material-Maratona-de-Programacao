# Binary Tree

Uma árvore binária é compostas por nós, no qual cada nó pode apontar para um nó na esquerda e na direita. Os nós a esquerda do nó principal são sempre menores que o nó principal, e os a direita são sempre maiores.

<img src="binary-tree.png" width=300/>

Uma árvore binária tem a vantagem no melhor caso, para uma inserção, remoção e busca ter custo de tempo O(log N). Porém quanto menos balanceada uma árvore binária estiver, maior vai ser o custo das operações, por isso existem implementações de algoritmos de balanceamento para esse tipo de árvore.


# Python - [Binary Tree](./AVLTree.md)

Em python, não existe nenhuma implementação na biblioteca padrão para árvores binárias. Depende muito do caso se você deve usar árvores binárias, mas se você realmente precisa utilizar essa estrutura, recomendo que pegue uma implementação que já inclui balanceamento. [Clique aqui](./AVLTree.md) para uma implementação que inclui balanceamento.
