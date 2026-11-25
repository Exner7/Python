# Shrinking a List: Remove

We can remove elements in a list using the `.remove()` Pyton method.

Suppose we have a filled list called `shopping_line` that represents a line at a grocery store:

```py
shopping_line = ["Cole", "Kip", "Chris", "Sylvana"]

```

We could remove `"Chris"` by using the `.remove()` method.

```py
shopping_line.remove("Chris")

print(shopping_line)

```

If we examine `shopping_line`,
we can see that it no longer contains `"Chris"`:

```txt
["Cole", "Kip", "Sylvana"]

```

If we use `.remove()` on a list that has duplicate elements,
only the first element that matches the specified value is removed:

```py
# Create a list
shopping_line = ["Cole", "Kip", "Chris", "Sylvana", "Chris"]

# Remove an element
shopping_line.remove("Chris")
print(shopping_line)

```

This will output:

```txt
["Cole", "Kip", "Sylvana", "Chris"]

```

Let's practice using the `.remove()` method to remove elements from a list.

## ✔️ Instructions

1. We have decided to get into the grocery store business.

   Our manager,
   Calla,
   has decided to store all the inventory purchases in a list to help track what products need to be ordered.

   Let's createa list called `order_list` with the following values (in this particular order):

   1. `"Celery"`
   2. `"Orange Juice"`
   3. `"Orange"`
   4. `"Flatbread"`

   Print `order_list` to see the current list.

   ---

2. We are in luck!

   We actually found a spare case of `"Flatbread"` in our back storage,
   so we won't need to order it anymore.

   Let's remove it from `order_list` using the `.remove()` method.

   Print out `order_list` to see the current list.

   ---

3. Our store has grown to be a huge success!

   We decided to open a econd store and require a new order list.

   Calla has done us the favor of figuring out what items we'll need.

   Create a new list called `new_store_order_list` and assign it to the following values (in order):

   1. `"Orange"`
   2. `"Apple"`
   3. `"Mango"`
   4. `"Broccoli"`
   5. `"Mango"`

   _Note_:
   _Our second store will need two orders of mangos_,
   _so the value is duplicated_.

   Print `new_store_order_list` to see the current list.

   ---

4. We are in luck again!

   We actually found a spare case of `"Mango"` in our back storage.

   We won't be needing to place two orders anymore.

   Let's remove one instance from `new_store_order_list` using the `.remove()` method.

   Print `new_store_order_list` to see the current list.

   ---

5. Calla ran to tell us some important news!

   She asked u to remove `"Onions"` from our new `new_store_order_list`.

   If we double-check our list,
   we will notice we don't have `"Onions"` on our list.

   Let's see what happens when we try to remove an item that does not exist.

   Call the `.remove()` method with the value of `"Onions"` on our new `new_store_order_list` list.
