# Algoritmos de Busca e Ordenação

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
