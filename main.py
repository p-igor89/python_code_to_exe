# BMI calculation software
print("Hi, and welcome to BMO calculation software!")

height = float(input("What's you height in centimeters? : "))
weight = float(input("What's you weight in kilograms? : "))
print('')

bmi = float("{0:.2f}".format(weight / ((height / 100) * (height / 100))))
print("Your BMI(Body Mass Index) is " + str(bmi))

input()
