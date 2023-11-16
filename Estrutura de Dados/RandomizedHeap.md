# Randomized Heap

Essa é a versão da Heap implementada usando nós em uma árvore. A grande vantagem dela é que permite que faça um merge de duas heaps em $log (n)$ mantendo a estrutura da heap. Toda as funções da heap são baseadas nessa função de merge, e todas tem complexidade $log (n)$.

É possivel fazer a remoção de um item que não seja o mínimo da árvore em tempo $log n$, desde que sua posição na árvore seja conhecida. A melhor forma de fazer isso é armazenando uma referencia daquele nó em um dicionário para assim depois conseguir fazer o merge. Provavelmente vai precisar de uma variavel também apontando para o nó pai na árvore. 

### Desvantagens:
 - Não tem como acessar um elemento que não seja o mínimo/máximo.
 - Usa uma arvore ao invéz de um array.

### Vantagem:
 - Garante que a execução sempre vai ser em O(log(n)).
 - Permite dar merge em duas heaps em O(log(n)).


# Python - HeapDictionary

Implementação do HeapDictionary feita por [Crazynds](https://github.com/crazynds)

```python
class RandomizedHeap:
    def __init__(self,value) -> None:
        self.l = None
        self.r = None
        self.value = value
        pass

# Log(n)
def merge(left: RandomizedHeap|None, right: RandomizedHeap|None)->RandomizedHeap:
    if not left or not right:
        return left if left!=None else right
    if right.value < left.value:
        right,left = left,right
    if random.randint(0,1) == 1:
        left.l,left.r = left.r,left.l
    left.l = merge(left.l,right)
    return left

# Log(n)
def min(heap: RandomizedHeap):
    return heap.value

# Log(n)
def removeMin(heap: RandomizedHeap)->RandomizedHeap:
    return merge(heap.l,heap.r)

# Log(n)
def add(heap: RandomizedHeap,val)->RandomizedHeap:
    node = RandomizedHeap(val)
    return merge(heap,node)

```


## Referencias

- [CP-Algorithms](https://cp-algorithms.com/data_structures/randomized_heap.html)