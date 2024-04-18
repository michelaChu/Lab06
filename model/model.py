from database.products_dao import ProductsDao
from database.sales_dao import SalesDao
from database.retailers_dao import RetailerssDao
from model import sale
from model.retailer import Retailer
from model.sale import Sale


class Model:
    def __init__(self):
        self._sales_list = SalesDao.get_sales() # list with all the sales

    ################################################################################
    ################################################################################
    #############      Metodi semplici di recupero dati dal dao   ##################
    ################################################################################
    ################################################################################
    def get_years(self):
        """
        Semplice metodo che chiede al dao gli anni delle vendite e li restituisce
        :return: una nested list di interi (gli anni delle vendite)
        """
        return SalesDao.get_years()

    def get_brands(self):
        """
            Semplice metodo che chiede al dao gli i brands dei prodotti e li restituisce
            :return: una nested list di stringhe (i brands dei prodotti)
        """
        return ProductsDao.get_brands()

    def get_retailers(self) -> set[Retailer]:
        """
            Semplice metodo che chiede al dao gli i retailers e li restituisce
            :return: un set di Retailer (i brands dei prodotti)
        """
        return RetailerssDao.get_retailers()

    ################################################################################
    ################################################################################
    ###############     Metodi che elaborano dati dal dao      #####################
    ################################################################################
    ################################################################################

    def get_filtered_sales(self, anno, brand, retailer):
        filtered_sales = []
        for listed_sale in self._sales_list:
            if ((anno is None or listed_sale.get_year() == anno)
                    and (brand is None or listed_sale.get_brand() == brand)
                    and (retailer is None or listed_sale.get_retailer() == retailer)):
                filtered_sales.append(listed_sale)
        return filtered_sales

    def get_top_sales(self, anno, brand, retailer) -> list[Sale]:
        """
            Funzione che legge dal dal dao le vendite con i filtri selezionati,
            e ne restituisce le prime 5 (se presenti) ordinate per ricavo decrescente
        """
        filtered_sales = self.get_filtered_sales(anno, brand, retailer)
        filtered_sales.sort(reverse=True)
        return filtered_sales[0:5]

    def get_sales_stats(self, anno, brand, retailer):
        """
            Funzione che legge dal dal dao le vendite con i filtri selezionati,
            e ne restituisce le prime 5 (se presenti) ordinate per ricavo decrescente
        """
        filtered_sales = self.get_filtered_sales(anno, brand, retailer)
        ricavo_totale = sum([sale.ricavo for sale in filtered_sales])
        retailers_involved = set([sale.retailer_code for sale in filtered_sales])
        product_involved = set([sale.product_number for sale in filtered_sales])
        return ricavo_totale, len(filtered_sales), len(retailers_involved), len(product_involved)
