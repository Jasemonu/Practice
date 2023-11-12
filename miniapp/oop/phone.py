# a subclass of items

from items import Items

class Phone(Items):
        def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
                # call to super function to have access to all attributes / methods
                super().__init__(name, price, quantity)

               # Run validation to the received arguments
                assert broken_phones >= 0, "Broken_phones {} is not greater than or equal to zero!".format(bbroken_phones)

                # assign objects
                self.name = name
                self.price = price
                self.quantity = quantity
                self.broken_phones = broken_phones
