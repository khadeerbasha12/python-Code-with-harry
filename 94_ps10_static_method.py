class Employee:
    company="Google"

# we should use the self object to runn or else we should use @staticmethod without giving self as argument
    # def greet(self):
    #     print("good morning")

    @staticmethod   #---> we can create a static method like this in python like java
    def greet():
        print("good morning")

khadeer =Employee()
khadeer.greet()