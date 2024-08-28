# Disjoint Sparse Table

Eu realmente não entendi direito. É uma estrutura de segtree porém utiliza operações de bitwise para achar o nó do range correto em $O(1)$ fazer queries executarem em $O(1)$

Build: $O(N log N)$
Query: $O(1)$


### C++

```c++
#define MAXN 1000000
#define MAXPOWN 1048576 // 2^(ceil(log_2(MAXN)))
#define MAXLEV 21       // ceil(log_2(MAXN)) + 1

int arr[MAXPOWN] = {6, 2, 4, 3, 9, 10, 4, 2, 7, 4, 8, 12};
int table[MAXLEV][MAXPOWN];
int maxlev, size;

using namespace std;
void init(int n)
{
    size = n;
    maxlev = __builtin_clz(n) ^ 31; // floor(log_2(n))
    if ((1 << maxlev) != n)
        size = 1 << ++maxlev;
}
inline int compute(int a, int b)
{
    return min(a, b);
    // return max(a,b);
    // return a^b;
    // return a+b;
    // return ((long long)a*b)%SOME_PRIME
}
void build(int level = 0, int l = 0, int r = size)
{
    int m = (l + r) / 2;

    table[level][m] = arr[m];
    for (int i = m - 1; i >= l; i--)
        table[level][i] = compute(table[level][i + 1], arr[i]);

    if (m + 1 < r)
    {
        table[level][m + 1] = arr[m + 1];
        for (int i = m + 2; i < r; i++)
            table[level][i] = compute(table[level][i - 1], arr[i]);
    }

    if (l + 1 != r) // r - l > 1
    {
        build(level + 1, l, m);
        build(level + 1, m, r);
    }
}

int query(int x, int y)
{
    if (x == y)
        return arr[x];
    int k2 = __builtin_clz(x ^ y) ^ 31;
    int lev = maxlev - 1 - k2;
    int ans = table[lev][x];
    if (y & ((1 << k2) - 1)) // y % (1<<k2)
        ans = compute(ans, table[lev][y]);
    return ans;
}

```
Note:

- I assume that size of int is 32 bits
- __builtin_clz() is an inbuilt function in gcc compiler(not in C++ standard) which returns the count of leading zeroes(hence the name)
- 31 - num = 31 ^ num. This this true for any number of the form $2^x-1$.



## Ref

- https://discuss.codechef.com/t/tutorial-disjoint-sparse-table/17404