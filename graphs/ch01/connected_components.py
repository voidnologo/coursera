#Uses python3

import sys


def number_of_components(adj, n):
    all = set(range(n))
    subgraphs = []

    def explore(idx):
        visited.add(idx)
        # print('-' * 20)
        # print(f'Index: {idx}')
        # print(f'Visited: {visited}')
        locals()['to_visit'] |= set([v for v in adj[idx] if v not in visited])
        # print(f'To Visit: {to_visit}')
        if not to_visit:
            return visited
        next = to_visit.pop()
        # print(f'Next: {next}')
        return explore(next)

    while True:
        remainder = all - set(item for sub in subgraphs for item in sub)
        if not remainder: break
        next = remainder.pop()
        visited = set()
        to_visit = set()
        subgraphs.append(explore(next))

    return subgraphs

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
    print(number_of_components(adj, n))
