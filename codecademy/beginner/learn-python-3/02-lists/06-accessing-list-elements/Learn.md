# Accessing List Elements

We are interviewing candidates for a job.

We will call each candidate in order,
represented by a Python list:

```py
calls = ["Juan", "Zofia", "Amare", "Ezio", "Ananya"]

```

First,
we'll call `"Juan"`,
then `"Zofia"`,
etc.

In Python,
we call the location of an element in a list its **index**.

Python lists are **zero-indexed**.

This means that the first element in a list has index `0`,
rather than `1`.

Here are the index numbers for the list `calls`:

| Element    | Index |
| ---------- | ----- |
| `"Juan"`   | `0`   |
| `"Zofia"`  | `1`   |
| `"Amare"`  | `2`   |
| `"Ezio"`   | `3`   |
| `"Ananya"` | `4`   |

In this example,
the element with the index `2` is `"Amare"`.

We can select a single element from a list by using square brackets (`[]`) and the index of the list item.

If we wanted to sselect the third element from the list,
we'd use `calls[2]`:

```py
print(calls[2])

```

This will output:

```txt
Amare

```

_Note_:
_When accessing elements of a list_,
_we must use an_ `int` _as the index_.

_If we use a_ `float`,
_we will get an error_.

_This can be especially tricky when using division_.

_For example_,
`print(calls[4/2])` _will result in an error_,
_because_ `4/2` _gets evaluated to a_ `float`,
`2.0`.

_To solve this problem_,
_we can force the result of our division to be an_ `int` _by using the_ `int()` _function_.

`int()` _takes a number and cuts off the decimal point_.

_For example_,
`int(5.9)` _and_ `int(5.0)` _will both become_ `5`.

_Therefore_,
`calls[int(4/2)]` _will result in the same value as_ `calls[2]`,
_whereas_ `calls[4/2]` _will result in a_ `TypeError`.

## ✔️ Instructions

1. Use square brackets (`[` and `]`) to access the fourth employee from the list `employees`.

   Save it to the variable `employee_four`.

2. Paste the following code into `script.py`:

   ```py
   print(employees[8])

   ```

   What happens?

   Why?

3. Accessing an element that does not exist produces an `IndexError`.

   In the line of code that you pasted,
   change `8` to an index that exists so that you don't get an `IndexError`.

   Run your code again!
