# Variables

Programming languages offer a method of storing data for reuse.

If there is a greeting we want to present,
a date we need to reuse,
or a user ID we need to remember,
we can create a variable to store the value.

In Python,
we assign variables by using the equals sign (`=`).

```py
message_string = "Hello there"
# Prints "Hello there"
print(message_string)

```

In the preceding example,
we store the message `"Hello there"` in a variable called `message_string`.

Variables can't have spaces or symbols in their names other than an underscore (`_`).

They cannot begin with numbers,
but may contain numbers after the first character (e.g.., `cool_variable_5` is okay).

---

It's no coincidence that we call them "variables".

If the context of a program changes,
we can update a variable while still performing the same logical processes on it.

```py
# Greeting
message_string = "Hello there"
print(message_string)

# Farewell
message_string = "Hasta la vista"
print(message_string)

```

In this example,
we create the variable `message_string`,
assign a welcome message,
and print the greeting.

After we gree the use,
we want to wish them goodbye.

We then update `message_string` to a departure message and print that out.

## ✔️ Instructions

1. Update the variable `meal` to reflect each meal of the day before we print it.

    _Note: We hav started the two reasignment statements for you._
    _The program will not run correctly if you do not complete these two statements_ -
    _it will yield an error._
    _We will investigate errors in more detail in the next exercise_!
