# name="Faith"
# print(type(name))
# Class
# class person:
#     # class atribute(properties)
#     species = "Homo sapien"
#
# # Method are funtions defined inside a class
#     def walk(self):
#         print("is walking")
#     def sleep(self):
#         print("{}is sleeping".format(self.name))
# p1=person()
# p2=person()
# p3=person()
# p1.species
# # print(p1.species)
# p1.name = "Faith"
# p2.name = "Ann"
# p3.name = "val"
# # print(p1.name)
# # p1.age=20
# # print(p1.age)
# # p1.race = "black"
# # print(p1.race)
# # p1.origin="African"
# # print(p1.origin)
# # p1.citizenship="Kenyan"
# # print(p1.citizenship)
# p1.walk()
# p1.sleep()
#
#
# class car:
#     make="BMW"
#
# c1=car()
# c1.name="Koech's Objects"
# c2=car()
# c3=car()
# c1.year="1982"
#
#  def speed(self):
#     print("{}is moving at 60km per hr".format(self.name))
#
#     print(c1.make)
#     print(c1.year)
# c1.speed()


# Runs as soon as you create
#     def __init__(self):
#      print("I am a constructor method")
#
#      self.name="Faith"
#      self.age=26
#
# p12=person("Kivuti", 26)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)

print(p1.name)
print(p1.age)
print(p1)