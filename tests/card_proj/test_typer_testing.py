from typer.testing import CliRunner
from cards.cli import app
import shlex

runner = CliRunner()

def tests_typer_runner():
    result = runner.invoke(app, ['version'])
    print()
    print(['version: {result.stdout}'])
    result = runner.invoke(app, ['list', '-o', 'brian'])
    print(f'list:\n{result.stdout}')\
        
        
def cards_cli(command_string):
    command_list = shlex.split(command_string)
    result = runner.invoke(app, command_list)
    output = result.stdout.rstrip()
    return output


def test_cards_cli():
    result = cards_cli('version')
    print()
    print(f'version--> {result}')
    result = cards_cli('list -o brian')
    print(f'list -> \n {result}')