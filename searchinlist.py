# Take input for the list from the user
list_input = input("Enter the elements of the list separated by spaces: ")
# Convert the input string to a list of integers
my_list = list(map(int, list_input.split()))

# Take input for the target element from the user
target = int(input("Enter the element to search for: "))

# Variable to track if the element is found
found = False

# Loop through the list
for index in range(len(my_list)):
    if my_list[index] == target:
        print(f"Element {target} found at index {index}.")
        found = True
        break

# If the element is not found
if not found:
    print(f"Element {target} not found in the list.")
