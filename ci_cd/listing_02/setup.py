from setuptools import setup

setup(
    name='webcount',
    version='1.0.0',
    license='Apache2.0',
    packages=['webcount', 'test'],
    install_requires=['requests'],
    author='golanghack',
    author_email='admin@admin.com',
    description='a simple experiment with setup, tox, pytest'
)