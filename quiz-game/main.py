from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random

# question_bank = []
# for ques in question_data:
#     new_question = Question(ques['text'], ques['answer'])
#     question_bank.append(new_question)

# quiz = QuizBrain(question_bank)

# while quiz.still_has_questions():
#     quiz.next_question()

def ask_questions(duration, question_data):
    num_questions = 0
    if duration == "short":
        num_questions = 5
    elif duration == "medium":
        num_questions = 10
    elif duration == "long":
        num_questions = 20
    else:
        return "Invalid duration selected. Please choose 'short', 'medium', or 'long'."

    # Shuffle the question data
    random.shuffle(question_data)
    
    # Select the first num_questions questions
    selected_questions = question_data[:num_questions]
    
    # Create a list of Question objects
    question_bank = [Question(ques['text'], ques['answer']) for ques in selected_questions]
    
    return question_bank

def main():
    duration = input("Choose the duration (short, medium, long): ").strip().lower()
    selected_questions = ask_questions(duration, question_data)
    
    if isinstance(selected_questions, str):
        print(selected_questions)
    else:
        quiz = QuizBrain(selected_questions)
        
        while quiz.still_has_questions():
            quiz.next_question()
        
        print(f"\nYou've completed the quiz!")
        print(f"Your final score was: {quiz.score}/{quiz.question_number}")

if __name__ == "__main__":
    main()