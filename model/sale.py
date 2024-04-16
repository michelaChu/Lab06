from dataclasses import dataclass
from datetime import date
@dataclass
class Sale:
    retailer_code: int
    product_number: int
    order_method_code: int
    date: date
    quantity: int
    unit_price: float
    unit_sale_price: float

    def __str__(self):
        return f"Date: {self.date}; Ricavo: {self.calcola_ricavo()}; Retailer code: {self.retailer_code}; Product number: {self.product_number}"

    def calcola_ricavo(self):
        return self.unit_sale_price*self.quantity

