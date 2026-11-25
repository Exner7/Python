# Boolean Variables

Before we go any further,
let's talk about a little bit about `True` and `False`.

You may notice that when they are typed in the code editor (with uppercase "T" and "F"),
they appear in different clor than variables or strings.

This is because `True` and `False` are their wn special type: **bool**.

---

`True` and `False` are the only `bool` types,
and any variable that is assigned one of these values is called a **Boolean variable**.

---

Boolean variables can be created in several ways.

The easiest way is to simply assign `True` or `False` to variable:

```py
set_to_true = True
set_to_false = False

```

You can also set a variable equal to a Boolean expression:

```py
bool_one = 5 != 7
bool_two = 1 + 1 != 2
bool_three = 3 * 3 == 9

```

These variables now contain Boolean values,
so when they are referenced,
they will only return the `True` or `False` values of the expression they where assigned.

```py
print(bool_one) # True
print(bool_two) # False
print(bool_three) # True

```

## ✔️ Instructions

1. Create a variable named `my_baby_bool` and set it equal to the string `"true"`.

2. Check the type of `my_baby_bool` using `type(my_baby_bool)`.

   Print the results in the terminal.

3. It's not a Boolean variable!

   Boolean values `True` and `False` always need to be capitalized and do not have quotation marks.

   Create a new variable named `my_baby_bool_two` and set it equal to `True`.

4. Check the type of `my_baby_bool_two` and make sure you successfully created a boolean variable.

   Print the results in the terminal.
