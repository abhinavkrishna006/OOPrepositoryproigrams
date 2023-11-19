import math

def hexagon_area(side_length):
    # Calculate the area of a regular hexagon
    area = (3 * math.sqrt(3) / 2) * side_length**2
    return area

# Example usage:
side_length = 5  # Replace with the length of your hexagon's side
area = hexagon_area(side_length)
print(f"The area of the regular hexagon with side length {side_length} is: {area}")
