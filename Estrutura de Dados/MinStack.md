# Min Stack / Min Queue

Estrutura de dados no qual é possivel inserir itens e remover o primeiro ou o ultimo em média $O(1)$.
Ao mesmo tempo que é possivel consultar o valor mínimo (Ou máximo) em $O(1)$.



### C++

Versão usando stack. Dessa forma é possivel apenas inserir ao final da stack, e remover apenas o ultimo elemento inserido:

```c++
stack<pair<int, int>> st;

void addItem(){
    int new_min = st.empty() ? new_elem : min(new_elem, st.top().second);
    st.push({new_elem, new_min});
}


int removeLast(){
    int removed_element = st.top().first;
    st.pop();
    return removed_element;
}

int min(){
    return st.top().second;
}
```

Usando deque é possivel atingir a forma oposta, removendo o elemento mais antigo inserido, dessa forma é necessário passar qual elementos queremos remover pois o elemento pode já ter sido removido anteriormente.
```c++
deque<int> q;

void addItem(){
    while (!q.empty() && q.back() > new_element)
        q.pop_back();
    q.push_back(new_element);
}


void removeElement(int remove_element){
    if (!q.empty() && q.front() == remove_element)
        q.pop_front();
}

int min(){
    return q.front();
}
```


Abaixo uma forma utiliza stacks para simular uma queue. Resolve o mesmo problema do código proposto acima em tempo $O(1)$

```C++
stack<pair<int, int>> s1, s2;

void addItem(int new_element){
    int minimum = s1.empty() ? new_element : min(new_element, s1.top().second);
    s1.push({new_element, minimum});
}


int removeFirst(){
    if (s2.empty()) {
        while (!s1.empty()) {
            int element = s1.top().first;
            s1.pop();
            int minimum = s2.empty() ? element : min(element, s2.top().second);
            s2.push({element, minimum});
        }
    }
    int remove_element = s2.top().first;
    s2.pop();
    return remove_element;
}

int min(){
    if (s1.empty() || s2.empty()) 
        return s1.empty() ? s2.top().second : s1.top().second;
    else
        return min(s1.top().second, s2.top().second);
}
```