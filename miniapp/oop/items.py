# a class of items 
import csv

class Items:
	pay_rate = 0.8
	all = []
	def __init__(self, name: str, price: float, quantity=0):
		# Run validation to the received arguments
		assert price >= 0, "Price {} is not greater than or equal to zero!".format(price)
		assert quantity >= 0, "Quantity {} is not greater than or equal to zero!".forat(quantity)

		# assign objects
		self.__name = name
		self.price = price
		self.quantity = quantity
		
		# actions to execute
		Items.all.append(self
)
	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, value):
		if len(value) > 10:
			raise Exceptio("The value is too long")
		else:
			self.__name = value

	def calculate_total_price(self):
		return self.price * self.quantity

	def apply_discount(self):
		self.price = self.price * Items.pay_rate
		return self.price

	@classmethod
	def instantiate_from_csv(cls):
		with open('items.csv', 'r') as file:
			reader = csv.DictReader(file)
			items = list(reader)
		for item in items:
			Items(
			name=item.get('name'),
			price=int(item.get('price')),
			quantity=int(item.get('quantity')),
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
		return "{}('{}',{}, {})".format(self.__class__.__name__, self.name, self.price, self.quantity)
