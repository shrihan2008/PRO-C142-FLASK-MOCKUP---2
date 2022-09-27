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
    return jsonify({
        "data": all_articles[0],
        "status": "success"
    })

@app.route("/liked-article", methods=["POST"])
def liked_article():
    article = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(article)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/unliked-article", methods=["POST"])
def unliked_article():
    article = all_articles[0]
    all_articles = all_articles[1:]
    not_liked_articles.append(article)
    return jsonify({
        "status": "success"
    }), 201

def populararticles():
    article_data=[]
    for article in output:
        d={
           "title": article[12], 
           "eventType": article[3], 
           "contentId": article[4] ,
           
        }
        article_data.append(d)
    return jsonify({
        'data':article_data,
        'status':'win'

             })   

if __name__ == "__main__":
  app.run()