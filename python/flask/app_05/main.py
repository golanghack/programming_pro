#! /usr/bin/env python3


import feedparser
from flask import Flask
from flask import render_template
from flask import request
from weather import weater_function as weather 

app = Flask(__name__)

FEEDS = {'prolog': 'https://www.prlog.org/news/rss.xml',
            'art': 'https://rss.art19.com/apology-line',
            'freeds': 'https://feeds.simplecast.com/54nAGcIl',
            'crime': 'https://feeds.simplecast.com/qm_9xx0g',
        }

@app.route('/', methods=['GET', 'POST'])
@app.route('/<rubric>')
def get_news():
    field = 'entries'
    query = request.form.get('rubric')
    weather_query = request.form.get('weather')
    if not query or query.lower() not in FEEDS:
        query = 'prolog'
    if not weather_query or weather_query == '':
        weather_query = 'Moscow'
    rubric = query.lower()
    feed = feedparser.parse(FEEDS[rubric])
    weather_full = weather(weather_query)

    return render_template('home.html', 
                            weather=weather_full,
                            articles=feed[field]
                            )


if __name__ == '__main__':
    app.run(port=5555, debug=True)