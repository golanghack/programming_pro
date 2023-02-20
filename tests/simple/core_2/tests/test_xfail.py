import sys 
import pytest

@pytest.mark.xfail
def test_simulation():
    pass

@pytest.mark.xfail(
    sys.platform.startswith('win'), 
    reason='flak in windows #42', 
    strict=False,
)
def test_login_dialog():
    pass

def check_credentials(name: str):
    raise NotImplementedError

@pytest.mark.xfail(
    raises=NotImplementedError, 
    reason='will be implemented in #987'
)
def test_credential_check():
    check_credentials('User')
    
class Particle:
    pass

def collide(p1, p2):
    pass

@pytest.mark.xfail(
    run=False, 
    reason='undefined particles cause a crash %625'
)
def test_undefined_particle_collision_crash():
    collide(Particle(), Particle())
    
def initialize_phisics():
    pass

def test_particle_plitting():
    initialize_phisics()
    import numpy
    
    if numpy.__version__ < '1.13':
        pytest.xfail('split computation fails with numpy < 1.13')
        