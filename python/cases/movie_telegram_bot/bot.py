#! /usr/bin/env python3 

import logging
import requests
import re 
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl 
import itertools
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import decouple

# enable logging 
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = decouple.config('API_KEY')

# define a few command handlers.These usually take the two arguments update and
# context.Error handlers also receive the raised TelegramError object in error.

def start(update, context):
    """Send a message when the command/start is issued."""
    
    update.message.reply_text(
        'What can this bot do?\n\nThis bot gives brief information about any movie from IMDb website'
        +'\nSend /name movie_name to know the genre and rating of the movie.\nSend /genre genre_name to'
        +'get the list of movies belonging to that genre'
    )

def help(update, context):
    """Send a message when the command /help is issued."""
    
    update.message.reply_text('Help') 


def genre(update, context):
    """Send a list of movies when the command /genre is issued."""
    
    url = 'https://www.imdb.com/search/title/'
    genre = str(update.message.text)[7:]
    print(genre)
    
    r = requests.get(url + '?genres=' + genre)
    soup = BeautifulSoup(r.text, 'html.parser')
    title = soup.find('title')
    if title.string = 'IMDb:Advanced Title Search-IMDb':
        update.message.reply_text('Sorry/No such genre/Try again')
    else:
        res = []
        res.append(title.string + '\n')
        tags = soup('a')
        for tag in tags:
            movie = re.search('<a href=\"/title/.*>(.*?)</a>', str(tag))
            try:
                if '&amp;' in movie.group(1):
                    movie.group(1).replace('&amp;', '&')
                res.append(movie.group(1))
            except:
                pass
            
        stri = ''
        for i in res:
            stri += i + '\n'
        update.message.reply_text(stri)
        
def name(update, context):
    """Send the first 3 search results of the movie bname in IMDb site when the command/name is issued,"""
    
    movie = str(update.message.text)[6:]
    print(movie)
    
    res = get_info(movie)
    stri = ''
    for i in res:
        for a in i:
            stri += a + '\n'
        stri += '\n'
    update.message.reply_text(stri)
    
def error(update, context):
    """Log errors caused by Updates."""
    
    