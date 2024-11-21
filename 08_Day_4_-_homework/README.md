![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


## Exercise 1

Write a Flask application that asks the user to enter the natural number `n` (on a GET "/" action), and then (on the POST "/" action) displays a table containing in consecutive rows:

* 2 to the power of n
* n to the power of n
* n factorial

Pass the number as parameter `n`.

**Hint: Remember to display a button for submitting the form!**


## Exercise 2

Write a Flask application that asks the user to enter a 10-digit ISBN number (on a GET "/" action), and then (on the POST "/" action) displays the information:

* `Correct ISBN` if the code is in valid Polish format (00-001).
* `Incorrect ISBN` otherwise.

Pass the code as parameter `isbn`.

##### 10-digit ISBN number validation
The check digit (the last one in ISBN number) is the sum of the preceding digits multiplied by their positions, modulo 11, with 10 being represented as X. 

For example, to find the checksum of an ISBN number whose first nine digits are 0-306-40615, calculate:

1x0 + 2x3 + 3x0 + 4x6 + 5x4 + 6x0 + 7x6 + 8x1 + 9x5 = 0 + 6 + 0 + 24 + 20 + 0 + 42 + 8 + 45 = 145 = 13x11 + 2

So the check digit is 2, and the full number is ISBN 0-306-40615-2.


**Hint: Remember to display a button for submitting the form!**
