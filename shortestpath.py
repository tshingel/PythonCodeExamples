# Dijkstra's shortest-path algorithm
# The file dijkstraData.txt contains an adjacency list representation of an undirected weighted graph 
# with 200 vertices labeled 1 to 200. Each row consists of the node tuples
# that are adjacent to that particular vertex along with the length of that edge.
# The program runs Dijkstra's shortest-path algorithm on this graph, 
# using 1 (the first vertex) as the source vertex, and computes the shortest-path 
# distances between 1 and every other vertex of the graph.
# selected distances are returned 

from heapdict import heapdict
#import time

#fin= open("Daijkstra_test.txt")

#G={}                                    # keeps vertices
#G_dist = {}                             # keeps corresponding distances to vertices in G
#for line in fin:                        # load data, create adjacency lists
#    lst=[]
#    temp=line.strip().replace(' ',',').split(',')
#    for node in temp:
#        lst.append(int(node))
#    G[lst[0]]=lst[1:len(lst)-1:2]
#    G_dist[lst[0]] = lst[2::2]

G={}                                    # keeps vertices
G_dist = {}                             # keeps corresponding distances to vertices in G
with open("dijkstraData.txt", 'r') as fin:
    for line in fin:
        lst = []
        temp = line.strip().replace('\t',',').split(',') 
        for node in temp:
            lst.append(int(node))      # create adjancency lists 
        G[lst[0]]=lst[1:len(lst)-1:2]
        G_dist[lst[0]] = lst[2::2]
    
def Dijkstras(G, s):
    CONST = 1000000
    s_dist = {}                         # distance from source to v is a list
    processed = []                      # list of processed vertices
    for v in G:
        s_dist[v] = CONST
        
    s_dist[s] = 0                       # distance from source to source
    hd =heapdict()                      # contains all vertices which haven't been processed 
    
    for v in G:                         # initialize the heap dictionary
        hd[v] = s_dist[v] 
         
    while len(hd) != 0:
            v = hd.popitem()[0]         # returns key from (key, priority) tuple with the lowest priority
            if s_dist[v] == CONST:
                break
            processed.append(v)  
            index = 0                   # for accessing edge_lenghts     
            for w in G[v]:              # grab adjacency list of v 
                if w not in processed:                    
                    alt = s_dist[v] + G_dist[v][index]
                    if alt < s_dist[w]:
                        s_dist[w] = alt                               
                    hd[w] = s_dist[w]   # update the priority value                                                             
                index += 1
    return(s_dist)
        
dist = Dijkstras(G, 1)       # dictionary with shortest distances from source 1   

print "distances are:", dist[7], dist[37], dist[59], dist[82], dist[99], dist[115], dist[133], dist[165], dist[188], dist[197]    