# Modulo

Python offers a companion to the division operator called the modulo operator.

The **modulo operator** is indicated by `%` and gives the remainder of a division calculation.

If the two numbers are (_perfectly_) divisible,
then the result of the module operation will be `0`.

```py
# Prints 4 because 29 / 5 is 5 with a remainder of 4
print( 29 % 5 )

# Prints 2 because 32 / 3 is 10 with a remainder of 2
print( 32 / 3 )

# Modulo by 2 returns 0 for even numbers and 1 for odd numbers

# Prints 0
print( 44 % 2 )

```

Here,
we use the modulo operator to find the remainder of division operations.

We see that `29 % 5` equals `4`,
`32 % 3` equals `2`,
and `44 % 2` equals `0`.

Let's look at another example to get a better idea of how module is useful in programming:

```py
print( 3 % 3 ) # Prints 0
print( 4 % 3 ) # Prints 1
print( 5 % 3 ) # Prints 2
print( 6 % 3 ) # Prints 0
print( 7 % 3 ) # Prints 1

```

In each of these modulee operations,
`3` is the divisor.

Since `3 % 3` equals `1` with no remainder,
the result of the first modulo is `0`.

_Note_: _As the dividend increases by_ `1`,
_the remainder also increases by_ `1`,
_until we reach the next number that is evenly divisible by_ `3` -
_this creates a pattern that repeats continuously as the divident increases by_ `1`!

Before of this,
the modulo operator is useful in programming when we want to perform an action every $n$-th time something occurs.

Imagine we own a small café and would like for every seventh customer to receive a survey.

If customer transactions are numbered in the order in which they occur,
we can determine which customers should receive the survey by calculating `transaction_number % 7` -
if the result is `0`,
hand out the survey!

## ✔️ Instructions

1. You are launching a new campaign for your online shop in which every 10th customer receives 10% off their next order.

   To easily calculate this,
   you decide that order numbers divisible by 10 will receive the coupon.

   Here's the first order of the day, #269!

   Create a new variable,
   `first_order_remainder`,
   and set it equal to `269` module `10`.

   Then,
   print out `first_order_remainder` to find out if that customer will receive a discount.

2. Look at the printed value of `first_order_remainder`.

   Was the remainder `0`,
   meaning that the customer should receive a coupon for this order?

   Create a new variable called `first_order_coupon` and assign to it a value of `"yes"` if the order should get a coupon.

   Otherwise,
   give `first_order_coupon` the value of `"no"`.

3. Here comes the second order of the day,
   #270 -
   let's see if they will get a discount!

   Find the remainder by calculating `270` modulo `10` and store the result in a new variable named `second_order_remainder`.

   Then print out `second_order_remainder`.

4. Based on the printed value of `second_order_remainder`,
   should the customer receive a coupon for this order?

   Create a new variable named `second_order_coupon` and give it the value of `"yes"` if the order should get a coupon.

   Otherwise,
   give `second_order_coupon` the value of `"no`.
