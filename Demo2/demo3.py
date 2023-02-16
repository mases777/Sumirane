''''name = input('Enter name= ')
print('Hello, ', end='')
print(name, end='!\n')

num1, num2, num3 = map(int, input().split())
print(num1 + num2 + num3)

first_name = input()
last_name = input()
age = int(input())
town = input()

print('You are {0} {1}, a {2}-years old person from {3}.'
      .format(first_name, last_name, age, town))'''''

print(2 ** 64)

width = 5
height = 7
print('width =', width, '; height =', height, '; area =', width * height)