# Algoritmos de uso Geral

Ler uma linha de inteiros sem tamanho definido

```c++
//2 3 5 3 63 133 4 5
char line[100000];
gets(line);
char* theChar = strtok(line, " "); //A sequence of calls to this function split str into tokens, which are sequences of contiguous characters separated by any of the characters that are part of delimiters.
while(theChar != NULL) {
 v[i] = atoi(theChar);
 theChar = strtok(NULL, " ");
 i++;
}
```


## Backtracking

```c++
/* 
 * construir todas as permutações possíveis para um certo conjunto.
 * a função construct_candidates é uma peneira pra não oegar todos os valores.
 */
bool finished = false;

int construct_candidates(int k, int n, int c[], int a[]) {
   bool in_perm[NMAX];
   for (int i = 1; i < NMAX; i++) in_perm[i] = false;
   for (int i = 1; i < k; i++) in_perm[a[i]] = true;
   
   int ncandidates = 0;
   for (int i = 1; i <= n; i++)
      if(in_perm[i] == false) {
      c[ncandidates] = i;
      ncandidates = ncandidates + 1;
   }
   return ncandidates;
}

void backtrack(int a[], int k, int n) {
   int c[NMAX];
   if (k == n) {
      printf("{ ");
      for (int i = 1; i <= k; i++)
         printf("%d ",a[i]);
      printf("}\n");
   }
   else {
      k = k + 1;
      int ncandidates = construct_candidates(k,n,c,a);
      for (int i = 0; i < ncandidates; i++) {
         a[k] = c[i];
         backtrack(a,k,n);
         if(finished) return;
      }
   }
}

int main() {
   int a[NMAX];

   backtrack(a,0,3);
   system("PAUSE");
}
```
```C++

/* 
 * Exemplo: construindo todos os subconjuntos.
 */
#define NMAX 100


bool finished = false;

int construct_candidates(int c[]) {
   c[0] = true;
   c[1] = false;
   return 2;
}

void backtrack(int a[], int k, int n) {
   int c[NMAX];
   if (k == n) {
      printf("{ ");
      for (int i = 1; i <= k; i++)
         if (a[i] == true) printf("%d ",i);
      printf("}\n");
   }
   else {
      k = k + 1;
      int ncandidates = construct_candidates(c);
      for (int i = 0; i < ncandidates; i++) {
         a[k] = c[i];
         backtrack(a,k,n);
         if(finished) return;
      }
   }
}

int main() {
   int a[NMAX];
   backtrack(a,0,3);
   system("PAUSE");
}
```

## Ano Bissexto

```c++
/* 
 * Função que retorna se o ano é bissexto ou não
 */
bool bissexto(int ano)
{
    char bissexto = 0;
    if ( ( (!(ano % 4)) && (ano % 100) ) || (!(ano % 400)) )
        return true;
    return false;
}
```

## Dia Consecutivo

```c++
/* 
 * Função que verificar entre o dia 1 e dia 2 se os mesmo são consecutivos.
 * D1, M1, Y1 -> dia mês e ano do dia 1(começando em 1 os dias e os meses)
 * D2, M2, Y2 -> dia mês e ano do dia 2(começando em 1 os dias e os meses)
 * Deve-se setar os dias:
 * dias[1] = 31;
 * dias[2] = 28;
 * dias[3] = 31;
 * dias[4] = 30;
 * dias[5] = 31;
 * dias[6] = 30;
 * dias[7] = 31;
 * dias[8] = 31;
 * dias[9] = 30;
 * dias[10] = 31;
 * dias[11] = 30;
 * dias[12] = 31;
 */
int dias[13];
int D1, M1, Y1, C1;
int D2, M2, Y2, C2;
bool isConsecutiveDay()
{
    if(Y1 == Y2)
    {
        if(M1 == M2)
        {
            if(D1 == D2-1)
            {
                return true;
            }
        }else if(M1 == M2-1){
            if(M1 == 2)
            {
                if(bissexto(Y1))
                {
                    if(D1 == 29 && D2 == 1)
                    {
                        return true;
                    }
                }else{
                    if(D1 == dias[M1] && D2 == 1)
                    {
                        return true;
                    }
                }
            }else{
                if(D1 == dias[M1] && D2 == 1)
                {
                    return true;
                }
            }
        }
    }else if(Y1 == Y2-1)
    {
        if(M1 == 12 && M2 == 1)//Fim e começo de ano
        {
            if(D1 == dias[12] && D2 == 1)
            {
                return true;
            }
        }
    }
    return false;
}
```

## Quadrado Perfeito
```c++
bool isPerfectSquare(int valor)
{
    int vsqrt = round(sqrt(valor));
    return (valor >= 0 && valor == vsqrt * vsqrt);
}
```

# Algoritmos de String


## Strtok – quebra a string em partes.

```c++
char a[] = "esta é uma string, bem simples?";
char *b;
b = strtok(a," ");

while(b!=NULL){
	   cout << b << endl;
	   b = strtok(NULL," ");
}
```    
Saída :
```
esta
É
Uma 
String,
Bem
Simples?
```


## strstr -> acha substring

```c++
char str[] ="This is a simple string";
char * pch;
pch = strstr (str,"simple");
```


## strncpy -> copia parte de uma string

```c++
char str1[]= "To be or not to be";
char str2[6];
strncpy (str2,str1,5);
```

## strncat -> contena string com pedaço de outra

```c++
strcpy (str1,"To be ");
strcpy (str2,"or not to be");
strncat (str1, str2, 6);
```

## Biblioteca <string>

rbegin e rend -> retorna iterator para string ao contrário
// string::rbegin and string::rend

```c++
#include <iostream>
#include <string>
using namespace std;

int main ()
{
  string str ("now step live...");
  string::reverse_iterator rit;  // inverte string
  for ( rit=str.rbegin() ; rit < str.rend(); rit++ )
    cout << *rit;
  return 0;
}
```

length -> retorna o núrmero de caracteres

```c++
string str ("Test string");
cout << "The length of str is " << str.length()<< endl;
```

1. c_str -> string equivalente em c
```c++
string ala ("xoxota");
char blaa [10];
strcpy(blaa,ala.c_str());
```

2. substr-> gera uma substring
```c++
string wow;
string ala("wow")

wow = ala.substr(0,2); // pega da posiçao 0 até a 2 e gera a string\
```
      
3. compare –> compara as strings

```c++
if (str1.compare(str2) == 0)
    	cout << str1 << "é igual a " << str2 << "\n";
```

## Suffix array 

```c++
#define max 200010
using namespace std;



char S[max]; // vetor de sufixos
int SA[max]; // compara sufixos
int RA[max], LCP[max], *fc, *sc,step;

char Q[max];

//usada para verificar se uma substring faz parte do suffix array
pair<int,int> range(int n,char *Q)
{ 
	int lo = 1, hi =n, m = strlen(Q), mid = lo; //index 0 - null
	while(lo <=hi){
		mid  = (lo+hi)/2;
		int cmp = strncmp(S+SA[mid],Q,m);
		if(cmp==0) break; //found
		else if(cmp>0) hi = mid -1;
		else lo = mid+1;
	}

	if (lo > hi)
		return make_pair(-1,-1);

	for(lo = mid;lo >=1 && strncmp(S+SA[lo],Q,m)==0;lo--);
	lo++;
	for(hi = mid;hi<=n && strncmp(S+SA[hi],Q,m)==0;hi++);
	hi--;

	return make_pair(lo,hi);
}


bool cmp(int a,int b){

	if (step==-1 || fc[a]!=fc[b]) return fc[a]<fc[b];

	return fc[a+(1<<step)] < fc[b+(1<<step)];
}

void suffix_array(char *s, int n){ //O nlog^2(n)
	for(int i=0;i<n;i++){
		RA[i] = S[SA[i]=i];
	}

	
	for (fc = RA,sc = LCP, step=-1;(1<<step)<n;step++){
		sort(SA,SA+n,cmp);
		int cnt = 0;
		for(int i = 0;i<n;i++){
			if(i>0 && cmp(SA[i-1],SA[i]))cnt++;
			sc[SA[i]] = cnt;
		}
		if(cnt==n-1)break; //all distinct
		swap(fc,sc);
	}
	for(int i=0;i<n;i++)RA[SA[i]] = i;
}


int main()
{
	cin >> S;
	int n = strlen(S);
	suffix_array(S,n+1);
	for(int i =1;i<=n;i++)
		cout << SA[i] << " " << S+SA[i] << endl;
	
	cin >> Q;
	pair <int,int> pos = range(n,Q);

	if(pos.first !=-1 && pos.second!=-1){

		cout << Q << " is found SA [ "<< pos.first << " .. " << pos.second << " of " << S << endl;
		cout << "They are:"<< endl;
		for(int i = pos.first; i<=pos.second;i++)
			cout << S+SA[i] << endl;
	}

	else {
		cout << Q << " is not found in "<< S << endl;
	}

	system("pause");
	return 0;
}
```

# PENDENTES!!
## Algoritmos para empareamento de Cadeias

```c++
//Naive String Matching - O(m * n)
bool NaiveStringMatching(string t, string p) { 
   for(int i = 0; i <= t.size() - p.size(); i++) {
      bool found = true;
      for (int j = 0; j < p.size(); j++) {
         if (p[j] != t[i + j]) {
            found = false;
            break;
         }
      }
      if (found) {
         return found;
      }
   }
   return false;
}
//Rabin Karp Match - O(m + n), nesta forma, mas sofre de problemas com numero grande, então O(m * n)
bool RabinKarpMatch(string t, string p) {
   float kP = 0;
   float kT = 0;
   for(int i = 0; i < p.size(); i++) {
      kP += pow(10.f, p.size() - i - 1) * (p[i] - 'a' + 1);
      kT += pow(10.f, p.size() - i - 1) * (t[i] - 'a' + 1);
   }

   for(int i = 0; i <= t.size() - p.size(); i++) {
      if (kP == kT) {
         return true;
      }
      kT = 10.f * (kT - pow(10.f, p.size() - 1) * (t[i] - 'a'  + 1)) + (t[i + p.size()] - 'a'  + 1);
   }
   return false;   
}
//KMP - O(n + m)
vector<int> preKMP(string p) {

   vector<int> vecPreKMP(p.size());
   vecPreKMP[0] = 0;
   int j = 0;
   int i = 1;
   while(i < p.size()) {
     if(p[j] == p[i]) { // j + 1 characters match
       vecPreKMP[i] = j + 1;
       i++;
       j++;
     } else if (j > 0) //j follows a matching prefix
       j = vecPreKMP[j - 1];
     else { // no match
       vecPreKMP[i] = 0;
       i++;
     }
   }
   return vecPreKMP;
}

bool KMP(string t, string p) {
   vector<int> vecPreKMP = preKMP(p);
   int i = 0;
   int j = 0;
   while (i < t.size()) {
      if (p[j] == t[i]) {
         if (j == p.size() - 1) {
            return true;// match
         }
         i++;
         j++;
      } 
      else if (j > 0) {
         j = vecPreKMP[j - 1];
      }
      else {
         i++; 
      }
   } 
   return false; // no match
}
//KMP2 - Mais rapido - O(n + m)
int KMP(string &source, int sourceOffset, int sourceCount, string &target, int targetOffset, int targetCount, int fromIndex) {
       if (fromIndex >= sourceCount) {
           return (targetCount == 0 ? sourceCount : -1);
       }
       if (fromIndex < 0) {
           fromIndex = 0;
       }
       if (targetCount == 0) {
           return fromIndex;
       }

       char first  = target[targetOffset];
       int max = sourceOffset + (sourceCount - targetCount);

       for (int i = sourceOffset + fromIndex; i <= max; i++) {
           /* Look for first character. */
           if (source[i] != first) {
               while (++i <= max && source[i] != first);
           }

           /* Found first character, now look at the rest of v2 */
           if (i <= max) {
               int j = i + 1;
               int end = j + targetCount - 1;
               for (int k = targetOffset + 1; j < end && source[j] ==
                        target[k]; j++, k++);

               if (j == end) {
                   /* Found whole string. */
                   return i - sourceOffset;
               }
           }
       }
       return -1;
}
```

# Algoritmos de Busca e Ordenação

## Busca Binária

```c++
/*faz uma busca binaria em vetor a procura pelo indice do valor que seja maior ou igual a val. */
int busca(int *vet, int val, int tamanho)
{
    int ini = 0, fim = tamanho-1;

    if(val > vet[fim] )
        return tamanho;
    if(val < vet[0] )  //aumentou o desempenho
        return 0;

    int achou = tamanho; /*posicao fora do range = nao achou*/
    while(ini <= fim)
    {
        int meio = (ini + fim )/2;
        int elem = vet[meio];
        if( elem >= val )
        {
            achou = meio;
            fim = meio - 1;
        }
        else /*if( elem < val ) */
            ini = meio + 1;
    }
    return achou;
}
```

## Bubblesort
```c++
void bubblesort(vector<int> &v) {
   for(int j = v.size() - 1; j > 0; j--) {
      for(int i = 0; i < j; i++) {
         if(v[i+1] < v[i]){ 
            swap(v[i+1], v[i]);
         }
      }
   }
}
```


# Algoritmos de matemática

## Fibonacci – pré-calculado (mais lento)
/* Fibonacci: Pré-computa um vetor com n valores fibonacci.*/
```c++
#define MAX 100000
int fibonacci[MAX];
void buildFibonacci(int n)
{
    fibonacci[0] = 0;
    fibonacci[1] = 1;
    if(n < 3)// 1 ou 2
    {
        return;
    }
    for(int i = 2 ; i < n ; i++)
    {
        fibonacci[i] = fibonacci[i-1] + fibonacci[i-2];
    }
}
```

## Números primos
Sieve: Algoritmo para verificar se um número é primo.

O algoritmo computa todos os números primos antes (função sieve()) para que depois a  verificação seja através da função prime(int p), onde p é o número que se deseja testar.

```c++
#define SIEVE_SIZE 1000
#include <bitset>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <iostream>
using namespace std;

int N;
int C;
vector<int> primes;
bitset<SIEVE_SIZE+2> bs;

void sieve()
{
    int i, j, max = SIEVE_SIZE + 1;
    bs.reset();
    bs.flip();
    bs.set(0, false);
    bs.set(1, true);
    for( i=2; i <= max; i++ )
    {
        if( bs.test(i) == true ) // i é primo, e todos os múltiplos de i nao
        {
            primes.push_back( i );
            for( j = i*i; j <= max; j += i )
            {
                bs.set(j, false);
            }
        }
    }
}

bool isPrime(int p)
{
    if( p < SIEVE_SIZE )
       return bs.test(p);
    for(int i=0; i< primes.size()-1; i++)
    {
        if( p % primes[i] == 0 )
           return false;
    }
    return true;
}
```

## Prime Factor
Retorna o menor fator primo de um valor n.

Ex: 6 = 2 * 3. No caso o menor valor é o 2 então este será retornado.
Se n for primo, o próprio n será retornado.

```c++
int primeFactor (int n)
{
	// Don't bother to use abs () <stdlib.h>
	if (n < 0)
		n = -n;
	// For n < 2; it is just n
	if (n < 2)
		return n;

	// otherwise, for an even number it is 2
	if (n % 2 == 0)
		return 2;

	// for other odd numbers, search for a divisor
	// until SQRT (n) [conceptual] n / div >= div is
	// equivalent to SQRT (n) >= div
	for (int div = 3; n / div >= div; div += 2)
	{
		// if div is a divisor, just return it.
		if (n % div == 0)
			return div;
	}

	// There is no divisor (n is prime), return it.
	return n;
}
```

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

# Algoritmos de Geometria Computacional

## Classe Point (Usando em alguns algoritmos)

```c++
class Point {
public:
   float x, y, z;

   Point() {
      x = y = z = 0;
   }

   Point(float x1, float y1, float z1) {
      x = x1;
      y = y1;
      z = z1;
   }

   Point operator - (Point a) {
      return Point(x - a.x, y - a.y, z - a.z);
   }

   Point operator + (Point a) {
      return Point (x + a.x, y + a.y, z + a.z);
   }

   Point operator / (float a) {
      return Point (x / a, y / a, z / a);
   }

   Point operator * (float a) {
      return Point (x * a, y * a, z * a);
   }
};
```


## Polígono



Sendo PI = π

```c++
/*Fórmula para achar o raio do polígono a partir da área 
'a' de um polígono com 'n' lados*/
raio = sqrt((2*a)/((double)n*sin((2*PI)/(double)n)));

/*lembrando que a área de um polígono pode ser calculada por:*/
area = ((l*raio)/2.0) * n;
/*tendo ‘l’ o comprimento do lado, raio sendo o raio do polígono (ou do círculo haja círculo circunscrito) e ‘n’ o número de lados do polígono:*/

/*Fórmula da apótema do polígono usando o raio encontrado na fórmula acima*/
apotema = cos(PI/(double)n) * raio;

/*Área de um círculo inscrito em um polígono baseado na apótema encontrada na fórmula acima*/
area1 = PI*apotema*apotema;

/*Área de um círculo circunscrito num polígono com o raio encontrado acima*/
area2 = PI*raio*raio;

/* Calcula a area de um poligono irregular */
const int max = 6; //quantidade de pontos no poligono

struct Point {
	float x, y;
};

float area_do_poligono(Point v[]) {
	float area = ((v[max-1].y + v[0].y) / 2) * (v[max-1].x - v[0].x);
	for (int i = 0; i < max - 1; i++) {
		area += ((v[i].y + v[i + 1].y) / 2) * (v[i].x - v[i + 1].x);
	}

	if (area < 0)
		area = -area;

	return area;
}
```


## Centro de um círculo a partir de 3 pontos (pontos cocirculares)
Resulta no circCentro que é o centro do círculo.

```c++
typedef struct Point {
   	double x,y;
}Point;

Point A,B,C;
Point circCentro;

double D = 2.0 * (A.x * (B.y - C.y) + B.x * (C.y - A.y) + C.x * (A.y - B.y));
if (D==0.0) { /*Não existe círculo pois são colineares*/ }
circCentro.x = ((A.y*A.y + A.x*A.x) * (B.y - C.y) + (B.y*B.y + B.x*B.x) * (C.y - A.y) + (C.y*C.y + C.x*C.x) * (A.y - B.y))/D;
circCentro.y = ((A.y*A.y + A.x*A.x) * (C.x - B.x) + (B.y*B.y + B.x*B.x) * (A.x - C.x) + (C.y*C.y + C.x*C.x) * (B.x - A.x))/D;
```

## Área de Triângulo
Fórmula denominada Heron of Alexandria

Calcular a área A de um triângulo cujas arestas são de tamanho a, b e c.
Se Tivermos os vértices A B C do triângulo basta que 'a' 'b' e 'c' sejam os resultados dos cálculos das distâncias entre AB BC CA.

```c++
float areaOfTriangle(float a, float b, float c)
{
    float s = (a + b + c) * 0.5f;
    return sqrt(s*(s-a)*(s-b)*(s-c));
}

/* Fórmula básica de área de quadrado.
*/
float areaOfTriangle(float b, float h)
{
    return 0.5f * b * h;
}
```

## Distância entre dois Pontos
Fórmula para o cálculo de distância entre dois pontos.

```c++
float dist3D(Point a, Point b) {
    return sqrt(pow(b.x - a.x, 2)  +  pow(b.y - a.y, 2) + pow(b.z - a.z, 2));
}

float dist2D(Point a, Point b) {
    return sqrt(pow(b.x - a.x, 2)  +  pow(b.y - a.y, 2));
}
```

## Produto Vetorial
```c++
Point cross(Point a, Point b) {
    Point result;
    result.x = a.y * b.z - a.z * b.y;
    result.y = a.z * b.x - a.x * b.z;
    result.z = a.x * b.y - a.y * b.x;

    return result;
}
```

## Produto Escalar
```c++
float dot(Point a, Point b) {
    return (a.x * b.x) + (a.y * b.y) + (a.z * b.z);
}
```

## Norma
```c++
float norma(Point a) {
    return sqrt(dot(a, a));
}
```

## Círculo

__THIS CIRCLE HAS BEEN SLICED INTO THE MAXIMUM NUMBER OF SECTIONS 
USING 10 SLICES. HOW MANY SECTIONS ARE THERE? HINT: COUNTING SECTIONS 
IS TOUGH!. TRY USING THE FORMULA PREVIOUSLY DEVELOPED.__


- Maximum number of sections of a Circle when sliced by a knife = [n(n+1)/2] +1.  
where "n" is the number of slices.

- A circle has an angle of 2 * PI and an Area of: PI * RAIO^2

- Area of Sector = (ANG/2) * RAIO^2              (when ANG is in radians)
- Area of Sector = ((ANG * PI/180)/2) * RAIO^2   (when ANG is in degrees)

- Arc Length = ANG * RAIO   (when ANG is in radians)
- Arc Length = ANG * PI/180 * RAIO   (when ANG is in degrees)

- Area of Segment  = (ANG - sin(ANG))/2 * RAIO^2   (when ANG is in radians)
- Area of Segment  = (ANG * PI/180 - sin(ANG))/2 * RAIO^2   (when ANG is in degrees)

## Intersecção entre retas (linhas ou segmentos), retornando o ponto da intersecção
p1 e p2 correspondem ao ponto inicial e final dado de uma linha1 

p3 e p4 correspondem ao ponto inicial e final dado de uma linha2

```c++
Point* intersection(Point p1, Point p2, Point p3, Point p4) {
    float x1 = p1.x, x2 = p2.x, x3 = p3.x, x4 = p4.x;
    float y1 = p1.y, y2 = p2.y, y3 = p3.y, y4 = p4.y;

    float d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4);

    // Se d é zero, não há intersecção.
    if (d == 0)
    {
        return NULL;
    }

    // Pega o x e y do ponto de intersecção.
    float pre = (x1*y2 - y1*x2), post = (x3*y4 - y3*x4);
    float x = ( pre * (x3 - x4) - (x1 - x2) * post ) / d;
    float y = ( pre * (y3 - y4) - (y1 - y2) * post ) / d;
    /******************************************************************/
    // Checa se as coordenadas do ponto então entre os dois segmentos
    //OBS: Se for linhas, esse código deve ser comentado, pois essa
    //parte do código é apenas quando se lida com SEGMENTOS de reta.
    if ( x < min(x1, x2) || x > max(x1, x2) ||
        x < min(x3, x4) || x > max(x3, x4) ) return NULL;
    if ( y < min(y1, y2) || y > max(y1, y2) ||
        y < min(y3, y4) || y > max(y3, y4) ) return NULL;
    /******************************************************************/
    // Retorna o ponto da intersecção
    Point* ret = new Point();
    ret->x = x;
    ret->y = y;
    return ret;
}
```


## Intersecção entre segmentos de reta (retornando booleano)
p1 e p2 correspondem ao ponto inicial e final dado de uma linha1 

p3 e p4 correspondem ao ponto inicial e final dado de uma linha2

```c++
bool intersection(Point p1, Point p2, Point p3, Point p4) {
    float x1 = p1.x, x2 = p2.x, x3 = p3.x, x4 = p4.x;
    float y1 = p1.y, y2 = p2.y, y3 = p3.y, y4 = p4.y;

    float d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4);
    if (d == 0) return false;

    float pre = (x1*y2 - y1*x2), post = (x3*y4 - y3*x4);
    float x = ( pre * (x3 - x4) - (x1 - x2) * post ) / d;
    float y = ( pre * (y3 - y4) - (y1 - y2) * post ) / d;
    /******************************************************************/
    // Checa se as coordenadas do ponto então entre os dois segmentos
    //OBS: Se for linhas, esse código deve ser comentado, pois essa
    //parte do código é apenas quando se lida com SEGMENTOS de reta.
    if ( x < min(x1, x2) || x > max(x1, x2) ||
        x < min(x3, x4) || x > max(x3, x4) ) return false;
    if ( y < min(y1, y2) || y > max(y1, y2) ||
        y < min(y3, y4) || y > max(y3, y4) ) return false;
    /******************************************************************/
    return true;
}
```


## Linhas coincidentes
p1 e p2 correspondem ao ponto inicial e final dado de uma linha1 

p3 e p4 correspondem ao ponto inicial e final dado de uma linha2

```c++
bool linesCoincident(Point p1, Point p2, Point p3, Point p4)
{
    float nominator_ua = ((p4.x - p3.x)*(p1.y - p3.y)) - ((p4.y - p3.y)*(p1.x - p3.x));
    float denominator_ua = ((p4.y - p3.y)*(p2.x - p1.x)) - ((p4.x - p3.x)*(p2.y - p1.y));
    float nominator_ub = ((p2.x - p1.x)*(p1.y - p3.y)) - ((p2.y - p1.y)*(p1.x - p3.x));
    float denominator_ub = ((p4.y - p3.y)*(p2.x - p1.x)) - ((p4.x - p3.x)*(p2.y - p1.y));
    // - Se os nominadores e denominadores para ua e ub forem 0  linhas são coincidentes.
    // - se apenas os denominadores forem iguais a zero  as retas são paralelas (essa parte 
    // não está no código. Se precisa, adicionar depois).
    if(nominator_ua == 0.f && denominator_ua == 0.f
        && nominator_ub == 0.f && denominator_ub == 0.f)
    {
        return true;
    }
    return false;
}
```

## Testar linhas coincidentes, paralelas e intersecção entre elas
sendo x1 e y1 e x2 e y2 o ponto inicial e final de uma reta

sendo x3 e y3 e x4 e y4 o ponto inicial e final de outra reta

```c++
int x1, y1;
int x2, y2;
int x3, y3;
int x4, y4;
double m1=1.0*((x1-x2)*(y3-y4))-((y1-y2)*(x3-x4));
double m2=1.0*((x3-x4)*(y3-y1))-((y3-y4)*(x3-x1));
double m3=1.0*(-((x3-x1)*(y1-y2))+((y3-y1)*(x1-x2)));
/*Caso as linhas sejam coincidentes*/
if(m1==0 && m2==0 && m3==0)
{
    printf("Linhas coincidentes.\n");
}
/*Caso as linhas sejam paralelas*/
else if(m1==0)
{
    printf("Linhas paralelas\n");
}
/*Se não ocorrer nenhum desses casos
 *então há um ponto x y de intersecção
 *entre as duas linhas.
 */
else
{
    double intr1=m2/m1;
    double intr2=m3/m1;
    double x=x1+intr2*(x2-x1);
    double y=y1+intr1*(y2-y1);
    printf("Ponto de inteseccao: %.2lf %.2lf\n",x,y);
}
```



## **(NÃO TESTADO)** Distância entre segmentos de reta
```c++
/* SMALL_NUM = ?
* a1 e a2 é uma reta
* b1 e b2 é a outra reta
*/
#define SMALL_NUM 0.01f
float distanceSegmentToSegment(Point a1, Point a2, Point b1, Point b2) {
    Point u,v,w;
    u = a2 - a1;
    v = b2 - b1;
    w = a1 - b1;

    float a = dot(u,u);
    float b = dot(u,v);
    float c = dot(v,v);
    float d = dot(u,w);
    float e = dot(v,w);

    float D = a * c - b * b;

    float sc, sN, sD = D;
    float tc, tN, tD = D;

    if(D < SMALL_NUM)	{
        sN = 0;
        sD = 1;
        tN = e;
        tD = c;
    } else {
        sN = (b * e - c * d);
        tN = (a * e - b * d);

        if(sN < 0) {
            sN = 0;
            tN = e;
            tD = c;
        } else if (sN > sD) {
            sN = sD;
            tN = e + b;
            tD = c;
        }
    }

    if (tN < 0)	{
        tN = 0;
        if (-d < 0) {
            sN = 0;
        } else if (-d > a) {
            sN = sD;
        } else {
            sN = -d;
            sD = a;
        }
    } else if (tN > tD) {
        tN = tD;
        if ((-d + b) < 0.0) {
            sN = 0;
        } else if ((-d + b) > a) {
            sN = sD;
        } else {
            sN = (-d + b);
            sD = a;
        }
    }

    sc = (abs(sN) < SMALL_NUM ? 0 : sN/sD );
    tc = (abs(tN) < SMALL_NUM ? 0 : tN/tD );

    return norma(w + u * sc - v * tc);
}
```

## Distância Ponto a Linha
```c++
float distPointToLine(Point c, Point p1, Point p2) {
   Point pV;
   pV = p2 - p1;

   Point pW;
   pW = c - p1;

   float c1 = dot(pW, pV);
   float c2 = dot(pV, pV);
   float b = c1 / c2;

   Point proj;
   proj = p1 + pV * b;

   return dist(c, proj);
}
```

## **(NÃO TESTADO)** Distância Ponto a Segmento de Reta
```c++
float distPointToSegment(Point c, Point p1, Point p2) {
   Point pV;
   pV = p2 - p1;

   Point pW;
   pW = c - p1;

   float c1 = dot(pW, pV);
   if(c1 <= 0)
      return dist(c, p1);

   float c2 = dot(pV, pV);
   if(c2 <= c1)
      return dist(c, p2);

   float b = c1 / c2;

   Point proj;
   proj = p1 +  pV * b;

   return dist(c, proj);
}
```

## **(NÃO TESTADO)** Projeção de um Ponto em um Plano

projeçao do ponto thePoint no plano ABC

```c++
Point projectionInPlane(Point thePoint, Point a, Point b, Point c) {
    Point normal, p1p2, p1p3, p1p0;
    p1p2 = b - a;
    p1p3 = c - a;
    p1p0 = thePoint - a;
    normal = cross(p1p2, p1p3);

    float sb, sn, sd;

    sn = -dot(normal, p1p0);
    sd =  dot(normal, normal);

    sb = sn / sd;

    return thePoint + normal * sb;
}

float distPointToPlane(Point thePoint, Point a,Point b, Point c) {   
	return dist(thePoint, projectionInPlane(thePoint, a, b, c));
}
```

## **(NÃO TESTADO)** Ponto dentro de Polígonos
Testa se ponto está dentro de um poligono pelo numero de vezes q ele passa por arestas verticalmente, funciona somente em 2D

V[] = vertex points of a polygon V[n+1] with V[n]=V[0]

Return:  0 = outside, 1 = inside
```c++
int crossingNumbers(Point P, vector<Point> V) { // 2D
   int cn = 0;
   float vt;
   float next;

   for(int i = 0; i < V.size(); i++) {
      next = i + 1;

      if(next == V.size()) next = 0;
         
      if(((V[i].y <= P.y) && (V[next].y > P.y)) || 
         ((V[i].y > P.y) && (V[next].y <= P.y))) {
         vt = (float)(P.y - V[i].y) / (V[next].y - V[i].y);

         if (P.x < V[i].x + vt * (V[next].x - V[i].x))
            ++cn;
      }
   }
   return (cn % 2);
}
```

# Algoritmos de Grafo

## Floyd Warshall

Calcula distâncias entre todos os nodos do grafo.

Entradas:
 - dist é uma matrix de adjacência do grafo, logo: dist[i][j] é o custo de ir de i até j.
 - Se não existe aresta entre i e j, o valor de dist[i][j] é igual a INFINITY.
 - Se i e j forem iguais, deve-se setar o dist[i][j] para zero.
 - Max_n é o número máximo de vértices (variável de acordo com o problema proposto)

Saidas:
 - dist[i][j]: Custo do menor caminho de i até j.
 - detour_path[i][j]: Para qual nodo ir partindo de i para se aproximar de j ou -1 se não 
existe caminho.

OBS: O algoritmo começa verificando na posição zero e vai até o valor < n, ou seja, se o grafo tiver 5 vértices, eles estarão na posição 0, 1, 2, 3, 4.

```C++
static const int max_n = 101;
#define INFINITY 1.0/0.0
float dist[max_n][max_n];
int detour_path[max_n][max_n];

void floyd_warshall(int n) {
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            detour_path[i][j] = -1;

    for (int k = 0; k < n; ++k) {
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                float new_dist = dist[i][k] + dist[k][j];
                if (new_dist < dist[i][j]) {
                    dist[i][j] = new_dist;
                    detour_path[i][j] = k;
                }
            }
        }
    }
}
```

## Ford-Fulkerson
Função Ford-Fulkerson(G, s, t) [Achar o fluxo máximo de um grafo]
- para cada (u, v) em E[G]
    - fluxo(u, v) := 0
    - fluxo(v, u) := 0
    - enquanto existir caminho de aumento p de s para t na rede residual
        - Cf(p) := capacidade do arco de menor capacidade em p
        - para cada (u, v) em p
            - fluxo(u, v) := fluxo(u, v) + Cf(p)
            - fluxo(v, u) := fluxo(v, u) - Cf(p)

setar as variáveis em:
- memset(FLOW, 0, sizeof(FLOW));
- memset(queue, 0, sizeof(queue));
- memset(F, 0, sizeof(F));
    
Basta apenas configurar a variável FLOW sendo:
- FLOW[A][B] = o fluxo máximo da aresta de A pra B.

Depois basta chamar maxflow, fTotal é o fluxo total do grafo.

```C++
#include<stdio.h>
#include<stdbool.h>
#define MAX 102

int FLOW[MAX][MAX];
int queue[MAX];
int head, tail;
int parent[MAX];
int V, E;
int s, t, fTotal;
int F[MAX][MAX];

bool reachable(int s, int t) {
   bool found = false;
   int vq;
   head = tail = 0;
   memset(parent, 255, sizeof(parent));
   queue[tail++] = s;
   parent[s] = s;

   while(head < tail && !found) {
      vq = queue[head++];
      int i;
      for(i=0; i<V; i++) {
         if(FLOW[vq][i] && parent[i] == -1) {
            queue[tail++] = i;
            parent[i] = vq;

            if(i == t) {
               found = true;
               break;
            }
         }
      }
   }
   return found;
}

void maxflow() {
   int vj, min;
   fTotal = 0;
   while(reachable(s, t)) {
       min = FLOW[parent[t]][t];
       vj = t;
       while(parent[vj] != vj) {
          if(FLOW[parent[vj]][vj] < min)
             min = FLOW[parent[vj]][vj];
             vj = parent[vj];
       }

       vj = t;
       while(parent[vj] != vj) {
          FLOW[parent[vj]][vj] -= min;
          FLOW[vj][parent[vj]] += min;
          F[parent[vj]][vj] += min;
          vj = parent[vj];
       }
       fTotal += min;
   }
}

int main () {
    /*Inicio do programa*/
    /*While para repetição dependendo do problema*/
    memset(FLOW, 0, sizeof(FLOW));
    memset(queue, 0, sizeof(queue));
    memset(F, 0, sizeof(F));
    /*Setar o FLOW (fluxo entre vértices*/
    maxflow();
    printf("O Fluxo total é %d.\n",++cases,fTotal);
    scanf("%d",&V);
    return 0;
}
```

## Bellman-Ford

BELLMAN-FORD - O Algoritmo de Bellman-Ford é um algoritmo de busca de caminho mínimo em um dígrafo ( ou Grafo direcionado) ponderado, ou seja, cujas arestas têm peso, inclusive negativo. 

**O(VxA)**

- edgecount – número de arestas do grafo.

- nodecount – número de nodos(vértices) do grafo.

- edges[MAX] – vetor que contém as arestas, com o peso de cada.

- MAX – Quantidade máxima de arestas.

Obs: dentro do algoritmo, a variável distance[] computa a distância mais curta encontrada entre cada um dos nodos.

```C++
#include <iostream>
#define INFINITY 99999999
#define MAX 10000
using namespace std;

typedef struct {
    int source;
    int dest;
    int weight;
} Edge;

Edge edges[MAX];
int edgecount;
int nodecount;

void bellman_ford(int source) {
    int i, j;
    int *distance = new int [nodecount];
    for(i = 0; i < nodecount; i++) {
        distance[i] = INFINITY;
    }
    distance[source] = 0;
    for (i = 0; i < nodecount; i++) {
        bool change = false;
        for (j = 0; j < edgecount; j++) {
            if (distance[edges[j].dest] > distance[edges[j].source] + edges[j].weight) {
                distance[edges[j].dest] = distance[edges[j].source] + edges[j].weight;
                change = true;
            }
        }
        if(change == false) break;
    }
    for (i = 0; i < edgecount; i++) {
        if (distance[edges[i].dest] > distance[edges[i].source] + edges[i].weight) {
            //cout << "Negative cycle." << endl;
            break;
        }
    }
    /*for (i = 0; i < nodecount; i++) {
       cout << "A distancia mais curta entre os nodos " 
       << source << " e " << i <<" eh " << distance[i] << endl;
    }*/
}
```

## Topological Sort
Utilizado com grafos direcionados.

O algoritmo só pode ser utilizado se o grafo não possuir ciclos direcionados. Topological sorting é útil para definir a ordem que “coisas” devem ser feitas (ou visitadas). Gerar uma ordem para os vértices.

Entrada:
- graph[][] – Matriz de adjacência do grafo ( o algoritmo começa a contar na posição 1  dos nodos (diferente dos outros que começa em 0).
- N – número de nodos do grafo
- indegree[] – vetor que diz para cada nodo, quantas arestas chegam nesse nodo (como é um grafo direcionado). Ex: se tivermos uma aresta 1 2, ou seja de 1 para 2, faça indegree[2]++; (aumenta o número de arestas incidentes em 2).

```C++
#define MAX 105
#include <cstdio>
#include <iostream>
#include <queue>
using namespace std;
int N;
int graph[MAX][MAX];
int indegree[MAX];
int top_sort[MAX];
void topological_sorting() {
   queue<int> Q;
   for(int i = 1; i <= N; i++) {
      if(indegree[i] == 0) {
         Q.push(i);
      }
   }

   int counter_sort = 1;

   while(!Q.empty()){
      int v = Q.front();
      Q.pop();
      top_sort[counter_sort] = v;
      counter_sort++;

      for(int i = 1; i <= N; i++) {
         if(graph[v][i] != 0) {
            indegree[i]--;
            if(indegree[i] == 0) {
               Q.push(i);
            }
         }
      }
   }
   for(int i = 1 ; i <= N; i++)
   {
      if(i == 1)
      {
         printf("%d", top_sort[i]);
      }else{
         printf(" %d", top_sort[i]);
      }
   }
   printf("\n");
}

int main () {
    /*Inicio do programa*/
    /*While para repetição dependendo do problema*/
    for(int i = 0 ; i < n ; i++)
      {
         for(int j = 0 ; j < n ; j++)
         {
            graph[i][j] = 0;
         }
         indegree[i] = 0;
      }
    /*Setar o graph e o indegree (configuração do grafo)*/
    topological_sorting();
    return 0;
}
```

## Depth-First Search
Realiza uma busca em profundidade no grafo.
- N – O número de nodos.
- v – Nodo inicial.

Para realizar o algoritmo:
- setar a variável graph[MAX][MAX] com a matriz de adjacência do grafo.
- setar todos os discovered[MAX] para false.


```C++
#define MAX 101
bool discovered[MAX];
int parent[MAX];
int graph[MAX][MAX];

void dfs(int v, int N) {
   discovered[v] = true;   
   for (int i = 1; i <= N; i++) {
      if(graph[v][i] != 0 && discovered[i] == false) { 
         parent[i] = v;
         dfs(i);
      }
   }
}
```

## Dijkstra
O algoritmo de Dijkstra soluciona o problema do caminho mais curto num grafo dirigido ou não dirigido com arestas de peso não negativo, em tempo computacional O([m+n]log n).

Deve-se setar a variável graph[MAX][MAX], sendo que esta matriz representa o peso/custo de cada aresta.
- em graph[][], tendo i e j, se i == j, graph[i][j] == 0. Se i != j, graph[i][j] = custo dele.
- Se não existir aresta entre i e j ( ou no caso no grafo direcionado de i para j), então o  custo é graph[i][j] = INF; (setado abaixo);

fazendo um for simples:
- graph[i][j] = (i == j ? 0 : INF);

OBS: Os nodos começam em ZERO (na matriz graph[][] no caso).

vCost corresponde ao caminho pra chegar até o nodo (partindo do nodo inicial dado quando foi chamada a função dijkstra).

Ex: se chamdou dijkstra(START = 0, END = 4)
vCost[4] é o vector com os índices dos nodos que foram visitados para chegar de 0 até 4.(ex 0 2 3 4).

```C++
#define MAX 1000
#define INF 999999999
int N;
int graph[MAX][MAX];
int visited[MAX],cost[MAX];
vector<int> vCost[MAX];

int dijkstra(int START, int END){
   int i, k, aux = 1,min=0;

   for(i=0 ; i<N ; i++) { /* inicializa foi e custo */
      visited[i] = 0;
      cost[i] = INF;
   }

   cost[START] = 0; /* a menor distância de INI já conhecida */
   visited[START] = 1;
   k = START;
   vCost[START].clear();
   vCost[START].push_back(START);

   while(!visited[END] && min!=INF){
      min = INF;

      for(i=0 ; i<N ; i++)
         if(!visited[i]){
            if(cost[i]>cost[k]+graph[k][i]) /* relaxamento */
            {
               cost[i]=cost[k]+graph[k][i];
               vCost[i] = vCost[k];
               vCost[i].push_back(i);
            }

            if(cost[i]<min){
               min=cost[i];
               aux=i;
            }
         }

         visited[aux]=1;
         k = aux;
   }

   if(visited[END]) return cost[END];
   else return -1;
}
```

## Dijkstra - Sem Memória Adicional
Mesmas instruções do algoritmo anterior, PORÉM nesse caso o algoritmo não guarda o vCost[], ou seja, os nodos percorridos para chegar de um nodo “ini” para um nodo “fim”.

No algoritmo abaixo foram comentadas linhas de impressão, onde é dito o nodo em questão e os nodos percorridos.

```C++
#include <cstring>
#include <iostream>
using namespace std;
#define MAX 100
#define INF 999999999
int N;
int graph[MAX][MAX];
int foi[MAX],custo[MAX];
int dijkstra(int INI, int FIM){
    int i, k, aux = 1,minimo=0;
    for(i=0 ; i<N ; i++) {
        foi[i] = 0;
        custo[i] = INF;
    }
    custo[INI] = 0;
    foi[INI] = 1;
    k = INI;
    int counter = 0;
    while(!foi[FIM] && minimo!=INF){
        //cout << counter << endl;
        counter++;
        minimo = INF;
        for(i=0 ; i<N ; i++) {
            //cout << "i: " << i << endl;
            if(!foi[i]){
                if(custo[i]>custo[k]+graph[k][i])
                    custo[i]=custo[k]+graph[k][i];
                if(custo[i]<minimo){
                    minimo=custo[i];
                    aux=i;
                }
            }
        }
        foi[aux]=1;
        k = aux;
    }

    if(foi[FIM]) return custo[FIM];
    else return -1;
}
```

## Simple Path entre dois vértices

O Algoritmo foi pego do problema hedge mazes da prova da maratona de 2011 – nacional, este algoritmo recebe um grafo com suas arestas e seta “componentes” para cada nodo do grafo.

Dois nodos tem a mesma componente quando: entre um nodo inicial e final há APENAS UM simple path possível.

    Simple Path – sequencia de nodos distintos que chegam de um nodo inicial a um final (sem repetição de nodos no caso). 

Seguindo o algoritmo abaixo, o teste das componentes eh realizado pela variável vis[MAX].


```C++
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#define MAX 10005
using namespace std;
vector <int> l[MAX];
int vis[MAX], viu[MAX], pai[MAX];
bool paiponte[MAX];
int cnt;

void dfs(int x){
   vis[x] = cnt++;
   viu[x] = vis[x];
   for (int i = 0; i < (int)l[x].size(); i++){
      if(l[x][i] != pai[x]){
         if(vis[l[x][i]] == -1){
            pai[l[x][i]] = x;
            dfs(l[x][i]);
            viu[x] = min(viu[x], viu[l[x][i]]);
         }
         viu[x] = min(viu[x], vis[l[x][i]]);
      }
   }
   for (int i = 0; i < (int)l[x].size(); i++){
      if(l[x][i] != pai[x] && viu[l[x][i]] > vis[x])
         paiponte[l[x][i]] = true;
   }
}

void dfsp(int x){
   vis[x] = cnt;
   for (int i = 0; i < (int)l[x].size(); i++){
      if(vis[l[x][i]] == -1 && ((pai[l[x][i]] == x && paiponte[l[x][i]]) || (pai[x] == l[x][i] && paiponte[x])) ){
         dfsp(l[x][i]);
      }
   }
}

/* função main para fins de exemplificação.
 */
int main(){
      /*Realizar a leitura da entrada.*/
      for (int i = 0; i < NUMERO_DE_VERTICES_DO_ATUAL_GRAFO; i++){
         pai[i] = vis[i] = viu[i] = -1;
         paiponte[i] = false;
         l[i].clear();
      }
      int x, y;
      for (int i = 0; i < QUANTIDADE_DE_ARESTAS_DO_GRAFO; i++){
         /*ler os dois vértices que pertencem a aresta*/
  /*No caso abaixo, o grafo é bidirecional*/
         l[x-1].push_back(y-1);
         l[y-1].push_back(x-1);
      }
      for (int i = 0; i < NUMERO_DE_VERTICES_DO_ATUAL_GRAFO; i++)
         if(vis[i] == -1){
            cnt = 0;
            dfs(i);
         }
      for (int i = 0; i < NUMERO_DE_VERTICES_DO_ATUAL_GRAFO; i++)
         vis[i] = -1;
      cnt = 0;

      for (int i = 0; i < NUMERO_DE_VERTICES_DO_ATUAL_GRAFO; i++)
         if (vis[i] == -1){
            dfsp(i);
            cnt++;
         }
      /*Ao final, basta fazer a seguinte comparação:*/
      if(vis[x] == vis[y])
         printf("Há uma Bridge entre X e Y (ou simple path).\n");
      else
         printf("Não há uma Bridge entre X e Y (ou simple path).\n");
      /*Se for um loop, volta em realizar a leitura de entrada:*/
  
   return 0;
}
```


## **(NÃO TESTADO)** Longest or Min Path in DAG

LONGEST OR MIM PATH IN DAG - Directed Acyclic Graphs

O(V + E)

```C++
void longest_path(int source) {
   for(int i = 1; i <= N; i++) {
      l_dist[i] = -90000000;
   }
   l_dist[source] = 0;

   for(int j = 1; j <= N; j++) {
      int v = top_sort[j];
      for(int i = 1; i <= N; i++) {
         if(graph[v][i] != 0) {
            if(l_dist[i] < l_dist[v] + graph[v][i]) {
               l_dist[i] = l_dist[v] + graph[v][i];
            }            
         }
      }
   }
}
```

## **(NÃO TESTADO)** Connected Components
CONNECTED COMPONENTES - Connected component of an undirected graph is a subgraph in which any two vertices are connected to each other by paths, and which is connected to no additional vertices.
```C++
void connected_components() { 
   int count_cc = 0;
   for(int i = 1; i <= N; i++) {
      if(discovered[i] == false) {
         count_cc++;
         dfs(i);
      }
   }
   cout << count_cc << endl;
}
```

## **(NÃO TESTADO)** Strongly Connected Components
STRONGLY CONNECTED COMPONENTES - Kosaraju's algorithm finds strongly-connected components in a directed graph. 
A directed graph is called strongly connected if there is a path from each vertex in the graph to every other vertex. In particular, this means paths in each direction; a path from a to b and also a path from b to a.
```C++
int N;
vector<int> SortNodes;
typedef struct {
   list<int> to;
} graph;
graph G[MAX];
graph Gt[MAX];
int component[MAX];
int visited[MAX];
int counter_scc;

void search(int v) {
   visited[v] = true;   

   for(list<int>::iterator it = G[v].to.begin(); it != G[v].to.end(); ++it){
      if(!visited[*it]) {
         search(*it);
      }
   }
   SortNodes.push_back(v);
}
void searchT(int v, int counter) {
   visited[v] = false; 
   component[v] = counter;

   for(list<int>::iterator it = Gt[v].to.begin(); it != Gt[v].to.end(); ++it){
      if(visited[*it]) {
         searchT(*it, counter);
      }
   }
}
void kosaraju(){
   for(int i = 1; i <= N; i++) {
      if(!visited[i]) {
         search(i);   
      }
   }
   for(int i = SortNodes.size() - 1; i >= 0; i--) {
      if(visited[ SortNodes[i] ]) {
         searchT(SortNodes[i], ++counter_scc);
      }
   }
}
```

## **(NÃO TESTADO)** Bridge
BRIDGE -  Bridge (also known as a cut-edge or cut arc or an isthmus) is an edge whose deletion increases the number of connected components
```C++
vector<bool> visited;
vector<int> prev, low, d;
vector<vector<int> > g;
vector<vector<bool> > is_bridge;
int N, counter;
counter = 0;

visited.assign(n, false);
prev.assign(n, -1);
low.resize(n);
d.resize(n);
g.assign(n, vector<int>());
is_bridge.assign(n, vector<bool>(n, false));

for (int i=0; i<n; ++i){
   if (!visited[i]){
      dfs(i);
   }
}

void dfs(int u){
   visited[u] = true;
   d[u] = low[u] = counter++;
   for (int i=0; i< (int)g[u].size(); ++i){
      int v = g[u][i];
      if (prev[u] != v){
         if(!visited[v]){
            prev[v] = u;
            dfs(v);
            if (d[u] < low[v]){
               is_bridge[u][v] = is_bridge[v][u] = true;
            }
            low[u] = min(low[u], low[v]);
         }else{
            low[u] = min(low[u], d[v]);
         }
      }
   }
}
```

## **(NÃO TESTADO)** Articulation Points
ARTICULATION POINTS - Vértice de corte ou ponto de articulação é um vértice de um grafo tal que a remoção deste vértice provoca um aumento no número de componentes conectados.
```C++
int N;
int graph[MAX][MAX];
int low[MAX];
int un[MAX];
int counter;
int art_points[MAX];
void find_art_points(int v, int u){
   low[v] = un[v] = counter++;
   for(int w = 1; w <= N; w++){
      if(graph[v][w] == 1 && w != u) {
         if(un[w] == 0) {
            find_art_points(w, v);
            low[v] = min(low[v], low[w]);
            if(un[v] == 1 && un[w] != 2) {
               art_points[v] = 1;
            }
            if(un[v] != 1 && low[w] >= un[v]){
               art_points[v] = 1;
            }
         } else {
            low[v] = min(low[v], un[w]);
         }
      }   
   }
}


for (int i = 1; i <= N; i++){
   if (un[i] == 0){
      find_art_points(i, -1);
   }
}
```
