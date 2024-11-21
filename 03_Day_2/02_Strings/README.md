![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


## Exercise 1

Write a function named `message` that takes a dictionary with the following keys as a parameter:

* **name**,
* **role**,
* **movie**.

Then the function should prepare a formatted string: "In _movie_, _name_ is a _role_.", and paste the values of the above keys in appropriate places.
If any of the keys is not in the dictionary, the function should return the value `None`.

##### Example:

```python
input_dict = {
    "name": "Han Solo",
    "role": "smuggler",
    "movie": "Star Wars"
}

print(message(input_dict))
```

##### Result:
```plaintext
In Star Wars, Han Solo is a smuggler.
```

```python
input_dict = {
    "name": "Bilbo Baggins",
    "role": "burglar"
}

print(message(input_dict))
```

##### Result:
```plaintext
None
```

