from flask import Flask, jsonify, request
import csv
from storage import liked_articles,not_liked_articles,all_articles,output
from contentfiltering import getreccomandation
all_articles = []

with open('articles.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

liked_articles = []
not_liked_articles = []


app = Flask(__name__)
@app.route("/get-article") 
def get_article(): 
    article_data = {
         "url": all_articles[0][11], 
         "title": all_articles[0][12], 
         "text": all_articles[0][13], 
         "lang": all_articles[0][14], 
         "total_events": all_articles[0][15] 
         } 
    return jsonify({ "data": article_data, "status": "success" })
    
@app.route("/liked-article", methods=["POST"]) 
def liked_article(): 
    article = all_articles[0] 
    liked_articles.append(article) 
    all_articles.pop(0) 
    return jsonify({ "status": "success" })

def not_liked_article(): 
    article = all_articles[0] 
    not_liked_articles.append(article) 
    all_articles.pop(0) 
    return jsonify({ "status": "success" })


def populararticles():
    article_data=[]
    for article in output:
        d={
          "url": all_articles[0][11], 
         "title": all_articles[0][12], 
         "text": all_articles[0][13], 
         "lang": all_articles[0][14], 
         "total_events": all_articles[0][15] 
        }
        article_data.append(d)
    return jsonify({
        'data':article_data,
        'status':'win'

             })   
if __name__ == "__main__":
  app.run()