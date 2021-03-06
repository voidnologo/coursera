# Uses python3

import sys
import queue
from dataclasses import dataclass


@dataclass()
class Node():
    idx: int
    distance: int
    children: set

    def __hash__(self):
        return self.idx

    def __repr__(self):
        return f'<Node {self.idx} - {self.distance} - {sorted(_.idx for _ in self.children)}>'


def build_graph(adj):
    nodes = [Node(idx, None, set()) for idx in range(len(adj))]  # entire graph
    for node in nodes:
        for child_idx in adj[node.idx]:
            node.children.add(nodes[child_idx])
    return nodes


def distance(adj, s, t):
    # write your code here
    pending = set()
    g = build_graph(adj)
    q = queue.SimpleQueue()
    start = g[s]
    start.distance = 0
    q.put(start)

    def get_distance(s):
        while not q.empty():
            current = q.get()
            pending.add(current)
            print(current)
            if current.idx == t:
                return 'Found it'
            for child in (current.children - pending):
                child.distance = current.distance + 1
                q.put(child)
            locals()['pending'] |= current.children
        return 'Not found it'

    return get_distance(start)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
