from dataclasses import dataclass
from database.DB_connect import DBConnect

@dataclass
class ProductDao:
    def get_brands(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select distinct(Product_brand)
                    from go_products"""
        cursor.execute(query)

        result = []
        for row in cursor:
            result.append(row["Product_brand"])

        cursor.close()
        cnx.close()
        return result

    def find_products_by_brand(self, brand):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select Product_number
                    from go_products
                    where Product_brand = %s"""
        cursor.execute(query, (brand,))

        result = []
        for row in cursor:
            result.append(row["Product_number"])

        cursor.close()
        cnx.close()
        return result
