from rdflib import Graph

g = Graph()

g.parse("http://bigasterisk.com/foaf.rdf")

qres = g.query(
    """CONSTRUCT ?a foaf:friends ?b
       WHERE {
          ?a foaf:knows ?b .
          ?b foaf:knows ?a .
       }""")

for row in qres:
    print("%s knows %s" % row)
