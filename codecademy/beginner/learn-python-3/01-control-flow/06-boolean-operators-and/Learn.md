# Boolean Operatrs: and

Often,
the conditions we want to check in our conditional statements will require more than one Boolean expression to cover.

In these cases,
we can build larger Boolean expressions using **Boolean operators**.

These <span style="color: cornflowerblue">operators</span> (also known as **logical operators**) combine smaller Boolean expressions into larger Boolean expressions.

---

These are three Boolean operators that we will cover:

- `and`
- `or`
- `not`

Let's start with `and`.

---

`and` combines two Boolean expresions and evaluates as `True` if both its components are `True`,
but `False` otherwise.

Consider this example:

```txt
Oranges are fruits, and carrots are vegetables.
```

This Boolean expression is comprise of two smaller expressions,
`oranges are fruits` and `carrots are vegetables`.

Both of these statements are `True` and are connected by the Boolean operator `and`,
so the entire expression is `True`.

---

Let's look at a few more examples of `and` statements in Python:

```py
(1 + 1 == 2) and (2 + 2 == 4) # True

(1 > 9) and (5 != 6) # False

(1 + 1 == 2) and (2 < 1) # False

(0 == 10) and (1 + 1 == 1) # False

```

Notice that in the second and third examples,
even though part of the expression is `True`,
the entire expresion as a whole is `False` because the other statement is `False`.

The fourth statement is also `False` because both components are `False`.

## ✔️ Instructions

1. Set the variables `statement_one` and `statement_two` equal to the results of the following Boolean expressions:

   Statement one:

   ```py
   (2 + 2 + 2 >= 6) and (-1 * -1 < 0)

   ```

   Statement two:

   ```py
   (4 * 2 <= 8) and (7 - 1 == 6)

   ```

2. Let's return to Calvin Coolidge's Cool College.

   120 credits aren't the only graduation requirement -
   one must also have a GPA of 2.0 or higher.

   Rewrite the `if` statement so that it checks to see if a student meets both requirements using an `and` statement.

   If they do,
   print the string.

   ```txt
    "You meet the requirements to graduate!"
    
   ```
