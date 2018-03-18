# MapReduce

This is a simple [MapReduce](https://en.wikipedia.org/wiki/MapReduce) implementation in python using the [PyActor](https://github.com/pedrotgn/pyactor) library.

[![Build Status](https://travis-ci.com/Constantine-32/map-reduce.svg?token=XRb3p57YXAyxoz4qpEXL&branch=master)](https://travis-ci.com/Constantine-32/map-reduce)
[![Code Health](https://landscape.io/github/Constantine-32/mapreduce/master/landscape.svg?style=flat&badge_auth_token=16a6c859fc234ba4a96ad2d17c3aa0f3)](https://landscape.io/github/Constantine-32/mapreduce/master)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)



## Installing PyActor

Packages required:

    python, python-dev, python-pip

Install with:

    sudo pip install pyactor

If pip installs pyactor but gives an error with gevent, check that 'python-dev'
is installed and try again with:

    sudo pip install gevent

Or download the source by cloning [PyActor](https://github.com/pedrotgn/pyactor)'s
repository and installing with:

    sudo python setup.py install

If you clone the repository, you will also have access to the tests and a folder
full of examples. Just check the github page and the documentation for a detailed
tutorial.