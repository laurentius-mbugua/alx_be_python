task = input("Enter your task: ")

while task:
    priority = input("Priority (high/medium/low): ")
    if priority not in ["high", "medium", "low"]:
        print("Please enter a valid priority (high, medium, or low).")
        continue

    time = input("Is it time-bound? (yes/no): ")

    match priority:
        case "high":
            if time =="yes":
                reminder = f"Reminder: {task} is a high priority task that requires immediate attention today!"
            else:
                reminder = f"Reminder: {task} is a high priority task. Consider completing it when you have free time"
        case "medium":
            if time =="yes":
                reminder =f"Reminder: {task} is a medium priority task that requires immediate attention today!"
            else:
                reminder =f"Reminder: {task} is a medium priority task. Consider completing it when you have free time"
        case "low":
            if time =="yes":
                reminder = f"Reminder {task} is a low priority task that requires immediate attention today!"
            else:
                reminder = f"Reminder {task} is a low priority task. Consider completing it when you have free time"

    print(reminder)
    break
