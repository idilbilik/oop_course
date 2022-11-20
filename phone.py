from item import Item

class Phone(Item):
    # all = []
    # super allows us to do, it allows us to have full access to all the attributes of the parent class
    # And by using the super func, we don't really need to hard code in the attribute assignment
    def __init__(self, name: str, price: float, quantity = 0, broken_phones = 0):
        # Call the super functionto have access to all attributes / methods
        # by using the super func in the child class, we will have access to the old attribute.
        super().__init__(
            name, price, quantity
        )
        # Run validations to the received arguments
        # assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        # assert quantity >= 0 , f"Quantity {quantity} is not greater than or equal to zero!"
        assert broken_phones >= 0 , f"Broken Phones {broken_phones} is not greater than or equal to zero!"
        # Assign to self object
        # self.name = name
        # self.price = price
        # self.quantity = quantity
        self.broken_phones = broken_phones
        
        #Actions to execute
        # Phone.all.append(self)
         
phone1 = Phone("jsvPhonev10", 500, 5, 1)
print(Item.all)
print(Phone.all)