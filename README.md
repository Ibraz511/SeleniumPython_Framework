### Brief description
login.py is the main file and it contains 2 test cases

### Page object with unittest
In unittest, test cases run in alphabetical order
<br>
tearDownClass(): Execute once after all the test. Similar to after() in cypress
<br>
tearDown(): similar to afterEach() in cypress
<br>
Similarly, setUpClass and setUp are equivalent to before() and beforeEach respectively

<br>
### Run unittest script from command line
navigate to the location where the python file is on CLI then run the command
`python -m unittest filename.py`
<br>
NB: Since we are running login.py which has several imports from other files, we wont be able
to run our project from CLI by just following the steps mentioned above. Rather we have to first
import these inside the file that we wanna run just before we start importing other files
<br>
import os
<br>
import sys
<br>
sys.path.append(os.path.join(os.path.dirname(__file__),"..","..")) #the .., is dependent on the nested folder structure your testfile is located
<br>
In our case, the login.py is just 2 folder structures level, the main folder ->Test_cases folder then we can find our test file. Therefore, we just need to include 2 dots, `..`
<br>
All those are needed if you wanna run the script from CLI, else neglect/remove them

For CLI: cd into Test_cases, where login.py is located then run `python login.py

<br>
### Adding HTML Reports
NB:You must run the script from CLI to see the report. <br>
 Firstly, import the testRunner module the use the command
Modify the way you run the script to include   `if __name__ == '__main__':`
    unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output='C:/Users/Ibrahim F A/Documents/SELENIUM PYTHON/SeleniumPython_Framework/Reports'))
<br> On CLI,cd into Test_cases, where login.py is located then run `python login.py`

<br>
The report gets stored in the location