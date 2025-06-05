# Creating a tuple
person = ("Alice", 30, "Engineer")
# Accessing elements
print("Name:", person[0])
print("Age:", person[1])
print("Occupation:", person[2])
# Tuples are immutable: the following line would cause an error if uncommented
# person[1] = 31
# Tuple unpacking
name, age, occupation = person
print("\nUnpacked:")
print("Name:", name)
print("Age:", age)
print("Occupation:", occupation)
# Tuple with one element (note the comma)
single_element = (42,)
print("\nSingle-element tuple:", single_element)
# Nested tuples
location = ("New York", (40.7128, -74.0060))
print("\nCity:", location[0])
print("Coordinates:", location[1])
# Looping through a tuple
print("\nLooping through person tuple:")
for item in person:
    print(item)
