#! /usr/bin/env python3

from queue import Queue
import threading
import urllib
from urllib.parse import urlparse
import feedparser

# Global
num_fetch_threads = 2
enclosure_queue = Queue()

# dont this in production app
feed_urls = [
    'https://talkpython.fm/episodes/rss',
]

def message(s: str) -> str:
    """Return messagers."""
    
    print(f'{threading.current_thread().name} -> {s}')
    
def download_enclosures(queue_elements):
    """Fucntion work thread.
    Work with elements from queue one to one.
    Threads this process-deamon into no-level loop
    and stop only then stop main thread.
    """
    while True:
        message('Looking for next eclosure')
        url = queue_elements.get()
        filename = url.rpartition('/')[-1]
        message(f'downloading {filename}')
        response = urllib.request.urlopen(url)
        data = response.read()
        
        # save downloading file in current directory
        message(f'Writing to {filename}')
        with open(filename, 'wb') as outfile:
            outfile.write(data)
        queue_elements.task_done()
        
# settin threads for outing includes
for i in range(num_fetch_threads):
    worker = threading.Thread(target=download_enclosures, args=(enclosure_queue,), name=f'worker-{i}')
    worker.setDaemon(True)
    worker.start()
    
# downloading chanels and adding URL in queue
for url in feed_urls:
    response = feedparser.parse(url, agent='fetch_podcast.py')
    for entry in response['entries'][:5]:
        for enclosure in entry.get('enclosures', []):
            parsed_url = urlparse(enclosure['url'])
            message(f'queuing {parsed_url.path.rpartition("/")[-1]}')
            enclosure_queue.put(enclosure['url'])
            
# wait end queue - downloading full all
message('*** main thread waiting')
enclosure_queue.join()
message('*** done')
        