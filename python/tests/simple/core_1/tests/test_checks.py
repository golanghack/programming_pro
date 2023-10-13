#! /usr/bin/env python3 

import pytest

class InvalidCharacterNameError(Exception):
    pass

class InvalidClassNameError(Exception):
    pass

class Character:
    pass

VALID_CLASSES = ['sorcerer', 'warrior']

def create_character(name: str, class_name: str) -> Character:
    """ 
    Creates a new character and inserts it into the database.
    :param name: the character name.
    :param class_name: the character class name.
    :raise IvalidCharacterNameError:
        if the character name is empty.
    :raise InvalidClassNameError:
        if the class name is invalid.
    :return: the newlycreate Character.
    """
    
    if not name:
        raise InvalidCharacterNameError('character name is empty.')
    if class_name not in VALID_CLASSES:
        message = f'Invalid class name -> "{class_name}"'
        raise InvalidCharacterNameError(message)
    
def test_empty_name() -> None:
    with pytest.raises(InvalidCharacterNameError):
        create_character(name='', class_name='warrior')
        
def test_invalid_class_name() -> None:
    with pytest.raises(InvalidClassNameError):
        create_character(name='Solaire', class_name='mage')
        
    