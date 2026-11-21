# Changing Numbers

Variables that are assigned numeric values can be treated the same as the numbers themselves.

Two variables can be added together,
divided by `2`,
and multiplied by a third variable without Pythong distinguishing between the variables and literals (like the number `2` in this example).

Performing arithmetic on variables does not change the variables -
we can only update a variable using the `=` sign.

```py
coffee_price = 1.50
number_of_coffees = 4

# Prints 6.0
print(coffee_price * number_of_coffees)

# Prints 1.5
print(coffee_price)

# Prints 4
print(number_of_coffees)

# Updating the price
coffee_price = 2.00

# Prints 8.0
print(coffee_price * number_of_coffees)

# Prints 2.0
print(coffee_price)

# Prints 4
print(number_of_coffees)

```

In this example,
we created two variables and assign numeric values to them.

Then,
we perform calculation on them.

This does not update the variables!

When we update the `coffee_price` variable and recalculate,
the calculations use the updated value!

## ✔️ Instructions

1. You've decided t get into quilting!
   To calculate the number of square you'll need for your first quilt,
   let's create two variables:
   `quilt_width` and `quilt_length`.
   Let's make this first quilt `8` squares wide and `12` quares long.

2. Print out the number of squares you'll need to create the quilt!

3. It turns out that the quilt required a little more material than you have on hand!
   Let's only make the quilt `8` squares long.
   How many squares will you need for the quilt,
   give the revised dimensions?
