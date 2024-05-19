from quiz_question_model import Question
from true_false_quiz_data import question_data
from quiz_system import QuizSystem

quiz_questions = []
for question in question_data:
    question_to_add = Question(question['text'], question['answer'])
    quiz_questions.append(question_to_add)

quiz_system = QuizSystem(quiz_questions)

while not quiz_system.still_has_questions():
    print(f"Your current score is {quiz_system.score}.")
    quiz_system.next_question()

print(f"Your final score was {quiz_system.score}!")
