class Car:              # (object class)
    CONT_MANUF = ("ASIA", "AFRICA", 'AMERICA', "EUROPE", "AUSTRALIA")
    __carlist = None

    # class method
    @classmethod
    def get_cont(cls):
        return cls.CONT_MANUF

    # static method
    def getcarlist():
        if Car.__carlist == None:
            Car.__carlist == []
        return Car.__carlist

    # (instance methods, instance attributes)
    def __init__(self, make, model, category, price, cont):
        self.make = make
        self.model = model
        self.category = category
        self.price = price
        self.__secret = "Secret attribute"

        if (not cont in Car.CONT_MANUF):
            raise ValueError (f"{cont} is not a valid manufacturing continent")
        else:
            self.cont = cont

    def get_price(self):
        if hasattr(self, '_discount'):
            return self.price - (self.price * self._discount)
        return self.price

    def set_discount(self, amount):
        self._discount = amount

# Car attribute
print("Manufacturing continent: ", Car.get_cont())

# Car instances
car1 = Car('Skoda', 'Superb Combi', 'SUV', 156900, 'EUROPE')
car2 = Car('Skoda', 'Fabia', 'CUV', 71850, "EUROPE")
# car3 = Car('Skoda', 'Fabia', 'CUV', 71850, "Antarctica")

# print(car1.get_price())
# print(car2.get_price())
# car1.set_discount(.12)
# print((car1.get_price().__ceil__()))

thecar = Car.getcarlist()
thecar.append(car1)
thecar.append(car2)
print(thecar)


