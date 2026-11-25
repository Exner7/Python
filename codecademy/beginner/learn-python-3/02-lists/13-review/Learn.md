# Review

So far,
we have learned how to:

- create a list

- access,
  add,
  remove,
  and modify list elements

- create a two-dimensional list

- access and modify two-dimensional list elements

Let's practice these skills.

## ✔️ Instructions

1. ☑️

   Maria is entering customer data for her web store.

   We're going to help her organize her data.

   Start by turning this list of customer first names into a list called `first_names`.

   Make sure to enter the names in this order:

   1. `"Ainsley"`
   2. `"Ben"`
   3. `"Chani"`
   4. `"Depak"`

   ---

2. ☑️

   Maria wants to track all customer's preferred sizes for her clothing.

   Create a list called `preferred_size`.

   Fill our new list `preferred_size` with the following data,
   containing the preferred sizes for `"Ainsley"`, `"Ben"`, and `"Chani"`:

   ```py
   ["Small", "Large", "Medium"]

   ```

   ---

3. ☑️

   Oh no!

   We forgot to add a size for `"Depak"`.

   `"Depak"` prefers `"Medium"` size.

   Use `.append()` to add `"Medium"` to the `preferred_size` list.

   Print `preferred_size` to see our change.

   ---

4. ☑️

   Maria is having a hard time visualizing which customer is associated with each size.

   Let's restructure our two lists into a two-dimensional list to help Maria.

   In addition to the data we already have,
   Maria is adding a third value for each customer,
   indicating whether they want expedited shipping on their orders.

   This will be reflected using a boolean value (`True` for expedited, `False` for regular).

   Create a two-dimensional list called `customer_data` using the following table as a reference for the data.

   Each sublist should contain a name,
   size,
   and expedited shipping option for a single person.

   | Name        | Size       | Expedited Shipping |
   | ----------- | ---------- | ------------------ |
   | `"Ainsley"` | `"Small"`  | `True`             |
   | `"Ben"`     | `"Large"`  | `False`            |
   | `"Chani"`   | `"Medium"` | `True`             |
   | `"Depak"`   | `"Medium"` | `False`            |

   Print `customer_data` to see the data.

   ---

5. ☑️

   `"Chani"` reached out to Maria.

   She requested to switch to regular shipping to save money.

   Change the data value for Chani's shipping preference to `False` in our two-dimensional list to reflect the change.

   ---

6. ☑️

   `"Ben"` reached out to Maria asking to remove his shipping option (the `True` or `False` value) because he is unsure what type he wants.

   Use the `.remove()` method to delete the shipping value from the sublist that contains `"Ben"` data.

   _Note_:
   _We never explicitly went over how to use the_ `.remove()` _method on a 2D list together_.
   _If you feel like you are struggling_,
   _look at the hint for guidance_.

   ---

7. ☑️

   Great job making it thi far!

   One last thing:
   Maria received new customers,
   `"Amit"` and `"Karim"`,
   the following 2D list contains their data:

   ```py
   [["Amit", "Large", True], ["Karim", "X-Large", False]]

   ```

   Create a new variable `customer_data_final`.

   Combine our existing list `customer_data` with our new customer 2D list using `+` by adding it to the end of `customer_data`.

   Print `customer_data_final` to see our final result.
