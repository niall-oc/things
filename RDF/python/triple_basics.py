from rdflib import Graph

g = Graph()

print( g.serialize(format='n3') )
