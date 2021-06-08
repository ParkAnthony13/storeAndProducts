from products import *

class Store:
    def __init__(self,name):
        self.name = name
        self.listOfProducts = []

    def add_product(self, name, price, category):
        self.new_product = Product(name,price,category)
        self.listOfProducts.append(self.new_product)
        return self
    
    def product_line(self):
        print("Start of Product Line")
        for i in range(0,len(self.listOfProducts)):
            self.listOfProducts[i].print_info()
            print(f"ID # : {i}")
        print("End of Product Line")
        return self
    
    def sell_product(self, id):
        self.listOfProducts.pop(id)
        return self

    def inflation(self,percent_change):
        for i in range(0,len(self.listOfProducts)):
            self.listOfProducts[i].update_price(percent_change, is_increased = True)
        return self
    
    def set_clearance(self, category, percent_change):
        for i in range(0,len(self.listOfProducts)):
            if self.listOfProducts[i].category == category:
                self.listOfProducts[i].update_price(percent_change, is_increased = False)
        return self