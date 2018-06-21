


# class User(object):
#     name = "Anna"
# anna = User()
# print "anna's name: ", anna.name
# User.name = "Bob"
# print "anna's name after change:", anna.name
# bob = User()
# print "bob's name:", bob.name

# declare a class and give it name User
# class Bike(object):
    # the __init__ method is called every time a new object is created
    # def __init__(self, price, max_speed, miles):
        # set some instance variables. just like any variable we can call these anything
        # self.price = price
        # self.max_speed = max_speed
        # self.miles = 0
    # this is a method we created to help a user login
    # def ride(self):
    #     self.miles = self.miles + 10
    #     print " Riding "
    #     return self

    # def reverse(self):
    #     self.miles = self.miles - 5
    #     print " Reversing "
    #     return self    

    # def displayInfo(self):
    #     print self.price + " is the price."
    #     print self.max_speed + " is the maximum speed."
    #     if self.miles < 1:
    #         self.miles = 0
    #     else:    
    #         pass
    #     print str(self.miles) + ": miles ridden."
    #     return self

#now create an instance of the class
# bike_1 = Bike("400","20 kph", 0)
# print bike_1.price
# print bike_1.max_speed
# bike_1.ride().ride().ride().displayInfo()
# print '*'*45
# bike_2 = Bike("200","2 kph", 0)
# print bike_1.price
# print bike_1.max_speed
# bike_2.reverse().reverse().reverse().displayInfo()

# Assignment: CAR
# class Car(object):
#     def __init__(self, price, speed, fuel, mileage):
#         self.price = price
#         self.speed = speed
#         self.fuel = fuel
#         self.mileage = mileage

#     def tax(self):
#         if self.price > 10000:
#             self.tax = 0.15
#             self.price = self.price * 1.15
#         else:
#             self.tax = 0.12
#             self.price = self.price * 1.12
#         return self

#     def display_all(self):
#         print "Price: " + str(self.price)
#         print "Speed: " + str(self.speed) + "mph"
#         print "Fuel: " + self.fuel
#         print "Mileage: " + str(self.mileage) + "mpg"  
#         print "Tax Rate: " + str(self.tax)       

# car_1 = Car(8000, 40, "gas, full", 45)
# car_1.tax().display_all()
# print '***' * 8
# car_2 = Car(12000, 65,"diesil, 3/4 full", 24)    

# dojo car solution

# class Car(object):
#     def __init__(self, price, speed, fuel, mileage):
#         self.speed = speed 
#         self.fuel = fuel
#         self.mileage = mileage
#         self.price = price
#         if price > 10000:
#            self.tax = .15
#         else:
#             self.tax = .12
#         self.display_all()

#     def display_all(self):
#         print 'Price: ' + str(self.price)
#         print 'Speed: ' + str(self.speed) + 'mph'
#         print 'Fuel: ' + self.fuel
#         print 'Mileage: ' + str(self.mileage) + 'mpg'
#         print 'Tax: ' + str(self.tax)
        
# car1 = Car(2000, 35, 'Full', 15)
# car2 = Car(2000, 5, 'Not Full', 105)
# car3 = Car(2000, 15, 'Kind of Full', 95)
# car4 = Car(2000, 25, 'Full', 25)
# car5 = Car(2000, 45, 'Empty', 25)
# car6 = Car(20000000, 35, 'Empty', 15)     
#  ---------------------------------------

class Product(object):
    def __init__(self, price, item_name, weight, brand, status = "for sale"):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = status

    def add_tax(self, tax = 0.0108):
        self.tax = tax
        self.price = self.price*self.tax + self.price
        return self

    def return_item(self, return_reason):
        self.return_reason = return_reason
        if self.return_reason == "defective":
            self.status = "defective"    
            self.price = 0
        if self.return_reason == "in box":
            self.status = "for sale"
        if self.return_reason == "opened":
            self.status = "used"
            self.price = self.price * .8
        return self

    def display_all(self):      
        print str(self.price) + " is the current price."
        print str(self.item_name) + " is the item."
        print str(self.weight) + "lbs is the packaged weight."
        print str(self.brand) + " is the brand name. "
        print str(self.status) + " is the current item status."

item_1 = Product(40, "sweater", 6, "abueg","for sale")
item_1.display_all()
print '*'*40
item_1.add_tax().return_item("in box").display_all()
print '*'*40

item_2 = Product(20, "tee-shirt", 2.5, "hanes","for sale")
item_2.display_all()
print '*'*40
item_2.add_tax().return_item("defective").display_all()
print '*'*40

# item_3 = Product(400, "shoes", 7, "nike","for sale")
# item_3.display_all()
# print '*'*40
# item_3.add_tax().return_item("opened").display_all()


class Store(object):
    def __init__(self,products,location,owner):
        self.products = products
        self.location = location
        self.owner = owner

    def add_products(self, product_name):
        self.products.append(product_name)
        return self

    def remove_products(self, remove_item):
        self.products.remove(remove_item)
        return self

    def inventory(self):
        print self.products
        return self

# store_1 = Store(["shirt","pants","socks"],"Seattle", "Jose")
# print store_1.products
# store_1.inventory()
# store_1.add_products("blue tie").inventory()
store_2 = Store(["mesas","platos","tazo"],"Tamarindo", "Alejandra")

store_2.add_products("sillas").add_products("camas").add_products("vasos").inventory()

store_2.remove_products("mesas").inventory()



