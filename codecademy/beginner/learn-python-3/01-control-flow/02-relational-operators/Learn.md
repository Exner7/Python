# Relational Operators

Now that we understand Boolean expresions,
let's learn how to create them.

In Python,
we create Boolean expressions using relational and logical operators.

- **Relational operators** compare two values and return `True` or `False` based on the operands.
  For this reason,
  we will sometimes hear them called <span style="color: cornflowerblue">comparison operators</span>.

- **Logical operators** are used to combine multiple Boolean expressions.

The two relational operators we'll cover first are "equal to" and "not equal to":

- The **equal to** operator (`==`) returns `True` if both its operands are the same.

  Otherwise,
  it returns `False`.

  For example,
  the Boolean expression `a == b` will return `True` if the alues `a` and `b` are the same.

  Otherwise,
  it will return `False`.

- The **not equal** operator (`!=`) is the negation of the equal operator.

  The Boolean expression `a != b` will return `True` if the values `a` and `b` are different.

  Otherwise,
  it will return `False`.

We can create Boolean expressions by comparing two values using these operators,
as follows:

```py
1 == 1 # Evaluates to True as the operands are the same

1 != 1 # Evaluates to False as the operands are the same

2 != 4 # Evaluates to True as the operands are different

3 == 5 # Evaluates to False as the operands are different

'7' == 7 # Evaluates to False as the operands are different types

```

## ✔️ Instructions

1. Determine if the following Boolean expression is `True` or `False`.

   Assign your answer as `True` or `False` to the variable `first_expression`

   ```py
   2 * 2 == 2 + 2

   ```

2. Next,
   consider the following expression:

   ```py
   3 + 3 != 3 * 3

   ```

   If the given Boolean expression is `True`,
   initialize a variable `second_expression` to `True`.

   Otherwise,
   initialize it to `False`.

3. Now,
   consider the expression:

   ```py
   3 * 3 == '9'
   ```

   If the given Boolean expression is `True`.
   initialize a variable `third_expression` to `True`.

   Otherwise,
   initialize it to `False`.
