# Hash Map

Em um HashMap, o valor da chave geralmente é usado para identificar exclusivamente o elemento, enquanto o valor mapeado é um objeto com o conteúdo associado a essa chave. Os tipos de chave e valor mapeado podem ser diferentes.

Internamente, os elementos no HashMap não são classificados em nenhuma ordem específica com relação a sua chave ou valores mapeados, mas organizados em baldes dependendo de seus valores de hash para permitir acesso rápido a elementos individuais diretamente por seus valores de chave (com uma constante complexidade de tempo média em média).



## C++ - [std::unsorted_map](https://cplusplus.com/reference/unordered_map/unordered_map/)

Vale destacar que a ```std::unsortedmap``` é implementada utilizando um hashmap, o que faz com que sua inserção, busca e remoção seja feito em tempo O(1), enquanto a ```std::map``` utiliza a implementação de uma [árvore binária](./BinaryTree.md) Red-Black, que já se mantém balanceada, então suas operações tem custo O(log n).

Nesse tópico vou apresentar as principais características da estrutura ```std::unsortedmap```
Para saber mais sobre ```std::map```, [clique aqui](./BinaryTree.md)

### Associativo
Os elementos em contêineres associativos são referenciados por sua chave e não por sua posição absoluta no contêiner.

### Não ordenado
Os contêineres não ordenados organizam seus elementos usando tabelas de hash que permitem acesso rápido aos elementos por sua chave.

### Mapa
Cada elemento associa uma chave a um valor mapeado: As chaves servem para identificar os elementos cujo conteúdo principal é o valor mapeado.

### Iteração:
- begin(): retorna um iterador a partir do inicio do vetor; 
- end(): retorna um iterador a partir do fim do vetor (não pega a ultima casa);

### Getters:
- operator[]: retorna o elemento da _chave_ indicada dentro do operator. Caso seja uma chave que não existe é inserido um novo item com o construtor padrão (para números geralmente é zero) e retornado uma referencia desse item;
- find(): retorna um iterador a partir desse elemento, caso não encontre retorna o map.end();

### Capacidade:
- size(): retorna o tamanho do vetor;
- empty(): retorna true se o vetor estiver vazio;

### Modificadores:
- insert(): existem algumas versões para o insert, sendo elas:
 - insert(std::pair<K,V>): insere um objeto par dentro do map;
 - insert(K,V): insere o valor V na posição K;
- erase(): apaga um elemento na posição passada, note que para remover o elemento da posição 4 deve-se chamar a função begin() e somar a 4;
 - erase(iterator): remove o item dessa posição do iterador;
 - erase(start,end): remove os items desde a posição start até end;


## Python - [dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

Os _dictionaries_ não possuem nenhuma função importante, e todos as manipulações deles são exemplificadas abaixo:

```python

d1 = {} # forma de criar um dicionário vazio
d2 = {
  1: 'S1', 
  2:'s2'
} # forma de criar um dicionário com elementos já
d3 = {x: x**2 for x in range(10)} # declarar um dicionario com elementos dinamicos

bool1 = 1 in d1 # forma de verificar se a chave existe no dicionario
bool2 = 2 not in d1 # forma de verificar se a chave não existe no dicionario

d1[1] = 'ola mundo' # forma de adicionar item no dicionario
d1[1] += '!' # é possivel manipular os itens do dicionaro também

del d1[1] # deleta o item com a chave 1 do dicionário


for key in d1:  # essa é a forma de iterar sobre o dicionário, porém o valor que é iterado é sobre as chaves, e não sobre os valores
    print(key,d1[key])

for key,val in d1.items():  # essa é a forma de iterar sobre o dicionário incluindo os valores
    print(key,val)

l = list(d1)  # cria uma lista com todas as chaves do dicionário
l = list(d1.items())  # cria uma lista com tuplas contendo a relação entre chave e valor

```
