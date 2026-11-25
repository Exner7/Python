# Magic 8-Ball

The [Magic 8-Ball](https://en.wikipedia.org/wiki/Magic_8-Ball) is a popular toy developed in the 1950s for fortune-tellin or advice seeking.

Write a `magic8.py` Python program that can answer any "Yes" or "No" question with a differentfortune each time it executes.

![Magic 8-Ball](./Figures/magic8ball.webp)

We'll be using the following nine possible answers for your Magic 8-ball:

- `Yes - definitely`

- `It is decidedly so`

- `Without a doubt`

- `Reply hazy, try again`

- `Ask again later`

- `Better not tell you now`

- `My sources say no`

- `Outlook not so good`

- `Very doubtful`

The output of the program will have the following format:

```txt
<NAME> asks: <QUESTION>
Magic 8-Ball's answer: <ANSWER>

```

For example

```txt
Joe asks: Is this real life?
Magic 8-Ball's answer: Better not tell you now

```

Let's get started!

## ✔️ Tasks

### **Setting Up**

#### TASK 1

In `magic8.py`,
declare a variable `name` and assign it to the name of the person who will be asking the Magic 8-Ball.

#### TASK 2

Next,
declare a variable `question`,
and assign it to a "Yes" or "No" question you'd like to ask the Magic 8-Ball.

#### TASK 3

We want to store the answer of the Magic 8-Ball in another variable,
which we'll call `answer`.

For now,
assign this variable to an empty string.

### **Generating a Random Number**

#### TASK 4

To ensure the answer differs each time we run the program,
we will use randomly generated values.

_Note_:
_This will be something new_!
_But don't worry_,
_we will explain this topic thoroughly as we go and also supply the code_.

In Python,
we can use the `.randint()` method from the `random` module to generate a random number from a range.

But first,
let's `import` this module so we can use its methods.

Add this line of code to the top of `magic8.py`:

```py
import random

```

#### TASK 5

Next,
we'll create a variable to store the randomly generated value.

Declare a variable called `random_number`,
and assign it to the function call:

```py
random.randint(1, 9)

```

which will generate a random number between `1` (inclusive) and `9` (inclusive).

Next,
add a `print()` statement that outputs the value of the `random_number`,
and run the program several times to ensure random values are being generated as expected.

Once you're sure this is working as expected,
feel free to comment out this `print()` statement.

### **Control Flow**

#### TASK 6

Now that we've declared all the variables needed,
it's time to implement the core logic of our program!

For this section,
we'll use control flow wih an `if` / `elif` / `else` statement to assign different answers based on each randomly generated value.

First,
write an `if` statement where `if` the `random_number` is equal to `1`,
`answer` is assigned to `"Yes - definitely"`.

#### TASK 7

Next,
write an `elif` statement after the `if` statement,
where if the `random_number` is equal to `2`,
`answer` is assigned to the phrase `"It is decidedly so"`.

Then,
continue writing `elif` statements for each of the remaining phrases for the values `3` to `9`.

Recall that the nine possible answers of the Magic 8-Ball are:

1. `Yes - definitely`
2. `It is decidedly so`
3. `Without a doubt`
4. `Reply hazy, try again`
5. `Ask again later`
6. `Better not tell you now`
7. `My sources say no`
8. `Outlook not so good`
9. `Very doubtful`

#### TASK 8

Following the `if` / `elif` statements,
add an `else` statement that will set `answer` to the string `Error` if the number was accidentally assigned a value outside of our range.

### **Seeing the Result**

#### TASK 9

Now,
let's see our program in action!

Write a `print()` statement to output the asker's `name` and their `question`,
which should be in the following format:

```txt
<NAME> asks: <QUESTION>

```

For example,
when we run the program,
the output should look something like:

```txt
Joe asks: Will I win the lottery?

```

#### TASK 10

Add a second `print()` statement that will output the Magic 8-Ball's `answer` in the following format:

```txt
Magic 8-Ball's answer: <ANSWER>

```

For example,
when running the program,
it should look something like:

```txt
Magic 8-Ball's answer: My sources say no

```

#### TASK 11

Great job!

You've successfully utilized your knowledge of conditionals and previous fundamental Python concepts to create a program that generates different fortunes.

Run your program several times to see that it's working as expected.

### **Optional Challenges**

#### TASK 12

If you're up for some more challenges,
try implementing the following features to your program.

So far,
the Magic 8-Ball provides nine possible fortunes.

Try to add a few more possible answers to the program.

To do this,
you will need to increase the range of randomly generated numbers and add additional `elif` statements for each new answer.

#### TASK 13

What if the asker does not provide a name,
such that the value of `name` is an empty string?

If the `name` string is empty,
the output of the program looks like the following:

```txt
 asks: Will I win the lottery?
Magic 8 Ball's answer: Outlook not so good

```

As you can see,
the formatting of the output can use some improvement when no name is provided.

We can address this by printing out just the question,
such that it looks like the following:

```txt
Question: Will I win the lottery?
Magic 8-Ball's answer: Outlook not so good

```

You can implement this by creating an `if` / `else` statement such that:

- If the name is an empty string,
  it will only print the question.

- Else,
  the player's name and question are both printed.

#### TASK 14

What if the `question` string is empty?

If the user does not provide a question,
then the Magic 8-Ball cannot provide a fortune.

Otherwise,
the fabric of reality is at risk!

To ensure that the fabric of reality is safe,
we can create an `if` / `else` statement where:

- If the question is an empty string,
  print out a message to the user.

- Else,
  print the name and question,
  with the Magic 8-Ball's answers.

### **Solution**

#### TASK 15

Don't forget to check off all the tasks before moving on.
