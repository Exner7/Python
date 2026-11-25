# Accessing 2D Lists

Let's return to our classroom heights example:

```py
heights = [["Noelle", 61], ["Ali", 70], ["Sam", 67]]

```

Two-dimensional lists can be accessed similarly to their one-dimensional counterparts.

Instead of providing a single pair of brackets `[ ]`,
we will be use an additional set for each dimension past the first.

If we wanted to access the height of `"Noelle"`:

```py
#Access the sublist at index 0, and then access the first index of that sublist. 
noelles_height = heights[0][1] 
print(noelles_height)

```

This would output:

```txt
61

```

Here are the index numbers to access data for the list `heights`:

---

| Element    | Index           |
| ---------- | --------------- |
| `"Noelle"` | `heights[0][0]` |
| `61`       | `heights[0][1]` |
| `"Ali"`    | `heights[1][0]` |
| `70`       | `heights[1][1]` |
| `"Sam"`    | `heights[2][0]` |
| `67`       | `heights[2][1]` |

---

Let's practice accessing data in a two-dimensional list.

## ✔️ Instructions

1. ☑️
   We want to have a way to store all of our classroom test score data.

   Using the provided table,
   create a two-dimenional list called `class_name_test` to represent the data.

   Each sublist in `class_name_test` should have one student's name and their associated score,.

   ---

   | Name       | Test Score |
   | ---------- | ---------- |
   | `"Jenny"`  | `90`       |
   | `"Alexus"` | `85.5`     |
   | `"Sam"`    | `83`       |
   | `"Ellie"`  | `101.5`    |

   ---

   Print `class_name_test` to see the result.

   ---

2. ☑️
   Use double square brackets (`[][]`) to select the test score for `"Sam"` from the list `class_name_test`.

   Save it to the variable `sams_score`.

   Print the variable `sams_score` to see the result.

   ---

3. ☑️
   Use double square brackets (`[][]`) to select the test score for `"Ellie"` from the list `class_name_test`.

   This time,
   only use negative indices!

   Save it to the variable `ellies_score`.

   Print the variable `ellies_score` to see the result
