print("---------------------------------------------")
fruit=["apple","banana","kiwi","cherry","orange"]
print(fruit)
print(f"the first fruit element is{fruit[0]}")
print(f"the last fruit element is{fruit[-1]}")
fruit[1]="mango"
print(fruit)
fruit.insert(2,"watermelon")
print(fruit)
print("----------------------------------------")
a=input("enter fruit name").lower()
if a in fruit:
    print("it is on the list")
else:
    print("sorry this fruit is not on the list  ")
print("here is the sorted list")
fruit.sort()
print(fruit)
print("----------------------------------------")
