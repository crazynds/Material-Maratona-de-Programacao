# Conjutos (Set)

Conjutos (set) são container que armazenam valores em uma estrutura de dados, com inserção, remoção e acesso constante. Geralmente usam [HashMap](./HashMap.md).

## C++ - [std::unordered_set](https://cplusplus.com/reference/unordered_set/unordered_set/)

Unordered sets are containers that store unique elements in no particular order, and which allow for fast retrieval of individual elements based on their value.


### Associação 
Elements in associative containers are referenced by their key and not by their absolute position in the container.

### Set
The value of an element is also the key used to identify it.

As principais funções utilizadas em sets são as citadas abaixo:

### Iteração:
- begin(): retorna um iterador a partir do inicio da lista; 
- end(): retorna um iterador a partir do fim da lista (não pega a ultima casa);
- rbegin(): retorna um iterador _reverso_ a partir do fim da lista; 
- rend(): retorna um iterador _reverso_ a partir do inicido da lista (não pega a primeira casa);

### Capacidade:
- size(): retorna o tamanho da lista;
- empty(): retorna true se a lista estiver vazio;

### Modificadores:
- insert(): existem algumas versões para o insert, sendo elas:
 - insert(val): insere o item val;
 - insert(iterator pos, val): a partir da posição passada insere o item val, ainda vai manter a ordem, porém pode adicionar eficiencia se a posição do iterator passada estiver próxima do local onde o item deve ser inserido;
- erase(): apaga um elemento na posição passada, a posição passada sempre é um iterator na posição que deseja remover;
- clear(): limpa todos os dados do set;

### Getters:
- find(): retorna um iterator se existir aquele dado no set, se não existir ele retorna um iterator end()



## Python - [set](https://docs.python.org/3/tutorial/datastructures.html#sets)


As principais funções de set em python são exemplificadas abaixo:

```python

v = {'banana', 'tomate', 'arroz'} # create a set

'banana' in v # True

for s in v: # for each item in set
    pass

v.add('laranja') # add item to set
v.remove('banana') # remove item from set

d = {'banana', 'tomate', 'feijão'}

d | v # in set d or v
d - v # in d but not in v (order matters)
d & v # in both sets (d and v)
d ^ v # in set d or in set v but not in both

```





