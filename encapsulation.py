from item import Item

item1 = Item("FirstItem", 750)

# item1.price = 900

# print(item1)
item1.apply_increment(0.2)
item1.apply_discount()
print(item1.price)

