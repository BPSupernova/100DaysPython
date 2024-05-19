class QuizSystem:
    def __init__(self, my_questions_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = my_questions_list

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        
        print(f"Q.{self.question_number + 1}: {current_question.text}")
        self.check_question()

        self.question_number += 1

    def check_question(self):
        current_question = self.questions_list[self.question_number]
        player_answer = input("Is this true or false? Enter 'True' or 'False': ")
        if player_answer == current_question.answer:
            print("That's correct!")
            self.score += 1
        else:
            print("That's incorrect")

    def still_has_questions(self):
        if self.question_number == len(self.questions_list):
            return True
        return False