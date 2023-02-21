#! /usr/bin/env python3 

import subprocess
from . import services

def test_start_service(monkeypatch) -> None:
    commands = []
    monkeypatch.setattr(subprocess, 'run', commands.append)
    services.start_service('web')
    assert commands == ['docker run web']