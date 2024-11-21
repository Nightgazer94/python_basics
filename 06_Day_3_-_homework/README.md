![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


## Exercise 1

Write a function `random_average(n)` that draws `n` natural numbers from 1 to 100, sums them, and returns the arithmetic mean of these numbers.

For the sake of automatic test construction, in this exercise use the following notation of `randint` function import:

```python
import random
```

and then use the following construct in your code:

```python
random.randint()
```


## Exercise 2

Write a function named `div` that:

* asks the user to enter 2 numbers from the keyboard,
* converts the entered data into natural numbers,
* divides one number by the other,
* displays the result.

Additionally, you should protect against all possible errors (incorrect data, division by zero).

Check the interactive Python console to see what errors might occur and protect your program against them.


## Exercise 3(*): Verifying correctness of a 13-digit ISBN number

Write a function `validate_isbn` that takes a 13-digit ISBN number as a text string, then checks its correctness and returns:

* `True` if the ISBN is correct,
* `False` if the ISBN is incorrect.

##### 13-digit ISBN number validation rules

This kind of ISBN number consists of 13 digits, the last of which is a check digit. The check digit of the 13-digit version of an ISBN is calculated as follows:

The individual digits of the ISBN are given corresponding weights. The first digit is given a weight of 1, the second 3, the third 1 and so on (the odd digits are given 1, the even digits 3). Each digit is multiplied by its weight and then all the products are added together. The resulting sum is divided by 10, and the remainder is subtracted from 10. If the remainder is 0, then the control digit is also 0.

For details see:
[https://en.wikipedia.org/wiki/International_Standard_Book_Number#ISBN-13_check_digit_calculation](https://en.wikipedia.org/wiki/International_Standard_Book_Number#ISBN-13_check_digit_calculation)