# Big O Notation

Como é feita a leitura do big O.

Oq é o Big O?


## No geral

De cima para baixo, a pior complexidade até a melhor.

- ```O(N^N)``` 
- ```O(!N)```
- ```O(2^N)``` -> This and above are almost impossible to use for competition algorithms 
- ```O(N^2)```
- ```O(N log N)```
- ```O(N)```
- ```O(log n)```
- ```O(log* n)``` -> From this is only the holy grail juice
- ```O(alpha n)``` _(alpha(n) is the inverse Ackermann function and grows much more slowly than log*)_
- ```O(1)```



## Grafico

![Big O Graph](./bigO.png)

### Log* N

> In computer science, the iterated logarithm of n, written log* n (usually read "log star"), is the number of times the logarithm function must be iteratively applied before the result is less than or equal to 1.

https://en.wikipedia.org/wiki/Iterated_logarithm