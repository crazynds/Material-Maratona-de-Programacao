# Fenwick Tree


Vai procurar vagabundo!

- [link 1](https://cp-algorithms.com/data_structures/fenwick.html)
- [link 2](https://www.geeksforgeeks.org/binary-indexed-tree-or-fenwick-tree-2/)

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


