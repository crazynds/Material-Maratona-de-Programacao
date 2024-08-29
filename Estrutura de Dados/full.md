# Vetores

Vetores são estruturas de dados muito legais em qualquer linguagem. Basicamente permite armazenar uma quantidade prédeterminada, ou indeterminada, de elementos e é possivel organiza-los dentro do vetor da forma que quiser.

Cada casa de um vetor geralmente é referenciada por um inteiro, indentificando a posição que determinado valor foi salvo. Dependendo da linguagem é possivel também possuir um vetor não continuo, ou seja, pode possuir a casa N mas não necessáriamente possue todas as casas de 0 a N, ou vetores no qual a chave da casa pode ser uma string ou até outro referenciador, sendo mais comum nesses casos serem chamados de _dictionary_.


## C++ - [std::vector](https://cplusplus.com/reference/vector/vector/)

### Sequência
Os elementos em contêineres de sequência são ordenados em uma sequência linear estrita. Elementos individuais são acessados por sua posição nesta sequência.
### Vetor dinâmico
Permite acesso direto a qualquer elemento na sequência, mesmo por meio de aritmética de ponteiro, e fornece adição/remoção relativamente rápida de elementos no final da sequência.
### Dinamicamente Alocado
O contêiner usa um objeto alocador para lidar dinamicamente com suas necessidades de armazenamento.

As principais funções utilizadas no vetor são as citadas abaixo:

### Iteração:
- begin(): retorna um iterador a partir do inicio do vetor; 
- end(): retorna um iterador a partir do fim do vetor (não pega a ultima casa);
- rbegin(): retorna um iterador _reverso_ a partir do fim do vetor; 
- rend(): retorna um iterador _reverso_ a partir do inicido do vetor (não pega a primeira casa);

### Getters:
- operator[]: retorna o elemento da casa indicada dentro do operator. Caso seja uma posição maior que a quantidade de itens então causa um _comportamento não definido_;
- front(): retorna o primeiro elemento;
- back(): retorna o ultimo elemento;

### Capacidade:
- size(): retorna o tamanho do vetor;
- empty(): retorna true se o vetor estiver vazio;
- capacity(): retorna o tamanho alocado atualmente para esse vetor;
- reserve(): reseva o tamanho informado para esse vetor;

### Modificadores:
- push_back(): adiciona um elemento ao final do vetor;
- pop_back(): remove um elemento ao final do vetor;
- insert(): existem algumas versões para o insert, sendo elas:
 - insert(iterator pos, val): a partir da posição, insere o item val;
 - insert(iterator pos, start, end): a partir da posição, insere o array que começa em start e termina em end;
- erase(): apaga um elemento na posição passada, note que para remover o elemento da posição 4 deve-se chamar a função begin() e somar a 4;

```C++
#include <vector> 

vector<int> *x = new vector<int> (3, 25); //x = (25, 25, 25)
vector<int> y (5,0); // y = (0, 0, 0, 0, 0)
*x = y; // x = (0, 0, 0, 0, 0)

int s[3] = {100, 231, 213};
y.assign(s, s+3); // x = (0, 0, 0, 0, 0) e y = (100, 231, 213)

y.insert(y.begin(), s, s+3); // y = (100, 231, 213, 100, 231, 213)
y.erase(y.begin(), y.begin() + 2); // y = (213, 100, 231, 213)

y.at(1); // == y[1] e assim por diante

vector<int>::iterator it;
for(it = y.begin(); it != y.end(); it++)
cout << *it << endl;  
```


## Python - [list](https://docs.python.org/3/tutorial/datastructures.html)

Em python não existem vetores, ao invéz disso todos as estruturas de array que são trabalhadas na linguagem se utiliza a estrutura de [listas](./Lista.md#python-list).

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

# Pilha

Pilha, ou também chamada de stack, é uma estrutura de dados que se baseaia no príncipio LIFO (_LAST IN FIRST OUT_).

Pilhas são fundamentalmente compostas por duas operações: push (empilhar) que adiciona um elemento no topo da pilha e pop (desempilhar) que remove o último elemento adicionado.


## C++ - [std::stack](https://cplusplus.com/reference/stack/stack/) 


As principais funções utilizadas na stack são as citadas abaixo:

- empty(): testa se a stack está vazia;
- size(): retorna o tamanho da stack;
- push(T): insere no topo da pilha o item T;
- pop(): remove o elemento do topo da pilha, destaque que ele **não retorna** esse elemento, ele apenas remove;
- top(): retorna o elemento do topo da pilha, sem remove-lo;

Abaixo um exemplo de utilização da stack:

```C++
// stack::push/pop
#include <iostream>       // std::cout
#include <stack>          // std::stack

int main ()
{
  std::stack<int> mystack;
  for (int i=0; i<5; ++i) mystack.push(i);
  std::cout << "Popping out elements...";
  while (!mystack.empty())
  {
     std::cout << ' ' << mystack.top();
     mystack.pop();
  }
  std::cout << '\n';

  return 0;
}
```



## Python - [deque](https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-queues)

Em python não existe pilha, mas ao mesmo tempo existe a estrutura _deque_ que é possivel utilizar as mesmas operações de uma stack, então [acesse aqui](./DoubleEndedQueue.md) para saber mais.



# Double Ended Queue

É um array no qual é possivel adicionar valores no inico e no final e também remover valores de ambos os lados.
Não necessáriamente o acesso a uma posição especifica do array vai garantir um acesso constante O(1), mas a inserção e remoção no inicio e final é sempre constante O(1)




## Python - [deque](https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-queues)

Em python existe a estrutura de dados _deque_ (Double Ended Queue) que é desenvolvida para ter _rápidas_ inserções e remoções para o início e o fim da lista.

Um _deque_ pode ser usado da seguinte forma:

```python
from collections import deque

l = [1,2,3,4]
dq = deque(l) # cria um deque a partir de uma lista, O(n)
dq.append(7) # adiciona ao final do deque o item 7, O(1)
dq.appendleft(7) # adiciona ao inicio do deque o item 7, O(1)
dq.popleft() # retorna e remove o primeiro elemento do deque, O(1)
dq.pop() # retorna e remove o ultimo elemento do deque, O(1)
dq.rotate(5) # ´rotaciona´ uma deque. rotate(5) fará 5 rotações no sentido normal (esquerda para direita). rotate(-5) faz no oposto (direita para esquerda)
```


## C++ - [deque](https://cplusplus.com/reference/deque/deque/)


Specific libraries may implement deques in different ways, generally as some form of dynamic array. But in any case, they allow for the individual elements to be accessed directly through random access iterators, with storage handled automatically by expanding and contracting the container as needed.

Therefore, they provide a functionality similar to vectors, but with efficient insertion and deletion of elements also at the beginning of the sequence, and not only at its end. But, unlike vectors, deques are not guaranteed to store all its elements in contiguous storage locations: accessing elements in a deque by offsetting a pointer to another element causes undefined behavior.




```c++
#include <iostream>       // std::cout
#include <deque>

using namespace std;

int main ()
{
    deque<int> second(4,100);                       // four ints with value 100
    deque<int> third(second.begin(),second.end());  // iterating through second
    deque<int> fourth(third);                       // a copy of third

    // the iterator constructor can be used to copy arrays:
    int myints[] = {16,2,77,29};
    deque<int> fifth(myints, myints + sizeof(myints) / sizeof(int) );

    cout << "The contents of fifth are:";
    for(deque<int>::iterator it = fifth.begin(); it!=fifth.end(); ++it)
        cout << ' ' << *it;
    cout << '\n';

    deque<int> mydeque;
    mydeque.push_back(100);
    mydeque.push_back(200);
    mydeque.push_back(300);
    mydeque.push_front(255);

    cout << mydeque.front() << " | .. | " << mydeque.back() << endl;

    // This do not return the content, only eliminate then!
    mydeque.pop_front();
    mydeque.pop_back();
    cout << mydeque.front() << " | .. | " << mydeque.back() << endl;
}

```


# Minimum Queue

Essa estrutura serve para adicionar e remover elementos de um conjunto em tempo constante, e consultar o menor elemento do conjunto em tempo constante.

Para essa estrutura funcionar de maneira correta, cada elementos inserido na stack deve ser removido somente após todos os elementos que já foram inseridos antes tenham sido removidos. Exemplo: insere(A),insere(B),insere(C),remove(A),remove(B),remove(C).

Dessa forma os itens só podem serem removidos na ordem que foram inseridos.

Tempos de inserção, remoção e consulta são em média O(1).

Mais informações pode ser visto [aqui](https://cp-algorithms.com/data_structures/stack_queue_modification.html).


Obs: É possivel adaptar o código para ter a _Maximum Queue_, no qual o valor importante é o máximo.

## C++ - [Minimum Queue](https://cp-algorithms.com/data_structures/stack_queue_modification.html) 


```C++
class MinimiumQueue{
private:
    deque<int> queue;

public:
    int getMin(){
        return queue.front();
    }

    void add(int new_element){
        while(!queue.empty() && queue.back()>new_element){
            queue.pop_back();
        }
        queue.push_back(new_element);
    }

    void rem(int element){
        if (!queue.empty() && queue.front()==element)
            queue.pop_front();
    }
};
```

## Outra Implementação para Minimum Queue

```cpp
struct MinQueue
{
    deque<pair<int, int>> minQueue;
    int contPush = 0;

    void add(int num)
    {
        // se (minQueue.back().first < num), vira maxQueue
        while(!minQueue.empty() && minQueue.back().first > num)
        {
            minQueue.pop_back();
        }

        minQueue.push_back({num, contPush});
        contPush++;
    }

    int getMin(int start = 0)
    {
        while(start > minQueue.front().second)
        {
            minQueue.pop_front();
        }

        return minQueue.front().first;
    }
};
```

Para utilizar, considere que `m` seja o tamanho dos subvetores e `n` o tamanho total do vetor.

```cpp
MinQueue minq;

for(int i = 0; i < m; i++)
{
    minq.add(v[i]);
}

// start = 0
cout << minq.getMin() << endl;

for(int i = 1; i <= v.size() - m; i++)
{
    minq.add(v[i + m - 1]);
       
    // start = i  
    cout << minq.getMin(i) << endl;
}
```

## Exercícios

- [Queries with Fixed Length](https://www.hackerrank.com/challenges/queries-with-fixed-length/problem)
- [Binary Land](https://www.codechef.com/MAY20A/problems/BINLAND)



# Heap (Arvore binaria em array)

O heap simula uma arvore binária em um array e sempre mantem o elemento de maior prioridade mais próximo do topo. Consegue ser muito eficiente na inserção de itens e remoção do item de maior prioridade. Com essa estrutura não é possivel acessar elementos sem ser o elemento do topo.

Aplicações:
 - Dijkstra
 - Priority Queue (fila)

## C++ - [std::priority_queue](https://cplusplus.com/reference/queue/priority_queue/)

Priority queues are a type of container adaptors, specifically designed such that its first element is always the greatest of the elements it contains, according to some strict weak ordering criterion.

This context is similar to a heap, where elements can be inserted at any moment, and only the max heap element can be retrieved (the one at the top in the priority queue).

### Default behavior

Note the prioriry_queue by default leave the **biggest** value at the top, unless you use custom compare function.

### Custom compare function

A binary predicate that takes two elements (of type T) as arguments and returns a bool.
The expression comp(a,b), where comp is an object of this type and a and b are elements in the container, shall return true if a is considered to go before b in the strict weak ordering the function defines.

The priority_queue uses this function to maintain the elements sorted in a way that preserves heap properties (i.e., that the element popped is the last according to this strict weak ordering). This can be a function pointer or a function object, and defaults to less<T>, which returns the same as applying the less-than operator (a<b).

The use of compare function pointer is examplified as follow.
```c++
#include <iostream>       // std::cout
#include <queue>          // std::priority_queue
#include <vector>         // std::vector
#include <functional>     // std::greater

class mycomparison
{
  bool reverse;
public:
  mycomparison(const bool& revparam=false)
    {reverse=revparam;}
  bool operator() (const int& lhs, const int&rhs) const
  {
    if (reverse) return (lhs>rhs);
    else return (lhs<rhs);
  }
};

int main ()
{
  int myints[]= {10,60,50,20};

  std::priority_queue<int> first;
  std::priority_queue<int> second (myints,myints+4);
  std::priority_queue<int, std::vector<int>, std::greater<int> >
                            third (myints,myints+4);
  // using mycomparison:
  typedef std::priority_queue<int,std::vector<int>,mycomparison> mypq_type;

  mypq_type fourth;                       // less-than comparison
  mypq_type fifth (mycomparison(true));   // greater-than comparison

  return 0;
}
```

As principais funções utilizadas nas listas são as citadas abaixo:
### Getters:
- top(): retorna o elemento no topo da queue, é o próximo que vai ser removido no pop;

### Capacidade:
- size(): retorna o tamanho da lista;
- empty(): retorna true se a lista estiver vazio;

### Modificadores:
- push(): adiciona um elemento a fila de prioridade;
- pop(): remove o elemento no topo da fila de prioridade;


## Python - [Heap](https://docs.python.org/3/library/heapq.html)

O python tem filas utilizando a biblioteca _heapq_ que já vem por padrão com o python nas versões mais recentes. (>=3.7)

As funções utilizados no heap são citadas abaixo:


### Modificadores:
 - heappush(): adiciona um elemento ao array heap;
 - heappop(): remove o menor elemento do array heap;
 - heappushpop(): adiciona um elemento ao array heap e remove o menor elemento, é mais eficiente que executar as duas funções em separado;
 - heapify(): transforma um array em um array heap;


Exemplo:
```python
import heapq

arr = [5,17,0,3,7,9]

arr = heapq.heapify(arr)  # transform unsorted array in heapified array

heapq.heappush(arr,6) # add 6 to heap array
heapq.heappush(arr,17) # add 17 to heap array
v1 = heapq.heappop(arr) # return the smallest element from heap array

v2 = heapq.heappushpop(arr,4) # return the smallest elemento and push 4 to heap array

```

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

# Disjoin

É uma estrutura capaz de manter rastreamento de quais 'chaves' pertencem a quais conjuntos em tempo O(1) e fazer a união de conjuntos em tempo O(n) ao menos. É muito útil quando trabalhando com grafos usando o algoritmo Kruskal's e precisa rastrear quais nós percencem a quais conjuntos para evitar criar um ciclo. 

Possue no mínimo duas funções:

- Find(x): qual o conjunto no qual _x_ faz parte?
- Union(x,y): unir o conjunto de _x_ e de _y_ e torna-los um só.


## C++ - [Disjoin](https://www.geeksforgeeks.org/disjoint-set-union-randomized-algorithm/)


O algoritmo abaixo é extremamente eficiente, sendo a busca e a união em O(alpha(n))
```c++
#include <iostream>
#include <vector>
#include <random>
using namespace std;

class DisjointSetUnion {
public:
    // Constructor that initializes the parent and size arrays
    DisjointSetUnion(int n) {
        parent = vector<int>(n);
        // this is the size of height of current three node
        size = vector<int>(n, 1);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }

    public int Find(int x)
    {
       if (parent[x] != x) {
           parent[x] = Find(parent[x]);
       }
       return parent[x];
    }
     
     
    // Merge the sets containing elements x and y
    void unite(int x, int y) {
        int root_x = find(x);
        int root_y = find(y);
        if (root_x == root_y) {
            return;
        }
        // Chose the bigger three to be the root
        cout << size[root_y] << " | " << size[root_x] << endl;
        if(size[root_y] > size[root_x])
            swap(root_x,root_y);
        // increase the three size
        else if(size[root_x] == size[root_y])
            size[root_x]++;

        parent[root_y] = root_x;

    }
     
private:
    vector<int> parent;
    vector<int> size;
};
```



## Python - [Disjoin](https://www.geeksforgeeks.org/disjoint-set-union-randomized-algorithm/)


O algoritmo abaixo é extremamente eficiente, sendo a busca e a união em O(alpha(n))
```python
 
class DisjointSetUnion:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
 
    def find(self, x):
       if self.parent[x] != x:
           self.parent[x] = self.find(self.parent[x])
       return self.parent[x] 

    # This function depends of the find method
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return

        if self.size[root_y] > self.size[root_x]:
            root_x, root_y = root_y, root_x
        elif self.size[root_y] == self.size[root_x]:
            self.size[root_x] += 1
 
        self.parent[root_y] = root_x
```


# Disjoint Sparse Table

Eu realmente não entendi direito. É uma estrutura de segtree porém utiliza operações de bitwise para achar o nó do range correto em $O(1)$ fazer queries executarem em $O(1)$

Build: $O(N log N)$
Query: $O(1)$


### C++

```c++
#define MAXN 1000000
#define MAXPOWN 1048576 // 2^(ceil(log_2(MAXN)))
#define MAXLEV 21       // ceil(log_2(MAXN)) + 1

int arr[MAXPOWN] = {6, 2, 4, 3, 9, 10, 4, 2, 7, 4, 8, 12};
int table[MAXLEV][MAXPOWN];
int maxlev, size;

using namespace std;
void init(int n)
{
    size = n;
    maxlev = __builtin_clz(n) ^ 31; // floor(log_2(n))
    if ((1 << maxlev) != n)
        size = 1 << ++maxlev;
}
inline int compute(int a, int b)
{
    return min(a, b);
    // return max(a,b);
    // return a^b;
    // return a+b;
    // return ((long long)a*b)%SOME_PRIME
}
void build(int level = 0, int l = 0, int r = size)
{
    int m = (l + r) / 2;

    table[level][m] = arr[m];
    for (int i = m - 1; i >= l; i--)
        table[level][i] = compute(table[level][i + 1], arr[i]);

    if (m + 1 < r)
    {
        table[level][m + 1] = arr[m + 1];
        for (int i = m + 2; i < r; i++)
            table[level][i] = compute(table[level][i - 1], arr[i]);
    }

    if (l + 1 != r) // r - l > 1
    {
        build(level + 1, l, m);
        build(level + 1, m, r);
    }
}

int query(int x, int y)
{
    if (x == y)
        return arr[x];
    int k2 = __builtin_clz(x ^ y) ^ 31;
    int lev = maxlev - 1 - k2;
    int ans = table[lev][x];
    if (y & ((1 << k2) - 1)) // y % (1<<k2)
        ans = compute(ans, table[lev][y]);
    return ans;
}

```
Note:

- I assume that size of int is 32 bits
- __builtin_clz() is an inbuilt function in gcc compiler(not in C++ standard) which returns the count of leading zeroes(hence the name)
- 31 - num = 31 ^ num. This this true for any number of the form $2^x-1$.






