# Arvore Segmentada

Vai procurar vagabundo!

- [link 1](https://cp-algorithms.com/data_structures/segment_tree.html)
- [link 2](https://www.youtube.com/watch?v=CN0N1ddJ9hA&ab_channel=GauravSen)
- [link 3](https://www.geeksforgeeks.org/segment-tree-data-structure/)


2 Funções importantes

- Query: realiza a consulta (Operação, calculo, etc...) a partir de um range de valor dado (inicial e final);
- Update: faz a troca de um valor de uma posição;

Build: O(N)
Atualização: O(log N)
Consulta: O(log N)
Espaço: O(4N)


# C - [SegTree](https://cp-algorithms.com/data_structures/segment_tree.html)

Versão mais simples de segtree.
Resolve atualização de valores e consultas da soma de um range de valores.

```C
int t[4*MAXN];

void build(int a[], int v, int tl, int tr) {
    if (tl == tr) {
        t[v] = a[tl];
    } else {
        int tm = (tl + tr) / 2;
        build(a, v*2, tl, tm);
        build(a, v*2+1, tm+1, tr);
        // the line above you execute your process
        t[v] = t[v*2] + t[v*2+1];
    }
}
int sum(int v, int tl, int tr, int l, int r) {
    if (l > r) // the default value for empty 
        return 0;
    if (l == tl && r == tr) {
        return t[v];
    }
    int tm = (tl + tr) / 2;
    // the line above you execute your process
    return sum(v*2, tl, tm, l, min(r, tm))
           + sum(v*2+1, tm+1, tr, max(l, tm+1), r);
}
void update(int v, int tl, int tr, int pos, int new_val) {
    if (tl == tr) {
        t[v] = new_val;
    } else {
        int tm = (tl + tr) / 2;
        if (pos <= tm)
            update(v*2, tl, tm, pos, new_val);
        else
            update(v*2+1, tm+1, tr, pos, new_val);
        // the line above you execute your process
        t[v] = t[v*2] + t[v*2+1];
    }
}

```

Versão do brizi para um problema usando seg tree.

```c
void update_tree(bool *tree, int requested_left_range, int requested_right_range, int min_node, int max_node, int current_node, int winner)
{
    if (tree[current_node])
    {
        return;
    }


    if (min_node == max_node)
    {       
        if (min_node != winner)
        {
            tree[current_node] = true;
            all_fighters[min_node] = winner;
        }
        return;
    }

    int middle = (min_node+max_node)/2;

    if (requested_left_range <= middle)
    {
        update_tree(tree, requested_left_range, requested_right_range, min_node, middle, current_node*2, winner);
    }

    if (requested_right_range > middle)
    {
        update_tree(tree, requested_left_range, requested_right_range, middle+1, max_node, current_node*2+1, winner);
    }

    tree[current_node] = tree[current_node*2] && tree[current_node*2+1];

}
```



# C++ - SegTree

Variação da SegTree de C usando classes e feita por [Crazynds](https://github.com/crazynds)

```C++
template <typename T>
class SegTree{
private:
    int size;

    T *t;

    void __build(T a[], int v, int tl, int tr) {
        if (tl == tr) {
            t[v] = a[tl];
        } else {
            int tm = (tl + tr) / 2;
            __build(a, v*2, tl, tm);
            __build(a, v*2+1, tm+1, tr);
            // the line above you execute your process
            t[v] = t[v*2] + t[v*2+1];
        }
    }
    T __query(int v, int tl, int tr, int l, int r) {
        if (l > r) // Change here the default value for empty
            return 0;
        if (l == tl && r == tr) {
            return t[v];
        }
        int tm = (tl + tr) / 2;
        int v1 = __query(v*2, tl, tm, l, std::min(r, tm));
        int v2 = __query(v*2+1, tm+1, tr, std::max(l, tm+1), r);
        // the line above you execute your process
        return v1+v2;
    }
    void __update(int v, int tl, int tr, int pos, T new_val) {
        if (tl == tr) {
            t[v] = new_val;
        } else {
            int tm = (tl + tr) / 2;
            if (pos <= tm)
                __update(v*2, tl, tm, pos, new_val);
            else
                __update(v*2+1, tm+1, tr, pos, new_val);
            // the line above you execute your process
            t[v] = t[v*2] + t[v*2+1];
        }
    }

public:
    SegTree(T a[], int size){
        this->t = new T[size*4+1];
        this->size = size;
        __build(a,1,0,size-1);
    }
    ~SegTree(){
        delete[] this->t;
    }
    
    T query(int l, int r) {
        return this->__query(1,0,this->size-1,l,r);
    }
        
    void update(int pos, int new_val) {
        this->__update(1,0,this->size-1,pos,new_val);
    }
};
```

Outra variação de SegTree que possibilita incrementar um range de valores:
```c++

class SegmentTree
{
private:
    int n;
    int *t;

    void build(int v, int tl, int tr)
    {   
        // Note que aqui estou inicializando com zero
        // É uma variação para a construção da segtree
        t[v] = 0;
        if (tl != tr)
        {
            int tm = (tl + tr) / 2;
            build(v * 2, tl, tm);
            build(v * 2 + 1, tm + 1, tr);
        }
    }

    void update(int v, int tl, int tr, int l, int r, int add)
    {
        if (tl > tr)
            return;
        if (l > r)
            return;
        // No update, como estou incrementando um range l,r se o nó
        // contempla o range inteiro, eu incremento o nó
        if (l == tl && r == tr)
        {
            t[v] += add;
        }
        else
        {
            int tm = (tl + tr) / 2;
            update(v * 2, tl, tm, l, min(r, tm), add);
            update(v * 2 + 1, tm + 1, tr, max(l, tm + 1), r, add);
        }
    }

    // A query que eu tenho é para verificar quantos casas o valor é maior que zero
    int count(int v, int tl, int tr)
    {
        
        if (tl > tr)
            return 0;
        int resp;
        if (t[v] > 0)
            resp = tr - tl + 1;
        else
        {
            if (tl == tr)
                resp = 0;
            else
            {
                int tm = (tl + tr) / 2;
                resp = count(v * 2, tl, tm) + count(v * 2 + 1, tm + 1, tr);
            }
        }
        return resp;
    }

public:
    SegmentTree(int n)
    {
        t = new int[4 * n];
        this->n = n;
        build(1, 0, n - 1);
        memset(t, 0, sizeof(t) * 4 * n);
    }

    ~SegmentTree()
    {
        delete[] t;
    }
};


```

Essa SegTree passada é muito boa para incrementar e decrementar ranges de valores dentro de um array, e contar quantos valores são maiores que zero. Isso pode ser usado para após vários ranges saber quantos espaços vazios ou ocupados existem, mesmo que esse problema seja resolvivel em O(n), mas com a segtree te possibilita realizar alterações nesses ranges, como inserir novos ranges para computar as contagens ou remover novos ranges.



# Python - SegTree

Variação da SegTree de C usando classes e feita por [Crazynds](https://github.com/crazynds)

Em python usualmente é mais bem mais lento que C++, se der timelimit, tente usar o código de C++ que pode ser que passe.


```python
class SegTree:

    def __init__(self,arr) -> None:
        self.t = [0 for _ in range(len(arr)*4+1)]
        self.left = 0
        self.right = len(arr)-1
        self.vertex_start = 1
        self.__build(arr,self.vertex_start,self.left,self.right)
        pass
            
    def __build(self,arr,vertex,left,right):
        if left == right:
            self.t[vertex] = arr[left]
        else:
            middle = (left+right) // 2
            self.__build(arr,vertex*2,left,middle)
            self.__build(arr,vertex*2+1,middle+1,right)
            # the line above you execute your process
            self.t[vertex] = self.t[vertex*2] + self.t[vertex*2+1]
        
    def query(self,left_query,right_query):
        return self.__query(self.vertex_start,self.left,self.right,left_query,right_query)
    def __query(self,vertex,left,right,left_query,right_query):
        if left_query>right_query: # Change here the default value for empty
            return 0
        if left_query==left and right_query == right:
            return self.t[vertex]
        
        middle = (left+right)//2
        l_val = self.__query(vertex*2,left,middle,left_query,min(right_query,middle))
        r_val = self.__query(vertex*2+1,middle+1,right,max(middle+1,left_query),right_query)
        # the line above you execute your process
        return  l_val + r_val

    def update(self, pos, val):
        return self.__update(self.vertex_start,self.left,self.right,pos,val)
    def __update(self,vertex,left, right, pos, val):
        if left == right:
            self.t[vertex] = val
        else:
            middle = (left+right)//2
            if pos <= middle:
                self.__update(vertex*2,left,middle,pos,val)
            else:
                self.__update(vertex*2+1,middle+1,right,pos,val)
            # the line above you execute your process
            self.t[vertex] = self.t[vertex*2] + self.t[vertex*2+1]
```

