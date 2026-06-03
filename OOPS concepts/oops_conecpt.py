#in this we are going to learn about the oops concept

#class is created using the class keyword

class StarCookie:
    pass

#to create an empty class we have to 'pass' in the class

STAR_COOKIE = StarCookie() #object creation

print(STAR_COOKIE)


#we can provide attributes to our objects using . notation after the object
STAR_COOKIE.weight = 15
STAR_COOKIE.colour = 'red'
print(STAR_COOKIE.weight)
print(STAR_COOKIE.colour)


#to create the object in a python class we have to initalize the initialzer
#we can do that by using the in-built function __init__ function

class Game:
    def __init__(self):
        print("maxpayne is the og game")


Game_Class = Game()
print(Game_Class)

#attrubute
class Starcokkie:
    def __init__(self, color):   #passed color as the attribute here
        self.color = color

my_cokkie_1 = Starcokkie("red")
print(my_cokkie_1)#give the stored location
print(my_cokkie_1.color)#gives the actual value


#We can also create methods
class Youtube:
    def __int__(self,users,subscribers = 0, subscriptions = 0):
        self.subscriptions = subscriptions
        self.users = users
        self.subscribers = subscribers

    #method
    def subscribe(self, users):
        users.subsribers += 1
        self.subscriptions += 1














