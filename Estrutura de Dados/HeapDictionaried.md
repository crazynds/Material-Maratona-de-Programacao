# Heap + Dictionarie

Uma estrutura mística nos contos de fadas, que sempre se ouviu falar mas até hoje não foi encontrado uma implementação decente (Não foi procurado muito, mas não deve ser dificil fazer).

A ideia é a seguinte, você vai ter a estrutura heap normal, porém você vai manter um dicionario atualizado dizendo qual chave contida no array heap está em qual posição do array heap. Isso é muito bom quando você quer adicionar uma operação de remoção rápida na heap, porém aumenta o custo da inserção (ainda é O(log n) a complexidade) e aumenta o custo do pop já que é necessário manter o dicionário atualizado. 

Alguns casos de usos são no caso de algoritmos como o Dijkstra que quando você acha um caminho mais curto para o nó X, você pode remover qualquer caminho que já vá para aquele nó, economizando memória e ao mesmo tempo se você for inserir um caminho mais longo, ele antes de fazer a inserção já verifica que o caminho é maior do que o que está na heap e nem insere, então isso evita ter uma heap muito grande, e evita diversas inserções e pop's desnecessários.


### Desvantagens:
 - Aumenta o custo da inserção e remoção do item do topo;

### Vantagem:
 - Dependendo do algoritmo previne a inserção de valores que nunca vão ser iterados na heap (valores repetidos para os mesmos nós/caminhos);
 - Diminui o consumo de memória da heap;
 - Remove elementos da heap se um novo elemento melhor for adicionado para o mesmo nó/caminho;

