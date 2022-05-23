def euler(g):
    stack = []
    circuit = []
    # current = g.random_vertex()
    current = 0
    stack.append(current)
    neighbour = g.adjMatrix[current].index(1)
    g.remove_edge(current, neighbour)
    current = neighbour
    while sum(g.adjMatrix[current]) >= 0 and len(stack) > 0:
        if sum(g.adjMatrix[current]) == 0:
            circuit.append(current)
            current = stack.pop()
        else:
            stack.append(current)
            neighbour = g.adjMatrix[current].index(1)
            g.remove_edge(current, neighbour)
            current = neighbour
    circuit.append(circuit[0])
    print(f'Euler: {circuit}')
    return circuit