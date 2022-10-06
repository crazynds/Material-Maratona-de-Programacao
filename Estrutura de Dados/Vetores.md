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

As principais funções utilizadas no vetor são as citadas abaixo:

### Iteração:
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