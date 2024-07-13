# Binary Trie

Sendo uma variação da trie para binários, no qual é possivel executar algumas operações binárias uteis nessa _trie_ em tempo $O(log(n))$.

Até o momento atual, é documentado que a binary trie consegue fazer as seguintes operações decentemente:
- $Max(valor {\oplus}arr[] )$ - Maior xor de _valor_ com qualquer os items do array (apenas positivos);
- $Min(valor {\oplus}arr[] )$ - Menor xor de _valor_ com qualquer os items do array (apenas positivos);

# Python - Binary Trie

Essa implementação de Trie, ele utiliza um array de nós para criar a árvore, sendo o item 0 o nó raiz.

Cada nó é um  array de 2 posições, o primeiro elemento é o indice do nó com o bit 0 naquela altura, e o segundo é o indice com o bit 1. Se algum dos indices for -1, significa que não exite nó naquela direção.



```python

class BinaryTrie:

    def __init__(self,maxN:int) -> None:
        self.arr = [[-1,-1]]
        self.free = deque()
        self.dict = defaultdict(int)
        # Calculate max height
        self.maxHeight = math.ceil(maxN)

    def add(self,value:int):
        v = 0
        for i in range(self.maxHeight-1,-1,-1):
            idx = (value>>i)&1
            if self.arr[v][idx] == -1:
                if len(self.free) > 0:
                    val = self.free.pop()
                    self.arr[v][idx] = val
                    # reset this position (Optional)
                    self.arr[val][0] = -1
                    self.arr[val][1] = -1
                else:
                    self.arr[v][idx] = len(self.arr)
                    self.arr.append([-1,-1])
            v = self.arr[v][idx]

        self.dict[value] += 1
    
    def remove(self,value:int):
        if value not in self.dict or self.dict[value] == 0:
            return

        self.dict[value] -= 1
        if(self.dict[value] > 0):
            return

        v = 0
        stack = [v]
        for i in range(self.maxHeight-1,-1,-1):
            idx = (value>>i)&1
            v = self.arr[v][idx]
            stack.append(v)
        
        # free myself
        self.free.append(stack.pop())

        for i,v in enumerate(reversed(stack)):
            idx = (value>>i)&1
            if self.arr[v][idx^1] != -1:
                self.arr[v][idx] = -1
                break
            self.arr[v][idx] = -1
            self.free.append(v)
        

    # get max value you can get using xor 
    # O(log(n))
    def getMaxXor(self,value:int):
        v = 0
        for i in range(self.maxHeight-1,-1,-1):
            # get iº bit
            idx = (value>>i)&1
            
            if self.arr[v][idx^1] != -1:
                #invert bit
                idx^=1
            
            value ^= idx << i
            v = self.arr[v][idx]
        return value

    # get min value you can get using xor 
    # O(log(n))
    def getMinXor(self,value:int):
        v = 0
        for i in range(self.maxHeight-1,-1,-1):
            # get iº bit
            idx = (value>>i)&1
            
            if self.arr[v][idx] != -1:
                #invert bit
                idx^=1
            
            value ^= idx << i
            v = self.arr[v][idx]
        return value
```
