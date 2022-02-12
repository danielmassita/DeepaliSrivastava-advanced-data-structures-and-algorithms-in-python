# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

class Vertex:
        def __init__(self, name):
           self.name = name

	  
class DirectedGraph:

        def __init__(self,size=20):
           self._adj = [  [0 for column in range(size)]  for row in range(size) ]
           self._n = 0
           self._vertexList = []
           

        def display(self):
            for i in range(self._n):
                for j in range(self._n):
                   print( self._adj[i][j], end =' ')
                print()


        def numVertices(self):
            return self._n


        def numEdges(self):
            e = 0
            for i in range(self._n):
                for j in range(self._n):
                    if self._adj[i][j]!=0:
                        e+=1
            return e


        def vertices(self):
            return [vertex.name for vertex in self._vertexList]


        def edges(self):
            edges = []
            for i in range(self._n):
                for j in range(self._n):
                   if self._adj[i][j] != 0:
                      edges.append( (self._vertexList[i].name, self._vertexList[j].name) )
            return edges


        def _getIndex(self,s):
            index = 0
            for name in (vertex.name for vertex in self._vertexList):
                if s == name:
                   return index
                index += 1
            return None


        def insertVertex(self,name):
            if name in (vertex.name for vertex in self._vertexList): 
                print("Vertex with this name already present in the graph")
                return
                
            self._vertexList.append( Vertex(name) )  
            self._n += 1


        def insertEdge(self, s1, s2):
            u = self._getIndex(s1)
            v = self._getIndex(s2)
            if u is None:
                print("Start vertex not present in the graph, first insert the start vertex")
            elif v is None:
                print("End vertex not present in the graph, first insert the end vertex")
            elif u == v:
                print("Not a valid edge") 
            elif self._adj[u][v] != 0 :
    	        print("Edge already present in the graph") 
            else:  
                self._adj[u][v] = 1


        def removeEdge(self, s1, s2):
             u = self._getIndex(s1)
             v = self._getIndex(s2)
             if u is None:
                print("Start vertex not present in the graph")
             elif v is None:
                print("End vertex not present in the graph")
             elif self._adj[u][v] == 0:
                print("Edge not present in the graph")
             else:	  
                self._adj[u][v] = 0


        def removeVertex(self,name):
             u = self._getIndex(name)
             if u is None:
                print("Vertex not present in the graph")
                return
        
             self._adj.pop(u)

             for i in range(self._n):
                  self._adj[i].pop(u)
                  
             self._vertexList.pop(u)
             self._n -= 1
               
   
        def isAdjacent(self, s1, s2):
            u = self._getIndex(s1)
            v = self._getIndex(s2)
            if u is None:
                print("Start vertex not present in the graph")
                return False
            elif v is None:
                print("End vertex not present in the graph")
                return False
            return False if self._adj[u][v] == 0 else True   

      
        def outdegree(self, s):
            u = self._getIndex(s)
            if u is None:
               print("Vertex not present in the graph")
               return
        
            outd = 0
            for v in range(self._n):
                if self._adj[u][v] != 0 :
                   outd+=1
            return outd
             

        def indegree(self, s):
            u = self._getIndex(s)
            if u is None:
               print("Vertex not present in the graph")
               return
        
            ind = 0

            for v in range(self._n):
                if self._adj[v][u] != 0 :
                    ind+=1
            return ind


if __name__ == '__main__':

  g = DirectedGraph() 

  g.insertVertex("AA")
  g.insertVertex("BB")
  g.insertVertex("CC")
  g.insertVertex("DD")
  g.insertVertex("EE")

  g.insertEdge("AA","BB")
  g.insertEdge("AA","CC")
  g.insertEdge("CC","DD")
  g.insertEdge("DD","AA")
  g.insertEdge("CC","AA")
  g.insertEdge("BB","EE")

  while True:
      print("1.Display Adjacency list, vertices and edges")
      print("2.Insert a vertex")
      print("3.Remove a vertex")
      print("4.Insert an edge")
      print("5.Delete an edge")
      print("6.Display indegree and outdegree of a vertex")
      print("7.Check if there is an edge between two vertices")
      print("8.Quit")
        
      option = int(input("Enter your choice : " ))

      if option == 1:
          g.display()
          print("Number of vertices : ", g.numVertices() )
          print("Number of edges : ", g.numEdges() )
          print("List of Vertices : ", g.vertices() )
          print("List of Edges : ", g.edges() )
      elif option == 2:
          s = input("Enter the name of vertex : ")
          g.insertVertex(s)
      elif option == 3:
          s = input("Enter the name of vertex : ")
          g.removeVertex(s)
      elif option == 4:
          s1 = input("Enter the name of start vertex : ")
          s2 = input("Enter the name of end vertex : ")
          g.insertEdge(s1,s2)
      elif option == 5:
          s1 = input("Enter the name of start vertex : ")
          s2 = input("Enter the name of end vertex : ")
          g.removeEdge(s1,s2)
      elif option == 6:
          s = input("Enter vertex name : ")
          i = g.indegree(s)
          if i is not None:
             print("Indegree of", s , "is", i)
          o = g.outdegree(s)
          if o is not None:
             print("Outdegree of", s , "is", o)
      elif option == 7:
          s1 = input("Enter the name of first vertex : ")
          s2 = input("Enter the name of second vertex : ")
          if g.isAdjacent(s1, s2):
              print("There is an edge from ", s1 , " to " , s2)
          else:
              print("There is no edge from " , s1 , " to " , s2)
      elif option == 8:
          break
      else:
          print("Wrong option")
   
      print()


   
