class Parent:
    def __init__(self,propertyValue,carValue,parentName):
        self.property = propertyValue
        self.cars = carValue
        self.nameOfParent = parentName

    def display_information(self):
        print("property:",self.property,"car:",self.cars)



class Child(Parent):
    def __init__(self,parentName,propertyValue,carValue,childName):
        super().__init__(parentName, propertyValue, carValue)
        self.childName = childName




deborah = Child("Thomas Kogolo","villa","tesla","Deborah Kogolo")

deborah.display_information( )
print(deborah.childName)
#clsp1 = Parent("house","BMW")
