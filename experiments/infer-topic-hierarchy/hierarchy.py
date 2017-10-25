#
# Induce a hierarchy from the probabilistic generative model fit to the corpus
#
import numpy as np
from gensim.corpora import Dictionary
from gensim.models.hdpmodel import HdpModel
from collections import OrderedDict
from scipy.stats import dirichlet
import edmonds
import pickle

out = '/home/mjg/data/descriptions'

# Load model
dictionary = Dictionary.load_from_text(out + '_wordids.txt.bz2')
hda = HdpModel.load(out + ".hdm")
topics = hda.show_topics(-1, -1, formatted=False)    

def mkarray(l):
  a = np.array([x for x in l])
  return a


# Calculate corpus probabilities
alpha = 0.1 * len(dictionary)
phi = []
for i in range(len(topics)):
  phic = {}
  for j in range(len(topics[i][1])):
    phic[topics[i][1][j][0]] = topics[i][1][j][1] 
  phi.append(OrderedDict(sorted(phic.items())))

# Make sure phi is that properly normalized
for i in range(len(topics)):
  norm = 1. / np.sum(mkarray(phi[i].values()))
  for key in phi[i]:
    phi[i][key] *= norm

def logprob(phi_c, phi_parent, root, alpha):
  x = mkarray(phi_c.values())
  if phi_parent == root:
    a = np.ones_like(x)
  else:
    a = alpha * mkarray(phi_parent.values())
  return dirichlet.logpdf(x, a)

# Determine maximum spanning tree 
root = np.random.randint(len(topics))
G = {}
for i in range(len(topics)):
  G[i] = {}
  for j in range(len(topics)):
    G[i][j] = -logprob(phi[i], phi[j], root, alpha)
    
g = edmonds.mst(root, G)

# Save tree
pickle.dump(g, open(out + ".mst", "wb"))
