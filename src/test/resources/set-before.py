# Demonstration of how sets work in Python
# Creating sets
fruits =  { "apple" ,  "banana" ,  "cherry" }
print("Initial set:", fruits)
# Adding elements
fruits.add("orange")
print("After adding 'orange':", fruits)
# Removing elements
# Raises KeyError if not found
fruits.remove("banana")
print("After removing 'banana':", fruits)
# Discarding elements (doesn't raise error if not found)
fruits.discard("pineapple")
print("After discarding 'pineapple' (not in set):", fruits)
# Checking membership
print("Is 'apple' in the set?", "apple"  in  fruits)
print("Is 'grape' in the set?", "grape"  in  fruits)
# Set operations
set_a = { 1 ,  2 ,  3 ,  4 }
set_b = { 3 ,  4 ,  5 ,  6 }
print("Set A:", set_a)
print("Set B:", set_b)
# Union
print("Union (A | B):",  set_a  |  set_b )
# Intersection
print("Intersection (A & B):" ,  set_a  &  set_b )
# Difference
print("Difference (A - B):" ,  set_a  -  set_b )
# Symmetric Difference
print("Symmetric Difference (A ^ B):" ,  set_a  ^  set_b )
# Converting list to set to remove duplicates
numbers = [ 1 ,  2 ,  2 ,  3 ,  4 ,  4 ,  5 ]
unique_numbers = set ( numbers )
print("Unique numbers from list:" ,  unique_numbers )
