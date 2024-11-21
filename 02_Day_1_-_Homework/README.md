![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


# Python programming basics - homework
> Solve all exercises in functions.
> If your functions do not return a value they will not pass.
> (unless you are instructed not to perform an operation in a function).
> Solve each exercise in a separate file (e.g. exercise 1 in exercise_1.py, exercise 2.
> In the file exercise_2.py, etc.).
> You can output information in the console, but **don't confuse this with returning values**.
>
> Exercises with an asterisk __(*)__ are for volunteers.
>
> Read the exercise instructions carefully.



## Exercise 0

Familiarize yourself with **PEP-8**. This is the official document that describes the coding style in Python:

[https://www.python.org/dev/peps/pep-0008/](https://www.python.org/dev/peps/pep-0008/)

Refer to it regularly as your learning progresses, and try to follow the guidelines given there.


## Exercise 1

(In this task you do not have to write functions)

Write a program in which you define a multi-line text string.
Type a stanza of your favorite poem there, then display it on the console.


## Exercise 2

Write a function called `square_area` that calculates and **returns** the area of a rectangle (the function takes two parameters denoting the lengths of the rectangle's sides). Assume that the input parameters are correct.


## Exercise 3

Write a function named `circle_circuit` which, given the diameter of a circle, **returns** its circumference.
Assume that the input parameters are correct. Assume that `pi=3.14`.


## Exercise 4
 
Write a function called `dogs_age` that calculates the age of a dog in dog years.

* the function should take the age of the dog as a parameter,
* for the first two years, each year of the dog's life is equal to 10.5 human years,
* over two years, each year of the dog's life is equal to 4 human years,
* the function should **return** the age of the dog.

##### Example:
```python
buddy = dogs_age(1.5)  # expected result: 1.5 * 10.5 = 15.75

tucker = dogs_age(5)  # expected result: 2 * 10.5 + 3 * 4 = 33
```


## Exercise 5

Write a function `chessboard` that takes an optional parameter `n`. The standard value of the parameter should be 8. The function will **return** a multiline string representing a chessboard composed of # characters and spaces. The chessboard should have dimensions **n x n**.

**Example:**
For n=8, the chessboard should consist of 8 lines, each with 8 characters: alternating # and space.
```python
c = chessboard()
print(c)
```
```
# # # # 
 # # # #
# # # # 
 # # # #
# # # # 
 # # # #
# # # # 
 # # # # 
```


## Exercise 6

Write a function `is_divisible_by_4` that takes a number and checks whether the number is divisible by 4 and returns `True` or `False` accordingly.


## Exercise 7

Write a function `histogram` that takes a list of numbers and **returns** a histogram made up of `#` characters.
If the user provides a value that is not a number, the function should return `None`.

The resulting histogram should be a multiline string consisting of the `#` characters.
One line = one histogram bar.
> **Solve the problem without using string multiplication!** Instead, use two loops.

##### Example:
```python
h = histogram([2, 6, 3, 1])
print(h)
```
```
##
######
###
#
```

```python
h = histogram([1, 2, 'error!'])
print(h)
```
```
None
```


## Exercise 8(\∗) - Fibonacci sequence

Write a function `fib` that calculates the Fibonacci sequence. The function should:

* take `n` as a parameter - a number; this should be the element for which the value is calculated,
* return the value of the string element for the element `n`.

##### Hint:

The Fibonacci sequence is a sequence of natural numbers. It is defined recursively as follows:
the first element is 0, the second is 1, each subsequent element is the sum of the previous two.

Look up on the internet what _recursion_ is and how to write a function that uses it.
