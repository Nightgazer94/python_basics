![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


## Exercise 1

Write a function named `make_tuple` that takes four parameters: `a`, `b`, `c`, and `d`. Parameters `c` and `d` should be optional, with default values of 3 and 4 respectively. Return a tuple of four elements, whose consecutive elements are parameter values.

##### Example:

```python
a = make_tuple("mom", "dad")
print(a)
```
```
('mom', 'dad', 3, 4)
```
```python
a = make_tuple(0, 0, 0, 0)
print(a)
```
```
(0, 0, 0, 0)
```


## Exercise 2

Write a function named `find_first_and_last` that takes a list or a tuple. Then return a tuple which will contain the first and last element of the parameter.


## Exercise 3

Write a function named `format_date` that takes 3 parameters:

* `day`,
* `month`,
* `year`.

The function should check if the date is correct:
* the month should be within (1, 12),
* the day must not be greater than 30 - 31 (or 28 in the case of February, don't check for leap years).

If any of the conditions does not match the calendar, the function should return `None`. 

The function should return a formatted text string in the "day month year" format.

##### Example

```python
d = format_date(12, 1, 2017)
print(d)
```
```
12 January 2017
```
```python
d = format_date(12, 13, 2017)
print(d)
```
```
None
```


## Exercise 4

Write a function named `find_boundaries` that takes a list of numbers.
The function should return a tuple with the smallest and the largest number in the set. 
If there is an element in the list that is not a number, it should be ignored. If an empty list is entered, the function should return `None`.

##### Example:
```python
b = find_boundaries([1, 5, 2, 3.5, -1])
print(b)
```
```
(-1, 5)
```
```python
b = find_boundaries([0, 2, "boo!", 10])
print(b)
```
```
(0, 10)
```


## Exercise 5

Write a function named `censor` that takes a text string of any length as a parameter. Then it:

* breaks the text string into a list of words,
* checks if there are any forbidden words in it,
* if so -- replaces them with four asterisks (`****`)
* concatenates the list back into a string and returns the value.

##### Forbidden words:
*Java*, *C#*, *Ruby*, *PHP*.
(it should be case-sensitive, e.g. 'PhP' should **not** be censored)

Keep forbidden words as a list inside the `censor` function.

##### Example
```python
c = censor("Java is the best, but PHP is the bestest!")  # ;-)
print (c)
```
```
**** is the best, but **** is the bestest!
```


## Exercise 6

Write a function named `check_palindrome` that takes one word and checks if it is a palindrome.
The function should return `True` if the string is a palindrome, `False` - if it is not.
