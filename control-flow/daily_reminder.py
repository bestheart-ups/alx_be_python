#prompt for a task
task = input("task description: ")
priority = input("high, medium, low: ")
time_bound = input("is the task time bound?, {yes} or {no}: ")

#process the task based on priority and time sensitivity

match priority:
    case "high":
        reminder = f"reminder:finish project report, is a high priority task that requires immediate attention."
    case "medium":
        reminder = f"reminder:finish project report, is a medium priority task that requres immediate action."
    case "low":
        reminder = f"reminder:finish project report, project is low priority."
        #modify reminder if time bound
if time_bound == "yes":
        reminder += "this task requires immediate action today!"
        print(reminder)

    