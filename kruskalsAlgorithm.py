#Kruskal's Algorithm Implementation
#Author: Matt Broe

#Kruskal's algorithm constructs a minimal spanning forest of a weighted
#simple undirected graph. 

import Edge
import myMinHeap
import random

def kruskalMSF(A):
    #Here A is the n x n adjacency matrix of a weighted simple undirected graph
    #G with vertex set {0, 1, ..., n-1}. The code may not work properly if A is
    #not symmetric.
    
    #The program uses the convention that A[i][j] = float('inf') when
    #there is no edge between vertex i and vertex j. 

    #The function assumes that the number
    #of vertices is the length of a row of the matrix.
    n = len(A[0])

    #msf is initialized as the matrix of a subgraph T of G with no edges. The 
    #algorithm adds edges to T and updates its matrix representation
    #accordingly until T is a minimal spanning forest of G. 
    
    msf = [[float("inf") for x in range(n)] for y in range(n)]

    #componentDict is a dict whose elements are the connected components of
    #T. componentNum[i] is the key whose associated value in componentDict is
    #the connected component containing vertex i.
    componentDict = {}
    componentNum = []

    for i in range(n):
        componentDict[i] = set([i])
        componentNum += [i]

    msfWeight = 0

    m = myMinHeap.minHeap((n**2)//2)

    #Push all edges of G to the min heap:
    for j in range(n):
        for i in range(j):
            if A[i][j] < float('inf'):
                e = Edge.Edge(i, j, A[i][j])
                m.push(e)

    while m.numElements > 0:
        
        #Try to add the minimum edge in the heap to T:
        
        newEdge = m.pop()
        u = newEdge.source
        v = newEdge.target

        u_comp = componentNum[u]
        v_comp = componentNum[v]
        
        if u_comp == v_comp:
            #If u and v belong to the same component of T,
            #then you cannot add an edge between u and v to T
            #without creating a cycle.
            continue

        #If u and v belong to different components, we adjoin newEdge
        #to T.

        
        #First, add all the vertices in v's component to u's component, and update
        #their keys in componentNum to point to u's component.
        
        componentDict[u_comp] = componentDict[u_comp].union(componentDict[v_comp])

        for i in componentDict[v_comp]:
            componentNum[i] = u_comp

        
        del componentDict[v_comp]

        #Add the new edge to msf.
        msf[u][v] = A[u][v]
        msf[v][u] = A[u][v]
        msfWeight += A[u][v]

        if len(componentDict) == 1:
            #If there is only one component, T is connected. Therefore T
            #is a minimal spanning tree of G and the function can return.
            break
    
    #Return an array containing the forest's matrix and weight.
    return [msf, msfWeight]



        
    
    
