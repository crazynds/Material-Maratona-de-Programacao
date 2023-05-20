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
- pop_front(): remove um elemento do inicio da lista;
- insert(): existem algumas versões para o insert, sendo elas:
 - insert(iterator pos, val): a partir da posição, insere o item val;
 - insert(iterator pos, start, end): a partir da posição, insere o array que começa em start e termina em end;
- erase(): apaga um elemento na posição passada, note que para remover o elemento da posição 4 deve-se chamar a função begin() e somar a 4;

### Operadores:
- sort(): Ordena os elementos da lista, é possivel passar uma função para fazer a comparação;
- merge(): Junta duas listas ordenadas, a lista final vai estar ordenada;
- remove(): Remove todos os elementos que possuem o mesmo valor passado no parametro;
- remove_if(): Remove todos os elementos que passam na condição. O parametro é uma função que é aplicada em todos os elementos, e deve retornar true ou false, sendo true para remover e false para manter na lista;

## Python - [list](https://docs.python.org/3/tutorial/datastructures.html)


As principais funções utilizadas nas listas são as citadas abaixo:
### Modificadores:
- append(x): adiciona o elemento x ao final da lista;
- extend(_iterable_): adiciona todos os elementos do _iterable_* a lista;
- insert(i,x): insere o item x a posição i da lista;
- remove(x): remove o primeiro item que seja igual a x;
- clear(): remove todos os elementos da lista;


### Operadores:
- sort(): ordena a lista;
 - key= fn(x) : o parametro key da função sort deve receber uma função que tem 1 parametro e retorna uma chave de comparação. Isso é bom quando se tem uma lista de objeto e para fazer o sort é necessário do item id do objeto, ou outro valor;
 - reverse= bool : define se deve ordenar a lista de forma crescente ou decrescente; 
- reverse(): reverte a lista;
- copy(): faz uma copia completa da lista;


### Getters:
- list.count(x): retorna a contagem de quantos elementos iguais ao x existem na lista;


\* _iterable_ em python é qualquer extrutura de dados que pode ser acessada de forma iterativa, e implementa a interface _iterable_


Note que em python, boa parte das função auxiliares não retornam uma lista, e sim um _iterable_. Caso queira converter um _iterable_ em uma lista para poder utilizar as funções de lista use o seguinte código:

```python
l = [1,2,3,4]
m = map(float,l) # a função map não retorna uma lista, e sim um objeto que extende iterable
l = [* m ] # dessa forma o python abre nosso iterable dentro de uma lista
```

Existem algumas formas de criar um array de maneira fácil em pyton:

```python
fruits = ['banana','longberry','passion fruit']
zeros = [0 for _ in range(10)]
squares = [x**2 for x in range(10)]
nums = [*range(10)] #Note que range também é um iterable logo é possivel abri-lo dentro de uma lista

ofMap = list(map(lambda x:x/2,range(10)))   #Note que list(...) é uma outra forma de escrever [*...]

val = [1,2,3]
a,b,c = val # note que é possivel desconstruir uma lista em que cada valor vai para uma variavel, mas é necessário que a lista tenha a mesma quantidade de valores que as variaves que recebem o valor.

```

Outra forma de remover um elemento de uma lista **sem retorna-lo** é utilizando a chamada _del_ do python. Segue um exemplo:

```python

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0] # remove o elemento na posição 0
del a[:2] # remove todos os elementos até a posição 2
del a[2:] # remove todos os elementos a partir da posição 2
del a[2:4] # remove todos os elementos a partir da posição 2 até a posição 4
del a[:] # remove todos os elementos do vetor
```
