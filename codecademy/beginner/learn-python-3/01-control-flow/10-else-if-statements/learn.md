# Else If Statements

We have `if` statements,
and now we have `else` statements.

There is another type of statement that goes with these:
`elif`,
which is short for "else if".

An `elif` statement checks another condition after the previous `if` statement's conditions aren't met.

---

We can use `elif` statements to control the order in which our program checks multiple conditional statements.

First,
the `if` statement is checked,
then each `elif` statement is checked from top to bottom,
then finally the `else` code is executed if none of the previous conditions have been met.

---

Let's take a look at this practice.

The following `if` statement will display a curated "thank you" message after someone donates to a charity,
depending on how much was given.

```py
print("Thank you for the donation!")

if 1000 <= donation:
    print("You've achieved platinum donor status")
elif 500 <= donation:
    print("You've achieved gold donor status")
elif 100 <= donation:
    print("You've achieved silver donor status")
else:
    print("You've achieved bronze donor status")

```

Take a moment to think about this control flow chain.

What would happen if all of the `elif` statements were simply `if` statements?

If you donated $1100.00,
then the first three messages would all print because each `if` condition has been met.

---

But because we used `elif` statements,
it checks each condition sequentially and only prints one message.

If I donate $600.00,
the code first checks if that is over 1000,
which it is not,
then it checks i it's over 500,
which it is,
so it prints that message,
then because all of the other statements are `elif` and `else`,
none of them get checked,
and no more messages get printed.

## ✔️ Instructions

1. Calvin Coolidge's Cool College has noticed that students prefer to get letter grades.

   Write an `if` / `elif` / `else` chain that:

   - prints `"A"` if `grade` is `90` or higher

   - otherwise,
     prints `"B"` if `grade` is `80` or higher

   - otherwise,
     prints `"C"` if `grade` is `70` or higher

   - otherwise,
     prints `"D"` if `grade` is `60` or higher

   - otherwise,
     prints `"F"`
