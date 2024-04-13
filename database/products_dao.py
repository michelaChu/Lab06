from database.DB_connect import DBConnect
from model.product import Product


class ProductsDao:

    @staticmethod
    def get_product(product_number) -> Product | None:
        """
        Function that reads all the products in the database and returns them as a set.
        :param product_number: the identification number of the product we want to retrieve.
        :return: a set of products or None if there are connection errors
        """
        cnx = DBConnect.get_connection()
        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT gp.*
                    FROM go_products gp
                    WHERE Product_number =%s"""
            cursor.execute(query, (product_number,))
            row = cursor.fetchone()
            row_product = Product(row["Product_number"],
                                    row["Product_line"],
                                    row["Product_type"],
                                    row["Product"],
                                    row["Product_brand"],
                                    row["Product_color"],
                                    row["Unit_cost"],
                                    row["Unit_price"])
            cursor.close()
            cnx.close()
            return row_product
        else:
            print("Errore nella connessione")
            return None

    # @staticmethod
    # def get_products(products_map) -> set[Product] | None:
    #     """
    #     Function that reads all the products in the database and returns them as a set.
    #     :param products_map: an identity map to store all products in the database.
    #     :return: a set of products or None if there are connection errors
    #     """
    #     cnx = DBConnect.get_connection()
    #     if cnx is not None:
    #         cursor = cnx.cursor(dictionary=True)
    #         query = """SELECT *
    #             FROM go_products"""
    #         cursor.execute(query)
    #         result = set()
    #         for row in cursor.fetchall():
    #             row_product = Product(row["Product_number"],
    #                                   row["Product_line"],
    #                                   row["Product_type"],
    #                                   row["Product"],
    #                                   row["Product_brand"],
    #                                   row["Product_color"],
    #                                   row["Unit_cost"],
    #                                   row["Unit_price"])
    #             result.add(row_product)
    #             products_map[row_product.product_number] = row_product
    #         cursor.close()
    #         cnx.close()
    #         return result
    #     else:
    #         print("Errore nella connessione")
    #         return None

    @staticmethod
    def get_brands() -> list[tuple[str]]:
        """
        Function that reads the brands present in the database and returns them.
        :return: a collection of brands. It returns None if there are connection errors.
        """
        cnx = DBConnect.get_connection()
        if cnx is not None:
            cursor = cnx.cursor()
            query = """SELECT DISTINCT gp.Product_brand
                FROM go_products gp"""
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()
            cnx.close()
            return rows
        else:
            print("Errore nella connessione")
            return None
