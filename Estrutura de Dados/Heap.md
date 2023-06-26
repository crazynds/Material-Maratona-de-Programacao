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





