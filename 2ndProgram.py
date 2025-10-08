# Input in Python
name = input("Name: ")
age = int(input("Age: "))
price = float(input("Price: "))
print(name, age, price)

# Traffic light for conditional statements
light = input("Color of light: ").lower()  # .lower() makes it case-insensitive
if light == "red":
    print("Stop")
elif light == "yellow":
    print("Look")
elif light == "green":
    print("Go")
else:
    print("Light is broken.")

# Grading sheet
marks = int(input("Marks: "))
if marks >= 90:
    print("A")
elif marks >= 80 and marks < 90:
    print("B")
else:
    print("C")
