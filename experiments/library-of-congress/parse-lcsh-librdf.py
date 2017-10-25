#!/usr/bin/env python2.7
#
# 2016-05-14 <mhucka@caltech.edu> Initially based on Matthew's code.
#
# I converted the NRF

from rdflib import Graph, ConjunctiveGraph, URIRef, RDFS, Literal
from rdflib.namespace import RDF, SKOS

lcsh = Graph("Sleepycat")
lcsh.open("store", create = True)
result = lcsh.parse("x", format="nt")

# predicates:
prefLabel = URIRef(u'http://www.w3.org/2004/02/skos/core#prefLabel')
altLabel  = URIRef(u'http://www.w3.org/2004/02/skos/core#altLabel')
broader   = URIRef(u'http://www.w3.org/2004/02/skos/core#broader')

def get_id(term):
    id = term.toPython()
    return id[id.rfind('/') + 1:].encode('utf-8')

labels = {}
count = 0
for subject, predicate, object in lcsh:
    count += 1
    id = get_id(subject)
    if predicate == prefLabel:
        labels[id] = object.toPython().encode('utf-8', 'replace')
    if count == 10000:
        break

print('{} pref labels'.format(len(labels)))

terms = {}
count = 0
for subject, predicate, object in lcsh:
    count += 1
    id = get_id(subject)
    if predicate == altLabel:
        others = terms[id][1] if id in terms else []
        others.append(object.toPython().encode('utf-8', 'replace'))
        if id in labels:
            terms[id] = (labels[id], others, None)
        else:
            import ipdb; ipdb.set_trace()

print('{} terms'.format(len(terms)))
print('{} alt labels'.format(count))

count = 0
for subject, predicate, object in lcsh:
    count += 1
    id = get_id(subject)
    if predicate == broader:
        import ipdb; ipdb.set_trace()
        others = terms[id][2]
        if others:
            others.append(get_id(object))
        else:
            others = [get_id(object)]
        terms[id] = (terms[id][0], terms[id][1], others)

print('{} broader terms'.format(count))

import ipdb; ipdb.set_trace()


pass
# each has
# - its own identifier, of the form http://id.loc.gov/authorities/subjects/sh85098119
# - one preflabel (a string)
# - one or more altlabels
# - one or more broader terms
#
# reduce the term id to the shxxxxx string.
# create a dictionary of tuples:
#   term: (label, [alt labels...], [broader terms...])
# where "term" is a string of the form shxxxxx.
# then walk down the structure and create a second dictionary:
#   term: [narrower terms...]
#
# still need to figure out how to find the top-most terms
#
# Output:
# term (label)
#    term (label == altlabel == altlabel)
#    term (label == altlabel == altlabel)
#       term (label == altlabel == altlabel)
#    term (label == altlabel == altlabel)

