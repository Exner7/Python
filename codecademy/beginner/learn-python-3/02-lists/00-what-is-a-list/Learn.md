# What is a List?

In programming,
it is common to want to work with collections of data.

In Python,
a **list** is one of the many built-in <span style="color: cornflowerblue">data structures</span> that allow us to work with a collection of data in sequential order.

Suppose we want to make a list of the heights of students in a class:

- Noelle is 61 inches tall.
- Ava is 70 inches tall.
- Sam is 67 inches tall.
- Mia is 64 inches tall.

In Python,
we can create a variable called `heights` to store these integers in a list (_Lists are mutable sequence data types used for storing a comma-separated collection of objects in a single variable._):

```py
heights = [61, 70, 67, 64]

```

Notice that:

1. A list begins and ends with square brackets (`[` and `]`).

2. Each item (i.e., `67` or `70`) is separated by a comma (`,`).

3. It's considered a good practice to insert a space (` `) after each comma,
   but our code will run just fine if we leave out the space.

Let's write our own list!

## ✔️ Instructions

1. Examine the existing list `heights` in your code editor.

   A new student just joined the class!

   - Chloe is 65 inches tall.

   Add Chloe's height to the end of the list `heights`.

2. Remove the `#` in front of the definition of the list `broken_heights`.

   If you run this code,
   you'll get an error in your terminal:

   ```txt
     File "/home/ccuser/workspace/create-python-list-intro-list/script.py", line 3
       broken_heights = [65 71 59 62]
                         ^^^^^
   SyntaxError: invalid syntax. Perhaps you forgot a comma?
   ```

   Add commas (`,`) to `broken_heights` so that it runs without errors.
