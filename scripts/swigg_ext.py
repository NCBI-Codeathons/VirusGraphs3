from collections import defaultdict
import argparse

import numpy as np
import pandas as pd

from collections import Counter
from Bio import SeqIO
import networkx as nx

import matplotlib.pyplot as plt

import sys
import os
sys.setrecursionlimit(500524)

# Function to contract nodes
class DFSOBJ:
    supernode_dict = defaultdict()
    supernodes = [[]]
    snid_g = 0
    sn_adj = defaultdict(list)

    def DFS(self, source, graph):
        visited = defaultdict()
        self.sn_adj = defaultdict(list)
        self.supernodes = [[]]
        self.snid_g = 0
        self.supernode_dict = defaultdict()
        return self.DFS_sub(source, visited, graph, False)

    def DFS_sub(self, curr, visited, graph, split):
        visited[curr] = 1
        # determine if a split is needed
        if split or graph.in_degree(curr)>1 or graph.out_degree(curr)>1:
            self.supernodes.append([curr])
            self.sn_adj[self.snid_g].append(self.snid_g+1)
            self.snid_g+=1
        else:
            self.supernodes[self.snid_g].append(curr)
        self.supernode_dict[curr] = self.snid_g
        if graph.out_degree(curr)>1:
            split = True
        else:
            split = False

    #     print(supernodes)
        for n in graph.neighbors(curr):
            if n not in visited:
                self.DFS_sub(n, visited, graph, split)
    #             print(pro)
    #             if pro and snid_2 not in sn_adj[snid]:
    #                 sn_adj[snid].append(snid_2)
            else:
                if self.supernode_dict[n] not in self.sn_adj[self.snid_g]:
                    self.sn_adj[self.snid_g].append(self.supernode_dict[n])

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter, \
description="""
swiggy.py

Given a list of fasta sequences, the script will produce a graph (.gexf) file to visualize the graphs using GEPHI.
""")

optional = parser._action_groups.pop()
required = parser.add_argument_group('required arguments')

########################################################
# required args:
required.add_argument("-k", "--kmer-length", type=int,
                    help="""required, the length of k-mer that needs to be used'
                    """,
                    required=True)

required.add_argument("-f", "--fasta", nargs="+",
                    help="required, set of all fasta sequences",
                    required=True)

required.add_argument("-o", "--out",
                    help='required, path to prefix of output file name. Graph file ".gexf" will be created',
                    required=True)

args = parser.parse_args()

outdir= args.out
fasta = args.fasta
k_length = args.kmer_length

seq_list = []
for seqfile in fasta:
    seq_list = seq_list + [(str(a.id),str(a.seq)) for a in list(SeqIO.parse(seqfile, "fasta"))]

seq_df = 0
if len(seq_list)>100:
    seq_df = pd.DataFrame(seq_list[:100])   # loads the first hundred sequences (otherwise the graph will be too big to visualize)
else:
    seq_df = pd.DataFrame(seq_list) 

seq_df.columns = ["name","Sequence"]
name_dict = list(enumerate(seq_df["name"]))

print("K-mer lengths = "+str(k_length))
kmer_pos_dict = defaultdict(list)
kmer_name_dict = defaultdict(list)
kmer_pos_dict = defaultdict(list)
kmer_dict = set()
for i in range(len(seq_df)):
    name = i
#             print(name)
    seq = seq_df.loc[i,"Sequence"]
    for j in range(len(seq)-k_length+1):
        kmer_dict.add(seq[j:j+k_length])
#     print(i,seq[j:j+k_length])
kmer_id_list = dict(zip(sorted(list(kmer_dict)), list(range(1,len(kmer_dict)+1))))
id_kmer_list = dict(zip(list(range(1,len(kmer_dict)+1)),sorted(list(kmer_dict))))

edges = defaultdict(list)
for i in range(len(seq_df)):
    name = i
    seq = seq_df.loc[i,"Sequence"]
    edges[0].append(kmer_id_list[seq[:k_length]])
    for j in range(len(seq)-k_length-1):
        edges[kmer_id_list[seq[j:j+k_length]]].append(kmer_id_list[seq[j+1:j+k_length+1]])
        kmer_name_dict[kmer_id_list[seq[j:j+k_length]]].append(name)
        kmer_pos_dict[kmer_id_list[seq[j:j+k_length]]].append(j)
    kmer_name_dict[kmer_id_list[seq[len(seq)-k_length:]]].append(name)
    kmer_pos_dict[kmer_id_list[seq[len(seq)-k_length:]]].append(j)

G = nx.DiGraph()

print("Number of nodes: ",len(kmer_id_list))
num = 0
edges_list = []
for j in edges:
    for i in edges[j]:
        G.add_edge(j,i)
        edges_list.append((j,i))
        num+=1
print("Number of edges: ",num)

print("Contracting nodes...")
source = [i for i in G.in_degree() if i[1]==0]
a = DFSOBJ()
a.DFS(0, G)

new_G = nx.DiGraph()
for i in a.sn_adj:
    for j in a.sn_adj[i]:
        new_G.add_edge(i, j)
print("Number of nodes: " + str(len(new_G.nodes)))
print("Number of edges: " + str(len(new_G.edges)))
nx.write_gexf(new_G, outdir+".gexf")




