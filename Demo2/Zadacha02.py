# Напишете програма, която намира
# най-голямото по стойност число,
# измежду три дадени числа.

x = 56
y = 102
z = -1
if x > y and x > z:
    print("x е най-голямото и стойността е: {}".format(x))
elif y > x and y > z:
    print("y е най-голямото и стойността е: {}".format(y))
else:
    print("z е най-голямото и стойността е: {}".format(z))