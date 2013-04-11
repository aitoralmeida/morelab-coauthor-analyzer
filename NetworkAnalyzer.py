# -*- coding: utf-8 -*-
"""
Created on Tue Mar 05 16:42:59 2013

@author: aitor
"""


import networkx as nx
import matplotlib.pylab as plt
from collections import OrderedDict

verbose = False

fh = open("./data/coauthors.txt", 'rb')
G = nx.read_edgelist(fh)
fh.close()

#remove posible self loops
G.remove_edges_from(G.selfloop_edges())

#network info
node_num = G.number_of_nodes()
edge_num = G.number_of_edges()
nodes = G.nodes()

if verbose:
    print "The loaded network has %s nodes and %s edges\r\n" % (node_num, edge_num)
    print "The nodes of the network are:"
    for n in nodes:
        print n

#simple network visualization 
nx.draw(G)
plt.savefig("./images/simpleNetwork.png")
if verbose:
    plt.show()

#centrality analysis
#degree centrality
cent_degree = nx.degree_centrality(G)
sorted_cent_degree = OrderedDict(sorted(cent_degree.items(), key=lambda t: t[1], reverse=True))
if verbose:
    print "\n\r*** Degree Centrality ***"
    for d in sorted_cent_degree:
        print "%s: %s" % (d, sorted_cent_degree[d])
        
#betweenness centrality
cent_betweenness = nx.betweenness_centrality(G)
sorted_cent_betweenness = OrderedDict(sorted(cent_betweenness.items(), key=lambda t: t[1], reverse=True))
if verbose:
    print "\n\r*** Betweenness Centrality ***"
    for d in sorted_cent_betweenness:
        print "%s: %s" % (d, sorted_cent_betweenness[d])

#closeness centrality
cent_closeness = nx.closeness_centrality(G)
sorted_cent_closeness = OrderedDict(sorted(cent_closeness.items(), key=lambda t: t[1], reverse=True))
if verbose:
    print "\n\r*** Closeness Centrality ***"
    for d in sorted_cent_closeness:
        print "%s: %s" % (d, sorted_cent_closeness[d])

#eigenvector centrality
cent_eigenvector = nx.eigenvector_centrality(G)
sorted_cent_eigenvector = OrderedDict(sorted(cent_eigenvector.items(), key=lambda t: t[1], reverse=True))
if verbose:
    print "\n\r*** Eigenvector Centrality ***"
    for d in sorted_cent_eigenvector:
        print "%s: %s" % (d, sorted_cent_eigenvector[d])
        
#pageRank
#eigenvector centrality
page_rank = nx.pagerank(G)
sorted_page_rank = OrderedDict(sorted(page_rank.items(), key=lambda t: t[1], reverse=True))
if verbose:
    print "\n\r*** PageRank ***"
    for d in sorted_page_rank:
        print "%s: %s" % (d, sorted_page_rank[d])
        
#groups
#cliques
cliques = list(nx.find_cliques(G))
if verbose:
    for c in cliques:
        print "\n\r*** Cliques ***"
        print c

#k-core
#main
core_main = nx.k_core(G)
nx.draw(core_main)
plt.savefig("./images/kCoreMain.png")
if verbose:
    print "\r\nk-Core: Main"
    print core_main.nodes()
    plt.show()
    
#k = 4
core_main = nx.k_core(G, k=4)
nx.draw(core_main)
plt.savefig("./images/kCore4.png")
if verbose:
    print "\r\nk-Core: 4"
    print core_main.nodes()
    plt.show()
   


