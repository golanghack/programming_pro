"""Counting word in website"""

import requests
from typing import List, Callable

def most_common_word_in_web_page(words: List[str], target_url: str) -> Callable:
    """ Return most common word from a list of words on url page"""

    response = requests.get(target_url)
    return most_common(words, response.text)

def most_common(words: List[str], text: str) -> int:
    """Return common word from a list of words in parts of text."""

    dict_word_frequency = {word: text.count(word) for word in words}
    return sorted(words, key=dict_word_frequency.get)[-1]