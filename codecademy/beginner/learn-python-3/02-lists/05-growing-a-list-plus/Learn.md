# Growing a List: Plus (+)

When we want to add multiple item to a list,
we can use `+` to combine two lists (also known as **concatenation**).

Below,
we have a list of items sold at a bakery called `items_sold`:

```py
items_sold = ["cake", "cookie", "bread"]

```

Suppose the bakery want to start selling `"biscuit"` and `"tart"`:

```py
items_sold_new = items_sold + ["biscuit", "tart"]
print(items_sold_new)
# Prints ['cake', 'cookie', 'bread', 'biscuit', 'tart']

```

In this example,
we created a new variable,
`items_sold_new`,
which combined the original items sold with the new items.

We can inspect the original `items_sold` and see that it did not change:

```py
print(items_sold)
# Prints ['cake', 'cookie', 'bread']

```

We can only use `+` with other lists.

If we try to run this code:

```py
my_list = [1, 2, 3]
my_new_list = my_list + 4

```

we will get the following error:

```txt
Traceback (most recent call last):
  File "/home/ccuser/workspace/create-python-list-growing-a-list-plus/script.py", line 2, in <module>
    my_new_list = my_list + 4
                  ~~~~~~~~^~~
TypeError: can only concatenate list (not "int") to list
```

If we want to add a single element using `+`,
we still have to put it into a list with brackets (`[]`):

```py
my_new_list = my_list + [4]
print(my_new_list)
# Prints [1, 2, 3, 4]

```

Now,
let's use `+` to practice combining two lists!

## ✔️ Instructions

1. Jiho is updating a list of `orders`.

   He just received orders for `"lilac"` and `"iris"`.

   Create a list named `new_orders` containing our new orders.

2. Use `+` to create a new list called `orders_combined` that combines `orders` with `new_orders`.
