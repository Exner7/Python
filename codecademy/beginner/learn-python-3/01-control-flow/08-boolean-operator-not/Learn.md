# Boolean Operators: not

The final Boolean operator we will cover is `not`.

This is straightforward:
when applied to any Boolean expression,
it reverses the Boolean value.

So if we have a `True` statement and apply a `not` operator,
we get a `False` statement.

```py
not True == False
not False == True

```

Consider the following statement

```txt
Oranges are not fruits.
```

Here,
we took the `True` statement `oranges are fruits` and added a `not` operator to make a `False` statement:
`oranges are not fruits`.

This example in English is slightly different from how it would appear in Python becaue in Python,
we add the `not` operator at the beginning of the statement.

Let's take a look at some of those:

```py
not 1 + 1 == 2 # False
not 7 < 0      # True

```

## ✔️ Instructions

1. Set the variables `statement_one` and `statement_two` equal to the results of the following Boolean expressions:

   Statement one:

   ```py
   not (4 + 5 <= 9)

   ```

   Statement two:

   ```py
   not (8 * 2) != 20 - 4

   ```

2. The registar's office at Calvin Coolidge's Cool College has been so impressed with your work so far that they have another task for you.

   They want you to write a series of `if` statements using `and` and `not` statements:

   - If a student does not have greater than or equal to `120` `credits`,
     print the following:

     ```txt
     "You do not have enough credits to graduate."

     ```

   - If their `gpa` is not greater than or equal to `2.0`,
     print the following:

     ```txt
     "Your GPA is not high enough to graduate."

     ```

   - If they do not have greater than or equal to `120` `credits` `and` their `gpa` is not greater than or equal to `2.0`,
     print the following:

     ```txt
     "You do not meet either requirement to graduate!"

     ```
