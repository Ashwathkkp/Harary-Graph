import numpy as np
import networkx as nx

def draw_graph(graph,nodes):
    
    G=nx.Graph()
    for node in nodes:
        G.add_node(node)
    for edge in graph:
        if (abs(edge[1]-edge[0])==1 or abs(edge[1]-edge[0])==n-1):
            G.add_edge(edge[0], edge[1],color='red')
        elif (abs(edge[1]-edge[0]) ==2 or abs(edge[1]-edge[0])==n-2):
            G.add_edge(edge[0], edge[1],color='blue')
        elif (abs(edge[1]-edge[0]) ==3 or abs(edge[1]-edge[0])==n-3):
            G.add_edge(edge[0], edge[1],color='black')
        elif (abs(edge[1]-edge[0]) ==4 or abs(edge[1]-edge[0])==n-4):
            G.add_edge(edge[0], edge[1],color='yellow')
        elif (abs(edge[1]-edge[0]) ==5 or abs(edge[1]-edge[0])==n-5):
            G.add_edge(edge[0], edge[1],color='green')
    pos = nx.shell_layout(G)
    edges = G.edges()
    colors = [G[u][v]['color'] for u,v in edges]
    nx.draw_networkx_nodes(G,pos,node_size=1600)
    nx.draw_networkx_edges(G,pos,width=2)
    nx.draw_networkx_labels(G,pos,font_size=16)
    nx.draw(G, pos,edges=edges, edge_color=colors)
    plt.show()
    
def Harary(n,k):
    r=int(k/2)
    graph =[]
    nodes=set()
    for x in range(0,n):
        nodes.add(x)
        for y in range(1,r+1):
            graph.append((x,(x+y)%n))
    if((n%2==0) and (k%2!=0)):
        for x in range(0,int(n/2)):
            graph.append((x,x+int(n/2)))
    if((n%2!=0) and (k%2!=0)):
        for x in range(0,int(n/2)+1):
            graph.append((x,x+int(n/2)))
        graph.append(( 0,int((n-1)/2) ))
 #       graph.append(( 0,int((n+1)/2) ))
        
    draw_graph(graph,nodes)

n=int(input("Enter value of n:"))
k=int(input("Enter value of k:"))

if k > n-1:
    print("Graph with k greater than or equal to n is not possible\n")
else:
    Harary(n,k)
