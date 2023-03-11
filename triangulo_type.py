# Read input values as floats and store them in a list
a, b, c = map(float, input().split())

# Sort the values in descending order
sides = sorted([a, b, c], reverse=True)

# Check if it's possible to form a triangle
if sides[0] >= sides[1] + sides[2]:
    print("NAO FORMA TRIANGULO")
else:
    # Check for right angle triangle
    if sides[0]**2 == sides[1]**2 + sides[2]**2:
        print("TRIANGULO RETANGULO")

    # Check for obtuse angle triangle
    if sides[0]**2 > sides[1]**2 + sides[2]**2:
        print("TRIANGULO OBTUSANGULO")

    # Check for acute angle triangle
    if sides[0]**2 < sides[1]**2 + sides[2]**2:
        print("TRIANGULO ACUTANGULO")

    # Check for equilateral triangle
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    # Check for isosceles triangle
    elif a == b or b == c or a == c:
        print("TRIANGULO ISOSCELES")
