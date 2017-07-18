class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):
    def __init__(self,name):
        # A Dog has-a Name
        self.name=name

## Cat is-a Animal
class Cat(Animal):
    def __init__(self,name):
        ## A Cat has-a Name
        self.name=name

## Person is a object
class Person(object):
    def __init__(self,name):
        ##Person has-a Name
        self.name=name
        
        ##Person has-a Pet
        self.pet=None

##Employee is-a Person
class Employee(Person):
    def __init__(self,name,salary):
        ##???
        super(Employee,self).__init__(name)
        ##Employee has-a salary
        self.salary=salary

##Fish is-a object
class Fish(object):
    pass

##Salmon is-a fish
class Salmon(Fish):
    pass

##Halibut is-a fish
class Halibut(Fish):
    pass

rover=Dog("Rover")

##satan is-a cat
satan=Cat("Satan")

##mary is-a person
mary=Person("Mary")

##mary has-a pet satan
mary.pet=satan

##frank is-a Employee
frank=Employee("Frank",120000)

##frank has-a pet rover
frank.pet=rover

##flipper is-a fish
flipper=Fish()

##crouse is-a salmon
crouse=salmon()

##harry is-a halibut
harry=Halibut()


