# Syntax Errors

When we are writing Python programs,
the interpreter is our first line of defense against errors.

`SyntaxError` means there is something wrong with the way your program is written -
punctuation that does not belong,
a command where it is not expected,
or a missing parenthesis can all trigger a `SyntaxError`.

Here's an example of a `SyntaxError`.

```txt
  File "/home/ccuser/workspace/python-errors-syntax-errors/script.py", line 1
    print(Hello world!)
          ^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?

```

The interpreter will tell us where (the file name and line number) it got into trouble and its best guess as to what is wrong.

After reading the error message,
we can assume that the cause of this error is lack of quotation marks around `Hello world!`

Some common syntax errors are:

- misspelling a Python keyword

- a missing colon `:`

- missing a closing parenthesis `)`.
  square bracket `]`,
  or curly brace `}`

## ✔️ Instructions

1. In `script.py`,
   your coworker Carolyn wrote a Fortune Cookie program that is supposed to print out a possible fortune based on a random number and an `if`/`elif`/`else` statement.

   Run the program to check it out.

2. Oh no, there are three `SyntaxError` errors inside `script.py`!

   Can you find them all?
