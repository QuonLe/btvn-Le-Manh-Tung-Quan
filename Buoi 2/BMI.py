H=int(input("Give me your height(cm)"))/100
W=int(input("Give me your weight(kg)"))

BMI = W / ( H * H )

if BMI < 16:
    print("Severely underweight")
elif 16 <= BMI <18.5:
    print("Underweight")
elif 18.5 <= BMI < 25:
    print("Normal")
elif 25 <= BMI <30:
    print("Overweight")
else:
    print("Obese")




