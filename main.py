from question_model import QuestionModel
from data import question_data
from new_data import questions
from quiz_brain import QuizBrain
question_bank = []

# for question in question_data:
#     new_question = QuestionModel(question['text'], question['answer'])
#     question_bank.append(new_question)
# New QUESTIONS DATA

for q in questions:
    new_q = QuestionModel(q['question'], q['correct_answer'])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You completed the quiz")
print(f"Your final score is {quiz.score}/{len(quiz.question_number)}")
