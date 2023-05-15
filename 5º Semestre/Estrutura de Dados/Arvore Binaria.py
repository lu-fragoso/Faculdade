class Node:
    
    def __init__(self, data):
        
        self.data = data
        self.right = None
        self.left = None
        
class Tree:
    """
    Arvore binaria de busca - implementacao dinamica
    """

    def __init__(self):
        self.root = None
        
    def insert(self, data, nohAtual = -1):
        """
        Insere um novo noh. Considera a regra de arvores
        binarias de busca em que a subarvore esquerda de um determinado noh 
        deve ter uma chaves menores que a desse noh, enquanto que a subarvore direita 
        deve ter chaves maiores
        """
        
        # se a arvore ainda nao possui noh raiz
        if self.root == None:
            self.root = Node(data)
            
        else:
            
            if nohAtual == -1: 
                nohAtual = self.root
        
            # se o valor do novo noh for menor que o valor do noh atual, insere na esquerda
            if data < nohAtual.data:
                
                if nohAtual.left is None:
                    
                    # insere um novo noh com o valor desejado na esquerda
                    nohAtual.left = Node(data)
                    
                else:
                    # se ja existe um noh na esquerda, nao podemos inserir o novo noh
                    # diretamente. Precisamos chamar a funcao insert recursivamente no 
                    # noh da esquerda
                    self.insert( data, nohAtual.left )
                
                
            # se o valor do novo noh for maior ou igual que o valor do noh atual, insere na direita
            else:
                
                if nohAtual.right is None:
                    
                    # insere um novo noh com o valor desejado na direita
                    nohAtual.right = Node(data)
                    
                else:
                    # se ja existe um noh na direita, nao podemos inserir o novo noh
                    # diretamente. Precisamos chamar a funcao insert recursivamente no 
                    # noh da direita
                    self.insert( data, nohAtual.right )
                    
                    
    def delete(self, searchedData, nohAtual = -1):
        """
        Deleta o noh que possui valor igual ao que foi informado na entrada.
        """
        
        if nohAtual == -1:
            nohAtual = self.root 
            
        previousNode = None
        encontrou = False
        while nohAtual is not None and encontrou == False:
            
            # se o dado que sera removido for igual ao dado do noh atual
            if searchedData == nohAtual.data:
                
                encontrou = True
                
                # se o previousNode eh None, significa que estamos removendo a raiz.
                # Portanto, devemos setar a raiz adequadamente
                if previousNode == None:
                    
                    # se a esquerda e direita do noh que sera excluido sao none, significa que a arvore ficara vazia
                    if nohAtual.left is None and nohAtual.right is None:
                        self.root = None
                    
                    # se o filho da esquerda eh None, a raiz recebe a subarvore da direita
                    elif nohAtual.left is None:
                        self.root = nohAtual.right
                        
                    # se o filho da direta eh None, a raiz recebe a subarvore da esquerda
                    elif nohAtual.right is None:
                        self.root = nohAtual.left
                        
                    # trata o caso onde o noh a ser removido tem filho na direita e na esquerda
                    # substitui o noh a ser excluido por um sucessor: aquele mais a esquerda da subarvore a direita
                    # outra opcao de sucessor que poderia ter sido usada eh: o noh mais a direita da subárvore esquerda
                    else:

                        # noh pai do no que ira se tornar o sucessor
                        auxPrevSucessor = nohAtual
                        
                        # noh que ira se tornar o sucessor
                        auxSucessor = nohAtual.right
                        
                        # atualiza o no noh sucessor na arvore: aquele mais a esquerda da 
                        # subarvore da direita do noh que sera removido
                        while auxSucessor.left is not None:
                            auxPrevSucessor = auxSucessor
                            auxSucessor = auxSucessor.left
                           
                        # caso o noh pai do sucessor seja diferente do noh que sera removido
                        # o seu filho a esquerda sera None, porque ele ira se tornar um noh folha
                        if auxPrevSucessor != nohAtual:
                            auxPrevSucessor.left = None

                        # caso o noh sucessor nao seja o proprio noh a direita do noh a ser removido,
                        # ele devera assumir o filho da direita do noh a ser removido                       
                        if auxSucessor != nohAtual.right:
                            auxSucessor.right = nohAtual.right
                           
                        # o noh sucessor deve assumir o filho da esquerda do noh que sera removido
                        auxSucessor.left = nohAtual.left
                        
                        self.root = auxSucessor

                # se o valor do noh anterior for > que o noh atual, 
                # segnifica que o noh atual esta do lado esquerdo do seu pai
                elif previousNode.data > nohAtual.data:   

                    # se a esquerda e direita do noh que sera excluido sao none, 
                    # significa que o pai dele se tornara uma folha                     
                    if nohAtual.left is None and nohAtual.right is None:
                        previousNode.left = None
                        
                    # se o filho da esquerda eh None, a pai dele recebe a subarvore da direita 
                    elif nohAtual.left is None:
                        previousNode.left = nohAtual.right
                        
                    # se o filho da direta eh None, a pai dele recebe a subarvore da esquerda
                    elif nohAtual.right is None:
                        previousNode.left = nohAtual.left
                        
                    # trata o caso onde o noh a ser removido tem filho na direita e na esquerda
                    # substitui o noh a ser excluido por um sucessor: aquele mais a esquerda da subarvore a direita
                    # outra opcao de sucessor que poderia ter sido usada eh: o noh mais a direita da subárvore esquerda
                    else:
                        
                        # noh pai do no que ira se tornar o sucessor
                        auxPrevSucessor = nohAtual
                        
                        # noh que ira se tornar o sucessor
                        auxSucessor = nohAtual.right
                        
                        # atualiza o no noh sucessor na arvore: aquele mais a esquerda da 
                        # subarvore da direita do noh que sera removido
                        while auxSucessor.left is not None:
                            auxPrevSucessor = auxSucessor
                            auxSucessor = auxSucessor.left
                           
                        # caso o noh pai do sucessor seja diferente do noh que sera removido
                        # o seu filho a esquerda sera None, porque ele ira se tornar um noh folha
                        if auxPrevSucessor != nohAtual:
                            auxPrevSucessor.left = None

                        # caso o noh sucessor nao seja o proprio noh a direita do noh a ser removido,
                        # ele devera assumir o filho da direita do noh a ser removido                       
                        if auxSucessor != nohAtual.right:
                            auxSucessor.right = nohAtual.right
                           
                        # o noh sucessor deve assumir o filho da esquerda do noh que sera removido
                        auxSucessor.left = nohAtual.left
                            
                        # o noh sucessor se tornara o filho da esquerda 
                        # do noh que sera removido
                        previousNode.left = auxSucessor


                # se o valor do noh anterior for < que o noh atual, 
                # significa que o noh atual esta do lado direito do seu pai                        
                elif previousNode.data < nohAtual.data:

                    # se a esquerda e direita do noh que sera excluido sao none, 
                    # significa que o pai dele se tornara uma folha                       
                    if nohAtual.left is None and nohAtual.right is None:
                        previousNode.right = None
                        
                    # se o filho da esquerda eh None, a pai dele recebe a subarvore da direita                         
                    elif nohAtual.left is None:
                        previousNode.right = nohAtual.right
                        
                    # se o filho da direta eh None, a pai dele recebe a subarvore da esquerda
                    elif nohAtual.right is None:
                        previousNode.right = nohAtual.left
                        
                    # trata o caso onde o noh a ser removido tem filho na direita e na esquerda
                    # substitui o noh a ser excluido por um sucessor: aquele mais a esquerda da subarvore a direita
                    # outra opcao de sucessor que poderia ter sido usada eh: o noh mais a direita da subárvore esquerda
                    else:
                        
                        # noh pai do no que ira se tornar o sucessor
                        auxPrevSucessor = nohAtual
                        
                        # noh que ira se tornar o sucessor
                        auxSucessor = nohAtual.right
                        
                        # atualiza o no noh sucessor na arvore: aquele mais a esquerda da 
                        # subarvore da direita do noh que sera removido
                        while auxSucessor.left is not None:
                            auxPrevSucessor = auxSucessor
                            auxSucessor = auxSucessor.left
                           
                        # caso o noh pai do sucessor seja diferente do noh que sera removido
                        # o seu filho a esquerda sera None, porque ele ira se tornar um noh folha
                        if auxPrevSucessor != nohAtual:
                            auxPrevSucessor.left = None

                        # caso o noh sucessor nao seja o proprio noh a direita do noh a ser removido,
                        # ele devera assumir o filho da direita do noh a ser removido                       
                        if auxSucessor != nohAtual.right:
                            auxSucessor.right = nohAtual.right
                           
                        # o noh sucessor deve assumir o filho da esquerda do noh que sera removido
                        auxSucessor.left = nohAtual.left

                        # o noh sucessor se tornara o filho da esquerda 
                        # do noh que sera removido                            
                        previousNode.right = auxSucessor

            # se o dado que sera removido for menor que o dado do noh atual                            
            elif searchedData < nohAtual.data:
                
                # se o filho da esquerda eh None, significa que o dado que 
                # foi passado como entrada nao existe na arvore
                if nohAtual.left is None:
                    nohAtual = None
                    print('Valor não encontrado')                    
                
                else:
                    # atualiza o noh atual e o seu pai
                    previousNode = nohAtual
                    nohAtual = nohAtual.left   


            # se o dado que sera removido for maior que o dado do noh atual                 
            else:
                
                # se o filho da direita eh None, significa que o dado que 
                # foi passado como entrada nao existe na arvore
                if nohAtual.right is None:
                    nohAtual = None
                    print('Valor não encontrado')   
                    
                else:
                    # atualiza o noh atual e o seu pai
                    previousNode = nohAtual
                    nohAtual = nohAtual.right   

            
        # deleta o noh
        del nohAtual
            
            
    def strPreorder(self, nohAtual = -1, info = ''):
        """
        Retorna uma string com os valores da arvore obtidos apos 
        o percurso "Pre Ordem"
        """
        
        if self.root is None:
            return ' '
            
        else:
            
            if nohAtual==-1:
                nohAtual = self.root
            
            if nohAtual.data is not None:
                
                info += ' ' + str(nohAtual.data)
                
                info += '('
                
                if nohAtual.left is not None: 
                    info += self.strPreorder(nohAtual.left)
                
                if nohAtual.right is not None:
                    info += self.strPreorder(nohAtual.right)
                    
                info += ' )'
                
                return info
            else:
                return info

        


if __name__ == "__main__":
    #---------------------    
    # testando a arvore
    
    tree1 = Tree()
    tree1.insert(6)
    tree1.insert(2)
    tree1.insert(7)
    tree1.insert(1)
    tree1.insert(3)
    tree1.insert(5)
    tree1.insert(4)
    
    info = tree1.strPreorder()
    print('strPreorder():', info)
