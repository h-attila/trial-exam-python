# TRIAL EXAM: Python Basics

### Getting Started
 - Fork this repository under your own account
 - Clone the forked repository to your computer
 - Commit your progress frequently and with descriptive commit messages
 - All your answers and solutions should go in this repository

### What can I use?
 - You can use any resource online, but **please work individually**
 - Instead of copy-pasting your answers and solutions, write them in your own words.


# Tasks
## 1-5. Complete the tasks seen in the 1-5.py files! (~90 mins)
### Acceptance criteria
The application is accepted if:
- The solution works according to specification [1p each]
- The solution follows [styleguide](https://github.com/greenfox-academy/teaching-materials/blob/master/styleguide/python.md) [1p]
- Has proper error handling where the specification says it [1p each]
- Has the correct loops, methods, filters [1p each]
- The code is clean, without unnecessary repetition, and with descriptive names [1p each]
- You commit frequently with descriptive commit messages [1p]

## 6. Question time! (~30 mins) [6p]

### Explain the algorithm used in exercise 2. Use a flowchart, structogram or pseudo code. [2p]
#### Your answer:

Define the letterCounter() function with 'fileName' parameter;
    Try to do something;
        Try to open the file with name 'fileName';
        Read all data from file to 'fileText' (string);
        Close file;
        Return the number of 'a' (number) in 'fileText' (string);
    If file not exist or not readable;
        Return zero


### How can you get a random number in python? [2p]
#### Your answer:

I can use the built in'random' module, by importing all functions: 'import random', or just one function eg. 'from random import randint'.
Random module can generate different type of random number (integer, float). I used these random functions in my exercises:
 - random integers: 'myRandomNumber = random.randint(a, b)', where myRandomNumber is integer, and a < myRandomNumber < b. It can used for example for a dice function.
 - random float: 'random.random()' this function can return a random float number between 0.0 and 1.0.
    Multily by 100 it can give back a random percent eg: print('How many percent of win a lottery?', int(random.random() * 100), '%')

 And finally one of my favorite:
 - random.choice: this can give back a random item from a list. For example: 'myRandomFruit = random.choice['alma', 'korte', 'szolo', ... , 'banan']'. I used it in Hero game for the random enemy movement.


### What does M stand for in MVC? [2p]
#### Your answer: M means 'Model'. Model contains all the calculating functions and logical structure (e.g.: file handling, working with data, calculating data, lists and variables, database handling).
It gets most of input informations from Controller module and gives it back to the Controller. Model also not communicating with the user or View.
A tipical workflow: get data from Controller (eg. a function call) -> calculating values -> give back the result.
