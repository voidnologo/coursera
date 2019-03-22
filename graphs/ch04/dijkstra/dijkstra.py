from dataclasses import dataclass
import pdb
import sys
from collections import deque, namedtuple


Child = namedtuple('Child', ['vertex', 'cost'])


@dataclass()
class Vertex():
    idx: int
    distance: int
    prev: 'typing.Any'
    children: set

    def __hash__(self):
        return self.idx

    def __repr__(self):
        return f'<Vertex {self.idx} - {self.distance} - {list((_[0].idx, _[1]) for _ in self.children)}>'


def build_graph(adj, cost):
    vertices = [Vertex(idx, float('inf'), None, set()) for idx in range(len(adj))]  # entire graph
    for vertex in vertices:
        for child_idx, weight in zip(adj[vertex.idx], cost[vertex.idx]):
            vertex.children.add(Child(vertices[child_idx], weight))
    return vertices


def min_feed(graph):
    Q = deque(sorted([v for v in graph], key=lambda x: x.distance))
    while Q:
        yield Q.popleft()


def display_route(graph, s, t):
    thing = [f'Vertex {graph[t].idx}']
    prev = graph[t].prev
    while prev and prev != s:
        thing.append(f'Vertex {prev.idx}')
        prev = prev.prev
    print(f'\nAnd the official order from {s} to {t}:')
    print(' > '.join(reversed(thing)))
    print('\nWith a cost of:')
    print(graph[t].distance)


def distance(adj, cost, s, t):
    graph = build_graph(adj, cost)
    graph[s].distance = 0
    Q = min_feed(graph)
    for v in Q:
        v = graph[v.idx]
        for child in v.children:
            alt = v.distance + child.cost
            print(v.idx, child.vertex.idx, child.vertex.distance, alt)
            if alt < child.vertex.distance:
                child.vertex.distance = alt
                child.vertex.prev = v
    print(graph)
    display_route(graph, s, t)


if __name__ == '__main__':
    # inp = sys.stdin.read()
    with open('graph_2') as f:
        inp = f.read()
    data = list(map(int, inp.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    distance(adj, cost, s, t)
