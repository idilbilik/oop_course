from item import Item

item1 = Item("FirstItem", 750)
# setting an attribute
item1.name = "OtherItem"
#Exception has occurred: AttributeError
#can't set attribute

#getting an attribute
print(item1.name)
# item1.name = "OtherItem"

# print(item1.read_only_name)

# item1.read_only_name = "BBB" #attribute error