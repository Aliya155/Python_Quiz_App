
print("================================")
print("       WELCOME TO QUIZ")
print("================================")

questions = [
    {
        "question": "1. What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Lucknow", "D. Kolkata"],
        "answer": "B"
    },
    {
        "question": "2. Which language is used for AI?",
        "options": ["A. Python", "B. HTML", "C. CSS", "D. SQL"],
        "answer": "A"
    },
    {
        "question": "3. What is 10 + 5?",
        "options": ["A. 10", "B. 20", "C. 15", "D. 25"],
        "answer": "C"
    },
    {
        "question": "4. Which one is a Python data type?",
        "options": ["A. int", "B. print", "C. input", "D. for"],
        "answer": "A"
    },
    {
        "question": "5. Which keyword defines a function?",
        "options": ["A. loop", "B. def", "C. if", "D. class"],
        "answer": "B"
    }
]

name = input("Enter your name: ")

while True:

    score = 0

    for q in questions:

        print("\n", q["question"])

        for option in q["options"]:
            print(option)

        while True:
            user_answer = input("Enter your answer (A/B/C/D): ").upper()

            if user_answer in ["A", "B", "C", "D"]:
                break
            else:
                print("Invalid input! Please enter A, B, C or D.")

        if user_answer == q["answer"]:
            print("Correct Answer!")
            score += 1
        else:
            print("Wrong Answer!")
            print("Correct answer:", q["answer"])

    print("\n========== QUIZ RESULT ==========")
    print("Name:", name)
    print("Your Score:", score, "/", len(questions))
    print("Percentage:", (score / len(questions)) * 100, "%")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again == "yes":
        print("\nStarting a new quiz...")
    elif play_again == "no":
        print("Thank you for playing!")
        break
    else:
        print("Invalid choice! Quiz ended.")
        break

