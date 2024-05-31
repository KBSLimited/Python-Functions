#Task 1: Develop a list of questions and answers.

#Question: Which company produced the first mass-produced car?
#Answer: Ford Motor Company produced the first mass-produced car, the Model T, in 1908.

#Question: What does SUV stand for?
#Answer: SUV stands for Sports Utility Vehicle.

#Question: What is the top speed of a Bugatti Chiron?
#Answer: The Bugatti Chiron has a top speed of 261 mph (420 km/h).

#Task 2: Write a function that quizzes the user and takes their answers.

def quiz_user():
    """Function to quiz the user."""
    questions_answers = [
        ("Which company produced the first mass-produced car?", "Ford"),
        ("What does SUV stand for?", "Sports Utility Vehicle"),
        ("What is the top speed of a Bugatti Chiron?", "261 mph")
    ]
    
    num_questions = len(questions_answers)
    score = 0
    
    print("Welcome to the Car Quiz!")
    print("Answer the following questions:")
    
    for question, answer in questions_answers:
        print("Question:", question)
        user_answer = input("Your answer: ")
        if user_answer.strip().lower() == answer.strip().lower():
            print("Correct!")
            score += 1
        else:
            print("Sorry, the correct answer is:", answer)
    
    print(f"You got {score} out of {num_questions} questions correct.")

# Example usage:
quiz_user()

#Task 3: Score the quiz and give the user feedback on their performance.

def quiz_user():
    """Function to quiz the user."""
    questions_answers = [
        ("Which company produced the first mass-produced car?", "Ford"),
        ("What does SUV stand for?", "Sports Utility Vehicle"),
        ("What is the top speed of a Bugatti Chiron?", "261 mph")
    ]
    
    num_questions = len(questions_answers)
    score = 0
    
    print("Welcome to the Car Quiz!")
    print("Answer the following questions:")
    
    for question, answer in questions_answers:
        print("Question:", question)
        user_answer = input("Your answer: ")
        if user_answer.strip().lower() == answer.strip().lower():
            print("Correct!")
            score += 1
        else:
            print("Sorry, the correct answer is:", answer)
    
    print(f"\nYou got {score} out of {num_questions} questions correct.")
    
    # Calculate percentage score
    percentage_score = (score / num_questions) * 100
    
    # Provide feedback based on score
    if percentage_score >= 70:
        print("Congratulations! You passed the quiz.")
    else:
        print("Sorry, you did not pass the quiz. Better luck next time!")

# Example usage:
quiz_user()