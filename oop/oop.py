class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def print_details(self):
        print(self.name)
        print(self.__age)


s1 = Student("Adarsh", 21)
s2 = Student("Khushi", 21)

s1.print_details()
s2.print_details()
