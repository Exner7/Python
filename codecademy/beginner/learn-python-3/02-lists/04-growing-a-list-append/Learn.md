# Growing a List: Append

We can add a single element to a list using the `.append()` Python method.

Suppose we have an empty list called `garden`:

```py
garden = []

```

We can add the element `"Tomatoes"` by using the `.append()`. method:

```py
garden.append("Tomatoes")

print(garden)

```

This will output:

```txt
['Tomatoes']

```

We see that `garden` now contains `"Tomatoes"`!

When we use `.append()` on a list that already has elements,
our new element is added to the end of the list:

```py
# Create a list
garden = ["Tomatoes", "Grapes", "Cauliflower"]

# Append a new element
garden.append("Green Beans")
print(garden)

```

This will output:

```txt
['Tomatoes', 'Grapes', 'Cauliflower', 'Green Beans']

```

## ✔️ Instructions

1. Jiho works for a gardening store called Petal Power.

   Jiho keeps a list of orders in `orders`.

   Use `print()` to inspect the orders he has received today.

2. Jiho just received a new order for `"tulips"`.

   Use `.append()` to add this string to `orders`.

3. Another order has come in!

   Use `.append()` to add `"roses"` to `orders`.
