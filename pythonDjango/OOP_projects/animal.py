class Animal(object):
    def __init__(self,animal_name):
        self.animal_name = animal_name
        self.animal_health = 100

    def walk(self):
        self.animal_health -= 1
        return self

    def run(self):
        self.animal_health -= 5
        return self

    def health(self):
        print "I am a " + self.animal_name
        if self.animal_health < 1:
            print self.animal_name + " : has met an untimely end."
        else:    
            print "Animal health: " + str(self.animal_health) 
        return self
cat = Animal("cat")
cat.health()
print "*"*25
cat.walk().walk().run().health()
print "*"*25
cat.run().run().health()

class Dog(Animal):
    def __init__(self,animal_name):
        super(Dog, self).__init__(animal_name) 
        self.animal_health = 150

    def pet(self):
        self.animal_health += 5
        print self.animal_health
        return self

dog = Dog('Chewy')
dog.pet().pet()
dog.pet().pet().health()

# EXAMPLE-----------------
# class Animal(object):
#     def __init__(self, name):
#         self.name = name
#         self.health = 100

#     def walk(self):
#         self.health -= 1
#         return self
    
#     def run(self):
#         self.health -= 5
#         return self
    
#     def displayHealth(self):
#         print 'My name is: ' + self.name
#         print 'I have: ' + str(self.health) + ' health'

# animal = Animal('Cosmo')
# animal.walk().walk().walk().run().run().displayHealth()

# class Dog(Animal):
#     def __init__(self, name):
#         super(Dog, self).__init__(name)
#         self.health = 150

#     def pet(self):
#         self.health += 5
#         return self

# dog = Dog('Snoopy')
# dog.walk().walk().walk().pet().displayHealth()

# class Dragon(Animal):
#     def __init__(self, name):
#         super(Dragon, self). __init__(name)
#         self.health = 170

#     def fly(self):
#         self.health -= 10
#         return self
    
#     def displayHealth(self):
#         print 'I am a Dragon'
#         super(Dragon, self).displayHealth()

# dragon = Dragon('ToothLess')
# dragon.fly().displayHealth()

# class Fish(Animal):
#     def __init__(self, name):
#         super(Fish, self).__init__(name)
#         self.health = 180

#     def swim(self):
#         self.health += 10
#         return self
    
#     def displayHealth(self):
#         print 'I am ' + self.name
#         print 'I have: ' + str(self.health) + ' health'

# fish = Fish('Dory')
# fish.swim().swim().swim().displayHealth()


#solution
# Create a class Animal

class Animal(object):
    def __init__(self, name):
        self.health = 100
        self.name = name

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print 'My name is: ' + self.name
        print 'I have: ' + str(self.health) + ' health'

animal = Animal('Garfield')
animal.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
    def __init__(self,name):
        super(Dog, self).__init__(name)
        self.health = 150
        
    def pet(self):
        self.health += 5
        return self

dog = Dog('Odie')
dog.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170

    def fly(self):
        self.health -= 10
        return self

    def displayHealth(self):
        print "This is a dragon"
        super(Dragon, self).displayHealth()

dragon = Dragon('Nightwing')
dragon.fly().displayHealth()
