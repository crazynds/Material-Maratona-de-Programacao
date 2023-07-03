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


