import sys

class Graph:
    def __init__(self, verticies, edges):
        self.V = verticies
        self.edges = edges
    
    def minDistance(self, dist, shortestPath):
        min_val = sys.maxsize
        minIndex = -1

        for v in range(self.V):
            if dist[v] < min_val and not shortestPath[v]:
                min_val = dist[v]
                minIndex = v

        return minIndex

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        shortestPath = [False] * self.V

        for _ in range(self.V):
            u = self.minDistance(dist, shortestPath)
            shortestPath[u] = True

            for v in range(self.V):
                if (
                    self.edges[u][v] > 0
                    and not shortestPath[v]
                    and dist[v] > dist[u] + self.edges[u][v]
                ):
                    dist[v] = dist[u] + self.edges[u][v]

        return dist
    

edges = [
    [0, 7, 9, 0, 0, 14,15],
    [7, 0, 10, 15, 0, 0,0],
    [9, 10, 0, 11, 0, 2,3],
    [0, 15, 11, 0, 6, 0,4],
    [0, 0, 0, 6, 0, 9,4],
    [14, 0, 2, 0, 9, 0,0],
    [14, 0, 2, 0, 9, 0,0],
]

g = Graph(7, edges)

src = 0
print(f"Shortest distance from Start Node to each node in graph: {g.dijkstra(src)}")