import sys

def calculate_bmi(weight, height):
    height_meters = height * 0.0254  # Convert inches to meters
    bmi = weight / (height_meters ** 2)  # BMI formula
    return round(bmi, 2)

def get_body_fat_percentage(bmi, age, gender):
    if gender == 1:  # Male
        return round((1.2 * bmi) + (0.23 * age) - 16.2, 2)
    else:  # Female
        return round((1.2 * bmi) + (0.23 * age) - 5.4, 2)

def get_caloric_requirement(goal, weight_change):
    return weight_change * 7716  # 1 kg = 7716 kcal

def get_meal_calories():
    meal_options = {
        'a': {"Idli": 58, "Vada": 97, "Dosa": 74, "Pancake": 168, "Egg": 86},
        'b': {"Lemon rice": 260, "Biriyani": 144, "Pasta": 369, "Curd Rice": 210, "Chappati": 71},
        'c': {"Salad": 45, "Pav Bhaji": 400, "Steak": 515, "Quesadilla": 450, "Burrito": 206},
        'd': {"Chocolate": 546, "Pani Puri": 330, "Fries": 321, "Potato Wedges": 123, "Chips": 536},
    }

    total_calories = 0
    while True:
        meal = input("Choose a meal (a: Breakfast, b: Lunch, c: Dinner, d: Snacks, q: Quit): ").lower()
        if meal == 'q':
            break
        if meal not in meal_options:
            print("Invalid meal choice! Try again.")
            continue

        print(f"Available items: {', '.join(meal_options[meal].keys())}")
        food = input("Enter the name of the food item you ate: ").title()

        if food in meal_options[meal]:
            total_calories += meal_options[meal][food]
            print(f"Added {food} ({meal_options[meal][food]} kcal). Total so far: {total_calories} kcal")
        else:
            print("Invalid food item! Try again.")

    return total_calories

def main():
    print("🌟 Welcome to the Nutrition Management Program! 🌟")
    name = input("Your name please: ")
    age = int(input("Enter your age: "))
    height = int(input("Enter your height (in inches): "))
    weight = int(input("Enter your weight (in kgs): "))

    bmi = calculate_bmi(weight, height)
    print(f"Your BMI is: {bmi} 📊")

    print("\nWhat is your goal?")
    print("1️⃣ Lose weight\n2️⃣ Gain weight")
    goal = int(input("Please enter your choice (1 or 2): "))

    if goal == 1:
        weight_change = int(input("How many kgs do you want to lose? "))
        calories_needed = get_caloric_requirement(goal, weight_change)
        print(f"🔥 You need to burn {calories_needed} kcal in total.")
    elif goal == 2:
        weight_change = int(input("How many kgs do you want to gain? "))
        calories_needed = get_caloric_requirement(goal, weight_change)
        print(f"🍕 You need to gain {calories_needed} kcal in total.")

        gender = int(input("Please enter your Gender (1 for Male, 2 for Female): "))
        body_fat = get_body_fat_percentage(bmi, age, gender)
        print(f"Your estimated body fat percentage is: {body_fat}% 🏋️‍♂️")

    else:
        print("❌ Invalid input! Exiting...")
        sys.exit()

    # Daily Caloric Intake Tracker
    print("\n🍽️ Let's track your daily food intake!")
    consumed_calories = get_meal_calories()

    remaining_calories = calories_needed - consumed_calories
    if remaining_calories > 0:
        print(f"⚠️ You need to consume {remaining_calories} more kcal to meet your goal.")
    elif remaining_calories < 0:
        print(f"✅ Great job! You have exceeded your calorie target by {-remaining_calories} kcal.")

    print("\nThank you for using the Nutrition Management Program! 💪")

if __name__ == "__main__":
    main()

    print("Calories left to be eaten=",(u-cal))
