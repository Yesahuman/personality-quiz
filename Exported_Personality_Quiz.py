# %%
# Score dictionary
# Keeps track of how many points the user gets for each type.
score = {"Introvert": 0, "Extrovert": 0}

# Function to ask a single question
def ask_question(question_num, total_questions, question, option_a, option_b, a_type, b_type):
    """
    Ask the user a question and update the score based on their answer.
    
    Parameters:
    - question_num (int): current question number (for progress)
    - total_questions (int): total number of questions
    - question (str): the actual question
    - option_a (str): description for option A
    - option_b (str): description for option B
    - a_type (str): personality type associated with option A
    - b_type (str): personality type associated with option B
    """

    print(f"\n📝 Question {question_num} of {total_questions}:")

    # Build the prompt
    prompt = (
        f"\n{question}\n"
        f"A. {option_a}\n"
        f"B. {option_b}\n"
        "Type A or B (or Q to quit): "
    )

    # Loop until valid input
    while True:
        answer = input(prompt).strip().upper()
        if answer == "A":
            print(f"You chose A: {option_a}")
            score[a_type] += 1
            break
        elif answer == "B":
            print(f"You chose B: {option_b}")
            score[b_type] += 1
            break
        elif answer == "Q":
            print("Quiz exited.")
            raise SystemExit
        else:
            print("Invalid input. Please type A, B, or Q.")

# %%
# Main function to run the quiz
def run_quiz():
    """
    Runs the full quiz, shows the result, saves it, and asks if the user wants to retake.
    """
    global score
    score = {"Introvert": 0, "Extrovert": 0}  # Reset scores

    # Total number of questions
    total_questions = 8

    # List of quiz questions and options
    questions = [
        ("How do you prefer to spend a Friday night?",
         "Reading or gaming alone at home", "Going out with friends"),
        
        ("What's your ideal weekend plan?",
         "Staying in and relaxing", "Exploring the city with friends"),
        
        ("How do you usually recharge?",
         "Spending time alone", "Being around others"),
        
        ("At a party, you tend to...",
         "Find a quiet corner or talk to a few close friends", "Mingle and talk to as many people as possible"),
        
        ("When meeting new people, you feel...",
         "Reserved and cautious", "Energized and excited"),
        
        ("Your ideal work environment is...",
         "Independent and quiet", "Collaborative and lively"),
        
        ("You prefer communication through...",
         "Texting or messaging", "Phone calls or face-to-face"),
        
        ("In group discussions, you...",
         "Listen more than speak", "Love sharing your ideas aloud"),
    ]

    # Loop through each question and ask it
    for i, q in enumerate(questions, start=1):
        ask_question(
            question_num=i,
            total_questions=total_questions,
            question=q[0],
            option_a=q[1],
            option_b=q[2],
            a_type="Introvert",
            b_type="Extrovert"
        )
    
    # Calculate result percentages
    total_score = score['Introvert'] + score['Extrovert']
    intro_percent = round((score['Introvert'] / total_score) * 100) if total_score else 0
    extro_percent = round((score['Extrovert'] / total_score) * 100) if total_score else 0

    # Display result
    print("\nPersonality Result:")
    print(f"Introvert score: {score['Introvert']} ({intro_percent}%)")
    print(f"Extrovert score: {score['Extrovert']} ({extro_percent}%)")

    # Determine personality type
    if score["Introvert"] > score["Extrovert"]:
        result_msg = "🌙 You are an Introvert – calm, thoughtful, and introspective."
    elif score["Extrovert"] > score["Introvert"]:
        result_msg = "🌞 You are an Extrovert – energetic, expressive, and outgoing."
    else:
        result_msg = "🌗 You are an Ambivert – balanced, adaptable, and versatile."

    print(result_msg)

    # Friendly disclaimer
    print("\nNote: This quiz is just for fun and doesn't define who you truly are.")
    print("Everyone is unique, and personality can be fluid.")

    # Save result to file
    save_result(result_msg, intro_percent, extro_percent) # type: ignore

    # Ask if user wants to retake the quiz
    again = input("\n Do you want to retake the quiz? (Y/N): ").strip().upper()
    if again == "Y":
        run_quiz()
    else:
        print("Thank you for playing! See you next time.👋")

# %%
# Save results to a text file with timestamp
import datetime

def save_result(result_msg, intro_percent, extro_percent):
    """
    Appends the quiz result to a text file with timestamp and percentages.
    """
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("your_quiz_result.txt", "a", encoding="utf-8") as f:  # 'a' means append
        f.write("=====================================\n")
        f.write(f"🕒 Quiz taken on: {now}\n")
        f.write(f"Introvert: {intro_percent}%\n")
        f.write(f"Extrovert: {extro_percent}%\n")
        f.write(f"{result_msg}\n")
        f.write("Note: This quiz is just for fun and doesn't define who you truly are.\n")
        f.write("Everyone is unique, and personality can be fluid.\n\n")
    print("💾 Result appended to 'your_quiz_result.txt'")

# %% [markdown]
# Hello, I'll try this quiz 3 times with different input intro, extro & ambi

# %%
run_quiz()


