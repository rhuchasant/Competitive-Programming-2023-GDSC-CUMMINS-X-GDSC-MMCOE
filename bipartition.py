from collections import defaultdict
import collections

def possible_bipartition(n, dislikes):
    if n == 1 or not dislikes:
        return True

    graph = defaultdict(list)
    
    for u, v in dislikes:
        graph[u].append(v)
        graph[v].append(u)

    group = [-1] * (n + 1)

    for i in range(1, n + 1):
        if group[i] == -1:
            group[i] = 0
            stack = collections.deque([i])

            while stack:
                node = stack.popleft()
                for neighbor in graph[node]:
                    if group[neighbor] == group[node]:
                        return False
                    if group[neighbor] == -1:
                        group[neighbor] = 1 - group[node]
                        stack.append(neighbor)

    return True

# Example usage:
n1 = 4
dislikes1 = [[1, 2], [1, 3], [2, 4]]
print(possible_bipartition(n1, dislikes1))  # Output: True

n2 = 3
dislikes2 = [[1, 2], [1, 3], [2, 3]]
print(possible_bipartition(n2, dislikes2))  # Output: False
