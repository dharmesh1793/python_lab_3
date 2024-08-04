# Define the classes
class A:
    def method_a(self):
        print("Method A")

class B:
    def method_b(self):
        print("Method B")

class C(A, B):
    pass

# Create an object of class C
obj = C()

# Call methods from classes A and B
obj.method_a()
obj.method_b()