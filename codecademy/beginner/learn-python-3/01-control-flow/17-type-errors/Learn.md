# Type Errors

A `TypeError` is reported by the Python interpreter when an operator is applied to a variable of an inappropriate type.

For example,
let's see what happens when we try to add together two incompatible types:

```py
piggy_bank = '2' + 0.25

```

This will result in a `TypeError` error message like:

```txt
Traceback (most recent call last):
  File "/home/ccuser/workspace/errors-in-python-type-errors/test1.py", line 1, in <module>
    piggy_bank = '2' + 0.25
                 ~~~~^~~~~~
TypeError: can only concatenate str (not "float") to str
```

This error is reporting that `0.25` is not a string.

Some common causes for a `TypeError` are:

- applying addition or subtraction to a number and a string

- calling a function on something of the incorrect type

## ✔️ Instructions

1. The word got out in the office that you are a pro bug catcher!

   Another peer,
   Alisha,
   suddenly appears and hands you a program that calculates the area of a triangle,
   a rectangle,
   and a circle.

   Run the program to check it out.

2. Oh no,
there's one `TypeError` error!

   Can you find it?
