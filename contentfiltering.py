from ast import literal_eval 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy
import pandas as pd

df=pd.read_csv('articles.csv')
df=df[df['title'].notna()]

count=CountVectorizer(stop_words='english')
count_matrix=count.fit_transform(df['title'])


cosine_sim=cosine_similarity(count_matrix,count_matrix)
df=df.reset_index()
indices=pd.Series(df.index,index=df['title'])

def getreccomandation(title):
  idx=indices[title]
  scores=list(enumerate(cosine_sim[idx]))
  scores=sorted(scores,key=lambda x:x[1],reverse=True)
  scores=scores[1:21]
  movies_indices=[i[0]for i in scores]
  return df['title'].iloc[movies_indices]

