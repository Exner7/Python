# Else Statements

As we can tell from our work with Calvin Coolidge's Cool College,
once we started including lots of `if` statements in a function,
the code became a little cluttered an clunky.

Luckily,
there are other tools we can ue to build control flow.

`else` statements allow us to elegantly describe what we want our code to do when certain conditions are not met.

`else` statements always appear in conjunction with `if` statements.

Consider our waking-up example to see how this works:

```py
if weekday:
    print("wake up at 06:30")
else:
    print("sleep in")

```

In this way,
we can build `if` statements that execute different code when the condition is not met.

This prevents us from needing to write `if` statements ofr each possible condition -
we can instead write a blanket `else` statement for all the times the condition is not met.

---

Let's return to our `if` statement for our movie streaming platform.

Previously,
all it did was check if the user's age was over `13` and if so,
print out a message.

We can use an `else` statement to return a message if the user is too young to watch a movie.

```py
if 13 <= age:
    print("Access granted.")
else:
    print("Sorry, you must be 13 or older to watch this movie.")

```

## ✔️ Instructions

1. Calvin Coolidge' Cool College has another request for you.

   They want you to add an additional check to a previous `if` statement.

   If a student is failing to meet one or both of the graduation requirement,
   they want it to print:

   ```txt
   "You do not meet the requirements to graduate."

   ```

   Add an `else` statement to the existing `if` statement.
