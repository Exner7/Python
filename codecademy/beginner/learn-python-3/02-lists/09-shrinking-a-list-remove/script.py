order_list = [
    "Celery",
    "Orange Juice",
    "Orange",
    "Flatbread"
]

print(order_list)

order_list.remove("Flatbread")
print(order_list)

new_store_order_list = [
    "Orange",
    "Apple",
    "Mango",
    "Broccoli",
    "Mango"
]

new_store_order_list.remove("Mango")
print(new_store_order_list)

new_store_order_list.remove("Onions")

#     new_store_order_list.remove("Onions")
#     ~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^
# ValueError: list.remove(x): x not in list
