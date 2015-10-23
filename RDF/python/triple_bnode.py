from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.namespace import DC, FOAF

g = Graph()

# Create an identifier to use as the subject for Donna.
donna = BNode()

# Add triples using store's add method.
g.add( (donna, RDF.type, FOAF.Person) )
g.add( (donna, FOAF.nick, Literal("donna", lang="foo")) )
g.add( (donna, FOAF.name, Literal("Donna Fales")) )
g.add( (donna, FOAF.mbox, URIRef("mailto:donna@example.org")) )

# Iterate over triples in store and print them out.
print("--- printing raw triples ---")
for s, p, o in g:
    print((s, p, o))

# For each foaf:Person in the store print out its mbox property.
print("--- printing mboxes ---")
for person in g.subjects(RDF.type, FOAF.Person):
    for mbox in g.objects(person, FOAF.mbox):
        print(mbox)

# Bind a few prefix, namespace pairs for more readable output
g.bind("dc", DC)
g.bind("foaf", FOAF)

print( g.serialize(format='n3') )
