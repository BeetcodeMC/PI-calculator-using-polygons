import math

def calculate_pi(n):
    # Initialize variables to store the sides of the polygons and their corresponding perimeters
    sides = []
    perimeters = []

    # Initialize the radius of the circle
    radius = 1.0

    for i in range(3, n + 1):
        # Calculate the angle in radians for each vertex of the polygon
        angle = 2 * math.pi / i

        # Calculate the side length of the polygon using trigonometry
        side_length = 2 * radius * math.sin(angle / 2)

        # Calculate the perimeter of the polygon
        perimeter = i * side_length

        # Append the number of sides and the corresponding perimeter to the lists
        sides.append(i)
        perimeters.append(perimeter)

    # Calculate pi using the perimeters of the polygons
    pi_approximation = perimeters[-1] / (2 * radius)

    return pi_approximation, sides, perimeters

# Specify the number of sides for the polygon (increase for higher precision)
n = 100000000000000000000000000000000000000
pi_approximation, _, _ = calculate_pi(n)
print(f'Approximation of π: {pi_approximation:.100f}')