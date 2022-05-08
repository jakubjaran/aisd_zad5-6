class Hamilton():

    def __init__(self, graph, once):
        self.graph = graph
        self.has_cycle = False
        self.once = once

    def is_safe(self, v, path, pos):
        if self.graph[path[pos - 1]][v] == 0:
            return False

        for i in range(pos):
            if path[i] == v:
                return False

        return True

    def ham_cycle(self):
        path = []
        path.append(0)

        visited = [False] * (len(self.graph))

        visited[0] = True

        self.find_ham_cycle(1, path, visited)

        if self.has_cycle is False:
            print("No Hamiltonian Cycle possible")
            return False

    def find_ham_cycle(self, pos, path, visited):
        if pos == len(self.graph):

            if self.graph[path[-1]][path[0]] != 0:
                path.append(0)
                print(f'Hamiltonian: {path}')
                path.pop()
                self.has_cycle = True
            return

        if self.once == True:
            if self.has_cycle == False:
                for v in range(len(self.graph)):

                    if self.is_safe(v, path, pos) and not visited[v]:
                        path.append(v)
                        visited[v] = True
                        self.find_ham_cycle(pos + 1, path, visited)
                        visited[v] = False
                        path.pop()
        else:
            for v in range(len(self.graph)):

                if self.is_safe(v, path, pos) and not visited[v]:
                    path.append(v)
                    visited[v] = True
                    self.find_ham_cycle(pos + 1, path, visited)
                    visited[v] = False
                    path.pop()