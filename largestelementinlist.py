def find_largest_element(lst):
    if not lst:
        return "The list is empty."

    # Initialize the largest element with the first element of the list
    largest_element = lst[0]

    # Iterate through the list to find the largest element
    for element in lst:
        if element > largest_element:
            largest_element = element

    return f"The largest element in the list is: {largest_element}"

# Example usage:
my_list = [10, 5, 7, 22, 15, 3, 18]
result = find_largest_element(my_list)
print(result)
