from collections import defaultdict,deque
import heapq
import re
from itertools import count,product,combinations
from functools import cache
file_path = 'data_23.txt'
#file_path='sample_23.txt'
codes=defaultdict(set)
with open(file_path, "r") as file:
    data = file.readlines()
    for line in data:
        line = line.strip()
        cl = line.split('-')
        codes[cl[0]].add(cl[1])
        codes[cl[1]].add(cl[0])
#print(codes)
def compute_triangles(graph):
    triangles = set()
    for node in graph:
        neighbors = graph[node]
        for neighbor in neighbors:
            common_neighbors = neighbors.intersection(graph[neighbor])
            for common in common_neighbors:
                triangle = tuple(sorted([node, neighbor, common]))
                triangles.add(triangle)
    return triangles

triangles = compute_triangles(codes)


ans_1 = sum(1 for triangle in triangles if any(node.startswith('t') for node in triangle))

print(ans_1)

def bron_kerbosch(R, P, X, graph, cliques):
    if not P and not X:
        cliques.append(R)
        return
    for node in list(P):
        bron_kerbosch(R.union({node}), P.intersection(graph[node]), X.intersection(graph[node]), graph, cliques)
        P.remove(node)
        X.add(node)


def find_largest_clique(graph):
    cliques = []
    bron_kerbosch(set(), set(graph.keys()), set(), graph, cliques)
    largest_clique = max(cliques, key=len)
    return largest_clique

largest_clique = find_largest_clique(codes)
print(",".join(sorted(largest_clique)))

