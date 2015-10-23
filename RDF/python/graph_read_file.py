from rdflib import Graph

g = Graph()

g.parse('my_rdf.n3', format='n3')

print( g.serialize(format='n3') )

print('\n\n\n===========================\n\n\n')

g.parse("http://bigasterisk.com/foaf.rdf")

print( g.serialize(format='n3') )
