#! /usr/bin/env python3

from subprocess import run

def start_service(service_name: str) -> None:
    run(f"docker run {service_name}")