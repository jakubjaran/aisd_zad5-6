from graph import random_graph
from euler import euler


def main():
    g = random_graph(20, 0.3)
    g.print_matrix()
    euler(g)


main()