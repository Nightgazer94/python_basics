![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


## Exercise 1 - done with the lecturer

Write a function named `safe_get` which takes two parameters:

* `l`: any list,
* `index`: number.

The function should return the element of the list that has the given `index`. If there is no such element, it should return `None`.

**Note:** do this using exception handling.


## Exercise 2

In the file **exercise2.py** you will find a simple guessing game: the computer draws a number from 1 to 10, then tells you to guess it.
Analyse the code. Run the program. Try to enter an incorrect number and see how the program behaves in this situation.

Improve the code so that it does not terminate with an error message after entering an incorrect value, but informs the user about the error and continues its operation.

**Hint: See what exception is reported and handle it appropriately.**


## Exercise 3

Write a function named `divide` that takes two arguments: `a` and `b`. They must be natural numbers. The function has to:

* check if `a` and `b` are numbers,
* handle the problem of dividing by zero.

Both of the above cases must be handled by exception catching.

If either of the above (invalid) cases is not satisfied, the function should return `None`.


## Exercise 4

Write a function named `phone` that takes the parameter `number`, which denotes a phone number.
The function has to check if the given number is in the list of numbers (invent some).
If so - the function should return the number given in the parameter. If not - it must return an exception of the type `Exception` with a comment `There is no such number!`.
