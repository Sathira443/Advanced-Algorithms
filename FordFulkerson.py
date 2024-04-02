from collections import defaultdict, deque


def bfs(graph, source, t, pred):
    visited = [False] * len(graph)
    queue = deque()
    queue.append(source)
    visited[source] = True

    while queue:
        u = queue.popleft()
        for v, capacity in enumerate(graph[u]):
            if not visited[v] and capacity > 0:
                queue.append(v)
                visited[v] = True
                pred[v] = u
                if v == t:
                    return True
    return False


def ford_fulkerson(residualGraph, source, sink):
    pred = [-1] * len(residualGraph)
    max_flow = 0

    while bfs(residualGraph, source, sink, pred):
        path_flow = float("inf")
        s = sink

        while s != source:
            path_flow = min(path_flow, residualGraph[pred[s]][s])
            s = pred[s]

        max_flow += path_flow

        v = sink
        while v != source:
            u = pred[v]
            residualGraph[u][v] -= path_flow
            residualGraph[v][u] += path_flow
            v = pred[v]

    return max_flow


graph = [[0, 16, 13, 0, 0, 0],
         [0, 0, 10, 12, 0, 0],
         [0, 4, 0, 0, 14, 0],
         [0, 0, 9, 0, 0, 20],
         [0, 0, 0, 7, 0, 4],
         [0, 0, 0, 0, 0, 0]]

source = 0
sink = 5
print("Max Flow:", ford_fulkerson(graph, source, sink))
