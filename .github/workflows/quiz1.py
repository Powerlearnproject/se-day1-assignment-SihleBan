# Function to display the quiz question and check the answer
def software_engineering_quiz():
    print("Which of the following best describes software engineering?")
    print("a) The study of hardware components")
    print("b) The process of designing, developing, and maintaining software")
    print("c) The analysis of networking protocols")
    print("d) The management of data storage systems")
    
    # Get user input
    answer = input("Enter the correct option (a/b/c/d): ").strip().lower()

    # Correct answer
    correct_answer = 'b'

    # Check if the answer is correct
    if answer == correct_answer:
        print("Correct! The process of designing, developing, and maintaining software is the best description of software engineering.")
    else:
        print("Incorrect. The correct answer is 'b'.")
        
# Call the function to run the quiz
software_engineering_quiz()
