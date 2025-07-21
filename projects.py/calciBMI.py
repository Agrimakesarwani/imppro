print("Welcome to the BMI Calculator!")
print("\nEnter weight and height only in numbers : ")
weight = float(input("Enter your weight in kilograms (kg): "))
height = float(input("Enter your height in meters (m): "))
bmi = weight / (height * height)
if weight <= 0 or height <= 0:
    print("Weight and height must be positive numbers.")
elif bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
