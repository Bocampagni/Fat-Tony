class main:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

    def getVertices(self):
        return list(self.gdict.keys())

    def getEdges(self):
        return list(self.gdict.values())
    
    def getGraphSize(self):
        amountOfEdges = 0
        for edge in self.getEdges():
            amountOfEdges+= len(edge)

        return len(self.getVertices()) + amountOfEdges

graph_elements = { 
   "a" : ["b","c"],
   "b" : ["a", "d"],
   "c" : ["a", "d"],
   "d" : ["e"],
   "e" : ["d"]
}
g = main(graph_elements)
print("Edges: ", g.getEdges()) 
print("Vertices: ", g.getVertices())
print("Size: ", g.getGraphSize())
