# from  turtle import Turtle, Screen
#
#
# timmy = Turtle()
# print(timmy)
# my_screen = Screen()
# print(my_screen)
# timmy.shape("turtle")
# timmy.color("coral")
# print(timmy.position())
# timmy.forward(100)
#
# print(my_screen.canvheight)
# my_screen.exitonclick()

# from prettytable import PrettyTable
# table = PrettyTable()
# table.add_column("Pokemon Name",["X","Y","Z"])
# table.add_column("Type",["X","Y","Z"])
# table.align = "l"
# print(table)

class Dog:
    def __init__(self):
        self.temparment = "loyal"

    def bark(self):
        print("Woof")

class Lavender(Dog):
    def __init__(self):
        self.temparment = "Friendly"       


dog = Lavender()
dog.bark()        