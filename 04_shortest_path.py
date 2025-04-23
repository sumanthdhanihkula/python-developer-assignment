"""
Problem 4: Shortest Path Finder (Using Dijkstra's Algorithm)

Given a weighted graph of cities connected by roads, determine the shortest path from a start city to a destination city.

Approach:
- Use Dijkstra’s Algorithm with a priority queue to find the shortest path from start to destination.
- Maintain distance and previous city mappings to reconstruct the shortest route.
"""

import heapq

def dijkstra(graph, start, end):
    distances = {city: float('inf') for city in graph}
    distances[start] = 0

    prev = {city: None for city in graph}
    visited = set()

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_city = heapq.heappop(priority_queue)

        if current_city in visited:
            continue
        visited.add(current_city)

        for neighbor, weight in graph[current_city].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                prev[neighbor] = current_city
                heapq.heappush(priority_queue, (distance, neighbor))

    # Reconstruct the shortest path
    path = []
    city = end
    while city:
        path.insert(0, city)
        city = prev[city]

    if distances[end] == float('inf'):
        return None, float('inf')

    return path, distances[end]

# Example Input
cities = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'C': 3, 'D': 9},
    'C': {'A': 10, 'B': 3, 'D': 1},
    'D': {'B': 9, 'C': 1}
}

start_city = 'A'
destination_city = 'D'

# Output Result
path, distance = dijkstra(cities, start_city, destination_city)
if path:
    print(f"Shortest path from {start_city} to {destination_city}: {' -> '.join(path)}")
    print(f"Total distance: {distance}")
else:
    print("No path found.")
