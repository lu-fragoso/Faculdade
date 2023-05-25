"""
Nesta implementacao, existe o risco de alguem adicionar arestas repetidas. 
Esse problema nao foi corrigido para o codigo ficar mais simples de entender.
"""

class Vertex:
    """
    Noh para uma arvore AVL
    """
    
    def __init__(self, data):
        
        self.data = data
        
class Graph:
    """
    Arvore AVL - implementacao dinamica
    """

    def __init__(self, directed=False):
        
        # a lista de vertices inicia vazia
        self.verticesList = []
        self.adjList = []
        self.directed = directed
 
        
    def addVertex(self, data, directed=False):
        """
        Adiciona um vertice no grafo
        """

        # crim um novo vertice
        tempVertice = Vertex(data)
        
        # adiciona o novo vertice na lista de vertices
        self.verticesList.append(tempVertice)
        
        # adiciona uma lista de adjacencias vazia para o novo vertice
        vertexAdj = []
        self.adjList.append( vertexAdj )
        
    def addEdge(self,origin,destination):
        """
        Adiciona uma aresta entre o vertice que contem o 
        valor origin e o vertice que contem o valor destination
        """
        
        idxOrig = -1
        idxDest = -1
        for idx, vertex in enumerate(self.verticesList):
            if vertex.data == origin:
                idxOrig = idx
            if vertex.data == destination:
                idxDest = idx 
           
        # se origin or destination forem invalidos, encerra o metodo
        # sem fazer nenhuma alteracao
        if idxOrig==-1 or idxDest==-1:
            return
        
        # adiciona a vertice de destino como adjacente ao vertice de origem
        self.adjList[idxOrig].append( idxDest )
        
        # se o grafo nao e orientado, adiciona o vertice de origem como adjacente ao vertice de destino
        if self.directed==False: 
            self.adjList[idxDest].append( idxOrig )

    def breadthFirstSearch(self, firstVertex=0):
        """
        Faz a busca em largura para todos os vertices, evitando
        que a busca deixa algum grafo sem visitar em caso do grafo ser desconexo 
        """ 

        # cria a variavel branco que indica que um vertice nao foi visitado
        branco = 0
    
        # visita o primeiro no desejado pelo usuario
        strBFS, cor = self.exploreVertexBFS(firstVertex)
        
        # usa parenteses para mostrar todas as visitas comecando pelo vertice atual
        strBFS = '('+ strBFS + ')'
        
        # verifica se existem nos sem visitar
        for idxVertex in range(len(self.verticesList)):
            if cor[idxVertex] == branco:
                auxStrBFS, cor = self.exploreVertexBFS(idxVertex, cor)
                
                # usa as parenteses para separar as arvores geradas pela busca
                strBFS += '(' + auxStrBFS + ')'
                
        return strBFS                    
    
    def exploreVertexBFS(self, firstVertex=0, cor=None):
        """
        Faz a busca em largura a partir de um
        determinado vertice indicado na entrada
        """

        # inicializa uma string que ira guardar a ordem dos nos visitados
        strBFS = ''
        
        # cria variaveis branco, cinza e preto
        branco = 0
        cinza = 1
        preto = 2

        # caso nenhuma lista de cores seja informado como entrada
        # inicia todos os vertices com a cor branca
        if cor is None:
            
            # pinta todos de branco
            cor = [branco]*len( self.verticesList )

        # marca o vertice atual de cinza
        cor[firstVertex] = cinza
        
        # como o vertice foi pintado de cinza, significando que ele
        # foi visitado, adiciona ele na string que mostra o percurso da busca
        strBFS += str(self.verticesList[firstVertex].data) + ' '
        
        # cria uma fila para guardar os vertices que ainda não foram visitados por completo
        fila = []
        
        # adiciona o primeiro vertice na fila
        fila.append( firstVertex )
        while len(fila)>0:
            
            # retorna o primeiro indice da fila
            idxVertex = fila[0]

            # percorre todos os vertices adjacentes
            for idxAdj in self.adjList[idxVertex]:
                if cor[idxAdj]==branco:

                    # marca o vertice como visitado
                    cor[idxAdj] = cinza
                    fila.append(idxAdj)
                    
                    # como o vertice foi pintado de cinza, significando que ele
                    # foi visitado, adiciona ele na string que mostra o percurso da busca
                    strBFS += str(self.verticesList[idxAdj].data) + ' '
                    
            # remove o vertice da fila ja que todos os seus 
            # adjacentes foram analizados
            fila.pop(0)
            
        return strBFS, cor

        
    def DFS(self, firtVertex):
        
        strDFS = ''

        branco = 0

        #pinta todos os vertices de branco
        cor = [branco]*len(self.verticesList)

        strDFS, cor = self.exploreVertexDFS(firtVertex)

        for i in range(len(self.verticesList)):
            
            if cor[i] == branco:
                auxStrDFS, cor = self.exploreVertexDFS(i, cor)

                strDFS += ' ' + auxStrDFS

        return auxStrDFS        

    def exploreVertexDFS(self, idxVertex, cor = None):

        strDFS = ''

        branco = 0
        cinza = 1
        preto = 2

        if cor is None:
            cor = [branco]*len(self.verticesList)

        cor [idxVertex] = cinza
        
        pilha  = []
        pilha.append(idxVertex)
       
        verticeAtual = self.verticesList[idxVertex]
        strDFS+= ' '+ str(verticeAtual.data)

        for idxAdj in self.adjList[idxVertex]:
            
            if cor[idxAdj]==branco: 
                auxStrDFS, cor = self.exploreVertexDFS(idxAdj, cor)

                strDFS += ' ' + auxStrDFS

        # saiu do for significa que visitou todos os adjacentes
        cor[idxVertex] = preto        

        return strDFS, cor


    
    
    def __str__(self):
        
        info = '\nLista de adjacencia:\n'+20*'='+'\n'
        for idx, vertex in enumerate(self.verticesList):
            
            info += str(vertex.data) + ': ['
            for idxAdj in self.adjList[idx]:
                data = self.verticesList[idxAdj].data
                info += str(data) + ' '
            
            info += ']\n'
            
        info += 20*'='+'\n'
           
        
        return info
            

if __name__ == "__main__":

    # cria o primeiro grafo
    grafo = Graph(directed=False)
    grafo.addVertex('A')
    grafo.addVertex('B')
    grafo.addVertex('C')
    grafo.addVertex('D')
    grafo.addVertex('E')
    grafo.addVertex('F') 
    grafo.addVertex('G')
    grafo.addVertex('H')

    grafo.addEdge('B','F')
    grafo.addEdge('B','A')    
    grafo.addEdge('A','E')
    grafo.addEdge('F','C')
    grafo.addEdge('F','G')
    grafo.addEdge('C','G')
    grafo.addEdge('C','D')
    grafo.addEdge('D','H')
    grafo.addEdge('h','G')
    
    print(grafo)
    #print( 'BFS (largura): ',grafo.breadthFirstSearch(firstVertex = 1) )
    #print( 'DFS (profundidade): ',grafo.depthFirstSearch(firstVertex = 1) )
     
    # cria o segundo grafo
    grafo = Graph(directed=True)
    grafo.addVertex('A')
    grafo.addVertex('B')
    grafo.addVertex('C')
    grafo.addVertex('D')
    grafo.addVertex('E')
    grafo.addVertex('F') 

    grafo.addEdge('A','C')    
    grafo.addEdge('A','B')
    grafo.addEdge('B','C')
    grafo.addEdge('C','F')
    grafo.addEdge('D','E')
    grafo.addEdge('E','C')
    
    print()
    print(grafo)
   
    print( 'BFS (largura): ',grafo.breadthFirstSearch())

    strDFS, cor = grafo.exploreVertexDFS(0)
    print('DFS (Profundidade): ', strDFS)
    
    
    

    

    
    
    