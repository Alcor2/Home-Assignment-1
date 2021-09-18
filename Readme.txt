This repository contains 5 files of .py format: main, task1, task2, task3 and task 4.

The file main.py contains 4 basic functions and takes elements (functions or classes) from files task1.py, task2.py, task3.py and task4.py.

The first function of main.py is power. It takes two lists of numeric arguments as input and powers elements of the 1st list times of 
elements of the 2nd list element-wise. Therefore, the function's output is also list.

The second function is mltp_strings. It takes two lists as an input. It is expected the first list to be a list of strings, while the
second list should be a list of integers. This function multiplicates the first list on the second element-wise and has list as an output.

The third function is qdr_eq. It takes as an input three numeric values a, b and c which are the coefficients of the quadratic equation:
a*x^2 + b*x + c = 0. Its output is a list of solutions, but the solution can be only real. Therefore, in case of imaginary solution the
output contains a list with string declaring, that there's no real solution of the given equation.

The fourth function is pscl_trgl. It draws the given amount of rows of the Pascal's Triangle. Therefore, it has no output data and has an
integer value as its input.

Decorator functions and classes, that are taken from the files task1-4.py, create new decorated functions in main.py in terms not to lose
access to the original ones. That's why there're additional functions which have prefixes (td - time_decorator, dd - dump_decorator, cd - 
class decorator, ed - error_decorator) and inherit the original functions' docstrings.

Function time_decorator from task1.py counts the decorated function's execution time and number of its calls and prints the data.

Function dump_decorator from task2.py in addition to the previous prints the imformation about the decorated function.

Class class_decorator from task3.py writes down the information about the decorated function into a txt file with name "Report". As soon 
as 4 decorated functions will be implemented the class method __call__ will also print a ranking table with 4 functions' execution times.

Class error_decorator from task4.py does the same actions as the class_decorator. In addition, in case of error it prints the error 
message into "LogFile" .log file. For the function which doesn't produce error message the output information is written into "EReport" 
.txt file.

The whole program should be implemented with main.py file only.