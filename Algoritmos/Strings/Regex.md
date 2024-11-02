# Algoritmo para criar e usar RegEx

Esse código cria um Automato Finito Nao Deterministico com base em uma RegEx e percorre ele para verificar se uma determinada palavra é representada ou não por ele.

Complexidade O(m*n), onde m é o tamanho da string e n é o tamanho do AFND. O tamanho do AFND é determinado pelo tamanho da RegEx.

Resolve o exercício https://judge.beecrowd.com/pt/problems/view/1109

## Python
```python
MAX_STATES = 450 # 3 vezes o numero de caracteres da regex eh o suficiente
EMPTY = 0 # Valor vazio
VALID = -1 # Valor de estado valido
UNION = '|'
CLOSURE = '*'
CONC = '.'

alphabet = set(['a', 'b'])
operators = {CONC: 0, UNION: 1, CLOSURE: 2} # Valores maiores tem precedencia

def CheckQuery(query, graph, start, end): # DFS em pilha
    query += '$'
    states = [(start, query)]
    visited = set([])

    while (len(states)):
        currentState = states.pop()
        visited.add(currentState)

        state, word = currentState[0], currentState[1]
        if word == '$':
            if VALID in graph[state]:
                return True
            if EMPTY in graph[state]:
                for connection in graph[state][EMPTY]:
                    neighbour = (connection, word)
                    if neighbour not in visited:
                        states.append(neighbour)
            continue

        for key in graph[state]:
            # print("State/Key ", state, key)
            if key == word[0]:
                for connection in graph[state][key]:
                    neighbour = (connection, word[1:])
                    if neighbour not in visited:
                        states.append(neighbour)
            elif key == EMPTY:
                for connection in graph[state][key]:
                    neighbour = (connection, word)
                    if neighbour not in visited:
                        states.append(neighbour)
    return False

def PostFix(regex): # Transforma a regex para sua forma pós fixada (1 + 2) => (1 2 +)
    output = []
    symbolStack = []

    for c in regex:
        if c in alphabet: # Simbolo do alfabeto
            output.append(c)
            continue
        if c == '(': # Inicializador de Regex
            symbolStack.append(c)
            continue
        if c == ')': # Finalizador de Regex
            while symbolStack[-1] != '(':
                output.append(symbolStack[-1])
                symbolStack.pop()
            symbolStack.pop()
            continue

        # Qualquer operador
        if symbolStack[-1] == '(':
            symbolStack.append(c)
            continue

        topElement = symbolStack[-1]
        if operators[c] > operators[topElement]: # Elemento no topo tem prioridade menor
            symbolStack.append(c)
            continue

        while topElement in operators and operators[topElement] >= operators[c]: # Enquanto elemento no topo tiver prioridade maior ou igual
            output.append(topElement)
            symbolStack.pop()
            topElement = symbolStack[-1]
        symbolStack.append(c)

    while (len(symbolStack)): # Operadores restantes na pilha
        output.append(symbolStack[-1])
        symbolStack.pop()
    return "".join([c for c in output])

def BuildGraph(regex): # Constroi o AFND com base no algoritmo de Thompson https://medium.com/swlh/visualizing-thompsons-construction-algorithm-for-nfas-step-by-step-f92ef378581b
    stackStates = []
    states = [{} for _ in range(MAX_STATES)]
    currentState = 0
    postFix = PostFix(regex)

    for c in postFix:
        if c in alphabet:
            if c not in states[currentState]:
                states[currentState][c] = []
                
            states[currentState][c].append(currentState+1)
            stackStates.append((currentState, currentState+1))

            currentState += 1
            states[currentState][VALID] = [VALID] # Determinacao de estado final
            currentState += 1
            continue

        if c == UNION:
            second = stackStates.pop()
            states[second[1]].pop(VALID, None)

            first = stackStates.pop()
            states[first[1]].pop(VALID, None)

            if EMPTY not in states[currentState]:
                states[currentState][EMPTY] = []
            states[currentState][EMPTY].append(first[0])
            states[currentState][EMPTY].append(second[0])

            if EMPTY not in states[first[1]]:
                states[first[1]][EMPTY] = []
            if EMPTY not in states[second[1]]:
                states[second[1]][EMPTY] = []

            stackStates.append((currentState, currentState+1))

            currentState += 1
            states[first[1]][EMPTY].append(currentState)
            states[second[1]][EMPTY].append(currentState)

            states[currentState][VALID] = [VALID]
            currentState += 1
            continue

        if c == CLOSURE:
            state = stackStates.pop()

            states[currentState][EMPTY] = [state[0]]
            states[currentState][EMPTY].append(currentState+1)
            stackStates.append((currentState, currentState+1))
            currentState += 1

            states[state[1]].pop(VALID, None)
            if EMPTY not in states[state[1]]:
                states[state[1]][EMPTY] = []

            states[state[1]][EMPTY].append(state[0])
            states[state[1]][EMPTY].append(currentState)
            states[currentState][VALID] = [VALID]
            currentState += 1
            continue

        if c == CONC:
            second = stackStates.pop()
            first = stackStates.pop()
            states[first[1]].pop(VALID, None)
            
            if EMPTY not in states[first[1]]:
                states[first[1]][EMPTY] = []
            states[first[1]][EMPTY].append(second[0])

            stackStates.append((first[0], second[1]))
            continue

    return states, stackStates[0][0], stackStates[0][1]

while True:
    try:
        regex = input()
    except EOFError:
        break

    graph, start, end = BuildGraph(regex)
    q = int(input())

    for _ in range(q):
        query = input()
        if CheckQuery(query, graph, start, end):
            print("Y")
        else:
            print("N")
    print()
```