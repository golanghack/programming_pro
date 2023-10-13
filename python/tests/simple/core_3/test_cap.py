#! /usr/bin/env python3

from textwrap import dedent

def script_main(args: str) -> int:
    if not args:
        show_usage()
        return 0 
        
def show_usage() -> None:
    print('Create/update webhooks.')
    print('Usage-> hooks Repo URL.')
    
def test_usage(capsys) -> None:
    script_main([])
    captured = capsys.readouterr()
    expected = dedent(
        """\
            Create/update webhooks.
            Usage-> hooks Repo URL.
        """
    )
    
    assert captured.out == expected
    