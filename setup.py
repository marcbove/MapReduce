# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
  name='mapreduce',
  version='0.0.1',
  author='Christian Callau, Marc Bove',
  url='https://github.com/Constantine-32/mapreduce',
  install_requires=['pyactor'],
  packages=find_packages(),
  license='MIT License',
  test_suite='tests',
)