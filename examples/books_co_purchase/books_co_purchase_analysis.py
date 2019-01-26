import networkx as nx
import matplotlib.pyplot as plt



#
# setting an name to the network graph
#
# parameters : none
#
def set_name():
    name = raw_input("Name of the network: ")
    G.name = name


# prints information about the graph
#
# parameters: graph
#
def print_graph_info(G):
    # info about the graph number of nodes and edges
    print nx.info(G)

    # check if the graph is directed
    if (nx.is_directed(G)):
        print "Graph G is directed "
    else:
        print "Graph G isn't directed "

    # check if the graph is multigraph
    if (nx.is_multigraphical(G)):
        print "Graph G is multigraph"
    else:
        print "Graph G isn't multigraph"

    # number of self nodes in graph G
    print "Number of self loops in the graph: " + str(nx.number_of_selfloops(G))


#
# printing dictionerys of centralities
#
# parameters: none
#
def get_centralities(G):
    print "Degree centrality: " + str(nx.degree_centrality(G))

    print "Closeness centrality: " + str(nx.closeness_centrality(G))

    print "Betweeness centrality: " + str(nx.betweenness_centrality(G))


#
# get degree distribution
#
# parameters: graph
#
def degree_distribution(G):
    degrees =  nx.degree(G)
    l = parse_list(degrees)
    unique_degree = l[0]
    degree_count = l[1]
    plt.plot(unique_degree, degree_count, 'bo-')
    plt.title(" Degree distribution ")
    plt.ylabel("Degree")
    plt.xlabel("Frequency")
    plt.grid(True)
    fig1 = plt.gcf()
    plt.show()
    plt.draw()
    fig1.savefig('Degree distribution.png', bbox_inches="tight")


#
# help function that run over list of tuples and count unique degree
#
# parameters: list of tuples
#
# return: list       # list that contain two lists , one for x-axis ant the other for y-axis
#
def parse_list(degrees):
    degree_list = []
    for k, v in degrees:
        n = degrees[k]
        degree_list.append(n)
    unique_degree = list(set(degree_list))
    degree_count = []
    for i in unique_degree:
        n = degree_list.count(i)
        degree_count.append(n)
    l = [unique_degree, degree_count]
    return l


#
# represent a graph with degree centrality, as bigger degree centrality of a node, the node became bigger
#
# parameters: graph
#
# return: none
#
def degree_centrality_graph(G):
    degree_centrality_dict = nx.degree_centrality(G)
    G.degree_centrality = {}

    for node in G:
        n =  degree_centrality_dict[node]
        G.degree_centrality[node] = n

    pos = nx.spring_layout(G)
    node_color = [G.degree_centrality[v]*500 for v in G.nodes()]
    colors = [G[u][v] for u, v in G.edges]
    node_size = [(G.degree_centrality[node]*800) for node in G.nodes()]
    nx.draw_networkx(G,pos ,node_size=node_size, node_color=node_color, edge_color=colors, with_labels=False)
    plt.title(" Degree centrality ")
    fig1 = plt.gcf()
    plt.show()
    plt.draw()
    fig1.savefig('Degree centrality.png', bbox_inches="tight")


#
# represent a graph with Betweeness centrality, as bigger degree centrality of a node, the node became bigger
#
# parameters: graph
#
# return: none
#
def Betweeness_centrality_graph(G):

    betweeness_centrality_dict = nx.degree_centrality(G)
    G.betweeness_centrality = {}

    for node in G:
        n = betweeness_centrality_dict[node]
        G.betweeness_centrality[node] = n

    pos = nx.spring_layout(G)
    colors = [G[u][v] for u, v in G.edges]

    # defined th color of a node
    node_color = [G.betweeness_centrality[v] * 500 for v in G.nodes()]

    # defined the size of the node
    node_size = [(G.betweeness_centrality[node] * 800) for node in G.nodes()]
    nx.draw_networkx(G, pos, node_size=node_size, node_color=node_color,edge_color=colors,cmap=plt.cm.Reds_r,with_labels=False)
    plt.title(" Betweeness centrality ")
    fig1 = plt.gcf()
    plt.show()
    plt.draw()
    fig1.savefig('Betweeness_centrality.png',bbox_inches = "tight" )





# creation of graph
G = nx.read_gml('polbooks.gml',label='id')

