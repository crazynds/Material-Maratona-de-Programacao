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