# ✅ 1...

first_names = [
    "Ainsley",
    "Ben",
    "Chani",
    "Depak"
]

# ✅ 2...

preferred_size = ["Small", "Large", "Medium"]

# ✅ 3...

preferred_size.append("Medium")
print(preferred_size)

# ✅ 4...

customer_data = [
    # -3:0,      -2:1,     -1:2
    [ "Ainsley", "Small",  True  ], # -4:0
    [ "Ben",     "Large",  False ], # -3:1
    [ "Chani",   "Medium", True  ], # -2:2
    [ "Depak",   "Medium", False ], # -1:3
    # Name,      Size,     Expedited-Shipping
]

print(customer_data)

# ✅ 5...

customer_data[2][2] = False

# ✅ 6...

customer_data[1].remove(False)

# ✅ 7...

customer_data_final = customer_data + [
    ["Amit",  "Large",   True ],
    ["Karim", "X-Large", False]
]

print(customer_data_final)
