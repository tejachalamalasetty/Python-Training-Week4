#zip() combines two or more iterables element by element.

names = ["Teja","Komal","Gopal"]
ages = ["21","20","21"]
cities = ["Machilipatnam","Hyderabad","Kakinada"]

for name, age, city in zip(names, ages, cities):
    print(name, age, city)
