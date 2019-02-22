#Uses python3

import sys

def reach(adj, x, y):
    visited = set()
    to_visit = set()

    def explore(idx):
        visited.add(idx)
        print('-' * 20)
        print(f'Index: {idx}')
        print(f'Visited: {visited}')
        if idx == y:
            return True
        locals()['to_visit'] |= set([v for v in adj[idx] if v not in visited])
        print(f'To Visit: {to_visit}')
        if not to_visit:
            return False
        next = to_visit.pop()
        print(f'Next: {next}')
        return explore(next)

    found = explore(x)
    return int(found)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))


'''
go to a node
mark it as visited
ask what it is connected to
if connected not in seen:
    push connected onto queue
pop node off of queue
repeat
profit
'''
