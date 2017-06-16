from rdflib import Graph

#g = Graph()

#g.parse('my_rdf.n3', format='n3')

#print( g.serialize(format='n3') )


print('\n\n\n===========================\n\n\n')
g2 = Graph()
g2.parse("http://bigasterisk.com/foaf.rdf")

print( g2.serialize(format='nt') )
