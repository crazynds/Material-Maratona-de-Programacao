# Vetores

Vetores são estruturas de dados muito legais em qualquer linguagem. Basicamente permite armazenar uma quantidade prédeterminada, ou indeterminada, de elementos e é possivel organiza-los dentro do vetor da forma que quiser.

Cada casa de um vetor geralmente é referenciada por um inteiro, indentificando a posição que determinado valor foi salvo. Dependendo da linguagem é possivel também possuir um vetor não continuo, ou seja, pode possuir a casa N mas não necessáriamente possue todas as casas de 0 a N, ou vetores no qual a chave da casa pode ser uma string ou até outro referenciador, sendo mais comum nesses casos serem chamados de _dictionary_.


## C++ - [std::vector](https://cplusplus.com/reference/vector/vector/)

### Sequência
Os elementos em contêineres de sequência são ordenados em uma sequência linear estrita. Elementos individuais são acessados por sua posição nesta sequência.
### Vetor dinâmico
Permite acesso direto a qualquer elemento na sequência, mesmo por meio de aritmética de ponteiro, e fornece adição/remoção relativamente rápida de elementos no final da sequência.
### Dinamicamente Alocado
O contêiner usa um objeto alocador para lidar dinamicamente com suas necessidades de armazenamento.

As principais funções utilizadas na stack são as citadas abaixo:

### Iteração
- begin(): retorna um iterador a partir do inicio do vetor; 
- end(): retorna um iterador a partir do fim do vetor (não pega a ultima casa);
- rbegin(): retorna um iterador _reverso_ a partir do fim do vetor; 
- rend(): retorna um iterador _reverso_ a partir do inicido do vetor (não pega a primeira casa);

### Getters:
- operator[]: retorna o elemento da casa indicada dentro do operator. Caso seja uma posição maior que a quantidade de itens então causa um _comportamento não definido_;
- front(): retorna o primeiro elemento;
- back(): retorna o ultimo elemento;

### Capacidade:
- size(): retorna o tamanho do vetor;
- empty(): retorna true se o vetor estiver vazio;
- capacity(): retorna o tamanho alocado atualmente para esse vetor;
- reserve(): reseva o tamanho informado para esse vetor;

### Modificadores:
- push_back(): adiciona um elemento ao final do vetor;
- pop_back(): remove um elemento ao final do vetor;
- insert(): existem algumas versões para o insert, sendo elas:
 - insert(iterator pos, val): a partir da posição, insere o item val;
 - insert(iterator pos, start, end): a partir da posição, insere o array que começa em start e termina em end;
- erase(): apaga um elemento na posição passada, note que para remover o elemento da posição 4 deve-se chamar a função begin() e somar a 4;

```C++
#include <vector> 

vector<int> *x = new vector<int> (3, 25); //x = (25, 25, 25)
vector<int> y (5,0); // y = (0, 0, 0, 0, 0)
*x = y; // x = (0, 0, 0, 0, 0)

int s[3] = {100, 231, 213};
y.assign(s, s+3); // x = (0, 0, 0, 0, 0) e y = (100, 231, 213)

y.insert(y.begin(), s, s+3); // y = (100, 231, 213, 100, 231, 213)
y.erase(y.begin(), y.begin() + 2); // y = (213, 100, 231, 213)

y.at(1); // == y[1] e assim por diante

vector<int>::iterator it;
for(it = y.begin(); it != y.end(); it++)
cout << *it << endl;  
```

# Pilha

Pilha, ou também chamada de stack, é uma estrutura de dados que se baseaia no príncipio LIFO (_LAST IN FIRST OUT_).

Pilhas são fundamentalmente compostas por duas operações: push (empilhar) que adiciona um elemento no topo da pilha e pop (desempilhar) que remove o último elemento adicionado.


## C++ - [std::stack](https://cplusplus.com/reference/stack/stack/) 

Declaração da stack:
```C++
#include <stack>          // std::stack

int main ()
{
  std::stack<int> first;                    // empty stack
}
```
As principais funções utilizadas na stack são as citadas abaixo:
- empty(): testa se a stack está vazia;
- size(): retorna o tamanho da stack;
- push(T): insere no topo da pilha o item T;
- pop(): remove o elemento do topo da pilha, destaque que ele **não retorna** esse elemento, ele apenas remove;
- top(): retorna o elemento do topo da pilha, sem remove-lo;

Abaixo um exemplo de utilização da stack:

```C++
// stack::push/pop
#include <iostream>       // std::cout
#include <stack>          // std::stack

int main ()
{
  std::stack<int> mystack;
  for (int i=0; i<5; ++i) mystack.push(i);
  std::cout << "Popping out elements...";
  while (!mystack.empty())
  {
     std::cout << ' ' << mystack.top();
     mystack.pop();
  }
  std::cout << '\n';

  return 0;
}
```

# Lista

Listas são contêineres de sequência que permitem operações de inserção e apagamento de tempo constante em qualquer lugar dentro da sequência e iteração em ambas as direções.

Os contêineres de lista são implementados como listas duplamente vinculadas; As listas duplamente vinculadas podem armazenar cada um dos elementos que contêm em locais de armazenamento diferentes e não relacionados. A ordenação é mantida internamente pela associação a cada elemento de um link para o elemento que o precede e um link para o elemento que o segue.


## C++ - [std::list](https://cplusplus.com/reference/list/list/) 

### Sequência
Os elementos em contêineres de sequência são ordenados em uma sequência linear estrita. Elementos individuais são acessados por sua posição nesta sequência.
### Lista duplamente ligada
Cada elemento guarda informações sobre como localizar o próximo e os anteriores, permitindo operações de inserção e apagamento em tempo constante antes ou depois de um elemento específico (mesmo de faixas inteiras), mas sem acesso aleatório direto.
### Dinamicamente Alocado
O contêiner usa um objeto alocador para lidar dinamicamente com suas necessidades de armazenamento


As principais funções utilizadas nas listas são as citadas abaixo:
### Iteração
- begin(): retorna um iterador a partir do inicio da lista; 
- end(): retorna um iterador a partir do fim da lista (não pega a ultima casa);
- rbegin(): retorna um iterador _reverso_ a partir do fim da lista; 
- rend(): retorna um iterador _reverso_ a partir do inicido da lista (não pega a primeira casa);

### Getters:
- front(): retorna o primeiro elemento;
- back(): retorna o ultimo elemento;

### Capacidade:
- size(): retorna o tamanho da lista;
- empty(): retorna true se a lista estiver vazio;

### Modificadores:
- push_back(): adiciona um elemento ao final da lista;
- pop_back(): remove um elemento do final da lista;
- push_front(): adiciona um elemento ao inicio da lista;
- pop_front()): remove um elemento do inicio da lista;
- insert(): existem algumas versões para o insert, sendo elas:
 - insert(iterator pos, val): a partir da posição, insere o item val;
 - insert(iterator pos, start, end): a partir da posição, insere o array que começa em start e termina em end;
- erase(): apaga um elemento na posição passada, note que para remover o elemento da posição 4 deve-se chamar a função begin() e somar a 4;

### Operadores:
- sort(): Ordena os elementos da lista, é possivel passar uma função para fazer a comparação;
- merge(): Junta duas listas ordenadas, a lista final vai estar ordenada;
- remove(): Remove todos os elementos que possuem o mesmo valor passado no parametro;
- remove_if(): Remove todos os elementos que passam na condição. O parametro é uma função que é aplicada em todos os elementos, e deve retornar true ou false, sendo true para remover e false para manter na lista;



# Map

A estrutura de dados map, conhecida em algumas linguagens como dicionário tem como objetivo armazenar de forma ordenada duplas de dados, sendo uma a chave e outra um valor. É um tipo de array associativo. 

Os dados são armazenados seguindo uma ordem das chaves, e o valor não influencia nessa ordem. 

Cada chave é única e ao definir outro valor para uma mesma chave, o comportamento esperado é que o novo valor deve sobrescrever o antigo.




## Map - [std::map](https://cplusplus.com/reference/map/map/)

### Associativo
Elementos em contêineres associativos são referenciados por sua chave e não por sua posição absoluta no contêiner.
### Ordenado
Os elementos no contêiner seguem uma ordem estrita o tempo todo. Todos os elementos inseridos recebem uma posição nesta ordem.
### Tuplas
Cada elemento associa uma chave a um valor mapeado: As chaves servem para identificar os elementos cujo conteúdo principal é o valor mapeado.
### Chaves únicas
Dois elementos no contêiner não podem ter chaves equivalentes.
### Memória auto gerenciada
O contêiner usa um objeto alocador para lidar dinamicamente com suas necessidades de armazenamento.

As principais funções utilizadas na stack são as citadas abaixo:

### Iteração
- begin(): retorna um iterador a partir do inicio do vetor; 
- end(): retorna um iterador a partir do fim do vetor (não pega a ultima casa);
- rbegin(): retorna um iterador _reverso_ a partir do fim do vetor; 
- rend(): retorna um iterador _reverso_ a partir do inicido do vetor (não pega a primeira casa);

### Getters:
- operator[]: retorna o elemento da _chave_ indicada dentro do operator. Caso seja uma chave que não existe é inserido um novo item com o construtor padrão (para números geralmente é zero) e retornado uma referencia desse item;
- find

### Capacidade:
- size(): retorna o tamanho do vetor;
- empty(): retorna true se o vetor estiver vazio;

### Modificadores:
- insert(): existem algumas versões para o insert, sendo elas:
 - insert(std::pair<K,V>): insere um objeto par dentro do map;
 - insert(K,V): insere o valor V na posição K;
- erase(): apaga um elemento na posição passada, note que para remover o elemento da posição 4 deve-se chamar a função begin() e somar a 4;
 - erase(iterator): remove o item dessa posição do iterador;
 - erase(start,end): remove os items desde a posição start até end;

### Operadores:
- find(): retorna um iterador a partir desse elemento, caso não encontre retorna o map.end();
- lower_bound(K): retorna um iterator para o maior elemento que é menor que K;
- upper_bound(K): retorna um iterator para o menor elemento que é maior que K;

Exemplo de uso do std::map

```C++
// map::lower_bound/upper_bound
#include <iostream>
#include <map>

int main ()
{
  std::map<char,int> mymap;
  std::map<char,int>::iterator itlow,itup;

  mymap['a']=20;
  mymap['b']=40;
  mymap['c']=60;
  mymap['d']=80;
  mymap['e']=100;

  itlow=mymap.lower_bound ('b');  // itlow points to b
  itup=mymap.upper_bound ('d');   // itup points to e (not d!)

  mymap.erase(itlow,itup);        // erases [itlow,itup)

  // print content:
  for (std::map<char,int>::iterator it=mymap.begin(); it!=mymap.end(); ++it)
    std::cout << it->first << " => " << it->second << '\n';

  return 0;
}
```