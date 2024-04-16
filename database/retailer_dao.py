from dataclasses import dataclass
from database.DB_connect import DBConnect
from model.retailer import Retailer

@dataclass
class RetailerDao:
    def get_all_retailers(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select *
                    from go_retailers """
        cursor.execute(query)

        result = []
        for row in cursor:
            result.append(Retailer(row["Retailer_code"], row["Retailer_name"], row["Type"], row["Country"]))

        cursor.close()
        cnx.close()
        return result

