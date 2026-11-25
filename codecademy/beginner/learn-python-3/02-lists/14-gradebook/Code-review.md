# Code review

## Purpose 🎯

Does the code do what it's supposed to do?

- Your code follow the Gradebook task flow:
  it creates subjects and grades,
  builds a two-dimensional gradebook,
  augments it with new subjects,
  updates a score,
  switches a grade to Pass.
  and combines with last_semester_gradebook.

  It prints the final structure as required and uses append and indexing correctly.

- The code aligns with the project objective of practicing Python lists to manage subjects and grades and runs without syntax errors.

## Readability 📖

Is the code easy to understand?

- Code is easy to follow with clear sections for each task and comments marking completed steps.

- Some variable naming is descriptive (gradebook,
  full_gradebook).

  Minor improvements:
  maintain consistent spacing and remove trailing spaces for readability.

- Optional:
  add brief comments above non-obvious lines to explain why gradebook[-1][-1] is incremented by 5 or why poetry is converted to Pass.

## Performance 🚀

Does the code run efficiently?

- Code perform all tasks with direct list operations and minimal overhead.

- Suggestion:
  ensure index references remain valid if the list structure changes in the future (e.g.,
  guard against empty gradebook before modification).

- Suggestion:
  if tasks expand,
  consider wrapping gradebook manipulations in small helper functions for clarity and reuse.
