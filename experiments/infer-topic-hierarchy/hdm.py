from gensim.corpora import TextCorpus, MmCorpus, Dictionary
from gensim.models import TfidfModel
from gensim.models.ldamodel import LdaModel
from gensim.models.hdpmodel import HdpModel
import bz2
    
out = '/home/mjg/data/descriptions'    
    
# Form corpus
corpus = TextCorpus(bz2.BZ2File(out + '.bz2'))

# remove common words
stoplist = set('a,able,about,across,after,all,almost,also,am,among,an,and,any,are,as,at,be,because,been,but,by,can,cannot,could,dear,did,do,does,either,else,ever,every,for,from,get,got,had,has,have,he,her,hers,him,his,how,however,i,if,in,into,is,it,its,just,least,let,like,likely,may,me,might,most,must,my,neither,no,nor,not,of,off,often,on,only,or,other,our,own,rather,said,say,says,she,should,since,so,some,than,that,the,their,them,then,there,these,they,this,tis,to,too,twas,us,wants,was,we,were,what,when,where,which,while,who,whom,why,will,with,would,yet,you,your'.split(','))
stop_ids = [corpus.dictionary.token2id[stopword] for stopword in stoplist if stopword in corpus.dictionary.token2id]
corpus.dictionary.filter_tokens(stop_ids)

# only keep the most frequent words
corpus.dictionary.filter_extremes(no_below = 20, no_above = 0.1, keep_n = 100000)
# save stuff
MmCorpus.serialize(out + '_bow.mm', corpus, progress_cnt = 10000)
corpus.dictionary.save_as_text(out + '_wordids.txt.bz2')
# save memory
dictionary = Dictionary.load_from_text(out + '_wordids.txt.bz2')
del corpus

# initialize corpus reader and word->id mapping
mm = MmCorpus(out + '_bow.mm')

# build tfidf
tfidf = TfidfModel(mm, id2word = dictionary, normalize = True)
tfidf.save(out + '.tfidf.model')
MmCorpus.serialize(out + '_tfidf.mm', tfidf[mm], progress_cnt=10000)

# Run hierarchical Dirichlet process over corpus
hda = HdpModel(corpus = mm, id2word = dictionary)
hda.save(out + ".hdm")
