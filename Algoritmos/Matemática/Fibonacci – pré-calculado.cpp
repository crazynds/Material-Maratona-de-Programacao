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