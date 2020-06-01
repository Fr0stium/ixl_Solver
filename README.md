# ixl_Solver

A program that helps you solve specific IXLs. Type in the problem, and the program will return the solution.

## Installation

Requirements: you must have [Python 3.8.3](https://www.python.org/downloads/), [mpmath](http://mpmath.org/doc/current/setup.html), and [sympy](https://www.sympy.org/en/download.html) installed. In order to download the last two, it is recommended you have [pip](https://pip.pypa.io/en/stable/installing/) installed as well.

### How to meet the requirements

1. To download Python, visit the link, download the 64-bit version, and follow the instructions. To make sure you have successfully installed it, open terminal or command prompt, and type in ```python3 --version```. It should output ```Python 3.8.3```.
2. After downloading Python, you should download pip, which is very easy. In terminal or command prompt, type ```curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py```, and then type ```python3 get-pip.py```.
3. Now that pip is installed, downloading the last two is also very easy. In terminal or command prompt, type ```pip install mpmath``` and then ```pip install sympy```.

### How to download this program

1. Download this program. You can use git, or you can click the green download button at the top of this page, and click "Download ZIP".
2. Open the program folder, and find the path of ```program.py```. Look up how to find a path if you don't know how.
3. Open terminal or shell, and type in ```python3 <path>```, where ```<path>``` is ```program.py```'s path.
4. The program should be working now.

## Usage

First, you will be asked to type in an IXL to solve. The formatting of this is ```grade.exercise```.
Example: if you were asked to do exercise A2 in Algebra 2, you would type in ```A2.A2```.

Afterwards, you will be given instructions on what to do next.

## Guidelines

To multiply, only type in ```*```. Do not omit the multiplication operator, and do not use ```()```, ```.```, ```⋅```, ```×```, ```x```, ```X```, or anything else that is not an asterisk.

To divide, only type in ```/```. Do not type in ```÷```.

To exponentiate, only type in ```**``` Even though ```^``` is more commonly used, you cannot type it in because Python's exponentiation operator is ```**```.

There are other useful functions and operators that you should know. In the following list, x is the argument of each function. The functions are case-sensitive:

- <img src="https://latex.codecogs.com/svg.latex?|x|" title="|x|" /> is ```Abs(x)```
- <img src="https://latex.codecogs.com/svg.latex?\sqrt{x}" title="\sqrt{x}" /> is ```sqrt(x)```.
- <img src="https://latex.codecogs.com/svg.latex?\sqrt[3]{x}" title="\sqrt[3]{x}" /> is ```cbrt(x)```.
- <img src="https://latex.codecogs.com/svg.latex?\sqrt[n]{x}" title="\sqrt[n]{x}" /> is ```root(x, n)```.
- Trigonometric functions, like <img src="https://latex.codecogs.com/svg.latex?\sin&space;(x)" title="\sin (x)" />, are the same: ```sin(x)```.
- Inverse trigonometric functions, like <img src="https://latex.codecogs.com/svg.latex?\arcsin&space;(x)" title="\arcsin (x)" />, are ```asin(x)```.
