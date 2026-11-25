# Modifying 2D Lists

Now that we know how to access two-dimensional lists,
modifying the elements should come naturally.

Let's return to a classroom example,
but now instead of heights or test scores,
our list stores the student's favorite hobby!

```py
class_name_hobbies = [["Jenny", "Breakdancing"], ["Alexus", "Photography"], ["Grace", "Soccer"]]

```

`"Jenny"` changed their mind and is now more interested in `"Meditation"`.

We will need to modify our `class_name_hobbies` list to accommodaate this change.

To change a value in a two-dimensional list,
reassign it using the corresponding indices.

```py
# The list of Jenny is at index `0`. The hobby is at index `1`. 
class_name_hobbies[0][1] = "Meditation"
print(class_name_hobbies)

```

This would output:

```txt
[["Jenny", "Meditation"], ["Alexus", "Photography"], ["Grace", "Soccer"]]

```

Negative indices will work as well.

```py
# The list of Grace is the last entry. The hobby is the last element. 
class_name_hobbies[-1][-1] = "Football"
print(class_name_hobbies)

```

This would output:

```txt
[["Jenny", "Meditation"], ["Alexus", "Photography"], ["Grace", "Football"]]

```

## ✔️ Instructions

1. ☑️

   Our school is expanding!

   We are welcoming a new group of students from all over the world today.

   Using the provided table,
   create  a two-dimensional list called `incoming_class` to represent the data.

   Each sublist in `incoming_class` should contain the name,
   nationality,
   and grade for a single student.

   | Name        | Nationality   | Grade Level |
   | ----------- | ------------- | ----------- |
   | `"Kenny"`   | `"American"`  | `9`         |
   | `"Tanya"`   | `"Ukrainian"` | `9`         |
   | `"Madison"` | `"Indian"`    | `7`         |

   Print `incoming_class` to see our list.

   ---

2. ☑️

   `"Madison"` passed an exam to advance a grade.

   She will be pushed into 8th grade rather than her current 7th grade in our list.

   Modify the list using double brackets `[][]` to make the change.

   Use positive indices.

   Print `incoming_class` to see our change.

   ---

3. ☑️

   `"Kenny"` likes to be called by his nickname `"Ken"`.

   Modify the list using double brackets `[][]` to accommodate the change,
   but only using negative indices.

   Print `incoming_class` to see our change.
