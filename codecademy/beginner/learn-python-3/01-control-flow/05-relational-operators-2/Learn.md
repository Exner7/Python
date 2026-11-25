# Relational Operators II

Now that we've added conditional statements to our toolkit for building control flow,
let's explore more ways to create Boolean expressions.

So far,
we know two relational operators,
equals and not equals,
but there are many (well,
four) more:

- `>` - **greater than**
- `>=` - **greater than or equal to**
- `<` - **less than**
- `<=` - **less than or equal to**

Let's say we're running a movie streaming platform an we want to write a program that checks if our users are onver 13 when showing them PG-13 movie.

We could write something like:

```py
if age <= 13:
    print("Parental caution strongly suggested")

```

This conditional statement will take the user's age and compare it to the number `13`.

If `age` is less than or equal to `13`,
it will print out a message

Let's try some more!

## ✔️ Instructions

1. Create an `if` statement that checks if `x` and `y` are equal.

   If so,
   print the following string:

   ```txt
   "these numbers are the same."
   ```

2. Calvin Coolidge's Cool College (or 4C,
   as the locals call it),
   requires students to earn at least 120 credits to graduate.

   Write an `if` statement that checks if the student has enough credits to graduate.
   If they do,
   print the string:

   ```txt
   "You have enough credits to graduate!"

   ```

   Can a student with 120 `credts` graduate from Calvin Coolidge's Cool College?
