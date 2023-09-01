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
/*tendo ‘l’ o comprimento do lado, 'raio' sendo o raio do círculo o qual o polígono é circunscrito (apótema) e
‘n’ o número de lados do polígono:*/

/*Fórmula da apótema do polígono usando o raio encontrado na fórmula acima*/
apotema = cos(PI/(double)n) * raio;

/*Área de um círculo inscrito em um polígono baseado na apótema encontrada na fórmula acima*/
area1 = PI*apotema*apotema;

/*Área de um círculo circunscrito num polígono com o raio encontrado acima*/
area2 = PI*raio*raio;

/* Calcula a area de um poligono irregular */

struct Point {
	float x, y;
};

//numP = número de pontos
float area_do_poligono(Point v[], int numP)
{
	float area = (v[numP - 1].y + v[0].y) * (v[numP - 1].x - v[0].x);

	for (int i = 0; i < numP - 1; i++)
    	{
		area += (v[i].y + v[i + 1].y) * (v[i].x - v[i + 1].x);
	}

	if (area < 0)
		area *= -1;

	return area / 2;
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

O produto vetorial entre os vetores $a$ e $b$ resulta em um vetor ortogonal (perpendicular) a ambos.
A norma do vetor resultante é: $|a| * |b| * sin(\alpha)$, sendo $\alpha$ o ângulo entre os vetores.

Se esse resultado for $0$, significa que os vetores são parelelos.

Esse resultado consiste na área do paralelogramo formado pelos vetores (ao dividir por 2, obtém-se a área do triângulo formado pelos vetores)

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

O produto escalar entre os vetores $a$ e $b$ resulta em: $|a| * |b| * cos(\alpha)$, sendo $\alpha$ o ângulo entre os vetores.

Se o resultado for $0$, significa que os vetores são perpendiculares.

```c++
float dot(Point a, Point b) {
    return (a.x * b.x) + (a.y * b.y) + (a.z * b.z);
}
```

## Norma

A norma nada mais é que o tamanho do vetor. Para obtê-la, basta realizar a raiz quadrada da soma dos quadrados dos componentes.

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

## (NÃO TESTADO) Sweep Line 

```c++
#include <bits/stdc++.h>
using namespace std;
 
// A point in 2D plane
struct Point
{
    int x, y;
};
 
// A line segment with left as Point
// with smaller x value and right with
// larger x value.
struct Segment
{
    Point left, right;
};
 
 
// An event for sweep line algorithm
// An event has a point, the position
// of point (whether left or right) and
// index of point in the original input
// array of segments.
struct Event {
    int x, y;
    bool isLeft;
    int index;
    Event(int x, int y, bool l, int i) : x(x), y(y), isLeft(l), index(i) {}
 
    // This is for maintaining the order in set.
    bool operator<(const Event& e) const {
            if(y==e.y)return x<e.x;
            return y < e.y;
    }
};
 
 
// Given three collinear points p, q, r, the function checks if
// point q lies on line segment 'pr'
bool onSegment(Point p, Point q, Point r)
{
    if (q.x <= max(p.x, r.x) && q.x >= min(p.x, r.x) &&
        q.y <= max(p.y, r.y) && q.y >= min(p.y, r.y))
       return true;
 
    return false;
}
 
// To find orientation of ordered triplet (p, q, r).
// The function returns following values
// 0 --> p, q and r are collinear
// 1 --> Clockwise
// 2 --> Counterclockwise
int orientation(Point p, Point q, Point r)
{
    // See https://www.geeksforgeeks.org/orientation-3-ordered-points/
    // for details of below formula.
    int val = (q.y - p.y) * (r.x - q.x) -
              (q.x - p.x) * (r.y - q.y);
 
    if (val == 0) return 0;  // collinear
 
    return (val > 0)? 1: 2; // clock or counterclock wise
}
 
// The main function that returns true if line segment 'p1q1'
// and 'p2q2' intersect.
bool doIntersect(Segment s1, Segment s2)
{
    Point p1 = s1.left, q1 = s1.right, p2 = s2.left, q2 = s2.right;
 
    // Find the four orientations needed for general and
    // special cases
    int o1 = orientation(p1, q1, p2);
    int o2 = orientation(p1, q1, q2);
    int o3 = orientation(p2, q2, p1);
    int o4 = orientation(p2, q2, q1);
 
    // General case
    if (o1 != o2 && o3 != o4)
        return true;
 
    // Special Cases
    // p1, q1 and p2 are collinear and p2 lies on segment p1q1
    if (o1 == 0 && onSegment(p1, p2, q1)) return true;
 
    // p1, q1 and q2 are collinear and q2 lies on segment p1q1
    if (o2 == 0 && onSegment(p1, q2, q1)) return true;
 
    // p2, q2 and p1 are collinear and p1 lies on segment p2q2
    if (o3 == 0 && onSegment(p2, p1, q2)) return true;
 
     // p2, q2 and q1 are collinear and q1 lies on segment p2q2
    if (o4 == 0 && onSegment(p2, q1, q2)) return true;
 
    return false; // Doesn't fall in any of the above cases
}
 
 
// Find predecessor of iterator in s.
 set<Event>::iterator pred(set<Event> &s, set<Event>::iterator it) {
    return it == s.begin() ? s.end() : --it;
}
 
// Find successor of iterator in s.
set<Event>::iterator succ(set<Event> &s, set<Event>::iterator it) {
    return ++it;
}
 
// Returns true if any two lines intersect.
int isIntersect(Segment arr[], int n)
{
    unordered_map<string,int> mp;  // to note the pair for which intersection is checked already
    // Pushing all points to a vector of events
    vector<Event> e;
    for (int i = 0; i < n; ++i) {
        e.push_back(Event(arr[i].left.x, arr[i].left.y, true, i));
        e.push_back(Event(arr[i].right.x, arr[i].right.y, false, i));
    }
 
    // Sorting all events according to x coordinate.
    sort(e.begin(), e.end(), [](Event &e1, Event &e2) {return e1.x < e2.x;});
 
    // For storing active segments.
    set<Event> s;
     int ans=0;
    // Traversing through sorted points
    for (int i=0; i<2*n; i++)
    {
        Event curr = e[i];
        int index = curr.index;
 
        // If current point is left of its segment
        if (curr.isLeft)
        {
            // Get above and below points
            auto next = s.lower_bound(curr);
            auto prev = pred(s, next);
            // Check if current point intersects with
            // any of its adjacent
            bool flag=false;
            if (next != s.end() && doIntersect(arr[next->index], arr[index])){
                string s=to_string(next->index+1)+" "+to_string(index+1);
                if(mp.count(s)==0){mp[s]++;ans++;} //if not already checked we can increase count in map
            }
            if (prev != s.end() && doIntersect(arr[prev->index], arr[index])){
                    string s=to_string(prev->index+1)+" "+to_string(index+1);
                if(mp.count(s)==0){mp[s]++;ans++;} //if not already checked we can increase count in map
            }
            // if same line segment is there then decrease answer as it got increased twice
            if(prev != s.end() && next != s.end() && next->index==prev->index)ans--;
 
 
            // Insert current point (or event)
            s.insert(curr);
        }
 
        // If current point is right of its segment
        else
        {
            // Find the iterator
            auto it=s.find(Event(arr[index].left.x, arr[index].left.y, true, index));
            // Find above and below points
            auto next = succ(s, it);
            auto prev = pred(s, it);
 
            // If above and below point intersect
            if (next != s.end() && prev != s.end())
               {  string s=to_string(next->index+1)+" "+to_string(prev->index+1);
                    string s1=to_string(prev->index+1)+" "+to_string(next->index+1);
                   if (mp.count(s)==0&&mp.count(s1)==0&&doIntersect(arr[prev->index], arr[next->index]))
                    ans++;
                    mp[s]++;
                  }
 
            // Remove current segment
            s.erase(it);
 
        }
    }
    //print pair of lines having intersection
 
    for(auto &pr:mp){
        cout<<"Line: "<<pr.first<<"\n";
    }
    return ans;
}
 
// Driver code
int main() {
    Segment arr[] = { {{1, 5}, {4, 5}}, {{2, 5}, {10, 1}},{{3, 2}, {10, 3}},{{6, 4}, {9, 4}},{{7, 1}, {8, 1}}};
    int n = sizeof(arr)/sizeof(arr[0]);
    cout<<"Number of intersection points: "<<isIntersect(arr, n);
    return 0;
}
```

[sweepLine](https://www.geeksforgeeks.org/given-a-set-of-line-segments-find-if-any-two-segments-intersect/)
