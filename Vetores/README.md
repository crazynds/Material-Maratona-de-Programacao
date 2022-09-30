# Vetores

Vetores são estruturas de dados muito legais em qualquer linguagem. Basicamente permite armazenar uma quantidade prédeterminada, ou indeterminada, de elementos e é possivel organiza-los dentro do vetor da forma que quiser.

Cada casa de um vetor geralmente é referenciada por um inteiro, indentificando a posição que determinado valor foi salvo. Dependendo da linguagem é possivel também possuir um vetor não continuo, ou seja, pode possuir a casa N mas não necessáriamente possue todas as casas de 0 a N, ou vetores no qual a chave da casa pode ser uma string ou até outro referenciador, sendo mais comum nesses casos serem chamados de _dictionary_.


## C++ - [std::vector](https://cplusplus.com/reference/vector/vector/)

Exemplo de uso do vetor, fique feliz e aproveite :-)

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