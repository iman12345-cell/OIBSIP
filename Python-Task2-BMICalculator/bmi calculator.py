#Iman Mirza
#Python Programming
#Task 2 - BMI Calculator

print("BMI Calculator")

# Get weight
while True:
    try:
        weight = float(input("Enter your weight in kg: "))

        if weight < 0:
            print("Error: Weight cannot be negative. Please try again.")
        else:
            break

    except ValueError:
        print("Error: Please enter a numeric value.")


# Get height
while True:
    try:
        height = float(input("Enter your height in meters: "))

        if height < 0:
            print("Error: Height cannot be negative. Please try again.")
        elif height == 0:
            print("Error: Height cannot be zero. Please try again.")
        else:
            break

    except ValueError:
        print("Error: Please enter a numeric value.")


# Calculate BMI
bmi = weight / (height ** 2)


# Classify BMI
if bmi < 18.5:
    category = "Underweight"

elif bmi < 25:
    category = "Normal"

elif bmi < 30:
    category = "Overweight"

else:
    category = "Obese"


# Display result
print("\nYour BMI is:", round(bmi, 2))
print("Category:", category)