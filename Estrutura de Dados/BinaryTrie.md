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
        # Calculate max height
        self.maxHeight = math.ceil(math.log2(maxN))

    def add(self,value:int):
        v = 0
        for i in range(self.maxHeight-1,-1,-1):
            idx = (value>>i)&1
            if self.arr[v][idx] == -1:
                self.arr[v][idx] = len(self.arr)
                self.arr.append([-1,-1])
            v = self.arr[v][idx]

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