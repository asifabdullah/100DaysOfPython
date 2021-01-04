from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in range(0, len(question_data)):
    text = question_data[i]["question"]
    answer = question_data[i]["correct_answer"]
    question = Question(text, answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You have complete the quiz")
print(f"Your final score was : {quiz.score}/{quiz.question_number}")
