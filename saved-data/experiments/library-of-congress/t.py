import RDF
parser = RDF.Parser(name="ntriples")
model = RDF.Model()
stream = parser.parse_into_model(model, 'file:///tmp/x')
for triple in model:
    import ipdb; ipdb.set_trace()
