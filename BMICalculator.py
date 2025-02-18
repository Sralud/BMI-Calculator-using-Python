def main():
    print("🏋️ BMI Calculator 💪")

    name = input("Enter your name: ")
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in centimeters: ")) / 100


    BMI, category, message = calculateBMI(weight, height)

    print(f"\n{name}'s BMI is: {BMI:.2f}")
    print(f"Category: {category}")
    print(f"\n{message}")

def calculateBMI(weight, height):
    BMI = weight / (height ** 2)

    if BMI < 18.5:
        category = "Underweight"
        message = "You're a bit underweight. Consider a balanced diet and strength-building exercises to stay healthy! 💪🍽️"
    elif 18.5 <= BMI < 24.9:
        category = "Normal weight"
        message = "Great job! You're maintaining a healthy weight. Keep up the good habits! 🎉🥗"
    elif 25 <= BMI < 29.9:
        category = "Overweight"
        message = "You're slightly above the healthy range. Regular exercise and mindful eating can help! You've got this! 🏃‍♂️🍎"
    else:
        category = "Obese"
        message = "Health is a journey! Small steps like daily walks and nutritious meals can make a big difference. Stay strong! 💙🚀"
    return BMI, category, message

main()