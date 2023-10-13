#! /usr/bin/env python3 


def dup(any_list: list) -> bool:
    """Searchin duplicate in list.
    
    :param -> list -> any list, any len(list).
    :return -> bool.
    """
    
    duplicate: list = [x for i, x in enumerate(any_list) if x in any_list[:i]]
    
    if len(duplicate) != 0:
        return False
    return True

def test_dup() -> None:
    
    assert (not dup([1, 2, 6, 3, 4, 5, 6, 7, 8]))
    assert (dup([1, 2, 3, 4]))

if __name__ == '__main__':
    import pytest
    pytest.main()
    