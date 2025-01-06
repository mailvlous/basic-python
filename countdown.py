import datetime

input_goal = input(" Enter your goal : ")
input_time = input(" Enter the date of your goal in the format 'dd/mm/yyyy' ")


goal_time = datetime.datetime.strptime(input_time, "%d/%m/%Y")
now = datetime.datetime.now()

time_left = goal_time - now

if time_left.days < 0:
    print("The date has passed")
    print(f"Time passed since your goal is {-time_left.days} days")
elif time_left.days == 0:
    print("The date is today")
else:
    print(f"Time left to reach your goal is {time_left} ")