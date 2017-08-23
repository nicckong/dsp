# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Lists and tuples are both a list of values. they are both indexed by numbers, starting from zero. 
Lists are mutable - you can add, remove and modify the values in lists, whereas Tuples are not. 
Tuples will work as keys in disctionaries due to its immutable type nature.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

Lists are ordered collections of elements. Examples of using lists ae iteration and list Comprehension.
Sets are unordered collections of unique elements. Examples of using sets are testing and eliminating duplicate entries.

Sets are more efficient than lists in finding an element. This is because sets use hash lookup and lists iterate. 

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

`Lambda` function is a way to create small functions without names. It is used wherever function objects are required. It is however restricted to a single expression. 

An exmple of `lambda` in the `key` argument to `sorted` is:

```python

sorted(['ABC', 'aaa', 'def', 'cde'], key=lambda word: word.lower())

```

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

List comprehensions provide a concise way to create lists based on existing lists. 

It consists of an iterable containing an expression followed by a `for` clause, then `for` or `if` clauses (optional). The expressions can be anything, meaning you can put in all kinds of objects in lists.

Example `map`
```python
a = [1,2,3,4]
b = [5,6,7,8]
print (list(map(lambda x,y:x+y, a,b)))
print ([x + y for x, y in zip(a,b)])
```

Example `filter`
```python
numbers = [1,4,2,32,25,8,13,18,34]

print (list(filter(lambda x: x % 2 == 0, numbers)))
print ([x for x in numbers if x % 2 == 0])
```

In cases where `map` / `filter` and list comprehensions can both be used, list comprehension is more preferred as it tends to be more efficient and easier to read.

However, list comprehensions is not applicable if the construction rule is too complicated to be expressed with `for` and `if` statements. In this case, `map` / `filter` should be used instead. 

Example set comprehension
```python
nums = {n**2 for n in range(10)}
```

Example disctionary comprehension
```python
d3 = {k: v for d in (d1, d2) for k, v in d.items()}
```

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)





