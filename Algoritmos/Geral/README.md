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


