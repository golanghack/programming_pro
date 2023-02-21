#! /usr/bin/env python3 

import subprocess

def start_service(service_name: str) -> None:
    subprocess.run(f'docker run {service_name}')