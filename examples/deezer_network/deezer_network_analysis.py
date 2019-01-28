
import json
import powerlaw
import csv
import networkx as nx
import matplotlib.pyplot as plt




#
#set name to graph
#
#parameters:   graph, string
#
#
def set_name(G,g_name):
    name = g_name
    G.name = name



#
# parametes:    string (path to the file)
#
#
#
# return:      dictionary where key is the number of
#             node and value is list of genres of the current node
#
def get_json_data(path):
    with open(path) as f:
        data = json.load(f)

    dict = {}
    for k, v in data.items():
        i = int(k)
        geners = []
        for j in v:
            mystr = j.encode('ascii', 'ignore')
            geners.append(mystr)
        dict[i] = geners

    return dict



#
# reads data from csv file
#
# prameters:   string
#
# return:     list of lists
#
def get_data_from_csv_file(filename):
    data = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = csvreader.next()
        int_line = []
        for row in csvreader:
            l=[]
            i = int(row[0])
            j = int(row[1])
            l.append(i)
            l.append(j)
            data.append(l)

    return data



#
# create graph from the data that sent
#
# parameters:    list of lists
#
# return:        networkx graph
#
def create_graph(data):
    nodes = []
    for line in data:
        nodes.append(line[0])
        nodes.append(line[1])
    sorted_nodes = sorted(set(nodes))
    G = nx.Graph()

    for node in sorted_nodes:
        G.add_node(node)

    for row in data:
        G.add_edge(row[0], row[1])
    return G



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
# get log log degree distribution
#
# parameters: three graphs
#
def loglog_distribution_plot(G,H,K):
    degrees_g = nx.degree(G)
    l = parse_list(degrees_g)
    unique_degree_l = l[0]
    degree_count_l = l[1]

    degrees_h = nx.degree(H)
    m = parse_list(degrees_h)
    unique_degree_m = m[0]
    degree_count_m = m[1]

    degrees_k = nx.degree(K)
    j = parse_list(degrees_k)
    unique_degree_j = j[0]
    degree_count_j = j[1]

    plt.style.use('seaborn')
    plt.rcParams['figure.figsize'] = (12, 8)

    plt.loglog(unique_degree_l, degree_count_l, 'bo-', label='Romanian network')
    plt.loglog(unique_degree_m, degree_count_m, 'ro-', label='Croatian network')
    plt.loglog(unique_degree_j, degree_count_j, 'go-', label='Hungarian network')

    plt.legend()
    plt.title(" Log log of degree distribution ")
    plt.ylabel("Frequency")
    plt.xlabel("Degree")
    plt.grid(True)
    plt.show()



#
# get degree distribution
#
# parameters: three graphs
#
def degree_distribution_plot(G,H,K):
    degrees_g = nx.degree(G)
    l = parse_list(degrees_g)
    unique_degree_l = l[0]
    degree_count_l = l[1]

    degrees_h = nx.degree(H)
    m = parse_list(degrees_h)
    unique_degree_m = m[0]
    degree_count_m = m[1]

    degrees_k = nx.degree(K)
    j = parse_list(degrees_k)
    unique_degree_j = j[0]
    degree_count_j = j[1]

    max_uniq = max(max(unique_degree_l),max(unique_degree_m),max(unique_degree_j))
    max_count = max(max(degree_count_l),max(degree_count_m),max(degree_count_j))

    plt.style.use('seaborn')
    plt.rcParams['figure.figsize'] = (12, 8)
    plt.plot(unique_degree_l, degree_count_l, 'bo-', label='Romanian network')
    plt.plot(unique_degree_m, degree_count_m, 'ro-', label='Croatian network')
    plt.plot(unique_degree_j, degree_count_j, 'go-', label='Hungarian network')
    plt.xticks(range(0, (max_uniq+15), 15))
    plt.yticks(range(0, (max_count+200), 200))
    plt.legend()
    plt.title(" Degree distribution ")
    plt.ylabel("Frequency")
    plt.xlabel("Degree")
    plt.grid(True)
    plt.show()



#
# present a diagram that shows min max and average degrees in the graph
#
# parameters:    graph
#
#
def max_min_degree_histo(G,country):
    degrees_tupels = G.degree
    degrees = []
    for pair in degrees_tupels:
        degrees.append(pair[1])
    max_degree = max(degrees)
    min_degree = min(degrees)
    average_degree = sum(degrees)/len(degrees)
    names = [' max degree ',' average degree ',' min degree']
    values = [max_degree, average_degree, min_degree]
    plt.style.use('seaborn')
    plt.text(0, 100, str(max_degree))
    plt.text(1, 100, str(average_degree))
    plt.text(2, 100, str(min_degree))
    plt.figure(1, figsize=( 10, 7))
    plt.bar(names,values, color = 'coral')
    plt.title('Max/Min degrees: '+ country)
    plt.yticks(range(0, max_degree + 20 ,20))
    plt.show()



#
# sorte a each genre and number of nodes (people) listening to it
#
# parameters:   dictionary
#
# return:       list - each value is a list with two parameters,
#                     genre and number of people that listening to it
#
def genres_popularity(dict):
    uniq_genres = []
    for k,v in dict.items():
        for i in v:
            if i not in uniq_genres:
                uniq_genres.append(i)
    popularity = []
    for i in uniq_genres:
        l = []
        l.append(i)
        count = 0
        for k,v in dict.items():
            for j in v:
                if j == i:
                    count+=1
        l.append(count)
        popularity.append(l)
    return popularity



#
# extract ten most popular genres
#
# parameters:     list
#
# return:         list - contain 10 values of pairs [genre, popularity],
#                       the most popular genres
#
def top_ten_genres(data):
    v = [i[1] for i in data]
    count =0
    l=sorted(v)
    l.reverse()
    top_ten = []
    while count < 10:
        for i in data:
            if l[count] == i[1]:
                top_ten.append(i)
        count+=1
    return top_ten



#
# plot the top ten genres that listening in the country
#
# parameters:    list - each value is a list of genre and amount
#                      of people that listening it
#
def plot_top_ten_genres(data,country):

    genres = [i[0] for i in data]
    values = [i[1] for i in data]

    plt.style.use('seaborn')
    plt.rcParams['figure.figsize'] = (12, 8)
    plt.title('Top 10 genres in ' + country)
    plt.xlabel('Genres')
    plt.ylabel('Amount of poeple')
    plt.yticks(range(0, values[0] + 2000, 2000))
    plt.grid(True)
    plt.bar(genres, values, color = 'khaki')
    plt.show()



#
# extract 20 nodes with the highest degree
#
# parameters:     graph, list - graph of the network of the country,
#                              list of top 10 genres
#
# return:         list of 20 nodes with the highest degree
#
def get_popular_nodes(G):
    uniq_nodes = []
    degrees = nx.degree(G)
    temp = [degree for node, degree in degrees]
    temp = sorted(temp)
    temp.reverse()
    top_degrees = temp[0:20]
    min_val= min(top_degrees)

    for node,degree in degrees:

        if degree >= min_val:
            try:
                top_degrees.remove(degree)
                l=[]
                l.append(node)
                l.append(degree)
                uniq_nodes.append(l)
            except ValueError:
                pass

    return uniq_nodes



#
# print data about top 20 nodes compared to top 10 genres, find out how many top
# genres exist in the node genres
#
# parameters:    list, list , list
#
#
# return:      none
#
def compare_top_genres_and_top_nodes(all_data,top_ten,top_nodes):
    dict = {}
    top_genres = [x[0] for x in top_ten]

    for node in top_nodes:
        node_genres = all_data[node[0]]
        dict[node[0]] = node_genres

    l = []

    for node, genres in dict.items():
        print "Node: " + str(node)
        print "Number of genres in his playlist: " + str(len(genres))
        print "Genres are: " ,genres

        num = 0
        temp = []
        for i in top_genres:
            if i in genres:
                num+=1
                temp.append(i)

        p = (len(temp)*100)/len(genres)
        p = int(p)
        l.append(p)
        print "Number of common genres to the node and to top 10: " + str(len(temp))
        print "Common genres are: " , temp
        print "Percent of the genres from the playlist: " + str(p)+ "%"
        print "******************************************************************************"

    avg_prcent = sum(l)/len(l)

    print "Average percent of popular genres in playlists: " + str(avg_prcent)



#
# find out the beta (exponent of the power law)
#
# parameters:     graph
#
# return:         float - the exponent of power law
#
def graph_beta(G):

    degrees = nx.degree(G)  # dictionary node:degree
    degree_values = []
    for t in degrees:
        degree_values.append(t[1])
    in_values = sorted(set(degree_values))
    in_hist = [degree_values.count(x) for x in in_values]
    results = powerlaw.Fit(in_hist)
    n = (results.power_law.alpha)
    return n



