#enumerate() returns both the index and the value while looping.

fruits = ["apple","banana","mango"]

for index,fruit in enumerate(fruits,start=2):
    print(index,fruit)
