# weight = 85
# height = 1.85

print("BMI CALCULATOR")

weight = float(input("\nWeight: \n"))
height = float(input("\nHeight: \n"))

bmi = weight / (height ** 2)

print(f"\nBMI: {round(bmi, 2)}")
if bmi < 18.5:
    print("underweight")
elif bmi >= 18.5 and bmi < 25:
    print("normal weight")
elif bmi >= 25:
    print("overweight")

