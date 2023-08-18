#! /usr/bin/env 

from . import services

def test_start_service(monkeypatch) -> None:
    commands = []
    monkeypatch.setattr(services, "run", commands.append)
    services.start_service("web")
    assert commands == ["docker run web"]