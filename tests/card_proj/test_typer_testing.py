from typer.testing import CliRunner
from cards.cli import app

runner = CliRunner()

def tests_typer_runner():
    result = runner.invoke(app, ['version'])
    print()
    print(['version: {result.stdout}'])
    result = runner.invoke(app, ['list', '-o', 'brian'])
    print(f'list:\n{result.stdout}')