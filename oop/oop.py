# # Access Modifier
# #1-> Public

# class Person:
#     def __init__(self , name,age):
#         self.name = name
#         self.age = age

#     # public function to print
#     def print_details(self):
#         print(self.name);
#         print(self.age)

    


# s1 = Person("Adarsh",21)
# s1.print_details()

# ## Protected (_)
# ## Private (__)



# # Inheritance
# class Student(Person):
#     def __init__(self, name, age,roll):
#         self.name=name;
#         self.age=age
#         self.roll=roll


# s2 = Student("Adarsh",22,1)
# s2.print_details()

class Person:
    def print_details(self):
        print("I am a person")


class Student(Person):
    def print_details(self):
        print("I am a student")


class Teacher(Person):
    def print_details(self):
        print("I am a teacher")


def display(obj):
    obj.print_details()


display(Student())
display(Teacher())
