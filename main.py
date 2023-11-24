# app.py

from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

NEWS_API_URL = 'https://newsapi.org/v2/top-headlines'


@app.route('/news', methods=['GET'])
def get_news():
    country = request.args.get('country') or 'us'
    api_key = request.args.get('apiKey')

    params = {'q': country, 'apiKey': api_key}
    response = requests.get(NEWS_API_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        articles = data.get('articles', [])
        formatted_articles = [{'title': article['title'], 'description': article['description']} for article in
                              articles]
        return jsonify({'articles': articles})
    else:
        return jsonify({'error': 'Failed to fetch news data'}), 500


if __name__ == '__main__':
    app.run(debug=True)
