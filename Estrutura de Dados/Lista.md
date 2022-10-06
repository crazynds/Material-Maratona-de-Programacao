# Lista

Listas são contêineres de sequência que permitem operações de inserção e apagamento de tempo constante em qualquer lugar dentro da sequência e iteração em ambas as direções.

Os contêineres de lista são implementados como listas duplamente vinculadas; As listas duplamente vinculadas podem armazenar cada um dos elementos que contêm em locais de armazenamento diferentes e não relacionados. A ordenação é mantida internamente pela associação a cada elemento de um link para o elemento que o precede e um link para o elemento que o segue.


## C++ - [std::list](https://cplusplus.com/reference/list/list/) 

### Sequência
Os elementos em contêineres de sequência são ordenados em uma sequência linear estrita. Elementos individuais são acessados por sua posição nesta sequência.
### Lista duplamente ligada
Cada elemento guarda informações sobre como localizar o próximo e os anteriores, permitindo operações de inserção e apagamento em tempo constante antes ou depois de um elemento específico (mesmo de faixas inteiras), mas sem acesso aleatório direto.
### Dinamicamente Alocado
O contêiner usa um objeto alocador para lidar dinamicamente com suas necessidades de armazenamento


As principais funções utilizadas nas listas são as citadas abaixo:
### Iteração:
- begin(): retorna um iterador a partir do inicio da lista; 
- end(): retorna um iterador a partir do fim da lista (não pega a ultima casa);
- rbegin(): retorna um iterador _reverso_ a partir do fim da lista; 
- rend(): retorna um iterador _reverso_ a partir do inicido da lista (não pega a primeira casa);

### Getters:
- front(): retorna o primeiro elemento;
- back(): retorna o ultimo elemento;

### Capacidade:
- size(): retorna o tamanho da lista;
- empty(): retorna true se a lista estiver vazio;

### Modificadores:
- push_back(): adiciona um elemento ao final da lista;
- pop_back(): remove um elemento do final da lista;
- push_front(): adiciona um elemento ao inicio da lista;
- pop_front()): remove um elemento do inicio da lista;
- insert(): existem algumas versões para o insert, sendo elas:
 - insert(iterator pos, val): a partir da posição, insere o item val;
 - insert(iterator pos, start, end): a partir da posição, insere o array que começa em start e termina em end;
- erase(): apaga um elemento na posição passada, note que para remover o elemento da posição 4 deve-se chamar a função begin() e somar a 4;

### Operadores:
- sort(): Ordena os elementos da lista, é possivel passar uma função para fazer a comparação;
- merge(): Junta duas listas ordenadas, a lista final vai estar ordenada;
- remove(): Remove todos os elementos que possuem o mesmo valor passado no parametro;
- remove_if(): Remove todos os elementos que passam na condição. O parametro é uma função que é aplicada em todos os elementos, e deve retornar true ou false, sendo true para remover e false para manter na lista;
