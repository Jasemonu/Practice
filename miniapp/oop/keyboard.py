from items import Items

class Keyboard(Items):
	pay_rate = 0.7
	def __init__(self, name: str, price: float, quantity=0):
		super().__init__(name, price, quantity)
