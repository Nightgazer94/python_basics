![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


## Exercise 1 - done with the lecturer

Write a function named `create_list` that takes two arguments of any type and returns a list whose consecutive elements are parameters repeated four times.

##### Example:

```python
my_list = create_list(1, 2)  # result: [1, 2, 1, 2, 1, 2, 1, 2]
my_list_2 = create_list(True, False)  # result: [True, False, True, False, True, False, True, False]
```


## Exercise 2 - done with the lecturer

Write a function named `list_keys(d)`, where `d` is a dictionary. The function should iterate over the keys of the dictionary with a **for** loop and return a list of those keys. Check the documentation to see if this can be done more simply.


## Exercise 3

Write a function named `find_short_words` that takes a list of words.
The function should return a list of words shorter than 5 characters.

##### Example
```python
l = find_short_words(['itsy', 'bitsy', 'spider', 'climbed', 'up', 'the', 'waterspout'])
print(l)
```
```
['itsy', 'up', 'the']
```


## Exercise 4

Write a function `sumup(numbers)` where `numbers` is a list of numbers of any type.
The function should return the sum of all elements of the `numbers` list. For simplicity, you may assume that all parameters entered by the programmer are valid numbers.

**Note:** we called the function slightly incorrectly, and we did it deliberately! We cannot call the function `sum()` because such a function already exists in the Python language standard.


## Exercise 5

Write the function `mean(numbers)`, where `numbers` is a list of numbers of any type. The function should return the arithmetic mean of all elements of the list of numbers.
Do you know any way to do it easier?
