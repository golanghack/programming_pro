#! /usr/bin/env python3
import feedparser
from flask import Flask

app = Flask(__name__)
FEEDS = {'prolog': 'https://www.prlog.org/news/rss.xml',
            'art': 'https://rss.art19.com/apology-line',
            'freeds': 'https://feeds.simplecast.com/54nAGcIl',
            'crime': 'https://feeds.simplecast.com/qm_9xx0g',
        }

def get_news(rubric):
    field = 'entries'
    main_feed = feedparser.parse(FEEDS[rubric])
    first_article = main_feed[field][0]
    return f""" 
        <html>
            <body>
                <h1>News</h1>
                <b>{first_article.get('title')}</b></br>
                <i>{first_article.get('published')}</i> </br>
                <p>{first_article.get('summary')}</p></br>
            </body>
        </html>
        """ 

@app.route('/')
@app.route('/prolog')
def get_prolog():
    return get_news('prolog')

@app.route('/art')
def get_art():
    return get_news('art')

@app.route('/freeds')
def get_freeds():
    return get_news('freeds')

@app.route('/crime')
def get_crime():
    return get_news('crime')


if __name__ == '__main__':
    app.run(port=5555, debug=True)