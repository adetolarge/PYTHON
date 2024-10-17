favoriteColors = ["Yellow", "Green", "Red", "Blue", "Gold"]
favoriteColors.append("Brown") 
# addColors = "Silver", "Brown"
# favoriteColors.append(addColors)
favoriteColors.append("Brown") 
# favoriteColors.remove("Yellow")
favoriteColors.pop(1)
# print(favoriteColors)

numbers = [3,2,4,4,5,7,3,5,66,77,43,20,15]
numbers.sort(reverse = True)
total_sum = sum(numbers)
# print(sum(numbers))

item = input("Enter five numbers separated by commas: ").split(",")
print(f"Original List {item}")
number_to_remove = input("Enter a number to remove: ")
if number_to_remove in item:
    item.remove(number_to_remove)
    print(f"Updated list: {item}")
else:
    print(f"{number_to_remove} not found in the list.")