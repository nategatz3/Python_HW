import imp

from initialize_functions import *

'''
To use a function, you call it. When you call a function, you must provide values, or arguments, for each of the function’s parameters.
Functions allow you to write code efficiently. When you need to perform an action more than once, wrap that code in a function and call it when you need it. When you need to change how the action is carried out, you can change the code in the function, and the improvement is applied everywhere.
'''

print("Invoking zero arg function")
zero_arg_function()

print("Invoking function with required arguments")
introduction("Harry", "Houdini")

print("Invoking function with default arguments")
introduction_with_default_args()

#TODO: In this file, go ahead and invoke the rest of the functions from the initialize_functions.py file

###### My Response

print("Invoking function with a mix of default arguments")
introduction_with_mix_of_default_args(first_name="Nathan", last_name="Gatz")

print("Invoking function that multiplies 2 numbers")
product_of_two_num(num1=7, num2=48)

print("Invoking a function that adds all the numbers up")
add_all_nums(1,7,98,24)

print("Invoking a function that doubles any number")
double(17956)

print("Invoking a function that demonstrates the Fibonacci Sequence")
fib(num=3)

print("Invoking a function that does subtraction")
subtract(num1=8, num2=6)

##### My Response