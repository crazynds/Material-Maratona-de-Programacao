# Strongly connected components

Let  $G=(V,E)$  be a directed graph with vertices  $V$  and edges  $E \subseteq V \times V$ . We denote with $n=|V|$  the number of vertices and with $m=|E|$  the number of edges in $G$ . It is easy to extend all definitions in this article to multigraphs, but we will not focus on that.

A subset of vertices $C \subseteq V$  is called a strongly connected component if the following conditions hold:

- For all $u,v\in C$ , if  $u \neq v$  there exists a path from $u$ to $v$  and a path from $v$  to $u$;
- $C$  is maximal, in the sense that no vertex can be added without violating the above condition;


![](./graph.svg)

![](./cond_graph.svg)

### C++

```c++

vector<bool> visited; // keeps track of which vertices are already visited

void dfs(int v, vector<vector<int>> const& adj, vector<int> &output) {
    visited[v] = true;
    for (auto u : adj[v])
        if (!visited[u])
            dfs(u, adj, output);
    output.push_back(v);
}

// input: adj -- adjacency list of G
// output: components -- the strongy connected components in G
// output: adj_cond -- adjacency list of G^SCC (by root vertices)
void strongy_connected_components(vector<vector<int>> const& adj,
                                  vector<vector<int>> &components,
                                  vector<vector<int>> &adj_cond) {
    int n = adj.size();
    components.clear(), adj_cond.clear();
    vector<int> order; // will be a sorted list of G's vertices by exit time
    visited.assign(n, false);
    // first series of depth first searches
    for (int i = 0; i < n; i++)
        if (!visited[i])
            dfs(i, adj, order);
    // create adjacency list of G^T
    vector<vector<int>> adj_rev(n);
    for (int v = 0; v < n; v++)
        for (int u : adj[v])
            adj_rev[u].push_back(v);
    visited.assign(n, false);
    reverse(order.begin(), order.end());

    vector<int> roots(n, 0); // gives the root vertex of a vertex's SCC
    // second series of depth first searches
    for (auto v : order)
        if (!visited[v]) {
            std::vector<int> component;
            dfs(v, adj_rev, component);
            sort(component.begin(), component.end());
            components.push_back(component);
            int root = component.front();
            for (auto u : component)
                roots[u] = root;
        }
    // add edges to condensation graph
    adj_cond.assign(n, {});
    for (int v = 0; v < n; v++)
        for (auto u : adj[v])
            if (roots[v] != roots[u])
                adj_cond[roots[v]].push_back(roots[u]);
}
```

### Versao do post-order DFS com pilha em vez de recursão
```cpp
void dfs(int v, map<int, set<int>> &connections, vector<int> &output)
{
    stack<int> pilha;
    pilha.push(v);

    while (pilha.size())
    {
        int current = pilha.top();
        if (visited.count(current) != 0 || connections.count(current) == 0)
        {
            visited.insert(current);
            output.push_back(current);
            pilha.pop();
            continue;
        }

        for (auto neighbour : connections[current])
            if (visited.count(neighbour) == 0)
                pilha.push(neighbour);
        visited.insert(current);
    }
}
```

## Ref

- https://cp-algorithms.com/graph/strongly-connected-components.html