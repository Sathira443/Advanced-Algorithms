from collections import deque

def bfs(graph, start, colors):
    queue = deque([start])
    colors[start] = 0
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if colors[neighbor] == -1:
                colors[neighbor] = 1 - colors[node]
                queue.append(neighbor)
            elif colors[neighbor] == colors[node]:
                return False
    return True

def consistent_labeling(graph, n):
    colors = [-1]*n
    for i in range(n):
        if colors[i] == -1:
            if not bfs(graph, i, colors):
                return -1
    return colors

#assign the nodes and edges for the graph
graph = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 3, 4],
    3: [0, 2],
    4: [2,3]
}

# Number of employees (nodes in the graph)
n = 5

# Call the function
labels = consistent_labeling(graph, n)

# Print the result
print(labels)
