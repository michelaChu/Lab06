from database.DB_connect import DBConnect
from model.sale import Sale


class SalesDao:

    @staticmethod
    def get_years() -> list[tuple[int]] | None:
        """
        Function that reads the database and returns the years in which there are sales
        return: a collection containing the years (empty, if there are no years). It returns None
        if there are errors with the connection
        """
        cnx = DBConnect.get_connection()
        if cnx is not None:
            cursor = cnx.cursor()
            query = """SELECT DISTINCT YEAR(gds.Date)
                FROM go_daily_sales gds"""
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()
            cnx.close()
            return rows
        else:
            print("Errore nella connessione")
            return None

    @staticmethod
    def get_sales() -> list[Sale] | None:
        """
            Function that reads the database and returns the sales.
            :param sales_map: an identity map used to store all the sales
            :return: a collection containing sales retrieved from the database. It returns None if
            there are connection errors
        """
        cnx = DBConnect.get_connection()
        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT gds.*
                FROM go_daily_sales gds"""
            cursor.execute(query)
            result = []
            for row in cursor:
                row_sale = Sale(row["Date"],
                                row["Quantity"],
                                row["Unit_price"],
                                row["Unit_sale_price"],
                                row["Retailer_code"],
                                row["Product_number"],
                                row["Order_method_code"])
                result.append(row_sale)
            cursor.close()
            cnx.close()
            return result
        else:
            print("Errore nella connessione")
            return None
