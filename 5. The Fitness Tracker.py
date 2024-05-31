#Task 1: Develop a function to log different fitness activities and their duration.

def log_fitness_activity(activity, duration, log_file="fitness_log.txt"):
    """
    Logs a fitness activity and its duration to a specified log file.

    Parameters:
        activity (str): The name of the fitness activity.
        duration (float): The duration of the activity in minutes.
        log_file (str): The file path to the log file. Default is 'fitness_log.txt'.
    """
    with open(log_file, "a") as file:
        file.write(f"{activity}: {duration} minutes\n")

# Example usage:
log_fitness_activity("Running", 30)
log_fitness_activity("Weightlifting", 45)
log_fitness_activity("Yoga", 60)

#Task 2: Write a simple function that estimates calories burned based on the activity and duration.

def estimate_calories_burned(activity, duration):
    """
    Estimates calories burned based on the activity and duration.

    Parameters:
        activity (str): The name of the fitness activity.
        duration (float): The duration of the activity in minutes.

    Returns:
        float: The estimated calories burned.
    """
    # Define calorie burn rates per minute for different activities (calories per minute)
    calorie_burn_rates = {
        "running": 10,   # example calorie burn rate for running (10 calories per minute)
        "cycling": 8,    # example calorie burn rate for cycling
        "swimming": 12,  # example calorie burn rate for swimming
        "weightlifting": 5,  # example calorie burn rate for weightlifting
        "yoga": 3       # example calorie burn rate for yoga
        # Add more activities and their respective calorie burn rates as needed
    }

    # Convert activity name to lowercase to handle case-insensitive matching
    activity = activity.lower()

    # Check if the activity is in the calorie burn rates dictionary
    if activity in calorie_burn_rates:
        # Calculate calories burned: calorie burn rate * duration (in minutes)
        calories_burned = calorie_burn_rates[activity] * duration
        return calories_burned
    else:
        print("Activity not found in calorie burn rates database.")
        return None

# Example usage:
activity = "running"
duration = 45  # in minutes
calories_burned = estimate_calories_burned(activity, duration)
if calories_burned is not None:
    print(f"Estimated calories burned for {duration} minutes of {activity}: {calories_burned} calories")

#Task 3: Create a summary function that provides a report of all activities and total calories burned for the day.

def generate_activity_summary(log_file="fitness_log.txt"):
    """
    Generates a summary report of all logged fitness activities for the day,
    along with the total calories burned.

    Parameters:
        log_file (str): The file path to the log file. Default is 'fitness_log.txt'.

    Returns:
        tuple: A tuple containing two elements:
            - summary (str): The summary report of activities and total calories burned.
            - total_calories (float): The total calories burned for the day.
    """
    activity_calories = {}  # Dictionary to store calories burned for each activity
    total_calories = 0  # Initialize total calories burned

    # Read the log file and process each line
    with open(log_file, "r") as file:
        for line in file:
            # Split the line into activity and duration
            activity, duration = line.strip().split(": ")
            # Convert duration to float
            duration = float(duration.split()[0])
            # Estimate calories burned for the activity
            calories_burned = estimate_calories_burned(activity, duration)
            if calories_burned is not None:
                # Update total calories burned
                total_calories += calories_burned
                # Update activity_calories dictionary
                activity_calories[activity] = activity_calories.get(activity, 0) + calories_burned

    # Generate summary report
    summary = "Activity Summary:\n"
    for activity, calories in activity_calories.items():
        summary += f"- {activity.capitalize()}: {calories} calories\n"
    summary += f"Total Calories Burned: {total_calories} calories\n"

    return summary, total_calories

# Example usage:
summary, total_calories = generate_activity_summary()
print(summary)