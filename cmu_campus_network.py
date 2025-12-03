"""
NetworkX Hello World Project

1. Create a graph network
2. Add nodes and weighted edges
3. Find shortest paths
4. Analyze network properties
5. Visualize the network

TODO: Fill in the missing code sections
"""

import networkx as nx
import matplotlib.pyplot as plt

# ============================================================================
# PART 1: Create the Graph
# ============================================================================
print("Part 1: Creating the graph...")

# Create an undirected graph
G = nx.Graph()

# CMU Buildings - we'll keep this simple with just 5 buildings
buildings = [
    'Gates Hillman Center',
    'Wean Hall',
    'Hunt Library',
    'Cohon Center',
    'Tepper Building'
]

# Add buildings as nodes
G.add_nodes_from(buildings)

print(f"Added {G.number_of_nodes()} buildings to the network")

# ============================================================================
# PART 2: Add Walking Paths with Times
# ============================================================================
print("\nPart 2: Adding walking paths...")

# Walking paths between buildings with estimated times in minutes
# Format: (building1, building2, walking_time_minutes)
paths = [
    ('Gates Hillman Center', 'Wean Hall', 2),
    ('Wean Hall', 'Hunt Library', 3),
    ('Hunt Library', 'Cohon Center', 2),
    ('Cohon Center', 'Tepper Building', 1),
    ('Tepper Building', 'Gates Hillman Center', 2),
    ('Wean Hall', 'Cohon Center', 4)  # Alternative longer path
]

# Add the paths as weighted edges
for building1, building2, time in paths:
    G.add_edge(building1, building2, weight=time)

print(f"Added {G.number_of_edges()} walking paths")

# ============================================================================
# PART 3: Find Shortest Path
# ============================================================================
print("Part 3: Finding shortest paths...")

# TODO: Find the shortest path from Gates Hillman Center to Hunt Library
start = 'Gates Hillman Center'
end = 'Hunt Library'

# YOUR CODE HERE: Use nx.shortest_path() to find the shortest route
# shortest_path = 
shortest_path = nx.shortest_path(G, source=start, target=end, weight='weight')
# YOUR CODE HERE: Use nx.shortest_path_length() to find the walking time
# walking_time = 
walking_time = nx.shortest_path_length(G, source=start, target=end, weight='weight')
# print(f"\nShortest route from {start} to {end}:")
# print(f"  Route: {' -> '.join(shortest_path)}")
# print(f"  Walking time: {walking_time} minutes")
print(f"\nShortest route from {start} to {end}:")
print(f"  Route: {' -> '.join(shortest_path)}")
print(f"  Walking time: {walking_time} minutes")
# ============================================================================
# PART 4: Network Analysis
# ============================================================================
print("Part 4: Analyzing the network...")

# TODO: Calculate the degree (number of connections) for each building
print("\nConnections per building:")
for building in G.nodes():
    # YOUR CODE HERE: Use G.degree(building) to get the number of connections
    degree = G.degree(building)
    print(f"  {building:25s}: {degree} connections")
    # degree = 
    # print(f"  {building:25s}: {degree} connections")

# TODO: Calculate betweenness centrality (which buildings are most "central")
# betweenness = 
# most_central = max(betweenness, key=betweenness.get)
# print(f"\nMost central building: {most_central}")
betweenness = nx.betweenness_centrality(G, weight='weight')
most_central = max(betweenness, key=betweenness.get)
print(f"\nMost central building: {most_central}")
# ============================================================================
# PART 5: Visualization
# ============================================================================
print("Part 5: Creating visualization...")

plt.figure(figsize=(12, 8))

# Use spring layout for positioning
pos = nx.spring_layout(G, seed=42)

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_color='lightblue', 
                       node_size=3000, alpha=0.9)

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

# Draw edges
nx.draw_networkx_edges(G, pos, edge_color='gray', width=2, alpha=0.6)

# Draw edge labels (walking times)
edge_labels = nx.get_edge_attributes(G, 'weight')
edge_labels = {k: f"{v} min" for k, v in edge_labels.items()}
nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=9)

plt.title("CMU Campus Walking Network", fontsize=16, fontweight='bold')
plt.axis('off')
plt.tight_layout()
plt.savefig('cmu_network.png', 
            dpi=300, bbox_inches='tight')
print("Visualization saved!")

# Save as GraphML (standard format for network analysis)
# Remove pos attribute (tuples) before export as GraphML doesn't support them
G_export = G.copy()
for node in G_export.nodes():
    if 'pos' in G_export.nodes[node]:
        del G_export.nodes[node]['pos']
nx.write_graphml(G_export, 'cmu_network.graphml')
print("Network exported to cmu_networks.graphml (can be opened in other tools)")

# ============================================================================
# Part 6: Harder Challenges (Pick 1 Challenge)
# ============================================================================
print("\n1. Find ALL possible paths from Gates Hillman Center to Hunt Library:")
# TODO: Use nx.all_simple_paths() to find all routes
all_paths = list(nx.all_simple_paths(G, source=start, target=end))
for i, path in enumerate(all_paths, 1):
    print(f"  Path {i}: {' -> '.join(path)}")
print("\n2. Recalculate shortest path after removing Wean Hall:")
# TODO: Remove Wean Hall and recalculate the shortest path
G_without_wean = G.copy()
G_without_wean.remove_node('Wean Hall')

new_path = nx.shortest_path(G_without_wean, source=start, target=end, weight='weight')
new_time = nx.shortest_path_length(G_without_wean, source=start, target=end, weight='weight')

print(f"  New route without Wean Hall: {' -> '.join(new_path)}")
print(f"  Walking time: {new_time} minutes")

print("\n3. Calculate the average walking time between any two buildings:")
# TODO: Use nx.average_shortest_path_length()
avg_walking_time = nx.average_shortest_path_length(G, weight='weight')
print(f"  Average walking time: {avg_walking_time:.2f} minutes")