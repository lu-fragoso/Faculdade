class Vertex:
   
    def __init__(self, data):
        
        self.data = data

class Graph:

    def __init__(self, directed = False):
        
        self.verticesList = []
        self.adjList = []
        
        self.directed = directed

    def addVertex(self, data):

        vertice = Vertex(data)
        
        self.verticesList.append(vertice)

        self.adjList.append([])

    def addEdge(self, orig, dest):

        idxOrig = -1
        idxDest = -1
        
        for idx, vertex in enumerate(self.verticesList):

            if vertex.data == orig:
                idxOrig = idx
            
            if vertex.data == dest:
                idxDest = idx

        if idxOrig == -1 or idxDest == -1:
            return    
        
        #orifVertex = self.verticesList[idxOrig]
        destVertex = self.verticesList[idxDest]

        self.adjList[idxOrig].append(destVertex)

        if self.directed is False:
            
            origVertex = self.verticesList[idxOrig]
            self.adjList[idxDest].append(origVertex)


    def __str__(self):

        info = " "
        for i, vertex in enumerate(self.verticesList):
            
            info += '\n'+ str(vertex.data) + ': '

            adjacentes = self.adjList[i]
            
            info += "["

            for j, vertexAdj in enumerate(adjacentes):

                info += " " + str(vertexAdj.data)

            info += "]"     

        return info    


grafo1 = Graph(directed=False)

grafo1.addVertex('A')
grafo1.addVertex('B')
grafo1.addVertex('C')
grafo1.addVertex('D')
grafo1.addVertex('E')
grafo1.addVertex('F')
grafo1.addVertex('G')
grafo1.addVertex('H')

grafo1.addEdge('E','A')
grafo1.addEdge('A','B')
grafo1.addEdge('B','F')
grafo1.addEdge('F','C')
grafo1.addEdge('C','G')
grafo1.addEdge('F','G')
grafo1.addEdge('G','H')
grafo1.addEdge('H','D')
grafo1.addEdge('C','D')

print(grafo1)

