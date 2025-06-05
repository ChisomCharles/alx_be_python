task = input("Enter your task:")
priority = input("Priority (high/medium/low):").lower()
time_bound = input("Is it time-bound? (yes/no):").lower()
match priority:
    case "high":
        message = f"'{task}' is a high priority task"
        if time_bound == "yes":
            message += "that requires immediate attention today!"
        else:
            message += "Try to complete it as soon as possible."
    case "medium":
        message = f"'{task}' is a medium priority task"
        if time_bound == "yes":
            message += "that requires immediate attention today!"
        else:
            message += "Consider completing it when you have free time."
print(message)