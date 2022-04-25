
from setuptools import setup

setup_args = dict (
    name="rsplib",
    version="0.9",
    description= 'A Python Client for RSP',
    license='MIT',
    url='https://github.com/riccardotommasini/colorwave',
    author='RSP Gang',
    author_email='riccardo.tommasini@polimi.it',
    packages=[ "rsplib" ],
    install_requires = [ 'setuptools',
                         'pandas',
                         'json2html',
                         'requests',
                         'matplotlib',
                         'pygments',
                         'websocket-client',
                         'rdflib==5.0.0',
                         'rdflib-jsonld<=0.5.0',
                         'json2html',
                         'pydot' ])


if __name__ == '__main__':
    setup( **setup_args )
