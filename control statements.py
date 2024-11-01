num=int(input("Enter a number: "))
if num%2==0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")

# create a program that checks if someone can vote or not  using age above 18
age=int(input("Enter your age: "))
if age>=18:
    print(f"Your are allowed to vote")
else:
    print(f" You are under age,your are not allowed to vote")

# create a program to grade student marks

marks=int(input("Enter your marks: "))
if marks<=100 and marks>=80:
     print(f"Your scored an A")
elif marks<=79 and marks>=60:
    print(f"Your scored B")
elif marks<=59 and marks>=40:
    print(f"Your scored C")
elif marks==0 and marks<=39:
    print(f"Your failed")
else:
    print(f"Invalid marks")

# calculate BMI
def calculate_bmi(weight_kg, height_m):
    """
    Calculate BMI given weight in kilograms and height in meters.

    Args:
        weight_kg (float): Weight in kilograms
        height_m (float): Height in meters

    Returns:
        tuple: (bmi_value, category)
    """
    bmi = weight_kg / (height_m ** 2)

    # Determine BMI category
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return round(bmi, 1), category


# Example usage
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi_value, category = calculate_bmi(weight, height)
print(f"\nYour BMI is: {bmi_value}")
print(f"Category: {category}")