### <h1 align=center>Homework 4</h1>
---
<p align=center>This repository contains the dependencies and code for Homework 4 along with custom tests and newly added calculator functions</p>

<p align=center><b> On cloning the repository, please use</b></p>
<div align=center>

`pip install -r requirements.txt` or `pip3 install -r requirements.txt`

</div>

---

### The Homework meets the following goals:

<ol>
<li>Add, Subtract, Multiply, and Divide</li>
<li>Throw exception for divide by zero and test that the exception is thrown.</li>
<li>Use at least one class, at least one static method, at least one class method.</li>
<li>It needs to store a history of calculations, so that you can retrieve the last calculation, add a calculation.</li>
<li>It needs to have 100% test coverage, pass pylint, and you need to do your best to not repeat any lines of code.</li>
<li>You should use type hints for input parameter types and return types.</li>
<li>Implement a pytest fixture to the tests.</li>
</ol>

---

### Packages Used:

<ol>
<li><b>pytest:</b> The pytest framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.</li>
<li><b>pytest-pylint:</b> Pylint analyses your code without actually running it. It checks for errors, enforces a coding standard, looks for code smells, and can make suggestions about how the code could be refactored.</li>
<li><b>pytest-cov: </b>Coverage.py is a tool for measuring code coverage of Python programs. It monitors your program, noting which parts of the code have been executed, then analyzes the source to identify code that could have been executed but was not.</li>
</ol>

---

### Calculator Functions:

<ol>
<li><b>Addition:</b> Adds two numbers</li>
<li><b>Subtraction:</b> Subtracts two numbers</li>
<li><b>Multiplication:</b> Multiplies two numbers</li>
<li><b>Division:</b> Divides two numbers and also catches the divide by zero exception</li>
<li><b>History:</b> Stores and clears history of the calculator
</ol>

---

<b>Note:</b> Test Cases have 100% coverage for all the above Calculator Functions using pytest. Use the following commands to execute the tests.

`pytest`
`pytest --pylint`
`pytest --pylint --cov`

---