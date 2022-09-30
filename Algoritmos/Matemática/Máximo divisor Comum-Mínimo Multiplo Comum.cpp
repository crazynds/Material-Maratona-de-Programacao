
#include <cstdlib> /*para poder utilizar o abs(int)*/

int GCD(int a,int b) { 
   while (b > 0) { 
      a = a % b; 
      a ^= b;    b ^= a;    a ^= b;  
   }  
   return a; 
} 

int LCM(int a,int b)
{
   return abs(a*b)/GCD(a,b);
}
