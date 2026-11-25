# If Statements

"Okay,
okay,
okay
Boolean variables,
Boolean expressions,
I thought we were learning how to build control flow into my code!"

We are,
I promise you!

Understanding Boolean variables and expressions is essential because they are the building blocks of conditional statements.

Recall the waking-up example from the beginning of this lesson.

The decision-making process of "Is it raining? If so, bring an umbrella" is a conditional statement.

Here it is phrased in a different way:

```txt
If it is raining, then bring an umbrella.
```

Can you pick out the Boolean expression here?

Right, `"it is raining"` is the Boolean expression,
and this conditional statement is checking to see if it is true.

If `"it is raining" == True`,
then the rest of the conditional statement will be executed,
and you will bring an umbrella.

This is the frm of a conditional statement:

```txt
If [it is raining] then [bring an umbrella]
```

In Python,
it looks very similar:

```py
if is_raining:
    print("bring an umbrella")

```

We'll notice that instead of "then" we have a colon `:`.

That tells the computer that what's coming next is the code to execute if the condition is met.

The code that should be executed is indented to show that it follows that condition.

---

Let's take a look at another conditional statement:

```py
if 2 == 4 - 2:
    print("apple")

```

Will this code print `apple` to the terminal?

Yes,
because the condition of the `if` statement,
`2 == 4 - 2` is `True`.

Let's work through a couple more together.

## ✔️ Instructions

1. In `script.py`,
   there is an `if` statement.

   I wrote this because y coworker Dave kept using my computer without my permission.

   If the `user_name` is `"Dave"`,
   it tells him to stay off my computer.

   Enter a user name in the field for `user_name` and try running the program.

2. Oh no! We got a `SyntaxError`!

   This happens when we make a small errr in the syntax of the conditional statement.

   Read through the error message carefully and see if you can find the error.

   Then, fix it,
   and run the code again.

3. Dave got around my security and has been logging onto my computer using our coworker Angela's user name,
   `"angela_catlady_87"`.

   Set your `user_name` to be `"angela_catlady_87"`.

   Update the program with a second `if` statement that checks for Angela's user name as well and print the following in reponse:

   ```txt
   "I know it is you, Dave! Go away!
   ```
