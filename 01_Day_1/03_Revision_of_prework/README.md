![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


## Exercise 1
1. Declare a variable `no_of_stars` in which there will be a random number from 1 to 20. To generate a random number you must use the module `random` and the function `randint`. The example below draws a number between 0 and 5 and displays it on the screen:
```python
import random
random_number = random.randint(0, 5)
print random_number
```
2. Display the drawn number on the screen.
3. Display on the screen as many stars (`*`) as the value of the number.

An example of how the program works:
```python
Drawn number: 6

******
```


## Exercise 2
1. Declare the variables `rows` and `columns` that will store random numbers between 5 and 15.
2. Display the numbers on the screen.
3. Display a rectangle of the drawn sizes, made up of stars (`*`).

An example of how the program works:
```python
Value of the variable rows: 5
Value of the variable columns: 10

**********
**********
**********
**********
**********
```


## Exercise 3
1. Declare the variable `size` that will store a random number between 3 and 9.
2. Display the drawn number on the screen.
3. Display a Christmas tree of the drawn size, made of stars (`*`).
> **Do not use string multiplication when solving this exercise!** Instead, use 2 loops.

An example of how the program works:
```plaintext
Christmas tree size: 5

*
**
***
****
*****
```

Hint:
You need to use two dependent `for` loops in this case.
