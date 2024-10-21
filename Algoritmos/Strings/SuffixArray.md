# Algoritmo para resolver problemas buxa entre strings

O Suffix Array é usado pra resolver problemas de substrings comuns entre strings muito grandes.

Esse código tem basicamente tudo, criação e uso. A busca binária é usada para encontrar de qual sufixo até qual sufixo existe um prefixo comum com a query.

Se a busca binária retornar valores fora dos limites, significa que a query não existe na string.

Esse código ainda faz a junção de múltiplas strings, comum também nos problemas.

```cpp
#include<bits/stdc++.h>
#include<chrono>

using namespace std;
using namespace std::chrono;

typedef pair<int, pair<int, int>> ppi;
typedef vector<pair<int, int>> vpi;
vector<string> words;

vector<int> sort_cyclic_shifts(string const& s) {
    int n = s.size();
    const int alphabet = 256;

    vector<int> p(n), c(n), cnt(max(alphabet, n), 0);
    for (int i = 0; i < n; i++)
        cnt[s[i]]++;
    for (int i = 1; i < alphabet; i++)
        cnt[i] += cnt[i-1];
    for (int i = 0; i < n; i++)
        p[--cnt[s[i]]] = i;
    c[p[0]] = 0;
    int classes = 1;
    for (int i = 1; i < n; i++) {
        if (s[p[i]] != s[p[i-1]])
            classes++;
        c[p[i]] = classes - 1;
    }

    vector<int> pn(n), cn(n);
    for (int h = 0; (1 << h) < n; ++h) {
        for (int i = 0; i < n; i++) {
            pn[i] = p[i] - (1 << h);
            if (pn[i] < 0)
                pn[i] += n;
        }
        fill(cnt.begin(), cnt.begin() + classes, 0);
        for (int i = 0; i < n; i++)
            cnt[c[pn[i]]]++;
        for (int i = 1; i < classes; i++)
            cnt[i] += cnt[i-1];
        for (int i = n-1; i >= 0; i--)
            p[--cnt[c[pn[i]]]] = pn[i];
        cn[p[0]] = 0;
        classes = 1;
        for (int i = 1; i < n; i++) {
            pair<int, int> cur = {c[p[i]], c[(p[i] + (1 << h)) % n]};
            pair<int, int> prev = {c[p[i-1]], c[(p[i-1] + (1 << h)) % n]};
            if (cur != prev)
                ++classes;
            cn[p[i]] = classes - 1;
        }
        c.swap(cn);
    }
    return p;
}

vector<int> suffix_array(string s) {
    s += "$";
    vector<int> sorted_shifts = sort_cyclic_shifts(s);
    sorted_shifts.erase(sorted_shifts.begin());
    return sorted_shifts;
} // Para a string aba resulta em [a, aba, ba]

class Compare
{
    public:
        bool operator()(ppi a, ppi b)
        {
            if (words[a.second.first].substr(a.first) > words[b.second.first].substr(b.first))
                return true;
            return false;
        }
};

vector<pair<int, int>> mergeKArrays(vector<vector<int>> &sas)
{
    vpi output;
    priority_queue<ppi, vector<ppi>, Compare> pq;

    for (int i = 0; i < sas.size(); i++)
        pq.push({ sas[i][0], {i, 0}});

    while (pq.empty() == false)
    {
        ppi curr = pq.top();
        pq.pop();

        int sa = curr.second.first;
        int idx = curr.second.second;

        output.push_back({curr.first, sa});

        if (idx + 1 < sas[sa].size())
            pq.push({ sas[sa][idx + 1], { sa, idx + 1}});
    }

    return output;
}

int binarySearch(string query, vpi &array, int l, int r, bool leftMost)
{
    int length = query.size();
    query += "$";

    bool exists = false;

    while (l <= r)
    {
        int m = (l + r) / 2;

        string middle = words[array[m].second] + "$";
        int lim = min(length, (int) middle.size() - array[m].first + 1);

        int i = 0;
        while (i < lim && query[i] == middle[i + array[m].first])
            i++;
        
        if (i == lim)
        {
            exists = true;
            if (leftMost)
                r = m - 1;
            else
                l = m + 1;
        }
        else if (query[i] < middle[i + array[m].first])
            r = m - 1;
        else
            l = m + 1;
    }

    if (!exists) return -2;
    if (leftMost) return l - 1;
    return r + 1;
}

int main()
{
    int n;

    cin >> n;
    for (int i = 0; i < n; i++)
    {
        string aux;
        cin >> aux;
        words.push_back(aux);
    }

    set<pair<int, pair<string, int>>> ranking;
    for (int i = 0; i < words.size(); i++)
    {
        ranking.insert({(int)words[i].size(), {words[i], i}});
    }
    int wordToRank[20001];
    int rankToWord[20001];

    int position = 0;
    for (auto element : ranking)
    {
        wordToRank[element.second.second] = position;
        rankToWord[position] = element.second.second;
        position++;
    }

    vector<vector<int>> allSA;
    for (string word : words)
        allSA.push_back(suffix_array(word));
    
    vpi sa = mergeKArrays(allSA);
    int q;
    cin >> q;

    for (int i = 0; i < q; i++)
    {
        string query;
        cin >> query;

        int l, r;
        l = binarySearch(query, sa, 0, sa.size() - 1, true);
        if (l == -2)
        {
            cout << -1 << endl;
            continue;
        }
        r = binarySearch(query, sa, l, sa.size() - 1, false);

        l++;
        r--;
        set<int> top10;

        for (int pos = l; pos <= r; pos++)
        {
            int label = sa[pos].second;
            top10.insert(wordToRank[label]);
            if (top10.size() > 10)
                top10.erase(prev(top10.end()));
        }

        int count = 0;
        set<int>::iterator it;
        
        for (it = top10.begin(); count < top10.size() - 1; it++, count++)
            cout << rankToWord[*it] + 1 << " ";
        cout << rankToWord[*it] + 1 << endl;
    }

    return 0;
}```

## LCP

Esse código aqui ele calcula o longest common prefix entre um suffix array e uma sequencia. Geralmente se usa o suffix array criado a partir da sequencia contra a propria sequencia.
```cpp
vector<int> longestCommonPrefix(vector<int> const& s, vector<int> const& p) {
    int n = s.size();
    vector<int> rank(n, 0);
    for (int i = 0; i < n; i++)
        rank[p[i]] = i;

    int k = 0;
    vector<int> lcp(n-1, 0);
    for (int i = 0; i < n; i++) {
        if (rank[i] == n - 1) {
            k = 0;
            continue;
        }
        int j = p[rank[i] + 1];
        while (i + k < n && j + k < n && s[i+k] == s[j+k])
            k++;
        lcp[rank[i]] = k;
        if (k)
            k--;
    }
    return lcp;
}
```


UVa 00719
UVa 00760 *
UVa 01223
UVa 01254
UVa 11107 *
UVa 11512 *
SPOJ 6409
IOI 2008
