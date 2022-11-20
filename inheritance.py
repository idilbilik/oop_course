import csv
class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity = 0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0 , f"Quantity {quantity} is not greater than or equal to zero!"
        
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
        #Actions to execute
        Item.all.append(self)
        
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
    #this method is actually designed for instantiating the object itself.
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv','r') as f:
            reader = csv.DictReader(f) # this method should go ahead and read our content as a list of dictionaries
            items = list(reader)
        
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )
  
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
        
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}','{self.price}','{self.quantity}')" 


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
# print(phone1.calculate_total_price()) 
# phone1.broken_phones = 1
# phone2 = Phone("jsvPhonev20", 700, 5, 1)
# phone2.broken_phones = 1

