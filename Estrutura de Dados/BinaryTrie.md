# Binary Trie

Sendo uma variação da trie para binários, no qual é possivel executar algumas operações binárias uteis nessa _trie_ em tempo $O(log(n))$.

Até o momento atual, é documentado que a binary trie consegue fazer as seguintes operações decentemente:
- $Max(valor {\oplus}arr[] )$ - Maior xor de _valor_ com qualquer os items do array (apenas positivos);
- $Min(valor {\oplus}arr[] )$ - Menor xor de _valor_ com qualquer os items do array (apenas positivos);

## C++ - Binary Trie

Nesse código estou usando bitset pois precisei de uma binary trie com mais de 64 de altura. Mas é possivel adapta-la para usar inteiros que executam mais rapidamente e não precisa do bitset.

```c++

#DEFINE SIZE 256

class BinarieTrie
{
private:
    vector<pair<ll, ll>> arr;
    unordered_map<bitset<SIZE>, ll> dict;
    ll maxHeight;

public:
    BinarieTrie(int maxN)
    {
        arr.push_back({-1, -1});
        maxHeight = maxN;
    }

    void add(bitset<SIZE> value)
    {
        ll v = 0;
        for (int i = maxHeight - 1; i >= 0; i--)
        {
            ll val = (value.test(i)) ? arr[v].second : arr[v].first;

            if (val == -1)
            {
                val = arr.size();
                if (value.test(i))
                {
                    arr[v].second = val;
                }
                else
                {
                    arr[v].first = val;
                }
                arr.push_back({-1, -1});
            }
            v = val;
        }
        dict[value] += 1;
    }

    void remove(bitset<SIZE> value)
    {
        if (dict[value] == 0)
            return;
        dict[value] -= 1;
        if (dict[value] > 0)
            return;

        ll v = 0;
        vector<ll> stack;
        stack.push_back(v);
        for (int i = maxHeight - 1; i >= 0; i--)
        {
            v = (value.test(i)) ? arr[v].second : arr[v].first;
            stack.push_back(v);
        }
        stack.pop_back();

        for (int i = 0; stack.size() > 0; i++)
        {
            v = stack.back();
            stack.pop_back();
            // get oposite bit
            if (value.test(i))
                arr[v].second = -1;
            else
                arr[v].first = -1;
            ll oposite = (value.test(i)) ? arr[v].first : arr[v].second;
            if (oposite != -1)
            {
                break;
            }
        }
    }

    bitset<SIZE> getMaxXor(bitset<SIZE> value)
    {
        ll v = 0;
        for (int i = maxHeight - 1; i >= 0; i--)
        {
            auto idx = value.test(i);
            auto val = (idx) ? arr[v].second : arr[v].first;
            auto oposite = (idx) ? arr[v].first : arr[v].second;

            if (oposite != -1)
            {
                // invert bit;
                val = oposite;
                idx ^= 1;
            }
            if (idx)
                value.flip(i);

            v = val;
        }
        return value;
    }
};

```

## Python - Binary Trie

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
