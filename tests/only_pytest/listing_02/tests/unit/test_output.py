#! /usr/bin/env python3 

import pytest
import src.fizzbuzz
from src.fizzbuzz import out_fizz, out_buzz, end_num

@pytest.fixture(params=['fizz', 'buzz'])
def expected_output(request):
    text = request.param
    if request.config.getoption('--upper'):
        text = text.upper()
    
    text_case_marker = request.node.get_marker('textcase')
    if text_case_marker:
        text_case, = text_case_marker.args
        if text_case == 'upper':
            text = text.upper()
        elif text_case == 'lower':
            text = text.lower()
        else:
            raise ValueError('Invalid Test Marker')

    yield getattr(src.fizzbuzz, f'out{request.param}'), text 


def test_output(expected_output, capsys):
    func, expected = expected_output

    func()

    out, _ = capsys.readouterr()
    assert out == expected

@pytest.mark.text_case('lower')
def test_lowercase_output(expected_output, capsys):
    func, expected = expected_output
    
    func()

    out, _ = capsys.readouterr()
    assert out == expected

class TestEndNum:

    def test_plain_number(self, capsys):
        end_num(1)
        end_num(4)
        end_num(7)

        out, _ = capsys.readouterr()

        assert out == '1\n4\n7\n'

    def test_omit_number(self, capsys):
        end_num(3)
        end_num(5)
        end_num(15)

        out, _ = capsys.readouterr()

        assert out == '\n\n\n'