# Fenwick Tree


Vai procurar vagabundo!

- [link 1](https://cp-algorithms.com/data_structures/fenwick.html)
- [link 2](https://www.geeksforgeeks.org/binary-indexed-tree-or-fenwick-tree-2/)

Parecido com [SegTree](./SegTree.md), porém consome menos espaço e é mais fácil de implementar.


2 Funções importantes

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
    const vector<int> *a;  // binary indexed tree
    int n;

    FenwickTree(vector<int> const &a){
        this->a = &a;
        this->n = a.size();
        bit.assign(this->n, 0);
        for (size_t i = 0; i < this->n; i++)
            update(i, a[i]);
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

        4&5
    }

    void update(int idx, int delta) {
        // OMG - ULTRA FAST WTF?
        for (; idx < n; idx = idx | (idx + 1))
            bit[idx] += delta;
    }
};

```




