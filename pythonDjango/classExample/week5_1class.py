
# google = {
#     'chairs': True,
#     'num_of_chairs':10,
#     'desk':True,
#     'num_of_desk':3,
#     'computers':True,
#     'num_of_computers':20,
#     'employees':['Ray','Nicci','Oliver','Ashton','Maya']
# }
# print google["chairs"]

# class Office(object):
#     def __init__(self, chairs, num_of_chairs,desk,num_of_desk,computers,num_of_computers,employees):
#         self.chairs = chairs
#         self.num_of_chairs = num_of_chairs
#         self.desk = desk
#         self.num_of_desk = num_of_desk
#         self.computers = computers
#         self.num_of_computers = num_of_computers
#         self.employees = employees

#     def print_emp(self):
#         print self.employees
#parent class
class decoration(object):
    def __init__(self, decor_type):
        self.decor_type = decor_type
    def print_type(self):
        print self.decor_type

#child class
class chair(decoration):
    def __init__(self, decor_type, num_of_legs, color, comfort):
        super(chair, self).__init__(decor_type)
        self.num_of_legs = num_of_legs
        self.color = color
        self.comfort = comfort
    def print_type(self):
        super(chair, self).print_type()
        print self.num_of_legs
        print self.color
        print self.comfort
        return self


chair1 = chair("furniture", 3, "blue", "high")
print chair1.decor_type  
chair1.print_type()

chair2 = chair("bed", 6, 'white', 'low')
print chair2
x = chair2.print_type().color
print x



# google = Office(True, 10, True, 3, True, 20,['Ray','Nicci','Oliver','Ashton','Maya'])
# amazon = Office(True, 10, True, 3, True, 20,['Ray','Nicci','Oliver','Ashton','Maya'])
# amazon.print_emp()
# print google.chairs