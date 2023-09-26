
## Máximo Divisor Comum / Greatest Common Divisor

Calcula o máximo divisor entre 'a' e 'b'

Ex: gcd(12, 8) = 4
```c++
long long gcd(long long a, long long b) { 
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

**OBS: Utiliza a fórmula do gdc**

```c++
#include <cstdlib> /*para poder utilizar o abs(int)*/
int mmc(int a, int b)
{
   return abs(a * b) / gdc(a,b);
}
```
**OBS: mmc(a, b, c) = mmc(mmc(a, b), c)**


## Em Python (melhor)

```python
from math import gcd, lcm

print(gcd(12,8)) # maior divisor comum
# 4

print(lcm(3,4)) # menor multiplo comum
# 12

```
