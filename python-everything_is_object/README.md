# Python3: Mutable, Immutable – Everything Is an Object

This project explores how Python handles objects internally, focusing on object identity,
mutability, and how variables reference objects in memory.

---

### 0. Who am I?
- **0-answer.txt**: What function would you use to print the type of an object?

type


---

### 1. Where are you?
- **1-answer.txt**: How do you get a variable's identifier (memory address in CPython)?

id


---

### 2. Right count
- **2-answer.txt**: In the following code, do `a` and `b` point to the same object?

```python
>>> a = 89
>>> b = 100
```
Answer: No

3. Right count =
3-answer.txt: In the following code, do a and b point to the same object?
```python
>>> a = 89
>>> b = 89
```
Answer: Yes

4. Right count =
4-answer.txt: In the following code, do a and b point to the same object?
```python
>>> a = 89
>>> b = a
```
Answer: Yes

5. Right count =+
5-answer.txt: In the following code, do a and b point to the same object?
```python
>>> a = 89
>>> b = a + 1
```
Answer: No

6. Is equal
What do these 3 lines print?
```python
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
```
Output: True

7. Is the same
What do these 3 lines print?
```python
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)
```
Output: True

8. Is equal
What do these 3 lines print?
```python
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)
```
Output: True

9. Is really the same
What do these 3 lines print?
```python
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)
```
Output: False

10. And with a list, is it equal
```python
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3]
>>> print(l1 == l2)
```
Output: True

11. And with a list, is it the same
```python
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3]
>>> print(l1 is l2)
```
Output: False

12. And with a list, is it really equal
```python
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
```
Output: True

13. And with a list, is it really the same
```python
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
```
Output: True

14. List append
```python
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> l1.append(4)
>>> print(l2)
```
Output: [1, 2, 3, 4]

15. List add
```python
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> l1 = l1 + [4]
>>> print(l2)
```
Output: [1, 2, 3]

16. Integer incrementation
```python
>>> def increment(n):
...     n += 1
>>> a = 1
>>> increment(a)
>>> print(a)
```
Output: 1

17. List incrementation
```python
>>> def increment(n):
...     n.append(4)
>>> l = [1, 2, 3]
>>> increment(l)
>>> print(l)
```
Output: [1, 2, 3, 4]

18. List assignation
```python
>>> def assign_value(n, v):
...     n = v
>>> l1 = [1, 2, 3]
>>> l2 = [4, 5, 6]
>>> assign_value(l1, l2)
>>> print(l1)
```
Output: [1, 2, 3]

19. Copy a list object
```python
def copy_list(a_list):
    return a_list[:]
```
20. Tuple or not?
```python
>>> a = ()
```
Answer: Yes

21. Tuple or not?
```python
>>> a = (1, 2)
```
Answer: Yes

22. Tuple or not?
```python
>>> a = (1)
```
Answer: No

23. Tuple or not?
```python
>>> a = (1,)
```
Answer: Yes

24. Who I am?
```python
>>> a = (1)
>>> b = (1)
>>> a is b
```
Output: True

25. Tuple or not
```python
>>> a = (1, 2)
>>> b = (1, 2)
>>> a is b
```
Output: True

26. Empty is not empty
```python
>>> a = ()
>>> b = ()
>>> a is b
```
Output: True

27. Still the same?
```python
>>> a = [1, 2, 3, 4]
>>> id(a)
>>> a = a + [5]
>>> id(a)
```
Answer: No

28. Same or not?
```python
>>> a = [1, 2, 3]
>>> id(a)
>>> a += [4]
>>> id(a)
```
Answer: Yes


---

## 🎯 Conclusion

Everything in Python is an object.  
Variables reference objects, not values.  
Mutable and immutable objects behave differently.  
== compares values, while is compares identity.  

Understanding these concepts prevents subtle bugs and makes Python code more predictable.
