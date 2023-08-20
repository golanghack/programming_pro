"""Counting word in website"""

import requests
from typing import List, Callable

def most_common_word_in_web_page(words: List[str], 
                                target_url: str,
                                user_agent=requests) -> Callable:
    """ Return most common word from a list of words on url page"""

    response = user_agent.get(target_url)
    return most_common(words, response.text)

def most_common(words: List[str], text: str) -> int:
    """Return common word from a list of words in parts of text."""

    dict_word_frequency = {word: text.count(word) for word in words}
    if len(words) < 1:
        raise Exception(IndexError, 'added element in list')
    return sorted(words, key=dict_word_frequency.get)[-1]