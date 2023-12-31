class Product:
    def __init__(self,price):
        self.price = price

    @property    
    def price(self):
        return self.__price
    

    #imp if we  dont add the setter then we cant change the value in future
    @price.setter
    def price(self,value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value

    # price = property(get_price,set_price)


product = Product(-50)
product.price = -1
print(product.price)
