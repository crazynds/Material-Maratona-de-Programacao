# Heap + Dictionarie

Uma estrutura mística nos contos de fadas, que sempre se ouviu falar <s>mas até hoje não foi encontrado uma implementação decente (Não foi procurado muito, mas não deve ser dificil fazer)</s>. Agora com uma implementação quentinha pra você em python.

A ideia é a seguinte, você vai ter a estrutura heap normal, porém você vai manter um dicionario atualizado dizendo qual chave contida no array heap está em qual posição do array heap. Isso é muito bom quando você quer adicionar uma operação de remoção rápida na heap, porém aumenta o custo da inserção (ainda é O(log n) a complexidade) e aumenta o custo do pop já que é necessário manter o dicionário atualizado. 

Alguns casos de usos são no caso de algoritmos como o Dijkstra que quando você acha um caminho mais curto para o nó X, você pode remover qualquer caminho que já vá para aquele nó, economizando memória e ao mesmo tempo se você for inserir um caminho mais longo, ele antes de fazer a inserção já verifica que o caminho é maior do que o que está na heap e nem insere, então isso evita ter uma heap muito grande, e evita diversas inserções e pop's desnecessários.


### Desvantagens:
 - Aumenta o custo da inserção e remoção do item do topo;
 - Código extremamente complexo, e dificil de entender e adaptar;

### Vantagem:
 - Dependendo do algoritmo previne a inserção de valores que nunca vão ser iterados na heap (valores repetidos para os mesmos nós/caminhos);
 - Diminui o consumo de memória da heap;
 - Remove elementos da heap se um novo elemento melhor for adicionado para o mesmo nó/caminho;


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


