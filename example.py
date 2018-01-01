#from buildindex import BuildIndex
from querytexts import Query

q = Query(['corpus/pg135.txt', 'corpus/pg76.txt', 'corpus/pg5200.txt'])

rank1 = q.phrase_query(string='the three of them left')
print(rank1)

rank2 = q.phrase_query(string='this ebook')
print(rank2)

rank3 = q.one_word_query(word='three')
print(rank3)

