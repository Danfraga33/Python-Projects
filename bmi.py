height = float(input("What is your height ?"))
weight = int(input('What is your weight ?'))
bmi = weight / (height**2)
if bmi < 18.5:
  print(f'Your BMI is {bmi}, you are underweight')

elif bmi > 18.5 and bmi < 35:
  print(f'Your BMI is {bmi}, you are normal')

else: 
  print(f'Your BMI is {bmi}, not looking good')
