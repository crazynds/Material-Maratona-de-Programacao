
## Máximo Divisor Comum
GCD – Greatest Common Divisor
Calcula o máximo divisor entre ‘a’ e ‘b’
```c++
int GCD(int a,int b) { 
   while (b > 0) { 
      a = a % b; 
      a ^= b;    b ^= a;    a ^= b;  
   }  
   return a; 
} 
```
## Mínimo Múltiplo Comum
LCM – Least Common Multiple
UTILIZA A FÓRMULA DO GCD (MÁXIMO DIVISOR COMUM)

Procura o menor valor que seja múltiplo de ‘a’ e ‘b’
Ex: O menor múltiplo de 3 e 4 é 12. Logo lcm(3,4) = 12

```c++
#include <cstdlib> /*para poder utilizar o abs(int)*/
int LCM(int a,int b)
{
   return abs(a*b)/GCD(a,b);
}
```
**OBS**: lcm(a,b,c) = lcm(lcm(a,b),c)