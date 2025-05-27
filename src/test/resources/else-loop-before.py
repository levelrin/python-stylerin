numbers = [1, 3, 5, 7, 9]
target = 4
for num in numbers:
    if num == target:
        print(f"Found the target number: {target}")
        break
else  :
      print(f"Target number {target} not found in the list.")
index = 0
while index < len(numbers):
    if numbers[index] == target:
        print(f"Found the target number: {target}")
        break
    index += 1
else  :
      print(f"Target number {target} not found in the list.")
