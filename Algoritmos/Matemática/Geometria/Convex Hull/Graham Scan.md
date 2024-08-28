# Graham Scan
*Jaime Antonio Daniel Filho e Juliano de Mello Pasa*

## O que é um envoltório convexo?
O "convex hull", como também é conhecido, é definido como o menor polígono convexo que engloba todos os pontos de um certo conjunto. Convexo significa que nenhuma das diagonais do polígono cruza o lado de fora.

![poligono_convexo_concavo](https://github.com/jaimeadf/Material-da-Maratona/assets/40345645/ae0ae734-6ea0-4666-acc4-0134cf519d5a)

Uma das maneiras de visualizar o envoltório convexo é utilizando um elástico de borracha. Para isso, suponha que os pontos são pregos em uma superfície plana. Imagine agora, o que aconteceria se você esticasse um elástico em torno dos pregos e depois o soltasse, permitindo que ele se contraia. O elástico englobaria todos os pregos e encostaria apenas nos mais externos, ou seja, nos que fazem parte do envóltorio convexo.

![analogia_do_elastico](https://github.com/jaimeadf/Material-da-Maratona/assets/40345645/2ee1f15e-086e-41e6-9e4d-d5476f6ecebb)

## O algoritmo

O Exame de Graham é um dos algoritmos utilizados para encontrar o envóltorio convexo de um conjunto de pontos. O algoritmo computa o subconjunto de pontos pertencentes ao envóltorio junto à ordem em que aparecem.

O primeiro passo é encontrar um ponto que certamente pertence ao envóltorio convexo. O ponto com menor coordenada y, por exemplo, é um deles. Caso mais de um ponto existir nessa mesma coordenada y, escolhemos o com a maior coordenada x. Tal ponto é chamado de P.

![algoritmo_parte_1](https://github.com/jaimeadf/Material-da-Maratona/assets/40345645/bc455bd2-65b7-4c3a-8c32-be0f4e25b991)

Depois, os pontos precisam ser ordenados pelo ângulo que ele forma com o ponto inicial P em relação ao eixo x. Se dois pontos possuírem o mesmo ângulo, ordenamos da maior para menor distância em relação a P.

![algoritmo_parte_2](https://github.com/jaimeadf/Material-da-Maratona/assets/40345645/99816ad2-f911-4f0d-b380-4239194ae5d3)

O algoritmo prossegue percorrendo todos os pontos no vetor ordenado e verificando se ele faz parte ou não do envóltorio convexo. Isso é determinado testando se o ponto atual realiza uma curva no sentido horário ou no sentido anti-horário em relação aos dois pontos anteriores. Caso a curva for no sentido horário, o ponto não pertence ao envóltorio e está dentro do polígono.

![algoritmo_parte_3](https://github.com/jaimeadf/Material-da-Maratona/assets/40345645/9c9ec097-8273-41c0-b029-367b50066ec1)

Os pontos pertencentes ao envóltorio são armazenados em uma pilha. Desse modo, a medida que percorremos o vetor, adicionamos um ponto e, enquanto for necessário girar no sentido horário partindo dos dois últimos pontos, removemos o topo da pilha.

O verdadeiro ângulo entre os pontos não precisa ser calculado para determinar o sentido da curva. Isso pode ser obtido por meio do cálculo do produto vetorial entre os dois vetores. O resultado é um vetor perpendicular com o sentido dado pela regra da mão direita.

![regra_da_mao_direita](https://github.com/jaimeadf/Material-da-Maratona/assets/40345645/5f35460c-80dd-4069-a3b3-6c7d32e91100)

Como os pontos pertencem ao plano xOy, o vetor perpendicular será constituído somente da componente z. Assim, dados três pontos $P_1=(x_1, y_1)$ $P_1=(x_2, y_2)$ e $P_3=(x_3, y_3)$, a componente z de $\vec{P_1P_2}\times\vec{P_1P_3}$ é calculada pela expressão $(x_2 - x_1)(y_3 - y_1) - (y_2 - y_1)(x_3 - x_1)$. Se o resultado for igual a 0, os pontos são colineares. Se for positivo, os três pontos formam uma curva no sentido anti-horário. Se for negativo, estão no sentido horário.

![algoritmo_parte_4](https://github.com/jaimeadf/Material-da-Maratona/assets/40345645/dfb81982-cdd6-4b61-9639-451a268d23b7)

Exemplo de excução do algoritmo com posição dos pontos na pilha. O ponto $P$ é o ponto atual do vetor sendo analisado. Os pontos $-1$ e $-2$ correspondem ao ponto no topo da pilha e o ponto logo abaixo (notação de índices em Python). Os pontos em $X$ vermelho são os pontos excluídos do polígono. As linhas verdes são arestas que farão parte do polígono convexo. As linhas azuis são as arestas que estão sendo analisadas, enquanto as linhas vermelhas são linhas que podem ser removidas. As linhas vermelhas serão removidas caso os pontos analisados não forme uma curva no sentido anti-horário.

![executionGif](https://github.com/jaimeadf/Material-da-Maratona/assets/40345645/06bf62cc-9cf2-402c-ae7a-a9869c3e43e6)

## Implementação C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

struct Point
{
    int x;
    int y;
};

// Calcula a distância euclidiana entre dois pontos.
int distance_squared(const Point &a, const Point &b)
{
    int dx = a.x - b.x;i
    int dy = a.y - b.y;

    return dx * dx + dy * dy;
}

// Calculate o produto vetorial entre AB e AC:
// AB x AC = 0 -> colinear
// AB x AC > 0 -> anti-horário
// AB x AC < 0 -> horário
int cross_product(const Point &a, const Point &b, const Point &c)
{
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
}

// ALgoritmo de Graham Scan para encontrar o menor envoltório convexo.
std::vector<Point> graham_scan(std::vector<Point> &points)
{
    // Se existirem 3 pontos, o menor envoltório convexo é formado por eles.
    if (points.size() <= 3)
    {
        return points;
    }

    // Vetor que armazena os pontos que formam o envoltório convexo.
    std::vector<Point> hull;

    // Inicia P0 com o primeiro ponto do vetor.
    Point p0 = points[0];

    // Encontra o ponto mais baixo e mais à direita.
    for (size_t i = 1; i < points.size(); i++)
    {
        if (points[i].y < p0.y || (points[i].y == p0.y && points[i].x > p0.x))
        {
            p0 = points[i];
        }
    }

    // Ordena os pontos de acordo com o ângulo que eles formam com P0.
    // Isto é, de modo que eles sempre estejam no sentido anti-horário
    // em relação a P0.
    std::sort(points.begin(), points.end(), [&](Point &a, Point &b) {
        int product = cross_product(p0, a, b);

        if (product != 0)
        {
            // Se o produto for positivo, o ponto mais à direita é o A, pois
            // giramos no sentido anti-horário partindo de A para chegarmos em B.
            return product > 0;
        }

        int distance_b = distance_squared(p0, b);
        int distance_a = distance_squared(p0, a);

        // Se os pontos forem colineares, o mais distante de P0 vem primeiro.
        return distance_a < distance_b;
    });

    // Percorre e verifica o restante do vetor de pontos.
    for (size_t i = 0; i < points.size(); i++)
    {
        // Enquanto ponto atual e os dois últimos pontos no envoltório
        // formarem um ângulo horário, remova o ponto do topo do envoltório.
        while (hull.size() >= 2 && cross_product(hull[hull.size() - 2], hull[hull.size() - 1], points[i]) <= 0)
        {
            hull.pop_back();
        }

        // Adiciona o ponto ao envoltório convexo.
        hull.push_back(points[i]);
    }

    return hull;
}

int main()
{
    std::vector<Point> points = {
    };

    std::vector<Point> hull = graham_scan(points);

    for (const Point &point : hull)
    {
        std::cout << "(" << point.x << ", " << point.y << ")" << std::endl;
    }

    return 0;
}
```

## Outra forma de calcular orientação

Na implementação em Python, a orientação foi calculada de uma forma diferente. Em vez de utilizar o produto vetorial entre os dois vetores formados pelos 3 pontos, foi calculada a diferença entre suas subidas. As operações são idênticas, mas as componentes multiplicadas são diferentes. Em decorrência disso, para pontos no sentido anti-horário, o valor será negativo, enquanto para pontos no senti horário o valor será positivo.

![desmos-graph (0)](https://github.com/jaimeadf/Material-da-Maratona/assets/40345645/ca2fd619-5cf5-426e-8798-dc4c99368588)

## Implementação Python
```python
from functools import cmp_to_key


# Calcula a orientacao de 3 pontos com base na diferença entre suas subidas.
# Essa funcao eh usada no ordenamento e no scan.
# A orientacao eh dada da seguinte forma:
#
#   valor < 0: os pontos estao no sentido anti-horario
#   valor = 0: os pontos sao colineares
#   valor > 0: os pontos estao no sentido horario
def CalculateOrientation(p1, p2, p3):
    return (p2[1] - p1[1]) * (p3[0] - p2[0]) - (p3[1] - p2[1]) * (p2[0] - p1[0])


# Calcula o quadrado da distancia entre dois pontos.
# Essa funcao eh usada no ordenamento.
def CalculateSquaredDistance(p1, p2):
    return (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2


# Funcao de comparacao que sera utilizada pelo sorted() do python.
# Funcoes de comparacao devem retornar valores inteiros da seguinte forma:
# 
#   valor < 0: p1 vem antes de p2  
#   valor = 0: p1 eh igual p2
#   valor > 0: p1 vem depois de p2
#
# No caso do scan de Graham, pontos com orientacao anti-horaria devem ser os primeiros da lista,
# entao basta retornar o valor da orientacao, pois a orientacao anti-horaria tem valor negativo.
# Caso a orientacao seja igual a zero, o ponto mais proximo do ponto inicial deve vir primeiro.
def CompareOrientation(p1, p2):
    orientation = CalculateOrientation(startingPoint, p1, p2)

    if orientation: 
        return orientation
    if CalculateSquaredDistance(startingPoint, p1) <= CalculateSquaredDistance(startingPoint, p2):
        return -1
    return 1


if __name__ == "__main__":
    n = int(input())
    points = []

    assert n > 2, "Nao e possivel montar um poligono com menos de 3 pontos"

    for i in range(n):
        points.append(tuple(map(int, input().split(" "))))

    # Esse ponto deve ser global pois ele eh utilizado na funcao de comparacao do sorted().
    # A funcao de comparacao recebe apenas dois valores (os valores que estao sendo comparados), 
    # e por isso nao eh possivel passar o startingPoint como terceiro parametro.
    global startingPoint
    startingPoint = points[0]

    # Laco para encontrar o ponto com o menor Y.
    # Se dois pontos tiverem o mesmo Y, eh selecionado o mais a esquerda
    # Complexidade: O(n)
    for r in points:
        if r[1] < startingPoint[1]:
            startingPoint = r
        elif r[1] == startingPoint[1] and r[0] < startingPoint[0]:
            startingPoint = r

    # Ordenacao dos pontos com base no angulo com o startingPoint
    # key=cmp_to_key() eh utilizado para alterar a funcao de comparacao
    # entre dois valores da estrutura
    # Complexidade: O(nLogN)
    points = sorted(points, key=cmp_to_key(CompareOrientation))

    # O ponto inicial sempre fara parte do fecho convexo
    filteredPoints = [startingPoint]

    # Nessa etapa do algoritmo, sao removidos os pontos colineares
    # e mantidos somente o ponto mais distante.
    # Caso um ponto nao seja colinear com o proximo ponto, entao ele 
    # eh o ponto mais distante do startingPoint com aquele angulo
    # Complexidade: O(n)
    for i in range(1, len(points) - 1):
        if CalculateOrientation(startingPoint, points[i], points[i+1]):
            filteredPoints.append(points[i])
    filteredPoints.append(points[-1])

    assert len(filteredPoints) > 2, "Nao ha mais de 2 pontos nao colineares entre si"

    # A etapa final do algoritmo eh o scan em si.
    # Os pontos que fazem parte do fecho sao guardados em uma pilha.

    # A pilha eh iniciada com os 3 primeiros pontos filtrados.
    resultStack = [startingPoint, filteredPoints[1], filteredPoints[2]]

    # Para cada ponto p restante, eh verificada sua orientacao com o ultimo
    # e o penultimo ponto da pilha. Se esses 3 pontos forem colineares ou de
    # orientacao horaria, significa que o ultimo ponto da pilha nao faz parte
    # do fecho, e entao ele eh removido. Agora, o ponto p sera comparado com os
    # novos ultimo e penultimo pontos.
    # Caso o ponto p tenha uma orientacao anti-horária, ele eh adicionado ao topo da pilha
    # Complexidade: O(n)
    for p in filteredPoints[3:]:
        while len(resultStack) > 1 and CalculateOrientation(resultStack[-2], resultStack[-1], p) >= 0:
            resultStack.pop()
        resultStack.append(p)

    print(resultStack)
```


## Grande Tratado da Bytelândia
A Grande Guerra da Bytelândia chegou ao fim. Os reinos restantes agora estão discutindo o Tratado
de Divisão, que dividirá todas as terras do mundo entre eles. Este tratado se refere não apenas ao
mundo conhecido, mas também a quaisquer territórios ainda não descobertos ou habitados, incluindo
terra ou mar. Podemos assumir que o mundo é um plano infinito.

Cada reino no continente da Bytelândia tem uma única capital, e o Tratado de Divisão será baseado
em suas localiza¸cões: ele declara que cada pedaço de terra pertence ao reino cuja capital é a mais
próxima em um voo de pássaro (ou em linha reta). Em outras palavras: onde quer que você esteja no
mundo, se $C$ é a capital mais próxima de você, você estará no território do reino de C. Se houver um
empate entre as distâncias de duas ou mais capitais, esse lugar estará na fronteira entre seus reinos.

Sob este tratado, alguns reinos podem ficar cercados por outros, enquanto outros reinos podem
ficar com território ilimitado. Por isso, alguns monarcas estão contestando o tratado. Para informar
essa discussão, eles exigem sua ajuda. Dadas as coordenadas das localizações de cada capital no
continente da Bytelândia, você deve descobrir quais reinos teriam territórios infinitos sob o Tratado
de Divisão.

### Entrada
A primeira linha da entrada contém um único inteiro $N (2 ≤ N ≤ 10^5)$, o número de reinos.
Cada reino é identificado por um número inteiro único entre 1 e N. Cada uma das N linhas seguintes
contém dois inteiros $X$ e $Y$ $(0 ≤ X, Y ≤ 10^4)$, as coordenadas 2D da localização da capital de um
reino. As capitais são dadas em ordem crescente de identificador do reino, não há duas capitais com
a mesma localização, e você pode assumir que toda capital tem tamanho insignificante.

### Saída
Imprima uma única linha com uma lista de inteiros separados por espaço em ordem crescente:
os identificadores dos reinos que teriam territórios infinitos sob o Tratado de Divisão descrito. É
garantido que sempre haverá pelo menos um reino assim.

<hr>

O problema fornece uma série de reinos, representados por pontos, e quer descobrir quais deles possuem terrenos infinitos. Utilizando o Diagrama de Voronoy, uma forma de decomposição que divide o espaço em áreas mais próximas a determinado pontos, podemos fácilmente visualizar o problema.

![voronoy](https://github.com/jaimeadf/Material-da-Maratona/assets/40345645/16589959-2bc6-4a85-b324-f90f1ef7e2ad)

Com o desenho dos pontos, é possível perceber que os reinos com terrenos infinitos são aqueles que fazem parte do envóltorio convexo. Entretanto, torna-se necessário realizar algumas adaptações no algoritmo de Graham Scan, pois, diferentemente do problema original, precisamos considerar também os pontos que estão na borda do envoltório, mas não são vértices do menor polígono.

O primeiro passo, então, é modificar o nosso algoritmo para que ele não remova pontos colineares, isto é, os pontos em que o produto vetorial seja igual a 0. 

### C++
```cpp
        // Modificamos a regra para remover os pontos apenas no sentido horário, ou seja, apenas
        // os que o produto vetorial for negativo (< 0).
        while (hull.size() >= 2 && cross_product(hull[hull.size() - 2], hull[hull.size() - 1], points[i]) < 0)
        {
            hull.pop_back();
        }
```

### Python
```python
        # O trecho que remove os pontos colineares deve ser removido da implementação
        for i in range(1, len(points) - 1):
            if CalculateOrientation(startingPoint, points[i], points[i+1]):
                filteredPoints.append(points[i])
        filteredPoints.append(points[-1])

        # O trecho do scan deve ser modificado, para remover somente os pontos no sentido horário, ou seja,
        # apenas os que a diferença entre a subida seja positiva (> 0).
        while len(resultStack) > 1 and CalculateOrientation(resultStack[-2], resultStack[-1], p) > 0:
            resultStack.pop()
```

Isso, porém, gera um pequeno problema. Quando os pontos possuírem o mesmo ângulo com o ponto inicial P, o algoritmo verificará os pontos do mais próximo para o mais distante pelas nossas regras de ordenação. Entretanto, caso esse pontos sejam os últimos, a curva realizada quando partirmos para o ponto seguinte será no sentido horário e o ponto anterior será removido.

![colineares](https://github.com/jaimeadf/Material-da-Maratona/assets/40345645/ece6be0a-7a55-4b28-a9be-93d42370a3d6)

*O algoritmo verifica inicialmente o ponto F e, quando parte para o ponto E, uma curva horária é formada e o F removido. Os polígono resultante será ABCDE.*

A solução para esse caso é reverter a ordem dos pontos colineares com maior ângulo para que eles sejam verificados da maior para a menor distância.
```cpp
    std::sort(...);

    size_t colinear_index = points.size() - 2;

    // Encontra os últimos pontos colineares em relação a P0.
    while (colinear_index > 0 && cross_product(p0, points.back(), points[colinear_index]) == 0)
    {
        colinear_index--;
    }

    // Inverte os pontos colineares para serem ordenados da maior para a menor distância.
    std::reverse(points.begin() + colinear_index + 1, points.end());
```

Outra solução para tratar os últimos pontos colineares é verificar se há mais pontos colineares entre o ponto inicial e o último ponto do polígono convexo. Caso haja mais pontos colineares ($CalculateOrientation == 0$), eles serão adicionados em um vetor. Esse vetor só será adicionado à pilha final caso existam outros pontos no polígono que não são colineares entre o último ponto e o ponto inicial. Essa extensão dos pontos resultantes deve seguir essa regra para evitar que os pontos sejam reinseridos caso o polígono inicialmente calculado seja composto somente de pontos colineares (os primeiros pontos calculados).
```python
    lastCollinear = []

    for i in range(len(reinos) - 2):
        if not CalculateOrientation(resultStack[-1], reinos[-2-i], start):
            lastCollinear.append(reinos[-2-i])
        else:
            resultStack.extend(lastCollinear)
            break
```

Por fim, adicionamos a leitura das entradas e imprimimos os pontos ordenados por um campo identificador.

## C++
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

struct Point
{
    int id;

    int x;
    int y;
};

int distance_squared(const Point &a, const Point &b)
{
    int dx = a.x - b.x;
    int dy = a.y - b.y;

    return dx * dx + dy * dy;
}

int cross_product(const Point &a, const Point &b, const Point &c)
{
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
}

std::vector<Point> graham_scan(std::vector<Point> &points)
{
    if (points.size() <= 3)
    {
        return points;
    }

    std::vector<Point> hull;

    Point p0 = points[0];

    for (size_t i = 1; i < points.size(); i++)
    {
        if (points[i].y < p0.y || (points[i].y == p0.y && points[i].x > p0.x))
        {
            p0 = points[i];
        }
    }

    std::sort(points.begin(), points.end(), [&](Point &a, Point &b) {
        int product = cross_product(p0, a, b);

        if (product != 0)
        {
            return product > 0;
        }

        int distance_b = distance_squared(p0, b);
        int distance_a = distance_squared(p0, a);

        return distance_a < distance_b;
    });

    size_t colinear_index = points.size() - 2;
    while (colinear_index > 0 && cross_product(p0, points.back(), points[colinear_index]) == 0)
    {
        colinear_index--;
    }

    std::reverse(points.begin() + colinear_index + 1, points.end());

    for (size_t i = 0; i < points.size(); i++)
    {
        while (hull.size() >= 2 && cross_product(hull[hull.size() - 2], hull[hull.size() - 1], points[i]) < 0)
        {
            hull.pop_back();
        }

        hull.push_back(points[i]);
    }

    return hull;
}

int main()
{
    std::ios_base::sync_with_stdio(false);

    size_t length;
    std::cin >> length;

    std::vector<Point> kingdoms(length);    
    
    for (size_t i = 0; i < length; i++)
    {
        kingdoms[i].id = i + 1;
        std::cin >> kingdoms[i].x >> kingdoms[i].y;
    }

    std::vector<Point> hull = graham_scan(kingdoms);

    std::sort(hull.begin(), hull.end(), [&](Point &a, Point &b) {
        return a.id < b.id;
    });

    for (const Point &point : hull)
    {
        std::cout << point.id << " ";
    }

    return 0;
}
```

## Python
```python
from functools import cmp_to_key


def CalculateOrientation(p1, p2, p3):
    return (p2[1] - p1[1]) * (p3[0] - p2[0]) - (p3[1] - p2[1]) * (p2[0] - p1[0])

def CalculateSquaredDistance(p1, p2):
    return (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2

def CompareOrientation(p1, p2):
    orientation = CalculateOrientation(start, p1, p2)

    if orientation: 
        return orientation
    if CalculateSquaredDistance(start, p1) <= CalculateSquaredDistance(start, p2):
        return -1
    return 1


n = int(input())
reinos = []

for i in range(n):
    info = input().split(" ")
    info.append(i+1)
    reinos.append(tuple(map(int, info)))

if n < 4:
    output = ""
    for r in reinos:
        output += str(f"{r[2]} ")

    print(output[:-1])
    quit()

start = reinos[0]

for r in reinos:
    if r[1] < start[1]:
        start = r
    elif r[1] == start[1] and r[0] < start[0]:
        start = r

reinos = sorted(reinos, key=cmp_to_key(CompareOrientation))
resultStack = [start, reinos[1], reinos[2]]

for p in reinos[3:]:
    while len(resultStack) > 1 and CalculateOrientation(resultStack[-2], resultStack[-1], p) > 0:
        resultStack.pop()
    resultStack.append(p)

lastCollinear = []

for i in range(len(reinos) - 2):
    if not CalculateOrientation(resultStack[-1], reinos[-2-i], start):
        lastCollinear.append(reinos[-2-i])
    else:
        resultStack.extend(lastCollinear)
        break

resultStack.sort(key=lambda x: x[2])
output = ""
for r in resultStack:
    output += str(f"{r[2]} ")

print(output[:-1])
```
