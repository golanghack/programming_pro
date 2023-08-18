#! /usr/bin/env python3 

from pathlib import Path
import unittest
from unittest import mock
from todo.db import BasicDB

class TestBasicDB(unittest.TestCase):
    
    def test_load(self):
        mock_file = mock.MagicMock(
            read=mock.Mock(return_value='["first", "second"]')
        )
        mock_file.__enter__.return_value = mock_file
        mock_opener = mock.Mock(return_value=mock_file)
        db = BasicDB(Path('testdb'), _fileopener=mock_opener)
        loaded = db.load()
        
        self.assertEqual(loaded, ['first', 'second'])
        self.assertEqual(mock_opener.call_args[0][0], Path('testdb'))
        
        mock_file.read.assert_called_with()
        
    def test_missing_load(self):
        mock_opener = mock.Mock(side_effect=FileNotFoundError)
        
        db = BasicDB(Path('testdb'), _fileopener=mock_opener)
        loaded = db.load()
        
        self.assertEqual(loaded, [])
        self.assertEqual(mock_opener.call_args[0][0], Path('testdb'))
        
    def test_save(self):
        mock_file = mock.MagicMock(write=mock.Mock())
        mock_file.__enter__.return_value = mock_file
        mock_opener = mock.Mock(return_value=mock_file)
        db = BasicDB(Path('testdb'), _fileopener=mock_opener)
        loaded = db.save(['first', 'second'])
        
        self.assertEqual(
            mock_opener.call_args[0][0:2],
            (Path('testdb'), 'w+')
        )
        
        mock_file.write.assert_called_with('["first", "second"]')
        
        
unittest.main()