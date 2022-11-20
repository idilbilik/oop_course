# we can dynamically assign an attribute to an instance from this magic method which is called double underscore init

class  Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    def __init__(self, name: str, price: float, quantity = 0): #magic methods 
        # print("Python called this double underscore init double underscore method twice, thanks to those two instances we have created!")
        # print("I AM CREATED")
        #print(f"An instance created: {name}")
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        # if the given values are not fix with assert than we will see this message at terminal.(validation)
        assert quantity >= 0 , f"Quantity {quantity} is not greater than or equal to zero!"
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
        
    def calculate_total_price(self): #methods
        return self.price * self.quantity
    
    def apply_discount(self):
        #self.price = self.price * Item.pay_rate
        self.price = self.price * self.pay_rate #instance level

item1 =  Item("phone", 100, 1)
item1.apply_discount()
print(item1.price)
# item1 =  Item("phone", 100, -1) give us assertion error cause of >= 0 situation
#print(item1.calculate_total_price())
# print(Item.pay_rate)
# print(item1.pay_rate)
# print(Item.__dict__) # magic attribute (All the attributes for Class level)
# print(item1.__dict__) # ( All the attributes for instance level)
# item1.name = "phone"
# item1.price = 100
# item1.quantity = 5
# print(item1.calculate_total_price(item1.price, item1.quantity))

# print(type(item1))
# print(type(item1.name))
# print(type(item1.price))
# print(type(item1.quantity))

# random_str = "aaa"
# print(random_str.upper())

item2 =  Item("laptop", 1000, 3)
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)
#print(item2.calculate_total_price())
# print(item2.pay_rate)
# item2.has_numpad = False
# item2.name = "laptop"
# item2.price = 1000
# item2.quantity = 3
# print(item2.calculate_total_price(item2.price, item2.quantity))

# print(item1.name)
# print(item1.price)
# print(item1.quantity)
# print(item2.name)
# print(item2.price)
# print(item2.quantity)