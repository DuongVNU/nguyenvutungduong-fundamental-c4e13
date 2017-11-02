weight = float(input("Enter your weight (kg) = "))
height = float(input("Enter your height (cm) = "))
height = height / 100
bmi = weight / ( height * height )
if bmi < 16:
    print("Severely underweight")
elif bmi >= 16 and bmi <= 18.5:
    print("underweight")
elif bmi >= 18.5 and bmi <= 25:
    print("Normal")
elif bmi >= 25 and bmi <= 30:
    print("Overweight")
elif bmi > 30:
    print("Obese")
