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

Em python existe a estrutura de dados _deque_ que é desenvolvida para ter _rápidas_ inserções e remoções para o início e o fim da lista.

Um _deque_ pode ser usado da seguinte forma:

```python
from collections import deque

l = [1,2,3,4]
queue = deque(l) # cria um deque a partir de uma lista
queue.append(7) # adiciona ao final do deque o item 7
queue.appendleft(7) # adiciona ao inicio do deque o item 7
queue.popleft() # remove o primeiro elemento do deque
queue.pop() # remove o ultimo elemento do deque
l = quee
```




