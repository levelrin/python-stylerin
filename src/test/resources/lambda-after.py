def add(x, y):
    return x + y


add_lambda = lambda x, y: x + y
print("Using def function:", add(5, 3))
print("Using lambda function:", add_lambda(5, 3))
