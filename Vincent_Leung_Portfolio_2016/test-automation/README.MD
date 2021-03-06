#Overview

This is a suite of automated web UI tests built on a Selenium WebDriver/Python framework. The product under test is the U.S. Treasury Department Office of Inspector General's public, front-facing website. Tests are focused on UAT and functional testing of departmental pages and integrity verification of public domain legal and audit documents. 

#Dependencies
This is an overview of tools required to run these tests (steps below for Mac OS X).

1. Python 2.7 is required for this test suite, available here: https://www.python.org/downloads/

2. Install Firefox from: http://www.mozilla.org

3. Install Firebug from: https://addons.mozilla.org/en-US/firefox/addon/firebug/

4. Install FirePath from: https://addons.mozilla.org/en-US/firefox/addon/firepath/

5. Install Selenium IDE from: http://docs.seleniumhq.org/download/

6. Install Chrome from: https://www.google.com/intl/en_us/chrome/browser/

7. Install Sublime Text Editor 2 from: http://www.sublimetext.com/2

8. Install Java SDK for Mac from: http://www.oracle.com/technetwork/java/javase/downloads/index.html

9. Install Chromedriver using the following steps:
  - Go to https://sites.google.com/a/chromium.org/chromedriver/
  - Find the local path by running the following command: 
    echo $PATH
  - Unzip the chromdriver file into the local path

10. Install Pip using the following steps:
  - Go to: https://pypi.python.org/pypi/setuptools
  - Scroll all the way to the bottom of the page and download the latest tar.gz version of setuptools
  - Untar the setuptools file by typing the following command: tar -vxzf FILENAME
  - cd into the setuptools folder and install setuptools by running the following command: 
    sudo python setup.py install
  - Install Pip by running the following command: 
    sudo easy_install pip

11. Install Selenium by running the following command: 
    sudo pip install –U selenium

12. Install nose by running the following command: 
    sudo pip install nose

13. Overwrite the PYTHONPATH using the following steps:
  - open the terminal and run: open .profile
  - Add the two lines below in the .profile file and save: <br />
    PYTHONPATH="/Users/YOUR_HOME_HERE/Desktop"<br />
    export PYTHONPATH<br />
  - Close the .profile file
  - Close the terminal
  - Open a new instance of the terminal and verify that the PYTHONPATH has been overwritten by running the following command:
    echo $PYTHONPATH

#Running the tests

1. Download the oig directory and place in your working directory 

2. Open terminal

3. cd into the oig\tests directory

4. To run all tests, run the following command: <br />
    nosetests --verbosity=2 --no-byte-compile

5. To run one or more specific tests, run the following command: <br />
    nosetests --verbosity=2 --no-byte-compile --tests="nameoftest1, nameoftest2,..."
