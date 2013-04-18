# -*- coding: utf-8 -*-
"""
Created on Tue Mar 05 16:42:59 2013

@author: aitor
"""


import networkx as nx
import matplotlib.pylab as plt
from collections import OrderedDict
import csv

verbose = True

def get_graph(path):
    fh = open(path, 'rb')
    G = nx.read_edgelist(fh)
    fh.close()
    #remove posible self loops
    G.remove_edges_from(G.selfloop_edges())
    return G
    
        
def write_csv_centralities(file_name, data):
    with open(file_name, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        for d in data:
            if verbose:
                print "%s: %s" % (d, data[d])
            writer.writerow([d, data[d]])
            
def write_csv_groups(file_name, groups):
    with open(file_name, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        for e in groups:
            if verbose:
                print e
            writer.writerow(e)
            
def write_csv_group(file_name, group):
    with open(file_name, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(group)

def get_graph_info(G):
    node_num = G.number_of_nodes()
    edge_num = G.number_of_edges()
    nodes = G.nodes()
    
    if verbose:
        print "The loaded network has %s nodes and %s edges\r\n" % (node_num, edge_num)
        print "The nodes of the network are:"
        for n in nodes:
            print n
            
    with open('./data/results/networkInfo.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(['nodes',node_num])    
        writer.writerow(['edges',edge_num])    

def draw_graph(G):
    nx.draw(G)
    plt.savefig("./images/simpleNetwork.png")
    if verbose:
        plt.show()

#**********CENTRALITIES***********
  
def calculate_degree_centrality(G):
    cent_degree = nx.degree_centrality(G)
    sorted_cent_degree = OrderedDict(sorted(cent_degree.items(), key=lambda t: t[1], reverse=True))
    if verbose:
        print "\n\r*** Degree Centrality ***"
    write_csv_centralities('./data/results/degreeCent.csv', sorted_cent_degree)

def calculate_betweenness_centrality(G):    
    cent_betweenness = nx.betweenness_centrality(G)
    sorted_cent_betweenness = OrderedDict(sorted(cent_betweenness.items(), key=lambda t: t[1], reverse=True))
    if verbose:
        print "\n\r*** Betweenness Centrality ***"
    write_csv_centralities('./data/results/betweennessCent.csv', sorted_cent_betweenness)

def calculate_closeness_centrality(G):   
    cent_closeness = nx.closeness_centrality(G)
    sorted_cent_closeness = OrderedDict(sorted(cent_closeness.items(), key=lambda t: t[1], reverse=True))
    if verbose:
        print "\n\r*** Closeness Centrality ***"
    write_csv_centralities('./data/results/closenessCent.csv', sorted_cent_closeness)   

def calculate_eigenvector_centrality(G):   
    cent_eigenvector = nx.eigenvector_centrality(G)
    sorted_cent_eigenvector = OrderedDict(sorted(cent_eigenvector.items(), key=lambda t: t[1], reverse=True))
    if verbose:
        print "\n\r*** Eigenvector Centrality ***"
    write_csv_centralities('./data/results/eigenvectorCent.csv', sorted_cent_eigenvector) 
        
def calculate_pagerank(G):
    page_rank = nx.pagerank(G)
    sorted_page_rank = OrderedDict(sorted(page_rank.items(), key=lambda t: t[1], reverse=True))
    if verbose:
        print "\n\r*** PageRank ***"
    write_csv_centralities('./data/results/pagerank.csv', sorted_page_rank)     
    
    
#**********COMMUNITIES***********
def calculate_cliques(G):
    cliques = list(nx.find_cliques(G))
    if verbose:
        print "\n\r*** Cliques ***"
    write_csv_groups('./data/results/cliques.csv', cliques)
    
def calculate_main_k_core(G):
    core_main = nx.k_core(G)
    nx.draw(core_main)
    plt.savefig("./images/kCoreMain.png")
    if verbose:
        print "\r\nk-Core: Main"
        print core_main.nodes()
        plt.show()
    write_csv_group('./data/results/mainKCore.csv', core_main.nodes())
    
def calculate_k_core(G, K):
    core_k = nx.k_core(G, k=K)
    nx.draw(core_k)
    plt.savefig("./images/kCore" + str(K) + ".png")
    if verbose:
        print "\r\nk-Core: " + str(K)
        print core_k.nodes()
        plt.show()
    write_csv_group('./data/results/kCore' + str(K) + '.csv', core_k.nodes())
    
def calculate_k_clique(G, K):
    communities = nx.k_clique_communities(G, K)
    if verbose:
        print "k-cliques " + str(K)
    write_csv_groups('./data/results/kClique' + str(K) + '.csv', communities)

        
    
    
print 'Analizing co-author data from ' + "./data/coauthors.txt"
G = get_graph("./data/coauthors.txt")
get_graph_info(G)
draw_graph(G)

#centralities
calculate_degree_centrality(G)
calculate_betweenness_centrality(G)
calculate_closeness_centrality(G)
calculate_closeness_centrality(G)
calculate_pagerank(G)

#communities
calculate_cliques(G)
calculate_main_k_core(G)
calculate_k_core(G,4)
#calculate_k_clique(G, 2)