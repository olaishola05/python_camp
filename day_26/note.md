# Comprehension in Python


## List Comprehension

Is a process of creating a new list from an existing list in python and only available in python

Example using keyword

```python
items = []
new_list = [item for item in items]
```
```python
numbers = [1, 2, 3]
new_numbers = [n + 2 for n  in numbers]
# Equals [3, 4, 5]
```

It also works with strings

```python
name = "Oladipupo"
letter_lists = [letter for letter in name]

# Returns list of letters
```

It works with python sequences
- list
- tuple
- range
- string

Working with range

```python
double_numbers = [num * num for num in range(1, 5)]
# double_numbers[1, 4, 9, 16]
```

### Conditional List Comprehension

example:

```
test_list = []
condition_list = [item for item in test_list if test]
```
To perform adding item to a new list if the actual condition or test passes

```python
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
short_names = [name for name in names if len(name) <5]
# ['Alex', 'Beth', 'Dave']
```

Return UPPERCASE item list if test pass

```python
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
long_names = [name for name in names if len(name) > 5]
# ['CAROLINE', 'ELEANOR', 'FREDDIE']
```
Filter list based on condition

```python
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
filtered_name = [name for name in names if name != "Alex"]
# ['Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
```

## Dictionary Comprehension

It allows creation of a new dictionary from an existing list or dictionary

```python
new_dict = {new_key:new_value for item in a_list}
import random

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
students_scores = {student:random.randint(1, 100) for student in names}

# result students_scores = {'Alex': 79, 'Beth': 24, 'Caroline': 91, 'Dave': 41, 'Eleanor': 51, 'Freddie': 2}

# OR

dict_new = {new_key:new_value for (key, value) in dict.items()}
```

### Conditional Dictionary comprehension

```python
dict_new = {new_key:new_value for (key, value) in dict.items() if test}

students_scores = {'Alex': 79, 'Beth': 24, 'Caroline': 91, 'Dave': 41, 'Eleanor': 51, 'Freddie': 2}
passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}

# {'Alex': 79, 'Caroline': 91}

```