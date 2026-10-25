# to check whether or not the triangle is a right angled triangle using function
def is_right_triangle(a, b, c):
    sides = sorted([a, b, c])

    if sides[0] <= 0:
        return False

    return sides[0]**2 + sides[1]**2 == sides[2]**2


a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if is_right_triangle(a, b, c):
    print("It is a right-angled triangle")
else:
    print("It is not a right-angled triangle")
