For this project, I am using Python==3.5.2 on Ubuntu 16.04

To download and install on Linux through command line, follow these instructions:

Step 1 – Install Required Packages

Use the following command to install prerequisites for Python before installing it.

$ sudo apt-get install build-essential checkinstall
$ sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev

Step 2 – Download Python 3.5.2

Download Python using following command from python official site. 

$ cd /usr/src
$ wget https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz

Now extract the downloaded package.

$ sudo tar xzf Python-3.5.2.tgz

Step 3 – Compile Python Source

Use below set of commands to compile python source code on your system using altinstall.

$ cd Python-3.5.2
$ sudo ./configure
$ sudo make altinstall

make altinstall is used to prevent replacing the default python binary file /usr/bin/python.

Step 4 – Check the Python Version

Check the latest version installed of python using below command

# python3.5 -V

Python 3.5.2

Install the requirements from requirements.txt

pip install -r requirements.txt

RUN THE APPLICATION

python3 main.py

RUN THE TESTS

python3 tests.py

TO RUN TEST CASES INDIVIDUALLY

python3 -m unittest tests.<ClassName>
for example: python3 -m unittest tests.ConnectTestCase