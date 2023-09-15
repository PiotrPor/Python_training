class Rectangle:
  def __init__(self):
    self.a = 0
    self.b = 0
  def __init__(self, a, b):
    self.a = a
    self.b = b
  def __str__(self):
    return f"Rectangle with dimensions of {self.a} x {self.b}"
  def give_area(self):
    return (self.a * self.b)
  def give_circumference(self):
    return (2*self.a + 2*self.b)

#what would be done in "main()"
AA = Rectangle(20,15)
print(AA)
xyz = 0   #this line isn't necessary
xyz = AA.give_area()
print("Area is "+ str(xyz))
xyz = AA.give_circumference()
print("Circumference is "+ str(xyz))