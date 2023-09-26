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

## Exercícios

- [Queries with Fixed Length](https://www.hackerrank.com/challenges/queries-with-fixed-length/problem)
- [Binary Land](https://www.codechef.com/MAY20A/problems/BINLAND)

