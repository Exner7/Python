weight = 4.8 # (Ground Shipping is cheapest)
weight = 41.5 # (Ground Shipping Premium is cheapest)

# Ground Shipping

cost = 20.00 # Flat Charge

# Added Price per Pound
if weight <= 2:
    cost += 1.50 * weight
elif weight <= 6:
    cost += 3.00 * weight
elif weight <= 10:
    cost += 4.00 * weight
else:
    cost += 4.75 * weight

print(
    "Ground Shipping:",
    weight, "(lb), $", cost
)

cheapest = cost
cheapest_method = "Ground Shipping"

# Ground Shipping Premium

premium_cost = 125.00 # Flat charge

if premium_cost < cheapest:
    cheapest = premium_cost
    cheapest_method = "Ground Shipping Premium"

print(
    "Ground Shipping Premium:",
    weight, "(lb), $", premium_cost
)

# Drone Shipping

drone_cost = 0.00

if weight <= 2:
    drone_cost += 4.50 * weight
elif weight <= 6:
    drone_cost += 9.00 * weight
elif weight <= 10:
    drone_cost += 12.00 * weight
else:
    drone_cost += 14.25 * weight

print(
    "Drone Shipping:",
    weight, "(lb), $", drone_cost
)

if drone_cost < cheapest:
    cheapest = drone_cost
    cheapest_method = "Drone Shipping"

print(
    "Cheapest method: " + cheapest_method
    + ", at $" + str(cheapest)
)
