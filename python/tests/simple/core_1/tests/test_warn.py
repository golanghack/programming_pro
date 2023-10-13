#! /usr/bin/env python3 

import warnings
from enum import Enum
from typing import Union
import pytest

class PlayerClass(Enum):
    """Simple player class."""
    
    WARRIOR = 1
    KNIGHT = 2
    SORCERER = 3
    CLERIC = 4


def get_initial_hit_points(player_class: Union[PlayerClass, str]) -> int:
    """ 
    Return the initial hit points of the given class.
    :param player_class: player class name.
    """
    
    if isinstance(player_class, str):
        message = """'Using player_class as str has been deprecated'
                      'and will be removed in the future.'"""
        warnings.warn(DeprecationWarning(message))
        player_class = get_player_enum_from_string(player_class)
        
        
def get_player_enum_from_string(player_class: PlayerClass) -> dict:
    """Return dict formation from PlayerClass data and string."""
    
    return {
        'warrior': PlayerClass.WARRIOR, 
        'knight': PlayerClass.KNIGHT, 
        'sorcerer': PlayerClass.SORCERER, 
        'cleric': PlayerClass.CLERIC,
    }
    
def test_get_initial_hit_points_warning() -> None:
    with pytest.warns(DeprecationWarning, match='.*str has been deprecated.*'):
        get_initial_hit_points('warrior')