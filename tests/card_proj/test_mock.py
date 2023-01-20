from unittest import mock   
import cards
import pytest
from cards.cli import app 
from typer.testing import CliRunner

runner = CliRunner()

def test_mock_version():
    with mock.patch.object(cards, '__version__', '1.2.3'):
        result = runner.invoke(app, ['version'])
        assert result.stdout.rstrip() == '1.2.3'
        

def test_mock_CardsDB():
    with mock.patch.object(cards, 'CardsDB') as MockCardsDB:
        print()
        print(f'class -> {MockCardsDB}')
        print(f'return_value -> {MockCardsDB.return_value}')
        with cards.cli.cards_db() as db:
            print(f'  object -> {db}')
            
