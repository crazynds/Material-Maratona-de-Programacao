# Material de agendamento de tarefas

## Agendamento em um único computador O(n log n)

O primeiro problema a ser resolvido é em que ordem agendar N trabalhos de forma que o custo da função de penalidade final seja mínimo.

Para casos em que a função é linear, basta ordenar os trabalhos pela razão custo/tempo.

Se a função for exponencial, basta ordenar por (1 - e^a*tempo) / custo

## Agendamento em dois computadores O(n log n)

Esse problema a ser resolvido se resume em que ordem os os trabalhos devem ser ordenados para finalizar no menor tempo possível. Um trabalho só pode ser agendado no segundo computador depois de ser finalizado na primeira.

Esse algoritmo surge a partir da tentativa de minimizar o tempo ocioso do segundo computador. Assim como o problema anterior, a solução para esse é um ordenamento dos trabalhos.

## C++
```cpp
struct Job {
    int a, b, idx;

    bool operator<(Job o) const {
        return min(a, b) < min(o.a, o.b);
    }
};

vector<Job> johnsons_rule(vector<Job> jobs) {
    sort(jobs.begin(), jobs.end());
    vector<Job> a, b;
    for (Job j : jobs) {
        if (j.a < j.b)
            a.push_back(j);
        else
            b.push_back(j);
    }
    a.insert(a.end(), b.rbegin(), b.rend());
    return a;
}

pair<int, int> finish_times(vector<Job> const& jobs) {
    int t1 = 0, t2 = 0;
    for (Job j : jobs) {
        t1 += j.a;
        t2 = max(t2, t1) + j.b;
    }
    return make_pair(t1, t2);
}
```