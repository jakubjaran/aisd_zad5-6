import random


class Graph():

    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
            self.size = size
            self.edges = 0

    def add_edge(self, v1, v2):
        # if v1 == v2:
        #     print(f'Same vertex {v1} and {v2}')
        #     return
        if self.adjMatrix[v1][v2] == 0:
            self.adjMatrix[v1][v2] = 1
            self.adjMatrix[v2][v1] = 1
            self.edges += 1

    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print(f'No edge betwwen {v1} and {v2}')
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def __len__(self):
        return self.size

    def print_matrix(self):
        for row in self.adjMatrix:
            for val in row:
                print(f'{val}', end=" ")
            print()

    def deg(self, v1):
        return sum(self.adjMatrix[v1])

    def random_vertex(self):
        return random.randint(0, self.size - 1)

    def random_connected_vertex(self):
        v = self.random_vertex()
        while self.deg(v) == 0:
            v = self.random_vertex()
        return v

    def random_disconnected_vertex(self):
        v = self.random_vertex()
        while self.deg(v) != 0:
            v = self.random_vertex()
        return v

    def random_uneven_vertex(self):
        v = self.random_connected_vertex()
        while self.deg(v) % 2 == 0:
            v = self.random_connected_vertex()
        return v

    def check_if_all_connected(self):
        for i in self.adjMatrix:
            if sum(i) == 0:
                return False
        return True

    def get_uneven(self):
        uneven = []
        for i in self.adjMatrix:
            if sum(i) % 2 != 0:
                uneven.append(i)
        return uneven

    def get_density(self):
        max = ((self.size * self.size) - self.size) / 2
        return self.edges / max


def random_graph(size, density):
    g = Graph(size)

    v1 = g.random_vertex()
    v2 = g.random_vertex()
    while v1 == v2:
        v2 = g.random_vertex()
    g.add_edge(v1, v2)

    while g.check_if_all_connected() == False:
        v1 = g.random_connected_vertex()
        v2 = g.random_disconnected_vertex()
        g.add_edge(v1, v2)

    while len(g.get_uneven()) != 0:
        uneven = g.get_uneven()
        if len(uneven) == 3:
            v1 = uneven[0]
            v2 = uneven[1]
            v3 = uneven[2]
            g.add_edge(v1, v2)
            g.add_edge(v2, v3)
            g.add_edge(v3, v1)
        else:
            v1 = g.random_uneven_vertex()
            v2 = g.random_uneven_vertex()
            if v1 == v2:
                continue
            g.add_edge(v1, v2)

    while g.get_density() < density:
        v1 = g.random_vertex()
        v2 = g.random_vertex()
        v3 = g.random_vertex()
        if g.adjMatrix[v1][v2] == 1 or g.adjMatrix[v1][v3] == 1 or g.adjMatrix[
                v2][v3] == 1 or v1 == v2 or v1 == v3 or v2 == v3:
            continue
        g.add_edge(v1, v2)
        g.add_edge(v2, v3)
        g.add_edge(v3, v1)

    g.print_matrix()
    print(g.get_density())
