import json
import os
from product import Electronics, Grocery, Clothing

class Inventory:
    def __init__(self):
        self._products = []

    def add(self, product):
        for p in self._products:
            if p.get_id() == product.get_id():
                raise Exception("⚠️ Duplicate Product ID!")
        self._products.append(product)
        print("✅ Product added.")

    def remove(self, product_id):
        for p in self._products:
            if p.get_id() == product_id:
                self._products.remove(p)
                print("🗑️ Product removed.")
                return
        print("❌ Product not found.")

    def search_by_name(self, name):
        return [p for p in self._products if p.get_name().lower() == name.lower()]

    def search_by_type(self, ptype):
        type_map = {"electronics": Electronics, "grocery": Grocery, "clothing": Clothing}
        cls = type_map.get(ptype.lower())
        return [p for p in self._products if isinstance(p, cls)] if cls else []

    def list_all(self):
        if not self._products:
            print("📭 Inventory is empty.")
        for p in self._products:
            print(p)

    def sell(self, product_id, qty):
        for p in self._products:
            if p.get_id() == product_id:
                p.sell(qty)
                print("✅ Product sold.")
                return
        print("❌ Product not found.")

    def restock(self, product_id, qty):
        for p in self._products:
            if p.get_id() == product_id:
                p.restock(qty)
                print("📦 Product restocked.")
                return
        print("❌ Product not found.")

    def total_value(self):
        total = sum(p.get_total_value() for p in self._products)
        print(f"💰 Total Inventory Value: {total}")

    def remove_expired(self):
        removed = False
        for p in self._products[:]:
            if isinstance(p, Grocery) and p.is_expired():
                self._products.remove(p)
                removed = True
        print("✅ Expired products removed." if removed else "🟢 No expired items.")

    def save_to_file(self, filename):
        data = []
        for p in self._products:
            info = {
                "type": type(p).__name__,
                "id": p.get_id(),
                "name": p.get_name(),
                "price": p.get_price(),
                "quantity": p.get_quantity()
            }
            if isinstance(p, Electronics):
                info.update({"warranty_years": p.warranty_years, "brand": p.brand})
            elif isinstance(p, Grocery):
                info.update({"expiry_date": p.expiry_date})
            elif isinstance(p, Clothing):
                info.update({"size": p.size, "material": p.material})
            data.append(info)
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_from_file(self, filename):
        if not os.path.exists(filename):
            return
        with open(filename, "r") as f:
            try:
                data = json.load(f)
            except:
                return
        for item in data:
            if item["type"] == "Electronics":
                p = Electronics(item["id"], item["name"], item["price"], item["quantity"], item["warranty_years"], item["brand"])
            elif item["type"] == "Grocery":
                p = Grocery(item["id"], item["name"], item["price"], item["quantity"], item["expiry_date"])
            elif item["type"] == "Clothing":
                p = Clothing(item["id"], item["name"], item["price"], item["quantity"], item["size"], item["material"])
            else:
                continue
            self._products.append(p)
