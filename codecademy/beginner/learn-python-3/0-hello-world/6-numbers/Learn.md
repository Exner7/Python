# Numbers

Computer can understand much more than just strings of text.

Python has a few numeric data types.

It has multiple ways of storing numbers.

Which on we use depends on our intended purpose for the number we are saving.

---

An **integer**,
or `int`,
is a whole number.

It has no decimal point and contains all counting numbers (`, 2, 3, etc.),
a well as their negative counterparts and the number 0.

If we were counting the number of people in a room,
the number of jellybeans in a jar,
or the number of keys on a keyboard,
we would likely use an integer.

---

A **floating point number**,
or a `float`,
is a decimal number.

It can be used to represent both fractional quantities and precise measurements.

If we were measuring the length of a bedroom wall,
calculating the average test score for a science class,
or storing a baseball player's batting average for the 1998 season,
we would likely use a `float`.

---

Numbers can be assigned to variables or used literally in a program:

```py
an_int = 2
a_float = 2.1

print(an_int + 3)
# Output: 5

```

In the preceding code,
we defined an integer and a float a the variables `an_int` and `a_float`.

We printed out the sum of the variable `an_int` with the number `3`.

We call the number `3` a **literal**,
meaning it's actually the number `3` and not a variable with the number `3` assigned to it.

---

Floating-point number can behave in some unexpected ways due to how computers store them.

For more information on floating-point number and Python,
review [Python's documentation of floating-point limitations](https://docs.python.org/3/tutorial/floatingpoint.html).

## ✔️ Instructions

1. A recent movie-going experience has you excited to publish a review.
   You rush out of the cinema and hastily begin programming to create your movie-review website:
   "The Big Screen's Greatest Scenes Decided By A Machine".

   Create the following variables and assign integer numbers to them:
   `release_year` and `runtime`.

2. Now,
   create the variable `rating_out_of_10` and assign it a `float` number between one and ten.
