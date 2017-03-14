#Prim's Algorithm Implementation
#Author: Matt Broe

#Kruskal's algorithm constructs a minimal spanning tree of a weighted
#simple undirected graph. 

import Edge
import myMinHeap

def primMST(A):
    #Here A is the n x n adjacency matrix of a weighted simple undirected graph
    #G with vertex set {0, 1, ..., n-1}.The code may not work properly if A 
    #is not symmetric.
    
    #The program uses the convention that A[i][j] = float('inf') when
    #there is no edge between vertex i and vertex j.
    
    #The number of vertices is taken to be the length of a row of the matrix.
    n = len(A[0])

    #mst is initialized as the matrix of an empty subgraph T of G. The 
    #algorithm adds edges to T and updates its matrix representation
    #accordingly until T is a minimal spanning tree of G. 
    
    mst = [[float("inf") for x in range(n)] for y in range(n)]

    #mstVertices[i] = 1 if vertex i is currently contained in T, and 0
    #otherwise.
    
    mstVertices = [0]*n

    #mstSize = number of vertices currently in tree
    mstSize = 0
    
    mstWeight = 0

    m = myMinHeap.minHeap((n**2)//2) 
    minWeight = float('inf')

    #Find the minimum edge in G:
    for j in range(n):
        for i in range(j):
            if A[i][j] < minWeight:
                minWeight = A[i][j]
                minEdge = Edge.Edge(i, j, A[i][j])
    
    u = minEdge.source
    v = minEdge.target

    mstVertices[u] = 1
    mstSize = 1

    #The tree now consists of a single vertex, u, which is the source of
    #the minimum edge.

    #Push all the edges in G that start at u to the minheap
    for x in range(n):
        if mstVertices[x] == 0 and A[u][x] < float("inf"):
            e = Edge.Edge(u, x, A[u][x])
            m.push(e)

    try:
        while mstSize < n and m.numElements > 0:
            
            newEdge = m.pop()
            u = newEdge.source
            v = newEdge.target

            if mstVertices[v] == 1:
                continue
            
            #newEdge is the minimum edge in G such that only one of its endpoints
            #currently lies in the tree. We know that newEdge.source is in the tree,
            #since we only push edges to the heap after their source has been added
            #to the tree.

            #Now we add newEdge to the tree.

            #First, add the other endpoint of newEdge to the vertex list
            mstVertices[v] = 1

            #Push all the edges starting at v that do not end at a vertex
            #which is already in T
            for x in range(n):
                if mstVertices[x] == 0:
                    e = Edge.Edge(v, x, A[v][x])
                    m.push(e)

            #Finally, add newEdge to mst.
            mstSize += 1
            mst[u][v] = A[u][v]
            mst[v][u] = A[u][v]
            mstWeight += A[u][v]

    except mstSize < n:
        print("Graph not connected, no spanning tree exists")
        return 

    #Return an array containing the tree's matrix and weight.
    return [mst, mstWeight]
        
        

    
    



    


