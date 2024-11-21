![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


# Basics of programming in Python &ndash; mock exam

Before you start solving tasks, read the following hints.

##### Write your answers to the programming questions in the appropriate files *answers1.py* &ndash; *answer6.py*.

**Good luck!**

----------------------------------------------------------------------------------------

## Task 1 (2 points)

Write a function named `shorten` that takes an arbitrarily long string and then returns the abbreviation of the string, as in the example:

```python
shortened = shorten("Don't repeat yourself")
print(shortened)
```
```
DRY
```
```python
shortened = shorten("Read the fine manual")
print(shortened)
```
```
RTFM
```
```python
shortened = shorten("All terrain armoured transport")
print(shortened)
```
```
ATAT
```

---

## Task 2 (3 points)

Create a function `singulars_and_plurals` that will accept just one argument: a list of nouns (strings). The function should return a dictionary:
{
"singulars": a list of singular nouns,
"plurals": a list of plural nouns,
}
For the purpose of this task assume that plurals are the words that end with "s".

**Example:**
```python
singulars_and_plurals(["tomato", "tomatoes", "potato", "potatoes", "cars", "unicorns", "horse", "cow"])
```
should return:
```
{"singulars": ["tomato", "potato", "horse", "cow"], "plurals": ["tomatoes", "potatoes", "cars", "unicorns"]}
```

---

## Task 3 (3 points)

Write a function named `check_palindrome` that takes an arbitrarily long text string and checks if it is a palindrome.
The function should return `True` if the string is a palindrome, `False` if it is not.

##### Hints:
1. A palindrome is a word or phrase that when read backwards sounds the same as it did from the beginning, such as "racecar", "level", "Was it a car or a cat I saw?".

2. When checking if a word is a palindrome, remember the spaces.

---

## Task 4 (3 points)

Write a function named `div` that takes 2 numerical arguments. The arguments are the beginning and end of a range of numbers.
As a result, the function should return a list of numbers in the given range, which are both divisible by 2 and indivisible by 3.
The entered range should be closed, i.e. the numbers which are the beginning and the end of the range should also be checked.


##### Example:
```python
result = div(0, 20)
print(result)
```
```
[2, 4, 8, 10, 14, 16, 20]
```

---

#### Task 5 (4 points)

Write a function named `roll` that takes 3 parameters:

* number of dice,
* optional: dice type (3, 4, 6, 8, 10, 12, and 100-sided dice allowed), default value is **6**,
* optional: score modifier (number added or subtracted from the dice score), default value is **0**.

Then, the function should simulate a roll of the appropriate number of dice, sum the results, and add (or subtract) the modifier. The result should be returned.

For the sake of simplicity, you may assume that all numbers given as parameters are natural numbers.

If the user enters a dice that is not in the above list, the function should throw an `Exception` with the message "No such dice!"


##### Hint
```python
roll(2, 10, 20)  # roll two 10-sided dice, add 20 to the result
roll(3, 6, -3)  # roll three 6-sided dice, subtract 3 from the result
```

---

## Task 6 (5 points)

Take a look at the `exam` module included in the file attached to this exam. This module contains a `movies` dictionary that lists some programmer's favorite and hated movies.

Using Flask, create a page and share it at `/movies`:
 
* if the user accesses the page using the GET method, display a form that:
    * will have a text field named `title`,
    * the description of the field will be: "Insert title",

* if the user enters the page using the POST method:
    * check if the movie is on the list of favorite movies; if so, return the text "favourite",
    * check if the movie is on the list of hated movies; if so, return the text "hated",
    * if the movie is not on any list, return the text "no such movie!".
    
**NOTE:** When launching the Flask app, use the variable `app`!
