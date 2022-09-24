
# Tratamento de Entrada e Saída de Dados

Neste material são apresentadas algumas formas de fazer a leitura de dados do arquivo texto presentes nos problemas da maratona, nas linguagens C, Java e Python. Para mais detalhes, veja o Capítulo 5 do livro Art of programming contest.


## 1. Extremely Basic: Beecrowd – **1001**

Observação: apenas uma entrada de dados. Nunca esquecer o ‘\n’ ao final da impressão. 


### Códigos
 - C:
```C++
int main() 
{
    int a, b;
    scanf("%d%d", &a, &b);
    printf("X = %d\n", a + b);
    return 0;
}
```

## 2. [The Circumference of the Circle](https://onlinejudge.org/external/4/438.pdf) – **438**

_Input Specification: The input file will contain one or more test cases. Each test case consists of one line containing six real numbers x1, y1, x2, y2, x3, y3 representing the coordinates of the three points. The diameter of the circle determined by the three points will never exceed a million. Input is terminated by end of file._

### Input:

```
0.0 -0.5 0.5 0.0 0.0 0.5
0.0 0.0 0.0 1.0 1.0 1.0
5.0 5.0 5.0 7.0 4.0 6.0
0.0 0.0 -1.0 7.0 7.0 7.0
50.0 50.0 50.0 70.0 40.0 60.0
0.0 0.0 10.0 0.0 20.0 1.0
0.0 -500000.0 500000.0 0.0 0.0 500000.0

```

### Códigos
 - C:
```C
int main(void)
{
   float v[6];

   while( true )
   {
      int cont = scanf(" %f %f %f %f %f %f",  
         &v[0],&v[1],&v[2],&v[3],&v[4],&v[5] );
      if( cont != 6 )
         break;
      processa()
   }
}

// while( scanf("%d %d", &p,&q) !=EOF ) 
// while( scanf("%ld %ld", &p,&q) !=EOF ) 
// while( scanf("%lld %lld", &p,&q) !=EOF ) 
```
 - Java:
```Java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Prob1 {
    public static void main(String[] args) throws IOException {

        // todos arrays em java são dinamicamente alocados
        float[] dados = new float[6];
        // inicializamos um reader com buffer para ler entradas
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            String  lines = br.readLine();
            String[] strs = lines.trim().split("\\s+");

            if (strs.length != 6) {
                break;
            }

            for (int i = 0; i < dados.length; i++) {
                dados[i] = Float.parseFloat(strs[i]);
            }

            for (int i = 0; i < dados.length; i++) {
                System.out.println(dados[i]);
            }
        }

        // processa()

    }
}

```
 - Python:
```Python
while True:
    # Le uma linha inteira, e divide ela para cada espaço
    arr = input().split()
    # Converte cada string da lista em inteiro
    arr = list(map(int,arr))
    if len(arr)!=6:
        break;
    # Processa os dados
    process()
```

## 3. [Binomial Showdown](https://onlinejudge.org/external/5/530.pdf) – **530**

_Input Specification: The input file will contain one or more test cases. Each test case consists of one line containing two integers n (n>=1) and k (0<=k<=n) . Input is terminated by two zeroes for n and k._

### Input: 
```
4 2
10 5
49 6
0 0
```
### Códigos:
- C:
```C
int main()
{
   int n,k;
   while(true)
   {
      scanf("%d %d",&n,&k);
      if(n==0 && k==0)
        return 0;
      Processa();
   }
}
```
- Java:
```Java
import java.util.Scanner;

public class Prob2 {
    public static void main(String[] args) {
        int n, k;
        Scanner sc = new Scanner(System.in);
        while (true) {
            n = sc.nextInt();
            k = sc.nextInt();
            if (n == 0 && k == 0) {
                System.exit(0);
            }
            // processa ();
        }
    }
}
```
- Python:
```Python
while True: 
    arr = input().split()
    a,b = list(map(float,arr))
    if a == 0 and b==0:
        break;
    process()
```
- C++
```C++
```

## 4. [Bingo!](https://www.beecrowd.com.br/judge/en/problems/view/1136) – **1136**


_Input Specification: Each test case is given using exactly two lines. The first line contains two integers N and B. The meaning of N was described above (1<= N<= 90), while B represents the number of balls which remained in the bag (2<= B<= N + 1). The second line contains B distinct integers bi, indicating the balls which remained in the bag (0<= bi<= N). The last test case is followed by a line containing two zeros._

### Input:
```
6 7
2 1 3 4 0 6 5
5 4
5 3 0 1
5 3
1 5 0
0 0
```
### Código:
- C:
```C
int main(void)
{
   char N, B;
   int vetBolas[SIZE]; 

   while(true)
   {
      scanf(" %d %d", &N, &B);
      if( N == 0 && B == 0)
         break;
      for(char i=0; i < B; i++)
         scanf("%d", &vetBolas[i]);

      processa();
   }
}
```
- Java:
```Java
import java.util.Scanner;

public class Prob3 {
    public static void main (String[] args) {
        char N, B;
        Scanner sc = new Scanner(System.in);
        while(true) {
            N = (char)sc.nextInt();
            B = (char)sc.nextInt();

            if (N == 0 && B == 0) break;

            int[] vetBolas = new int[B];

            for (char i = 0; i < B; i++) {
                vetBolas[i] = sc.nextInt();
            }

            // processa()
        }
    }
}
```
- Python:
```Python
while True:
    arr = input().split()
    a,b = list(map(int,arr))
    if a==0 and b==0:
        break;
    vet = input().split()
    process()
```
- C++
```C++
```
