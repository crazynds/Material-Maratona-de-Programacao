# Estruturas de dados

# Vetores

## C++ - [std::vector](https://cplusplus.com/reference/vector/vector/)

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

# Lista

## C++ - [std::list](https://cplusplus.com/reference/list/list/) 


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

# Double Ended Queue

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

# Hash Map


## C++ - [std::unsorted_map](https://cplusplus.com/reference/unordered_map/unordered_map/)

Vale destacar que a ```std::unsortedmap``` é implementada utilizando um hashmap, o que faz com que sua inserção, busca e remoção seja feito em tempo O(1), enquanto a ```std::map``` utiliza a implementação de uma [árvore binária](./BinaryTree.md) Red-Black, que já se mantém balanceada, então suas operações tem custo O(log n).

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

## C++ - [std::unordered_set](https://cplusplus.com/reference/unordered_set/unordered_set/)

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

# Heap (Arvore binaria em array)

## C++ - [std::priority_queue](https://cplusplus.com/reference/queue/priority_queue/)

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


# Heap + Dictionary

# Python - HeapDictionary

Implementação do HeapDictionary feita por [Crazynds](https://github.com/crazynds)

Ja vou mandar a dica também, em python a biblioteca _heapq_ é otimizada para rodar de forma nativa, já uma implementação manual como a abaixo, a estrutura heap acaba perdendo um pouco de performance. As vezes o desempenho que tu ganha na utilização de um _HeapDictionary_ não compensa por conta da biblioteca _heapq_ rodar de forma nativa.

Mas para linguagens compiladas como __C++__ pode tacar-lhe o pau na implementação, que o boost vai ser imenso. Use como referencia o código em python para fazer a sua implementação.

```python
class HeapDictionary:

    # Execution time: O(N)
    def __init__(self, iterable, key: callable):
        '''
            Iterable is the content you want initialize
            key is the function to extract the key value from the itens
        '''
        self.heap = list(iterable)
        heapq.heapify(self.heap)
        self.dict = {}
        self.extractor = key
        for i,v in enumerate(self.heap):
            key = self.extractor(v)
            if key in self.dict:
                raise Exception('No duplicate keys allowed during class initialization!')
            self.dict[key] = i

    def len(self):
        return len(self.heap)

    # Execution time: O(log N)
    def push(self,item):
        key = self.extractor(item)
        # If item already in the heap and is bigger than the current value, so ignore
        if key in self.dict:
            position = self.dict[key]
            if self.heap[position] <= item:
                return
            self.heap[position] = item
            self.__siftdown(0,position)
        else:
            self.heap.append(item)
            self.__siftdown(0, len(self.heap)-1)

    # Execution time: O(log N)
    def pop(self):
        lastelt = self.heap.pop()
        if self.heap:
            returnitem,self.heap[0] = self.heap[0],lastelt
            self.__update_dict(returnitem,None)
            self.__siftup(0)
            return returnitem
        return lastelt

    # Optional function, faster than push and pop separately
    # Execution time: O(log N)
    def pushpop(self,item):
        key = self.extractor(item)
        # If item already in the heap and is bigger than the current value, so ignore
        if key in self.dict:
            position = self.dict[key]
            if self.heap[position] <= item:
                return
            self.push(item)
            item = self.pop()
        elif self.heap and self.heap[0] < item:
            item, self.heap[0] = self.heap[0], item
            self.__update_dict(item,None)
            self.__siftup(0)
        return item
    
    # Optional function
    # Execution time: O(log N)
    def removebykey(self,key):
        if key not in self.dict:
            return
        position = self.dict[key]
        lastlt = self.heap.pop()
        if self.heap and len(self.heap)!=position:
            self.heap[position] = lastlt
            self.__siftup(position)

        del self.dict[key]
    
    def __update_dict(self,item,pos):
        item = self.extractor(item)
        if pos == None:
            del self.dict[item]
        else:
            self.dict[item] = pos

    def __siftdown(self,start,position):
        newitem = self.heap[position]
        # Follow the path to the root, moving parents down until finding a place
        # newitem fits.
        while position > start:
            parentpos = (position - 1) >> 1
            parent = self.heap[parentpos]
            if not newitem < parent:
                break
            self.heap[position] = parent
            self.__update_dict(parent,position)
            position = parentpos

        self.heap[position] = newitem
        self.__update_dict(newitem,position)

    def __siftup(self,position):
        endpos = len(self.heap)
        startpos = position
        newitem = self.heap[position]
        # Bubble up the smaller child until hitting a leaf.
        childpos = 2*position + 1    # leftmost child position
        while childpos < endpos:
            # Set childpos to index of smaller child.
            rightpos = childpos + 1
            if rightpos < endpos and not self.heap[childpos] < self.heap[rightpos]:
                childpos = rightpos
            # Move the smaller child up.
            self.heap[position] = self.heap[childpos]        
            self.__update_dict(self.heap[position],position)

            position = childpos
            childpos = 2*position + 1
        # The leaf at position is empty now.  Put newitem there, and bubble it up
        # to its final resting place (by sifting its parents down).
        self.heap[position] = newitem
        self.__update_dict(newitem,position)
        self.__siftdown(startpos, position)
```

# Disjoin

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

# AVL Tree

A arvore AVL é uma arvore binária que implementa um algoritmo que mantém a arvore balanceada. Como a arvore se mantém balanceada é ótimo para executar consultas em tempo $log N$.

Inserção: O(log N)  
Remoção: O(log N)  
Espaço: O(N)

Esse tipo de arvore de acordo com o algoritmo as chaves podem ser únicas, ou podem repetir. Nas arvores binárias podem otimizar consultas (min, max, search, etc...) em tempo $log N$ com caches em cada nó.


# Python - AVL Tree

Implementação que permite chaves duplicas.

```python
# Create a tree node
class TreeNode():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

    # Get the height of the node
    def getHeight(self):
        return self.height

    # Get balance factore of the node
    def getBalance(self):
        return (self.left.getHeight() if self.left else 0) - (self.right.getHeight() if self.right else 0)

    def getMinNode(self):
        if not self.left:
            return self
        return self.left.getMinNode()

    def find(self,key):
        if self.key == key:
            return True
        elif self.key > key and self.left:
            return self.left.find(key)
        elif self.key > key and self.right:
            return self.right.find(key)
        return False

        # Function to perform left rotation
    def leftRotate(self):
        y = self.right
        temp = y.left
        y.left = self
        self.right = temp
        self.height = 1 + max(self.left.getHeight() if self.left else 0,
                           self.right.getHeight() if self.right else 0)
        y.height = 1 + max(y.left.getHeight() if y.left else 0,
                           y.right.getHeight() if y.right else 0)
        return y

    # Function to perform right rotation
    def rightRotate(self):
        if not self.left:
            return self
        y = self.left
        temp = y.right
        y.right = self
        self.left = temp
        self.height = 1 + max(self.left.getHeight() if self.left else 0,
                           self.right.getHeight() if self.right else 0)
        y.height = 1 + max(y.left.getHeight() if y.left else 0,
                           y.right.getHeight() if y.right else 0)
        return y

    def insert_node(self, key):

        # Find the correct location and insert the node
        if key < self.key:
            self.left = self.left.insert_node(key) if self.left else TreeNode(key)
        else:
            self.right = self.right.insert_node(key) if self.right else TreeNode(key)

        self.height = 1 + max(self.left.getHeight() if self.left else 0,
                              self.right.getHeight() if self.right else 0)

        # Update the balance factor and balance the tree
        balanceFactor = self.getBalance()
        if balanceFactor > 1:
            if key < self.left.key:
                return self.rightRotate()
            else:
                self.left = self.left.leftRotate()
                return self.rightRotate()

        if balanceFactor < -1:
            if key > self.right.key:
                return self.leftRotate()
            else:
                self.right = self.right.rightRotate()
                return self.leftRotate()

        return self

    # Function to delete a node
    def delete_node(self, key):

        if key < self.key:
            self.left = self.left.delete_node(key) if self.left else None
        elif key > self.key:
            self.right = self.right.delete_node(key) if self.right else None
        else:
            if self.left is None:
                temp = self.right
                self = None
                return temp
            elif self.right is None:
                temp = self.left
                self = None
                return temp
            temp = self.right.getMinNode()
            self.key = temp.key
            self.right = self.right.delete_node(temp.key) if self.right else None
        if self is None:
            return self

        # Update the balance factor of nodes
        self.height = 1 + max(self.left.getHeight() if self.left else 0,
                              self.right.getHeight() if self.right else 0)

        balanceFactor = self.getBalance()

        # Balance the tree
        if balanceFactor > 1:
            if self.left.getBalance() >= 0:
                return self.rightRotate()
            else:
                self.left = self.left.leftRotate() if self.left else None
                return self.rightRotate()
        if balanceFactor < -1:
            if self.right.getBalance() <= 0:
                return self.leftRotate()
            else:
                self.right = self.right.rightRotate() if self.right else None
                return self.leftRotate()
        return self        
    
    def iterate(self,reverse= False):
        if reverse:
            if self.right:
                for key in self.right.iterate(reverse):
                    yield key
            yield self.key
            if self.left:
                for key in self.left.iterate(reverse):
                    yield key
        else:
            if self.left:
                for key in self.left.iterate(reverse):
                    yield key
            yield self.key
            if self.right:
                for key in self.right.iterate(reverse):
                    yield key
    
    def __str__(self):
        return str(self.key)



class AVLTree(object):

    def __init__(self) -> None:
        self.root = None
        self.size = 0
        self.min = None
        self.max = None
        pass

    def insert(self,value):
        self.size += 1
        self.min = min(self.min if self.min else float('inf'),value)
        self.max = max(self.max if self.max else float('-inf'),value)
        if not self.root:
            self.root = TreeNode(value)
        else:
            self.root = self.root.insert_node(value)

    def find(self,value):
        if not self.root:
            return False
        return self.root.find(value)

    def delete(self,value):
        if not self.root:
            return None
        if self.root.find(value):
            self.root = self.root.delete_node(value)
            self.size-=1
            if value == self.min:
                self.min = next(self.root.iterate()) if self.root else None
            if value == self.max:
                self.max = next(self.root.iterate(reverse=True)) if self.root else None
    
    def empty(self):
        return self.size==0

    def iterate(self,reverse= False):
        if not self.root:
            return range(0)
        return self.root.iterate(reverse)

```

# Arvore Segmentada

2 Funções importantes

- Query: realiza a consulta (Operação, calculo, etc...) a partir de um range de valor dado (inicial e final);
- Update: faz a troca de um valor de uma posição;

Build: O(N)
Atualização: O(log N)
Consulta: O(log N)
Espaço: O(4N)


# C - [SegTree](https://cp-algorithms.com/data_structures/segment_tree.html)

Versão mais simples de segtree.
Resolve atualização de valores e consultas da soma de um range de valores.

```C
int t[4*MAXN];

void build(int a[], int v, int tl, int tr) {
    if (tl == tr) {
        t[v] = a[tl];
    } else {
        int tm = (tl + tr) / 2;
        build(a, v*2, tl, tm);
        build(a, v*2+1, tm+1, tr);
        // the line above you execute your process
        t[v] = t[v*2] + t[v*2+1];
    }
}
int sum(int v, int tl, int tr, int l, int r) {
    if (l > r) // the default value for empty 
        return 0;
    if (l == tl && r == tr) {
        return t[v];
    }
    int tm = (tl + tr) / 2;
    // the line above you execute your process
    return sum(v*2, tl, tm, l, min(r, tm))
           + sum(v*2+1, tm+1, tr, max(l, tm+1), r);
}
void update(int v, int tl, int tr, int pos, int new_val) {
    if (tl == tr) {
        t[v] = new_val;
    } else {
        int tm = (tl + tr) / 2;
        if (pos <= tm)
            update(v*2, tl, tm, pos, new_val);
        else
            update(v*2+1, tm+1, tr, pos, new_val);
        // the line above you execute your process
        t[v] = t[v*2] + t[v*2+1];
    }
}

```


# C++ - SegTree

Variação da SegTree de C usando classes e feita por [Crazynds](https://github.com/crazynds)

```C++
template <typename T>
class SegTree{
private:
    int size;

    T *t;

    void __build(T a[], int v, int tl, int tr) {
        if (tl == tr) {
            t[v] = a[tl];
        } else {
            int tm = (tl + tr) / 2;
            __build(a, v*2, tl, tm);
            __build(a, v*2+1, tm+1, tr);
            // the line above you execute your process
            t[v] = t[v*2] + t[v*2+1];
        }
    }
    T __query(int v, int tl, int tr, int l, int r) {
        if (l > r) // Change here the default value for empty
            return 0;
        if (l == tl && r == tr) {
            return t[v];
        }
        int tm = (tl + tr) / 2;
        int v1 = __query(v*2, tl, tm, l, std::min(r, tm));
        int v2 = __query(v*2+1, tm+1, tr, std::max(l, tm+1), r);
        // the line above you execute your process
        return v1+v2;
    }
    void __update(int v, int tl, int tr, int pos, T new_val) {
        if (tl == tr) {
            t[v] = new_val;
        } else {
            int tm = (tl + tr) / 2;
            if (pos <= tm)
                __update(v*2, tl, tm, pos, new_val);
            else
                __update(v*2+1, tm+1, tr, pos, new_val);
            // the line above you execute your process
            t[v] = t[v*2] + t[v*2+1];
        }
    }

public:
    SegTree(T a[], int size){
        this->t = new T[size*4+1];
        this->size = size;
        __build(a,1,0,size-1);
    }
    ~SegTree(){
        delete[] this->t;
    }
    
    T query(int l, int r) {
        return this->__query(1,0,this->size-1,l,r);
    }
        
    void update(int pos, int new_val) {
        this->__update(1,0,this->size-1,pos,new_val);
    }
};
```


# Python - SegTree

Variação da SegTree de C usando classes e feita por [Crazynds](https://github.com/crazynds)

Em python usualmente é mais bem mais lento que C++, se der timelimit, tente usar o código de C++ que pode ser que passe.


```python
class SegTree:

    def __init__(self,arr,start,end) -> None:
        self.t = [0 for _ in range(len(arr)*4+1)]
        self.left = 0
        self.right = len(arr)-1
        self.vertex_start = 1
        self.__build(arr,self.vertex_start,self.left,self.right)
        pass
            
    def __build(self,arr,vertex,left,right):
        if left == right:
            self.t[vertex] = arr[left]
        else:
            middle = (left+right) // 2
            self.__build(arr,vertex*2,left,middle)
            self.__build(arr,vertex*2+1,middle+1,right)
            # the line above you execute your process
            self.t[vertex] = self.t[vertex*2] + self.t[vertex*2+1]
        
    def query(self,left_query,right_query):
        return self.__query(self.vertex_start,self.left,self.right,left_query,right_query)
    def __query(self,vertex,left,right,left_query,right_query):
        if left_query>right_query: # Change here the default value for empty
            return 0
        if left_query==left and right_query == right:
            return self.t[vertex]
        
        middle = (left+right)//2
        l_val = self.__query(vertex*2,left,middle,left_query,min(right_query,middle))
        r_val = self.__query(vertex*2+1,middle+1,right,max(middle+1,left_query),right_query)
        # the line above you execute your process
        return  l_val + r_val

    def update(self, pos, val):
        return self.__update(self.vertex_start,self.left,self.right,pos,val)
    def __update(self,vertex,left, right, pos, val):
        if left == right:
            self.t[vertex] = val
        else:
            middle = (left+right)//2
            if pos <= middle:
                self.__update(vertex*2,left,middle,pos,val)
            else:
                self.__update(vertex*2+1,middle+1,right,pos,val)
            # the line above you execute your process
            self.t[vertex] = self.t[vertex*2] + self.t[vertex*2+1]
```

# BizarreTree

É uma criação minha que implementa as funcionalidades de uma arvore sem uma árvore.

Isso é util em python que não tem uma implementação nativa, e implementar uma árvore manualmente pode ser muito demorado além dela ser extremamente lenta na execução. Tem também o problema de balanceamento que deve se levar em conta dependendo do problema.

A _BizarreTree_ não é uma árvore de fato, ela utiliza um _dictionary_ e duas _heap_ para simular as funções principais de uma árvore, podendo assim pegar o menor valor, o maior e iterar sobre ela de maneira crescente e decrescente.

Os custos das operações seguem abaixo:

 - Inserção: O(log n) _heap push_
 - Remoção: O(1) _dictionary acess_
 - Find: O(1) _dictionary acess_
 - Min: O(k log n) k* _heap pop_
 - Max: O(k log n) k* _heap pop_
 - Iterate: O(n log n + (n + k)) _sort_ + (_valid values_ + _deleted value_)

Para k sendo a quantidade de elementos que foram removidos da árvore entre as chamadas de _min_ e _max_.

- [Crazynds](https://github.com/crazynds)

## Python

Como eu fiz ela especialmente para resolver as funções de árvores em python, só faz sentido a implementação em python. Mas é possivel adaptar em qualquer outra linguagem. 

```python
import heapq
from collections import defaultdict

class BizarreTree:

    def __init__(self) -> None:
        self.minArr = []
        self.maxArr = []
        self.size = 0
        self.data = defaultdict(int)
        pass

    def find(self,val):
        return self.data[val] > 0

    def insert(self,val):
        self.data[val] += 1
        self.size += 1
        heapq.heappush(self.minArr,val)
        heapq.heappush(self.maxArr,-val)

    def delete(self,val):
        if self.data[val] > 0:
            self.size -= 1
            self.data[val] -= 1
    
    def min(self):
        while self.data[self.minArr[0]] == 0:
            heapq.heappop(self.minArr)
        return self.minArr[0]

    def max(self):
        while self.data[-self.maxArr[0]] == 0:
            heapq.heappop(self.maxArr)
        return -self.maxArr[0]

    def iterate(self,reverse = False):
        # https://stackoverflow.com/questions/59903948/how-to-iterate-heapq-without-losing-data
        if not reverse:
            self.minArr.sort()  # using heap structure makes sort faster
            # sorted array is also a valid heap
            it = self.minArr
        else:
            self.maxArr.sort()
            it = map(lambda a: -a,self.maxArr)
        cont = 0
        lastI = 0
        for i in self.minArr:
            cont = (cont+1) if i == lastI else 1
            if self.data[i] >= cont:
                yield i

```


# Fenwick Tree

Parecido com [SegTree](./SegTree.md), porém consome menos espaço e é mais fácil de implementar.


Funções importantes

- Query: realiza a consulta (Operação, calculo, etc...) a partir de um range de valor dado (inicial e final);
- Update: faz a troca de um valor de uma posição;

  Build: O(N)  
Atualização: O(log N)  
Consulta: O(log N)  
Espaço: O(N)  



# C++ - [Fenwick Tree](https://cp-algorithms.com/data_structures/fenwick.html#finding-sum-in-one-dimensional-array)

Versão mais simples de Fenwick Tree.
Resolve atualização de valores e consultas da soma dos valores de range de valores.

```C++
struct FenwickTree {
    vector<int> bit;  // binary indexed tree
    vector<int> currentArray;  // array
    int n;

    FenwickTree(vector<int> const &a){
        this->n = a.size();
        currentArray.assign(this->n, 0);
        bit.assign(this->n, 0);
        for (size_t i = 0; i < this->n; i++)
            this->update(i, a[i]);
    }

    
    // make f(a[l..r]) = f(a[0..r]) - f(a[0..l-1])
    int query(int l, int r) {
        return query(r) - v(l - 1);
    }

    // make f(a[0..r])
    int query(int r) {
        int ret = 0;
        // OMG - ULTRA FAST WTF?
        for (; r >= 0; r = (r & (r + 1)) - 1)
            ret += bit[r];
        return ret;
    }

    void update(int idx, int newVal) {
        int delta = newVal - this->currentArray[idx];
        this->currentArray[idx] = newVal;
        // OMG - ULTRA FAST WTF?
        for (; idx < n; idx = idx | (idx + 1))
            bit[idx] += delta;
    }
};

```

# Python - [FenwickTree](#)

Adaptação feita por [Crazynds](https://github.com/crazynds)

```python
class FenwickTree:
    def __init__(self,arr: list) -> None:
        self.n = len(arr)
        self.original_arr = [0]*self.n
        self.bit = [0]*self.n
        for i in range(self.n):
            self.update(i,arr[i])
        pass

    def update(self,idx, newVal):
        delta = newVal - self.original_arr[idx]
        self.original_arr[idx] = newVal
        # OMG - ULTRA FAST WTF?
        while idx < self.n:
            self.bit[idx] += delta
            idx |= (idx + 1)
    
    # make f(a[0..r])
    def query_zero(self,r):
        ret = 0
        # OMG - ULTRA FAST WTF?
        while r>=0:
            ret += self.bit[r]
            r = (r & (r + 1)) - 1
        return ret
    
    # make f(a[l..r]) = f(a[0..r]) - f(a[0..l-1])
    def query(self,l, r):
        return self.query_zero(r) - self.query_zero(l - 1)
```




# Arvores em C++


# C++ - [std::set](https://cplusplus.com/reference/set/set/) [std::multiset](https://cplusplus.com/reference/set/multiset/)


A única diferença entre o set e o multiset é que no caso do multiset ele permite a inserção de valores duplicados, que no caso do set se um valor já existir ele não cria uma nova entrada. 
Para o multiset, deve-se incluir a mesma biblioteca ```#include <set>```.



# C++ - [std::map](https://cplusplus.com/reference/map/map/)

Em C++ existe a implementação de árvore binária na biblioteca padrão. A estrutura de dados ```std::map``` por padrão implementa uma árvore binária Red-Black, que já traz uma estrutura de balanceamento da árvore. Geralmente a ```std::map``` já implementa a versão mais omitizada de uma árvore binária. 

### Associativo
Elementos em contêineres associativos são referenciados por sua chave e não por sua posição absoluta no contêiner.
### Ordenado
Os elementos no contêiner seguem uma ordem estrita o tempo todo. Todos os elementos inseridos recebem uma posição nesta ordem.
### Tuplas
Cada elemento associa uma chave a um valor mapeado: As chaves servem para identificar os elementos cujo conteúdo principal é o valor mapeado.
### Chaves únicas
Dois elementos no contêiner não podem ter chaves equivalentes.
### Memória auto gerenciada
O contêiner usa um objeto alocador para lidar dinamicamente com suas necessidades de armazenamento.

As principais funções utilizadas no map são as citadas abaixo:

### Iteração:
- begin(): retorna um iterador a partir do inicio do vetor; 
- end(): retorna um iterador a partir do fim do vetor (não pega a ultima casa);
- rbegin(): retorna um iterador _reverso_ a partir do fim do vetor; 
- rend(): retorna um iterador _reverso_ a partir do inicido do vetor (não pega a primeira casa);

### Getters:
- operator[]: retorna o elemento da _chave_ indicada dentro do operator. Caso seja uma chave que não existe é inserido um novo item com o construtor padrão (para números geralmente é zero) e retornado uma referencia desse item;
- find(): retorna um iterador a partir desse elemento, caso não encontre retorna o map.end();
- lower_bound(K): retorna um iterator para o maior elemento que é menor que K;
- upper_bound(K): retorna um iterator para o menor elemento que é maior que K;

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


Exemplo de uso do std::map

```C++
// map::lower_bound/upper_bound
#include <iostream>
#include <map>

int main ()
{
  std::map<char,int> mymap;
  std::map<char,int>::iterator itlow,itup;

  mymap['a']=20;
  mymap['b']=40;
  mymap['c']=60;
  mymap['d']=80;
  mymap['e']=100;

  itlow=mymap.lower_bound ('b');  // itlow points to b
  itup=mymap.upper_bound ('d');   // itup points to e (not d!)

  mymap.erase(itlow,itup);        // erases [itlow,itup)

  // print content:
  for (std::map<char,int>::iterator it=mymap.begin(); it!=mymap.end(); ++it)
    std::cout << it->first << " => " << it->second << '\n';

  return 0;
}
```

