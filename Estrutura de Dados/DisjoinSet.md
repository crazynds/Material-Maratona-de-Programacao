# Disjoin

É uma estrutura capaz de manter rastreamento de quais 'chaves' pertencem a quais conjuntos em tempo O(1) e fazer a união de conjuntos em tempo O(n) ao menos. É muito útil quando trabalhando com grafos usando o algoritmo Kruskal's e precisa rastrear quais nós percencem a quais conjuntos para evitar criar um ciclo. 

Possue no mínimo duas funções:

- Find(x): qual o conjunto no qual _x_ faz parte?
- Union(x,y): unir o conjunto de _x_ e de _y_ e torna-los um só.


## C++ - [Disjoin](https://www.geeksforgeeks.org/disjoint-set-union-randomized-algorithm/)


O algoritmo abaixo é extremamente eficiente, sendo a busca e a união em O(alpha(n))
```c++
#include <iostream>
#include <vector>
#include <random>
using namespace std;

class DisjointSetUnion {
public:
    // Constructor that initializes the parent and size arrays
    DisjointSetUnion(int n) {
        parent = vector<int>(n);
        // this is the size of height of current three node
        size = vector<int>(n, 1);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }

    public int Find(int x)
    {
       if (parent[x] != x) {
           parent[x] = Find(parent[x]);
       }
       return parent[x];
    }
     
     
    // Merge the sets containing elements x and y
    void unite(int x, int y) {
        int root_x = find(x);
        int root_y = find(y);
        if (root_x == root_y) {
            return;
        }
        // Chose the bigger three to be the root
        cout << size[root_y] << " | " << size[root_x] << endl;
        if(size[root_y] > size[root_x])
            swap(root_x,root_y);
        // increase the three size
        else if(size[root_x] == size[root_y])
            size[root_x]++;

        parent[root_y] = root_x;

    }
     
private:
    vector<int> parent;
    vector<int> size;
};
```



## Python - [Disjoin](https://www.geeksforgeeks.org/disjoint-set-union-randomized-algorithm/)


O algoritmo abaixo é extremamente eficiente, sendo a busca e a união em O(alpha(n))
```python
import random
 
 
class DisjointSetUnion:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
 
    def find(self, x):
       if self.parent[x] != x:
           self.parent[x] = self.find(self.parent[x])
       return self.parent[x] 

    # This function depends of the find method
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return

        if self.size[root_y] > self.size[root_x]:
            root_x, root_y = root_y, root_x
        elif self.size[root_y] == self.size[root_x]:
            self.size[root_x] += 1
 
        self.parent[root_y] = root_x
```

