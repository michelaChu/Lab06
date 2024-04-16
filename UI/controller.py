import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fill_dd_anno(self):
        anni = self._model.get_anni()
        self._view.dd_anno.options.append(ft.dropdown.Option("Nessun filtro"))
        for anno in anni:
            self._view.dd_anno.options.append(ft.dropdown.Option(anno))
        self._view.update_page()

    def fill_dd_brand(self):
        brands = self._model.get_brands()
        self._view.dd_brand.options.append(ft.dropdown.Option("Nessun filtro"))
        for brand in brands:
            self._view.dd_brand.options.append(ft.dropdown.Option(brand))
        self._view.update_page()

    def fill_dd_retailer(self):
        retailers = self._model.get_all_retailers()
        self._view.dd_retailer.options.append(ft.dropdown.Option("Nessun filtro"))
        for retailer in retailers:
            self._view.dd_retailer.options.append(ft.dropdown.Option(key= retailer.retailer_code,
                                                                     text=retailer.retailer_name,
                                                                     data=retailer,
                                                                     on_click=self.read_retailer))
        self._view.update_page()

    def read_retailer(self, e):
        retailer = e.control.data

    def handle_top_vendite(self, e):
        anno = self._view.dd_anno.value
        brand = self._view.dd_brand.value
        retailer = self._view.dd_retailer.value
        self._view.lst_result.clean()
        if anno is None and brand is None and retailer is None:
            self._view.create_alert("Selezionare almeno un filtro!")
            return
        sales = self._model.get_all_sales()
        if anno is not None and anno != "Nessun filtro":
            sales = self._model.find_sales_by_year(anno)
        if brand is not None and brand != "Nessun filtro":
            result = []
            products = self._model.find_products_by_brand(brand)
            for sale in sales:
                for product in products:
                    if sale.product_number == int(product):
                        result.append(sale)
            sales = result
        if retailer is not None and retailer != "Nessun filtro":
            result = []
            for sale in sales:
                if sale.retailer_code == int(retailer):
                    result.append(sale)
            sales = result
        sales.sort(key=lambda s: s.calcola_ricavo(), reverse=True)
        for sale in sales[:5]:
            self._view.lst_result.controls.append(ft.Text(sale))
        self._view.update_page()


    def handle_analizza_vendite(self, e):
        anno = self._view.dd_anno.value
        brand = self._view.dd_brand.value
        retailer = self._view.dd_retailer.value
        self._view.lst_result.clean()
        if anno is None and brand is None and retailer is None:
            self._view.create_alert("Selezionare almeno un filtro!")
            return
        sales = self._model.get_all_sales()
        if anno is not None and anno != "Nessun filtro":
            sales = self._model.find_sales_by_year(anno)
        if brand is not None and brand != "Nessun filtro":
            result = []
            products = self._model.find_products_by_brand(brand)
            for sale in sales:
                for product in products:
                    if sale.product_number == int(product):
                        result.append(sale)
            sales = result
        if retailer is not None and retailer != "Nessun filtro":
            result = []
            for sale in sales:
                if sale.retailer_code == int(retailer):
                    result.append(sale)
            sales = result
        self._view.lst_result.controls.append(ft.Text("Statistiche vendite: "))
        self._view.lst_result.controls.append(ft.Text(f"Giro d'affari: "
                                                      f"{sum(sale.calcola_ricavo() for sale in sales)}"))
        self._view.lst_result.controls.append(ft.Text(f"Numero vendite: "
                                                      f"{len(sales)}"))
        self._view.lst_result.controls.append(ft.Text(f"Numero retailers coinvolti: "
                                                      f"{len(set(sale.retailer_code for sale in sales))}"))
        self._view.lst_result.controls.append(ft.Text(f"Numero prodotti coinvolti: "
                                                      f"{len(set(sale.product_number for sale in sales))}"))
        self._view.update_page()


