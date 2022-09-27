import pandas as pd
import numpy as np

df=pd.read_csv('articles.csv')
C=df['vote_average'].mean()
m=df['vote_count'].quantile(0.87)
qarticles=df.copy().loc[df['vote_count']>m]
def weightedrating(x,m=m,C=C):
  v=x['vote_count']
  R=x['vote_average']
  return ((v/(v+m))*R)+((m/(v+m))*C)

qarticles['score']=qarticles.apply(weightedrating,axis=1)
qarticles=qarticles.sort_values('score',ascending=False)
output=qarticles['title','contentId','total_events','eventType'].head(20).values.tolist()

