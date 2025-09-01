# ...existing code...
class Vehicle:
    def __init__(self, model: int, brand: str, price: float):
        self.model = model
        self.brand = brand
        self.price = float(price)

    def display_info(self):
        print(f"Model Number={self.model}, Brand={self.brand}, Price={self.price:.2f}")

    def apply_discount(self, percent: float):
        """Reduce the price by a given percentage (0-100)."""
        if percent < 0 or percent > 100:
            raise ValueError("percent must be between 0 and 100")
        self.price -= self.price * (percent / 100)

    def update_price(self, new_price: float):
        """Set a new price (must be non-negative)."""
        if new_price < 0:
            raise ValueError("new_price must be non-negative")
        self.price = float(new_price)

    def get_brand(self) -> str:
        return self.brand

    def is_luxury(self, threshold: float = 500000) -> bool:
        return self.price > threshold

    def to_dict(self) -> dict:
        return {"model": self.model, "brand": self.brand, "price": self.price}

    def __repr__(self):
        return f"Vehicle(model={self.model}, brand='{self.brand}', price={self.price:.2f})"


# Demonstration / simple usage
vehicle1 = Vehicle(1, "Rolls Royce", 969000)
vehicle2 = Vehicle(2, "Lamborghini", 1969000)
vehicle3 = Vehicle(3, "Bugatti", 549000)

vehicles = [vehicle1, vehicle2, vehicle3]

print("Before changes:")
for v in vehicles:
    v.display_info()

# Apply a 10% discount to vehicle2
vehicle2.apply_discount(10)
# Update price of vehicle3
vehicle3.update_price(499999)
# Get brand of vehicle1
brand_v1 = vehicle1.get_brand()
# Check luxury status
luxuries = [v.model for v in vehicles if v.is_luxury()]

print("\nAfter changes:")
for v in vehicles:
    v.display_info()

print(f"\nBrand of vehicle1: {brand_v1}")
print(f"Luxury vehicles (model numbers): {luxuries}")