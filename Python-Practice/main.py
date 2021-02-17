# import cv2
# import math
# print("Hello World")
# age=9
# if age<10:
#     print("Hello")

# print(math.gcd(3, 6))

# # a=5
# # b="Sagar"
# # print(a+b)

# print(type(age))

# # Type casting
# num = 30
# print(type(num))
# str = str(num)
# print(type(str))
# print(str)

# # multiline string
# name = '''This is a 
# multiline string'''
# print(name)

# To print numbers from 1 to 1000

# for num in range(1,10):
#     print(num)

def sum(a, b):
    return a+b

print(sum(5,6))

class Dog():
    
    def __init__(self, dog_breed, dog_name, dog_spots): # Constructor
        self.breed=dog_breed
        self.name=dog_name
        self.spots=dog_spots

mydog=Dog("lab", "tucker", False)
print(mydog.breed)

a = input("Enter the number : ")
print(a)