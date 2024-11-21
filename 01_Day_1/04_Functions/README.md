![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


## Exercise 1 - done with the lecturer

The aim of this exercise is to familiarize you with the structure of functions and show you how the `return` clause works. Do it together with the lecturer.
Do not hesitate to ask if you do not understand something.

* Write a function `square(num)` that returns the value `num` squared.
* Create a function `square_print(num)`. Let this function be identical to the function in the previous subsection, but instead of returning (`return`), it should print the result (`print`).
* Now let's do a test: declare the variable `a`, assign to it the result of the function `square(10)` and add 10 to it.
What value will the variable `a` have?
* We continue the test: declare the variable `b`, assign the result of the function `square_print(10)` to it, and add 10 to it.
What happened? Why did it happen? If you don't understand - ask your lecturer.


## Exercise 2 - done with the lecturer

Write a function `multiply(subject, times)` that returns the value of the variable `subject` multiplied by the value of the argument `times`.
Note what happens if you type a number as the value of argument `subject`, and what if you type a string.



## Exercise 3

Write a function `power` that takes two arguments:

* `base`: mandatory,
* `exponent`: optional with a standard value of 2.

The function should return the value `base` raised to the power of `exponent`.


## Exercise 4

Write a function `convert_to_usd` that takes a parameter `euros`, which is the amount of money in euros. The function should return the given amount in American dollars.
Assume the conversion rate of 0.82 EUR = 1 USD.


## Exercise 5

Write a function `to_celsius` that takes the parameter `fahrenheit`, which is the temperature in degrees Fahrenheit. The function should convert the temperature given in the parameter, to degrees Celsius.

Use the following formula:

```
     (F - 32) * 5
C =  ------------
          9
```
where:

* C - temperature in degrees Celsius,
* F - temperature in degrees Fahrenheit.


## Exercise 6

Write a function `calculate_net` that takes arguments:

* `gross` - the gross amount of the purchase price,
* `vat` - the value of VAT tax. You can assume that VAT should be a floating point number in the range 0 &ndash; 1.

The function should return the net value of the price. What calculations do you need to perform?


## Exercise 7

* Write a function `is_even` that takes a parameter `number` - any integer (you may assume that the programmer will enter a valid number, you don't have to check it). The function has to **return** `True` if the number is even, `False` - if not.

**Hint:** A number is even if it divides by 2 without any remainder. Use the modulo operator `%`.

* Write a function `iterate_through` that takes the parameter `number` (you don't need to validate it). Then the function in the loop should iterate from 1 to the value `number` and check the evenness of the next number. The result should be **printed** on the screen (not returned). Use the function `is_even`, written a while ago, to check evenness.
