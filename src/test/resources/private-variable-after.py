class MyClass:

    def __init__(self):
        self.public_var = "I'm public"
        self.__private_var = "I'm private"

    def show_vars(self):
        print("Inside class:")
        print("Public:", self.public_var)
        print("Private:", self.__private_var)

    def get_private_var(self):
        return self.__private_var

# Create an instance
obj = MyClass()
# Accessing public variable (works)
print("Outside class:")
print("Public:", obj.public_var)
# Accessing private variable directly (will raise an AttributeError)
try:
    print("Private:", obj.__private_var)
except AttributeError as e:
    print("Error accessing private_var directly:", e)
# Accessing private variable using name mangling (not recommended)
print("Private (via name mangling):", obj._MyClass__private_var)
# Proper way to access private variable: use a method
print("Private (via method):", obj.get_private_var())
