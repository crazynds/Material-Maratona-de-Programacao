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



