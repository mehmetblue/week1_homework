"""
The parameter that shows whether a person's weight is normal for their height is called Body Mass Index.
In short, if we divide a person's weight by the square of the person's height, the body mass index is obtained.
The result obtained by taking the weight and height from the user;
     if it is below 25 print a warning as NORMAL,
     If it is between 25-30 print a warning as OVER WEIGHT,
     if it is between 30-40 print a warning as OBESE,
     If it is 40 and above print a warning as OVERFAT.
"""
height = float(input("Please Type Your Height (m): "))
weight = float(input("Please Type Your Weight (kg): "))
bmi = round(weight / (height**2), 2)

if bmi < 25:
    print("NORMAL")
elif 25 <= bmi <= 30:
    print("OVERWEIGHT")
elif 30 <= bmi <= 40:
    print("OBESE")
else:
    print("OVERFAT")