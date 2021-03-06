import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import networkx as nx
import nxviz as nv

np.random.seed(42)

data = pd.read_csv('references_list_current.csv')
data = data.drop(data.columns[0], axis=1)

#This code will pull out all pubs with references to the leadership pubs (6-22)

def specific_pubs(df, keyword):
    """Pull specific pubs or groups of pubs out of the total doctrine list"""
    df2 = pd.DataFrame(columns=df.columns)
    for i, row in enumerate(df.values):
        for value in row:
            if keyword in value:
                df2 = pd.concat([df2, (df[i:i+1])])
    return df2   

lead = specific_pubs(data, '6-22')

G = nx.from_pandas_dataframe(lead, source='pub', target='reference', create_using=nx.MultiDiGraph())

def get_nodes(keyword, network):
    """Identify nodes in a given network that contain a given keyword"""
    l = []
    for node in G.nodes():
        if keyword in node:
            l.append(node)
    return l

adp_nodes = get_nodes('ADP', G)
adrp_nodes = get_nodes('ADRP', G)
fm_nodes = get_nodes('FM', G)
atp_nodes = get_nodes('ATP', G)
attp_nodes = get_nodes('ATTP', G)

#Plot the final graph of all current Army doctrine

plt.figure(figsize=(12,12))
pos = nx.spring_layout(G, k=.25)
_ = nx.draw_networkx_nodes(G, pos, nodelist=adp_nodes, node_size=1500, node_color='red', node_shape='*')
_ = nx.draw_networkx_nodes(G, pos, nodelist=adrp_nodes, node_size = 1500, node_color='yellow', node_shape='*')
_ = nx.draw_networkx_nodes(G, pos, nodelist=fm_nodes, node_size = 250, node_color='green', node_shape='^')
_ = nx.draw_networkx_nodes(G, pos, nodelist=atp_nodes, node_size = 100, node_color='red', node_shape='.')
_ = nx.draw_networkx_nodes(G, pos, nodelist=attp_nodes, node_size = 100, node_color='red', node_shape='.')
_ = nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')   
_ = nx.draw_networkx_edges(G, pos, edge_color='blue', width=.5, alpha=.5) 
plt.axis('off')
plt.savefig('plot9_leadership_graph.png') 

deg = G.degree()
in_deg = G.in_degree()
out_deg = G.out_degree()

#Plotting degree of each node (publication)

name = []
degree = []

for key, value in deg.items():
    name.append(key)
    degree.append(value)
    
degree_df = pd.DataFrame()
degree_df['name'] = name
degree_df['degree'] = degree
degree_df = degree_df.sort_values(by='degree', ascending=False)

plt.figure(figsize=(10, 25))
_ = sns.barplot(x='degree', y='name', data=degree_df[:15], orient='h')
_ = plt.xlabel('Degree')
_ = plt.ylabel('Node')
_ = plt.title('Node Degrees in Army Leadership Doctrine')
plt.savefig('plot10_leadership_degree_graph.png')

#Plotting in-degree of each node (publication)

name = []
indegree = []

for key, value in in_deg.items():
    name.append(key)
    indegree.append(value)
    
in_degree_df = pd.DataFrame()
in_degree_df['name'] = name
in_degree_df['in_degree'] = indegree
in_degree_df = in_degree_df.sort_values(by='in_degree', ascending=False)

plt.figure(figsize=(10, 25))
_ = sns.barplot(x='in_degree', y='name', data=in_degree_df[:15], orient='h')
_ = plt.xlabel('In-Degree')
_ = plt.ylabel('Node')
_ = plt.title('Node In-Degrees in Army Leadership Doctrine')
plt.savefig('plot11_leadership_indegree_graph.png')

#Plotting out-degree of each node (publication)

name = []
outdegree = []

for key, value in out_deg.items():
    name.append(key)
    outdegree.append(value)
    
out_degree_df = pd.DataFrame()
out_degree_df['name'] = name
out_degree_df['out_degree'] = outdegree
out_degree_df = out_degree_df.sort_values(by='out_degree', ascending=False)

plt.figure(figsize=(10, 25))
_ = sns.barplot(x='out_degree', y='name', data=out_degree_df[:15], orient='h')
_ = plt.xlabel('Out-Degree')
_ = plt.ylabel('Node')
_ = plt.title('Node Out-Degrees in Army Leadership Doctrine')
plt.savefig('plot12_leadership_outdegree_graph.png')
