class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def display(self):
        print(self.name,"Pass" if self.marks>=40 else "Fail")

s=Student("Rahul",76)
s.display()