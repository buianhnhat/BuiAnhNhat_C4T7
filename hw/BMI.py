print ("Do you want to know your BMI(Body Mass Index)? Type your weight(kg) and height(cm)!")
m = int (input("Weight = "))
h = float (input("Height = "))
h = h/100
bmi = m/(h*h)
print ("BMI = ", bmi)
if (bmi>30):
    print ("Based on your BMI, you are Obese!!!")
else:
    if (bmi<25):
        if (bmi<18.5):
            if(bmi<16):
                print ("Based on your BMI, you are severely underweight!!!")
            else: print ("Based on your BMI, you are underweight!")
        else: print ("Based on your BMI, you are normal! Congratulations!")
    else: print ("Based on your BMI, you are verweight!")