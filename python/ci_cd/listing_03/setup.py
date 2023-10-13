from setuptools import setup

setup(
    name='math_json_tree',
    version='1.0.0',
    description='Evaulation of expression trees',
    author='golanghack',
    author_email='admin@admin.com',
    requires=['flask', 'pytest', 'gunicorn'],
    setup_requires=['pytest-runner'],
    packages='math_json_tree'
)