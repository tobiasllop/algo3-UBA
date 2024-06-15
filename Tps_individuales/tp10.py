"""
Entregable 10 - TDA UBA
Tobias Llop
LU: 871/22
Vjudge: tobiasllop
"""
import heapq

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, u, v, weight):
        self.adjacency_list[u].append((v, weight))
        self.adjacency_list[v].append((u, weight))
    
    def dijkstra(self, start):
        distances = {vertex: float('infinity') for vertex in self.adjacency_list}
        distances[start] = 0
        priority_queue = [(0, start)]
        
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            
            if current_distance > distances[current_vertex]:
                continue
            
            for neighbor, weight in self.adjacency_list[current_vertex]:
                distance = current_distance + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        return distances



def main():
    try:
        while True:
            n, k = map(int, input().split())
            T = list(map(int, input().split()))
            G = Graph()
            for i in range(n):
                pisos_alcanzados = list(map(int, input().split()))
                
                for j in range(100*i, 100*(i+1)): # Grafo de 100*n vertices
                    G.add_vertex(j)
                
                for p in range(len(pisos_alcanzados)-1):
                    G.add_edge(100*i + pisos_alcanzados[p], 100*i + pisos_alcanzados[p+1], (pisos_alcanzados[p+1] - pisos_alcanzados[p])* T[i])
            

            for i in range(100 * n): # Agregamos las aristas en las que cambio de ascensor
                if i in G.adjacency_list:
                    for j in range(i + 100, 100 * n, 100):
                        if j in G.adjacency_list:
                            if i % 100 == 0:  
                                G.add_edge(i, j, 0)  
                            else:
                                G.add_edge(i, j, 60) 
            
            distances = G.dijkstra(0)

            objetivo = None
            min_distance = float('infinity')
            for i in range(n):
                vertex = 100 * i + k
                if vertex in distances and distances[vertex] < min_distance:
                    objetivo = vertex
                    min_distance = distances[vertex]
            
            if objetivo in distances and distances[objetivo] != float('infinity'):
                print(distances[objetivo]) 
            else:
                print("IMPOSSIBLE")
    except EOFError:
        pass


if __name__ == "__main__":
    main()