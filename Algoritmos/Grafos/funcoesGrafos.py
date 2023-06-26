import heapq
import matplotlib.pyplot as plt
import networkx as nx


def convertEdgesArrayToNonDirectedGraph(edges,vertices):
    graph = [{} for _ in range(vertices)]

    for (a,b,cost) in edges:
        graph[a][b] = cost
        graph[b][a] = cost
    return graph

def convertEdgesArrayToDirectedGraph(edges,vertices):
    graph = [{} for _ in range(vertices)]

    for (a,b,cost) in edges:
        graph[a][b] = cost
    return graph

def convertGraphToEdgesArray(graph):
    edges = []

    for a in range(len(graph)):
        for b in graph[a]:
            if a<b:
                edges.append((a,b,graph[a][b]))
    return edges

def getReverseGraph(graph):
    reverse = [{} for _ in range(len(graph))]
    for a in range(len(graph)):
        for b in graph[a]:
            reverse[b][a] = graph[a][b]
    return reverse



def drawGraph(edges):
    G = nx.Graph()
    for (a,b,cost) in edges:
        G.add_edge(a,b,weight=cost)
    pos = nx.spring_layout(G, seed=0)
    nx.draw_networkx_nodes(G, pos, node_size=700)
    nx.draw_networkx_edges(G, pos, edgelist=[(u, v) for (u, v, d) in G.edges(data=True)], width=6)
    nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels)
    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()
    plt.show()