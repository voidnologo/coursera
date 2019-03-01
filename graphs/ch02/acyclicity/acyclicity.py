#Uses python3

'''
Explore
keep track of seen
if new verticies is in already seen
then we have a cycle
'''
import sys
from dataclasses import dataclass


@dataclass()
class Node():
    idx: int
    pre: int
    post: int
    children: set

    def __hash__(self):
        return self.idx

    def __repr__(self):
        return f'<Node {self.idx} - {self.pre} - {self.post} - {sorted(_.idx for _ in self.children)}>'


def set_counter():
    counter = 0
    while True:
        node, which = yield
        setattr(node, which, counter)
        counter += 1


def build_graph(adj):
    nodes = [Node(idx, None, None, set()) for idx in range(len(adj))]  # entire graph
    for node in nodes:
        for child_idx in adj[node.idx]:
            node.children.add(nodes[child_idx])
    return nodes


def acyclic(adj):

    nodes = set(build_graph(adj))
    seen = set()
    counter = set_counter()
    next(counter)


    def explore(node):
        counter.send((node, 'pre'))
        seen.add(node)
        locals()['to_visit'] |= set([v for v in node.children if v not in seen])
        if to_visit:
            explore(to_visit.pop())
        counter.send((node, 'post'))
        return

    while True:
        to_visit = set()
        remainder = nodes - seen
        node = None if not remainder else remainder.pop()
        if node is None:
            break
        explore(node)

    from jpprint import jpprint
    jpprint(seen)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    acyclic(adj)
    # print(acyclic(adj))
