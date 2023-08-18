#! /usr/bin/env python3 

import locale
import pytest

@pytest.fixture(autouse=True)
def setup_locale() -> None:
    locale.setlocale(locale.LC_ALL, 'en_US')
    yield
    locale.setlocale(locale.LC_ALL, None)
    
def test_currency_us() -> None:
    assert locale.currency(10.5) == '$10.50'
    
@pytest.fixture(autouse=True)
def setup_locale(request) -> None:
    mark = request.node.get_closest_marker('change_locale')
    loc = mark.args[0] if mark is not None else 'en_US'
    locale.setlocale(locale.LC_ALL, loc)
    yield
    locale.setlocale(locale.LC_ALL, None)
    
    
@pytest.mark.change_locale('pt_BR')
def test_currency_br() -> None:
    assert locale.currency(10.5) == 'R$ 10.50'
    