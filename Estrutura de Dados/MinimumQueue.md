# Minimum Queue

Essa estrutura serve para adicionar e remover elementos de um conjunto em tempo constante, e consultar o menor elemento do conjunto em tempo constante.

Para essa estrutura funcionar de maneira correta, cada elementos inserido na stack deve ser removido somente após todos os elementos que já foram inseridos antes tenham sido removidos. Exemplo: insere(A),insere(B),insere(C),remove(A),remove(B),remove(C).

Dessa forma os itens só podem serem removidos na ordem que foram inseridos.

Tempos de inserção, remoção e consulta são em média O(1).

Mais informações pode ser visto [aqui](https://cp-algorithms.com/data_structures/stack_queue_modification.html).


Obs: É possivel adaptar o código para ter a _Maximum Queue_, no qual o valor importante é o máximo.

## C++ - [Minimum Queue](https://cp-algorithms.com/data_structures/stack_queue_modification.html) 


```C++
class MinimiumQueue{
private:
    deque<int> queue;

public:
    int getMin(){
        return queue.front();
    }

    void add(int new_element){
        while(!queue.empty() && queue.back()>new_element){
            queue.pop_back();
        }
        queue.push_back(new_element);
    }

    void rem(int element){
        if (!queue.empty() && queue.front()==element)
            queue.pop_front();
    }
};
```

## Outra Implementação para Minimum Queue

```cpp
struct MinQueue
{
    deque<pair<int, int>> minQueue;
    int contPush = 0;

    void add(int num)
    {
        // se (minQueue.back().first < num), vira maxQueue
        while(!minQueue.empty() && minQueue.back().first > num)
        {
            minQueue.pop_back();
        }

        minQueue.push_back({num, contPush});
        contPush++;
    }

    int getMin(int start = 0)
    {
        while(start > minQueue.front().second)
        {
            minQueue.pop_front();
        }

        return minQueue.front().first;
    }
};
```

Para utilizar, considere que `m` seja o tamanho dos subvetores e `n` o tamanho total do vetor.

```cpp
MinQueue minq;

for(int i = 0; i < m; i++)
{
    minq.add(v[i]);
}

// start = 0
cout << minq.getMin() << endl;

for(int i = 1; i <= v.size() - m; i++)
{
    minq.add(v[i + m - 1]);
       
    // start = i  
    cout << minq.getMin(i) << endl;
}
```

## Exercícios

- [Queries with Fixed Length](https://www.hackerrank.com/challenges/queries-with-fixed-length/problem)
- [Binary Land](https://www.codechef.com/MAY20A/problems/BINLAND)

