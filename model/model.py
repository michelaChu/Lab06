from database.sale_dao import SaleDao
from database.product_dao import ProductDao
from database.retailer_dao import RetailerDao
class Model:
    def __init__(self):
        self.sale_dao = SaleDao()
        self.product_dao = ProductDao()
        self.retailer_dao = RetailerDao()

    def get_anni(self):
        return self.sale_dao.get_anni()

    def get_brands(self):
        return self.product_dao.get_brands()

    def get_all_retailers(self):
        return self.retailer_dao.get_all_retailers()


    def get_all_sales(self):
        return self.sale_dao.get_all_sales()

    def find_sales_by_year(self, year):
        return self.sale_dao.find_sales_by_year(year)

    def find_products_by_brand(self, brand):
        return self.product_dao.find_products_by_brand(brand)


