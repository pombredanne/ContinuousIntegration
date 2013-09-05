from setuptools import setup, find_packages

setup(
    name='jenkins_client',
    version='0.1.0',
    author='Shawn Crosby',
    author_email='scrosby@salesforce.com',
    packages=find_packages(),
    license='Be Real',
    url='https://pypi.python.org/pypi?r6_commit',
    description='Jenkins client wrapper',
    long_description=open('README.txt').read(),
    install_requires=[
        "jenkinsapi",
        "sc_pylibs>=0.1.1",
    ],
)
