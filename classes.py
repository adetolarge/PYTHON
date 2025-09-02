class Person:
    def __init__(self,name, age):
        self.name = name 
        self.age = age
person1 = Person('Ahmed', 20)
print(person1.name)
print(person1.age)
if(person1):
    print('person1 created')
else:
    print('person 1 not created')
class Car:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color 
    def startDriving(self):
        return f"{self.name} {self.model} {self.color} is moving"
    def stopDriving(self):
        return f"{self.name} {self.model} {self.color} stop driving"
myCar = Car('Benz', 'GLE AMG 63', 'Gold')
print(myCar.startDriving)
print(myCar.stopDriving)
#inheritance
class Student(Person):
    def __init__(self, name, age, grade, hostel):
        super().__init__(name, age)
        self.grade = grade
        self.hostel = hostel
    def studentHostel(self):
        return f"{student.name} is in {student.hostel} hostel"
student = Student('Emeka', 17, 'SS2', 'Block 2')
print(student.studentHostel)
