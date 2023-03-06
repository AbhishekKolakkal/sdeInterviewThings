class A:

  def __init__(self, x, y):

    self.x = x
    self.y = y

  def __str__(self):  
    return 1
  def __eq__(self, other):

    return self.x * self.y == other.x * other.y

# obj1 = A(9, 8)
# obj2 = A(8, 9)
# print(obj1.__eq__())
# print(obj1 == obj2)



import datetime

mydate = datetime.datetime.now()

# print("__str__() string: ", mydate.__str__())
# print("str() string: ", str(mydate))

# print("__repr__() string: ", mydate.__repr__())
# print("repr() string: ", repr(mydate))

class AI:
    def check(self):
        return "AI's check"
    def display(self):
        print(self.check(),end=" ")

class ML(AI):
    def check(self):
        return "ML's check"

# AI().display()
# ML().display()

class Player:
  # class variables
  club = 'United'
  sport = 'Football'

  def __init__(self, name):
    # Instance variable
    self.name = name

  def show(self):
    print('Name:', self.name, 'Club:', self.club, 'Sports:', self.sport, end=" ")

# p1 = Player('Sanjay')
# p1.club = 'Real Madrid'
# p1.show() # Name: Sanjay, R

# p2 = Player('Ravi')
# p2.sport = 'Tennis'
# p2.show()

class Student:
    def __init__(self,roll,marks):
        self.roll = roll
        self.marks = marks
    def display(self):
        print('Roll:', self.roll,'Marks:',self.marks, end=" ")

student1 = Student(34,'A')
student1.age = 17
# print(student1.display(), 'Age:',student1.age)

class fruits:
    def __init__(self, price):
        self.price = price

obj=fruits(50)
obj.quantity=10
obj.bags=2

print(obj.quantity+len(obj.__dict__))
print(obj.__dict__)