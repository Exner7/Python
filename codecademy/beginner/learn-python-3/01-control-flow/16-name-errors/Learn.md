# Name Errors

A `NameError` is reported by the Python interpreter when it detects a variable that is unknown.

This can occur if a variable is used before it has been assigned a value or if a variable name is spelled differently than it was when it was defined.

The Python interpreter will display the line of code where the `NameError` was detected and indicate which name is found that was not defined.

Here's an example of a `NameError` error message:

```txt
File "/home/ccuser/workspace/python-errors-name-errors/test1.py", line 2, in <module>
    print(score)
          ^^^^^
NameError: name 'score' is not defined
```

This error is suggesting that the variable `score` was never defined in the program.

Some common name errors are:

- misspelling a variable name
- forgetting to define a variable

## ✔️ Instructions

1. In `script.py`,
   another teammate,
   Alex,
   wrote a [Who Wants to Be a Millionaire](https://youtu.be/_tmkOI6bWKs) question and four options.

   If the answer is an uppercase or lowercase `"A"`,
   then the score goes up.

   Run the program to check it out.

2. Oh no,
   there are two `NameError` errors!

   Can you find them both?
