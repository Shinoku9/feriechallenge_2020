import random
import datetime

age = input("Age: ")
weight = float(input("Weight (kg): "))
height = float(input("Height (cm): "))

bmi_factor = weight / ((height / 100) ** 2)

bmi_thresholds = {0: "Very severely underweight",
                  15: "Severely underweight",
                  16: "Underweight",
                  18.5: "Normal (healthy weight)",
                  25: "Overweight",
                  30: "Obese Class I (Moderately obese)",
                  35: "Obese Class II (Severely obese)",
                  40: "Obese Class III (Very severely obese)"}

sports = ["walking", "yoga", "running", "swimming", "biking", "rope-jumping", "full body workout"]
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
avg_train_time = 30

for threshold, description in bmi_thresholds.items():
    if bmi_factor >= threshold:
        bmi_description = description
        current_threshold = threshold
    else:
        break

print("Your BMI factor is: " + str(round(bmi_factor,2)) + " " + str(bmi_description)) 
user_max_train_time = float(input("Enter max time you can spend on training a day: "))

for threshold in bmi_thresholds.keys():
    if current_threshold == 0:
        time_multiplier = 0.2
    elif current_threshold == 15:
        time_multiplier = 0.5
    elif current_threshold == 16:
        time_multiplier = 0.8
    elif current_threshold == 18.5:
        time_multiplier = 1
    elif current_threshold == 25:
        time_multiplier = 1.25
    elif current_threshold == 30:
        time_multiplier = 2
    elif current_threshold == 35:
        time_multiplier = 3
    elif current_threshold == 40:
        time_multiplier = 5
    else:
        break

today = datetime.datetime.today().weekday()
days = []
for current_day in range(today, 7):
    days.append(current_day)
    if current_day == 6:
        for current_day in range (0, 7-len(days)):
            days.append(current_day)

def training_plan():
    print("Your training plan for next 7 days is:")
    if time_multiplier * avg_train_time >= user_max_train_time:
        for x in range(7):
            print(weekdays[days[x]] + ": exercise: " + str(random.choice(sports)) + " for " + str(user_max_train_time) + " minutes.")
            file.write(weekdays[days[x]] + ": exercise: " + str(random.choice(sports)) + " for " + str(user_max_train_time) + " minutes.\n")

    else:
        for x in range(7):
            print(weekdays[days[x]] + ": exercise: " + str(random.choice(sports)) + " for " + str(time_multiplier * avg_train_time) + " minutes.")
            file.write(weekdays[days[x]] + ": exercise: " + str(random.choice(sports)) + " for " + str(time_multiplier * avg_train_time) + " minutes.\n")

file = open("Training_plan.txt","w+")
file.write("Age: " + str(age) + "\n")
file.write("Weight: " + str(weight) + "kg\n")
file.write("Height: " + str(height) + "cm\n")
file.write("BMI: " + str(round(bmi_factor,2)) + " " + str(bmi_description) + "\n")
training_plan()
file.close()
