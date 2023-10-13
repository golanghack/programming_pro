#! /usr/bin/env python3 

import pytest


def test_tmp(tmp_path: str):
    file = tmp_path / 'file.txt'
    print('FILE -> ', file)

    file.write_text('Hello')

    file_read = tmp_path / 'file.txt'
    assert file_read.read_text() == 'Hello'