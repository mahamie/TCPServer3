from distutils.core import setup
from setuptools import find_packages

setup(name='tcp3',
      version='0.1',
      description='A Simple TCP Server on Python3 ',
      author='ibinas',
      author_email='ibinasch@gmail.com',
      url='https://github.com/mahamie',
      packages=find_packages(exclude=['*.pyc']),
      scripts=['bin/tcp3'],
     )
