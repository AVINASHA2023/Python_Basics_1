class Person:
    c = "2.Child"
    def parent(self,a,b):
      print(a,"\n",b)

# Derived Class (Child)
class Student(Person):
  def child(self):
      print(self.c)

x = Student()
x.parent("Single Inheritance Example","1.Parent")
x.child()