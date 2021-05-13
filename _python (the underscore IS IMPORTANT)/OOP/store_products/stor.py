from Store_Products import KKK


class Store:
    def __init__(self,name,list_of_products=[]):
        self.name = name
        self.list_of_products = list_of_products
    def add_product(self, new_product):
        self.list_of_products.append(new_product)
        return self.list_of_products
    def sell_product(self, product):
        if type(product) == int:
            self.list_of_products.pop(product)
            self.list_of_products.pop(product).print_info()
        else:
            self.list_of_products.remove(product)
            self.list_of_products.remove(product).print_info()
    def inflation(self, percent_increase):
        for i in self.list_of_products:
            i.update_price(percent_increase,is_increased = True)
    def set_clearance(self, category, percent_discount):
        for i in self.list_of_products:
            if i.category == category:
                i.update_price(percent_discount,is_increased = False)
    def stack(self,product):
        return self.list_of_products.count(product)
    def display_products(self):
        for i in KKK.list_of_products:
            i.print_info()
