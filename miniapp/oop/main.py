from items import Items
from phone import Phone
from keyboard import Keyboard


#phone1 = Phone("jscPhonev10", 500, 5, 1)
#print(phone1.calculate_total_price())
#phone2 = Phone("scPhonev20", 700, 5, 1)

#print(Items.all)
#print(Phone.all)
Items.instantiate_from_csv()
print(Items.all)

item1 = Keyboard("jscKeyboard", 1000, 3)
item1.apply_discount()
print(item1.price)


