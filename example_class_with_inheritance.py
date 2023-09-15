#this is the base class
class BaseClass:
  def __init__(self):
    self.main = 1
  def __str__(self):
    return f"Object of base class holds number {self.main}"

#this is the derived class
class Inher(BaseClass):
 def __init__(self, a):
   super().__init__()
   self.second = a
 def __str__(self):
   first = super().__str__()
   return f"{first}\nInheriting object holds number {self.second}"

# this is what program is doing
# in C or C++ it would be in "main()"
AA = BaseClass()
BB = Inher(22)
print(AA)
print("--------")
print(BB)