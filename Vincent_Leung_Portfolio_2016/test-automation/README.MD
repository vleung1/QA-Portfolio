#Overview

This is a suite of automated web UI tests built on a Selenium WebDriver/Python framework. The product under test is the U.S. Treasury Department Office of Inspector General's public, front-facing website. Tests are focused on UAT and functional testing of departmental pages and verification of public domain legal and audit documents. 

#Dependencies
This is an overview of tools required to run these tests (steps below for Mac OS X).

- Python 2.7 is required for this test suite.
- Install Firefox from: http://www.mozilla.org
- Install Firebug from: https://addons.mozilla.org/en-US/firefox/addon/firebug/
- Install FirePath from: https://addons.mozilla.org/en-US/firefox/addon/firepath/
- Install Selenium IDE from: http://docs.seleniumhq.org/download/
- Install Chrome from: https://www.google.com/intl/en_us/chrome/browser/
- Install Sublime Text Editor 2 from: http://www.sublimetext.com/2
- Install Java SDK for Mac from: http://www.oracle.com/technetwork/java/javase/downloads/index.html]
- Install Chromedriver using the following steps:

a) Go to https://sites.google.com/a/chromium.org/chromedriver/

b) Find the local path by running the following command: echo $PATH

c) Unzip the chromdriver file into the local path

- Install Pip using the following steps:

a) Go to https://pypi.python.org/pypi/setuptools

b) Scroll all the way to the bottom of the page and download the latest tar.gz version of setuptools

c) Untar the setuptools file by typing the following command: tar -vxzf FILENAME

d) cd into the setuptools folder and install setuptools by running: sudo python setup.py install

e) Install Pip by running the following command: sudo easy_install pip

- Install Selenium by running: sudo pip install –U selenium
- Install nose by running: sudo pip install nose
- Overwrite the PYTHONPATH using the following steps:

a) open the terminal and run: open .profile

b) Add the two lines below in the .profile file and save: 
PYTHONPATH="/Users/YOUR_HOME_HERE/Desktop"
export PYTHONPATH

d) Close the .profile file

e) Close the terminal

f) Open a new instance of the terminal and verify that the PYTHONPATH has been overwritten by running the following command:
echo $PYTHONPATH

#Running the tests

1. Open terminal
2. cd into the oig\tests directory
3. To run all tests, run the following command: nosetests --verbosity=2 --no-byte-compile
4. To run one or more specific tests, run the following command: nosetests --verbosity=2 --no-byte-compile --tests="nameoftest1, nameoftest2,..."
