import networkx as nx
import matplotlib.pyplot as plt

# Step 1: Initialize Graph with Nodes and Edges
map_graph = nx.Graph()
edges = [
    ('A', 'B', 10), ('A', 'C', 15), ('B', 'C', 7),
    ('B', 'D', 10), ('C', 'D', 10), ('C', 'E', 20),
    ('D', 'E', 10), ('D', 'F', 5), ('E', 'F', 5)
]
map_graph.add_weighted_edges_from(edges)

# Step 2: Define Dijkstra's Algorithm for Shortest Path Calculation
def dijkstra_route(graph, start, end):
    path = nx.dijkstra_path(graph, start, end)
    path_length = nx.dijkstra_path_length(graph, start, end)
    return path, path_length

# Step 3: Visualization Function
def visualize_route(graph, path):
    pos = nx.spring_layout(graph)  # Generate node positions
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
    
    # Draw edges with weights (e.g., travel time or distance)
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    
    # Highlight the shortest path in red
    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_edges(graph, pos, edgelist=path_edges, edge_color='red', width=2)
    
    plt.title(f"Optimal Route from {path[0]} to {path[-1]}")
    plt.show()

# Step 4: Compute Initial Route and Display
start_location, end_location = 'A', 'F'
initial_path, initial_cost = dijkstra_route(map_graph, start_location, end_location)
print("Initial optimal route:", initial_path)
print("Route cost:", initial_cost)

visualize_route(map_graph, initial_path)

# Step 5: Simulate Real-Time Update (e.g., traffic increase on ('B', 'D') from 10 to 20)
map_graph['B']['D']['weight'] = 20

# Recompute Route with Updated Weights and Display Updated Route
updated_path, updated_cost = dijkstra_route(map_graph, start_location, end_location)
print("Updated optimal route:", updated_path)
print("Updated route cost:", updated_cost)

visualize_route(map_graph, updated_path)