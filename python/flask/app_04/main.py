#! /usr/bin/env python3
import feedparser
from flask import Flask
from flask import render_template

app = Flask(__name__)
FEEDS = {'prolog': 'https://www.prlog.org/news/rss.xml',
            'art': 'https://rss.art19.com/apology-line',
            'freeds': 'https://feeds.simplecast.com/54nAGcIl',
            'crime': 'https://feeds.simplecast.com/qm_9xx0g',
        }

@app.route('/')
@app.route('/<rubric>')
def get_news(rubric='crime'):
    field = 'entries'
    main_feed = feedparser.parse(FEEDS[rubric])
    return render_template('home.html',
                            articles=main_feed[field])

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