from dataclasses import dataclass
from database.DB_connect import DBConnect
from model.sale import Sale

@dataclass
class SaleDao:
    def get_anni(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select distinct(year(date)) as year
                    from go_daily_sales"""
        cursor.execute(query)

        result = []
        for row in cursor:
            result.append(row["year"])

        cursor.close()
        cnx.close()
        return result

    def get_all_sales(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select *
                    from go_daily_sales
                    """
        cursor.execute(query)

        result = []
        for row in cursor:
            result.append(Sale(row["Retailer_code"], row["Product_number"], row["Order_method_code"], row["Date"],
                               row["Quantity"], row["Unit_price"], row["Unit_sale_price"]))

        cursor.close()
        cnx.close()
        return result

    def find_sales_by_year(self, year):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select *
                    from go_daily_sales
                    where year(date) = %s"""
        cursor.execute(query, (year,))

        result = []
        for row in cursor:
            result.append(Sale(row["Retailer_code"], row["Product_number"], row["Order_method_code"], row["Date"],
                               row["Quantity"], row["Unit_price"], row["Unit_sale_price"]))

        cursor.close()
        cnx.close()
        return result



