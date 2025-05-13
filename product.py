from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, product_id, name, price, quantity):
        self._product_id = product_id
        self._name = name
        self._price = price
        self._quantity = quantity

    @abstractmethod
    def restock(self, amount): pass

    @abstractmethod
    def sell(self, amount): pass

    def get_total_value(self):
        return self._price * self._quantity

    def get_id(self):
        return self._product_id

    def get_name(self):
        return self._name

    def get_quantity(self):
        return self._quantity

    def get_price(self):
        return self._price

    def __str__(self):
        return f"📦 ID: {self._product_id} | Name: {self._name} | Price: {self._price} | Stock: {self._quantity}"

class Electronics(Product):
    def __init__(self, product_id, name, price, quantity, warranty_years, brand):
        super().__init__(product_id, name, price, quantity)
        self.warranty_years = warranty_years
        self.brand = brand

    def restock(self, amount):
        self._quantity += amount

    def sell(self, amount):
        if self._quantity < amount:
            raise Exception("❌ Not enough stock!")
        self._quantity -= amount

    def __str__(self):
        base = super().__str__()
        return base + f" | Brand: {self.brand} | Warranty: {self.warranty_years} yr 🧰"

class Grocery(Product):
    def __init__(self, product_id, name, price, quantity, expiry_date):
        super().__init__(product_id, name, price, quantity)
        self.expiry_date = expiry_date

    def restock(self, amount):
        self._quantity += amount

    def sell(self, amount):
        if self._quantity < amount:
            raise Exception("❌ Not enough stock!")
        self._quantity -= amount

    def is_expired(self, today="2025-10-01"):
        return self.expiry_date < today

    def __str__(self):
        base = super().__str__()
        return base + f" | Expiry: {self.expiry_date} 🛒"

class Clothing(Product):
    def __init__(self, product_id, name, price, quantity, size, material):
        super().__init__(product_id, name, price, quantity)
        self.size = size
        self.material = material

    def restock(self, amount):
        self._quantity += amount

    def sell(self, amount):
        if self._quantity < amount:
            raise Exception("❌ Not enough stock!")
        self._quantity -= amount

    def __str__(self):
        base = super().__str__()
        return base + f" | Size: {self.size} | Material: {self.material} 👕"
