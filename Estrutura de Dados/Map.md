# Map

A estrutura de dados map, conhecida em algumas linguagens como dicionário tem como objetivo armazenar de forma ordenada duplas de dados, sendo uma a chave e outra um valor. É um tipo de array associativo. 

Os dados são armazenados seguindo uma ordem das chaves, e o valor não influencia nessa ordem. 

Cada chave é única e ao definir outro valor para uma mesma chave, o comportamento esperado é que o novo valor deve sobrescrever o antigo.




## C++ - [std::map](https://cplusplus.com/reference/map/map/)

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

As principais funções utilizadas no map são as citadas abaixo:

### Iteração:
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