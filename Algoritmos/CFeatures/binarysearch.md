# Busca binária


Em C++ a biblioteca ```std``` já implementa funções super uteis para busca binária. Segue as funções abaixo.


## std::sort

Não podemos esquecer que todas essas funções trabalham com vetores ordenados, então trate de ordenar seus dados antes de utilizar.

```c++
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    vector<int> vec(7,3,7,4);

    // ordena bem default msm
    sort(vec.begin(),vec.end());

    struct l{
        int a,b;
    };

    vector<struct l> vec2;

    vec2.push_back({1,2});
    vec2.push_back({5,7});
    vec2.push_back({3,1});
    vec2.push_back({9,2});
    vec2.push_back({2,6});  
    // Ordena vetor de struct
    sort(vec2.begin(),vec2.end(),
        // Lambda function in C++ OMG!!!!!
        [](const struct l& s1,const struct l& s2 ){
            if(s1.a==s2.a)return s1.b < s2.b; 
            return s1.a < s2.a;
        });

}

```

Vamos falar a verdade, não precisa inventar função para fazer o sort, **USA O DEFAULT**.



## std::binary_search

Essa função é horrivel, sem nexo e serve apenas para checar se o valor existe no vetor ordenado. Isso, retorna ```true``` ou ```false```, apenas isso.


Eu ia colocar a função aqui, mas estaria fazendo um deserviço para a sociedade, então apenas saiba que você pode usar as funções abaixo para a mesma coisa, e a ```std::binary_search``` é **INUTIL**.


## std::lower_bound / std::upper_bound

Essas funções são úteis de verdade. Retorna um iterador para o primeiro elemento que de _match_ na condição especificada. Se não achar nenhum retorna um iterador para o fim do vetor, então tem que checar ```it != vec.end()```


```c++
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    // Vetor ordenado
    vector<int> vec(1,3,5,7,9);

    // retorna um iterador para o menor elemento que é maior ou igual ao valor passado
    auto it1 = lower_bound(vec.begin(),vec.end(),5);
    // retorna um iterador para o maior elemento que é menor ou igual ao valor passado
    auto it2 = upper_bound(vec.begin(),vec.end(),4);

    struct l{
        int a,b;
    };

    // Vetor ordenado
    vector<struct l> vec2;

    // retorna um iterador para o menor elemento que é maior ou igual ao valor passado
    auto it3 = lower_bound(vec.begin(),vec.end(),5,
        [](const struct l& s1,const int v ){ // LAMBDA FUNCTION IN C++ OMG!!!!
            return s1.a < v;
        });
    // retorna um iterador para o maior elemento que é menor ou igual ao valor passado
    auto it4 = upper_bound(vec.begin(),vec.end(),4,
        [](const struct l& s1,const int v ){ // OTHER LAMBDA FUNCTION IN C++ OMG!!!!
            return s1.a < v;
        });

}
```


## std::distance

Essa função é mais uma auxiliar para os irmãos _bound's_. Ela de diz a distancia entre dois iterators de um mesmo vetor. Então se você quer saber o index do resultado do ```std::lower_bound``` é possivel saber com essa função e o primeiro parametro sendo ```vec.begin()```.

Ele não retorna o valor absoluto da distancia, então o primeiro parâmetro deve ser a posição anterior e o segundo uma posição posterior.


```c++
int main(){
    // Vetor ordenado
    vector<int> vec(1,3,5,7,9);

    // retorna um iterador para o menor elemento que é maior ou igual ao valor passado
    auto it1 = lower_bound(vec.begin(),vec.end(),5);
    int idx1 = distance(vec.begin(),it1);

    // retorna um iterador para o maior elemento que é menor ou igual ao valor passado
    auto it2 = upper_bound(vec.begin(),vec.end(),4);
    int idx2 = distance(vec.begin(),it2);

}
```