#! /usr/bin/env python3 

"""Script for build and start app."""

import os 
from app import create_app, db 
from app.models import User, Role
from flask_migrate import Migrate

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app. db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)

# unit test launcher command 
@app.cli.command()
def test():
    """Run the unit tests."""
    
    import unittest
    
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)