import datetime
from dataclasses import dataclass

from database.products_dao import ProductsDao
from model.product import Product
from model.retailer import Retailer

from database.retailers_dao import RetailerssDao


@dataclass
class Sale:
    """
    Class representing a sale from the table "go_daily_sales".
    """
    date: datetime.date
    quantity: int
    unit_price: float
    unit_sale_price: float

    # relazioni. Keep in mind that the PK of a sale is given by the tuple
    # (retailer_code, product_number, order_method_code)
    retailer_code: int
    product_number: int
    order_method_code: int
    retailer: Retailer = None # May be needed later
    product: Product = None # May be needed later

    # ricavo: campo non presente nel database, ma che aggiungo per comodità,
    # calcolandolo nel __post_init__(), ovverosia dopo che gli attributi principali sono già
    # stati popolati
    def __post_init__(self):
        """
        After initialization, it computes the "ricavo" of the sale as unit_sale_price * quantity.
        """
        self.ricavo: float = self.unit_sale_price * self.quantity

    def __str__(self):
        return f"Data: {self.date}; Ricavo: {self.ricavo}; Retailer: {self.retailer_code}; Product: {self.product_number}"

    def __eq__(self, other):
        return (self.retailer_code == other.retailer_code
                and self.product_number == other.product_number
                and self.order_method_code == other.order_method_code)

    def __hash__(self):
        return hash((self.retailer_code, self.product_number, self.order_method_code))

    def __lt__(self, other):
        return self.ricavo < other.ricavo

    def get_year(self) -> int:
        """
        Function that returns the year of the sale.
        :return: the year of the sale
        """
        return self.date.year

    def get_retailer(self) -> Retailer:
        """
        Function that returns the retailer that made the sale.
        :return: a Retailer.
        """
        if self.retailer is None:
            self.retailer = RetailerssDao.get_retailer(self.retailer_code)
        return self.retailer

    def get_brand(self) -> str:
        """
        Function that returns the brand of the product sold in this sale.
        :return: the string with the brand information.
        """
        if self.product is None:
            self.product = ProductsDao.get_product(self.product_number)
        return self.product.product_brand
