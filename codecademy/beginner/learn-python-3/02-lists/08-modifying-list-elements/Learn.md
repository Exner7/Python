# Modifying List Elements

Let's return to our garden

```py
garden = ["Tomatoes", "Green Beans", "Cauliflower", "Grapes"]

```

Unfortunately,
we forgot to water our cauliflower,
and we don't think it will recover.

Thankfully,
our friend Jiho from Petal Power came to the rescue.

Jiho figted u some strawberry seeds.

We will replace the cauliflower with our new seeds.

We will need to modify our `garden` list to accommodate this change.

To change a value in a list,
reassign the value using the specific index.

```py
garden[2] = "Strawberries"

print(garden)

```

This will output:

```txt
["Tomatoes", "Green Beans", "Strawberries", "Grapes"]

```

Negative indices will work as well.

```py
garden[-1] = "Raspberries"

print(garden)

```

This will output:

```txt
["Tomatoes", "Green Beans", "Strawberries", "Raspberries"]

```

## ✔️ Instructions

1. We have decided to start selling some of our garden produce.

   Word around our town has spread,
   and people are interested in getting some of our delicious vegetables and fruit.

   We decided to create a waitlist to ensure we can sell to all our new customers!

   Define a list called `garden_waitlist` and set the value to contain our customers (in order):
   `"Jiho"`,
   `"Adam"`,
   `"Sonny"`,
   and `"Alisha".`

2. `"Adam"` decided his fridge is too full at the moment and asked us to remove him from the waitlist and make spacefor one of our other townsfolk.

   Replace `"Adam"` with our other interested customer,
   `"Calla"`,
   using indexing as we did in the narrative.

   For this task,
   use a positive index.

   Print `garden_waitlist` to see the change!

3. `"Alisha"` realized she was already stocked with all the items we are selling.

   She asked us to replace her with her friend `"Alex"`,
   who just ran out.

   Replace `"Alisha"` with `"Alex"` using a negative index.

   Print `garden_waitlist` again to see the change!
