#! /usr/bin/env python3 

import json 
import os 
from pathlib import Path
import pytest

def write_json(f: str, data: str) -> None:
    Path(f).write_text(json.dumps(data))
    
def test_empty(tmpdir: str) -> None:
    assert os.path.isdir(tmpdir)
    assert os.listdir(tmpdir) == []
    
def test_save_curves(tmpdir: str) -> None:
    data = dict(status_code=200, values=[225, 300])
    fn = tmpdir.join('somefile.json')
    write_json(fn, data)
    assert fn.read() == '{"status_code": 200, "values": [225, 300]}'
    
    