from flask import Flask, jsonify
from db_controller import fetch_article_by_url, fetch_new_articles, top_five_authors, all_articles

app = Flask(__name__)


@app.route('/fetch_article/<url>', methods=['GET'])
def fetch(url):
    article = fetch_article_by_url(url)
    if article:
        return jsonify(article)
    else:
        return jsonify({"message": "Article not found"}), 404


@app.route('/fetch_new_articles', methods=['GET'])
def fetch_new():
    fetch_new_articles()
    return jsonify({"message": "Fetching new articles initiated"})\



@app.route('/fetch_top_authors', methods=['GET'])
def fetch_top_authors():
    top_authors = top_five_authors()
    return jsonify(top_authors)


@app.route('/fetch_all_articles', methods=['GET'])
def fetch_all_articles():
    articles = all_articles()
    return jsonify(articles)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
