current_age = int(input("What is your current age? "))
max_age = 90

def life_in_weeks(current_age, max_age):
    years_left = max_age - current_age
    weeks = years_left * 52
    print(f"You have {weeks} weeks left.")
    
life_in_weeks(current_age, max_age)
