# MapReduce

This is a simple [MapReduce](https://en.wikipedia.org/wiki/MapReduce) implementation in python using the [PyActor](https://github.com/pedrotgn/pyactor) library.

[![Build Status](https://travis-ci.org/Constantine-32/mapreduce.svg?branch=master)](https://travis-ci.org/Constantine-32/mapreduce)
[![codecov](https://codecov.io/gh/Constantine-32/mapreduce/branch/master/graph/badge.svg)](https://codecov.io/gh/Constantine-32/mapreduce)
[![Coverage Status](https://coveralls.io/repos/github/Constantine-32/mapreduce/badge.svg?branch=master)](https://coveralls.io/github/Constantine-32/mapreduce?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/f504a3d2e2da4f3599574fbf5ee381cc)](https://www.codacy.com/app/Constantine-32/mapreduce?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Constantine-32/mapreduce&amp;utm_campaign=Badge_Grade)
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

In order to execute the mapreduce function you must follow the following steps:
1. Open a terminal for each client, in this case 3 and execute the following function in each of them:
```
    python client_i.py
```
Replace i for 0, 1 and 2. Each terminal must have a different number
2. In another separate terminal, the Apache server will be initialized with the following command:
```
    python -m SimpleHTTPServer
```
3. Finally in another terminal the main function will be executed as follows:
```
    python host.py
```

It will ask the name of the file to be treated and the function to be executed, either countWords or wordCount.

If you want to use the code in distributed mode, instead of opening 5 terminals, one laptop would be responsible for initializing the server and running the host.py while each of the other computers would run its client. Do not forget to change the IPs!
