
## Máximo Divisor Comum

Calcula o máximo divisor entre 'a' e 'b'

Ex: mdc(12, 8) = 4
```c++
int mdc(int a, int b) { 
   while (b > 0) { 
      a = a % b; 
      a ^= b;    b ^= a;    a ^= b;  
   }  
   return a; 
} 
```
## Mínimo Múltiplo Comum

Procura o menor valor que seja múltiplo de 'a' e 'b'

Ex: mmc(3, 4) = 12

**OBS: Utiliza a fórmula do mdc**

```c++
#include <cstdlib> /*para poder utilizar o abs(int)*/
int mmc(int a, int b)
{
   return abs(a * b) / mdc(a,b);
}
```
**OBS: mmc(a, b, c) = mmc(mmc(a, b), c)**
