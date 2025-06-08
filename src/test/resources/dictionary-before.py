# Creating a dictionary
person =  { "name"  :   "Alice" , "age" :  30 , "city" :  "New York" }
# Accessing values
print("Name:", person [ "name" ] )
print("Age:", person [ "age" ] )
print("City:", person [ "city" ] )
# Adding a new key-value pair
person [ "job" ] = "Engineer"
print("Job:", person [ "job" ])
# Updating an existing value
person["age"] = 31
print("Updated Age:", person["age"])
# Removing a key-value pair
del  person["city"]
print("After removing city:" ,  person )
# Looping through keys and values
print("\nAll key-value pairs:")
for  key ,  value  in  person.items():
    print( key ,  ":" ,  value )
# Checking if a key exists
if "name"  in  person:
    print("\n'Name' key exists in the dictionary")
# Getting the value with a default fallback
print("Country:", person.get ( "country" ,  "Not specified" ) )
