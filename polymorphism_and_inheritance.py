import math

#base class for the next 2 classes
class Figure2DBaseClass:
    area = float()
    circumference = float()
    def __init__(self):
        self.area = 0
        self.circumference = 0
    def __str__(self):
        return f"2-dimensional figure"
    def give_area(self):
        return self.area
    def give_circumference(self):
        return self.circumference

#first derived class
class Rectangle(Figure2DBaseClass):
  a = float()
  b = float()
  def __init__(self):
      super().__init__()
      self.a = 0
      self.b = 0
  def __init__(self, x, y):
      super().__init__()
      self.a = x
      self.b = y
  def __str__(self):
      if self.a == self.b:
          return f"Square with side of {self.a}"
      else:
          return f"Rectangle with dimensions of {self.a} x {self.b}"
  def give_area(self):
      if self.area == 0:
          self.area = self.a * self.b
      return self.area
  def give_circumference(self):
      if self.circumference == 0:
          self.circumference = 2*self.a + 2*self.b
      return self.circumference

#second derived class
class Circle(Figure2DBaseClass):
  R = float()
  def __init__(self):
      super().__init__()
      self.R = 0
  def __init__(self, r):
      super().__init__()
      self.R = r
  def __str__(self):
      return f"Circle with radius of {self.R}"
  def give_area(self):
      if self.area == 0:
          self.area = self.R*self.R*math.pi
      return self.area
  def give_circumference(self):
      if self.circumference == 0:
          self.circumference = 2*self.R*math.pi
      return self.circumference

#------
#------
F1 = Rectangle(5,5)
F2 = Rectangle(12,3)
F3 = Circle(8)
print(F1)
print(F2)
print(F3)
ar2 = F2.give_area()
cm2 = F2.give_circumference()
ar3 = F3.give_area()
cm3 = F3.give_circumference()
print("Rectangle's area is " + str(ar2))
print("Circle's circumference is " + str(cm3))