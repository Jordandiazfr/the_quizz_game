class QuizBrain:

    def __init__(self, question_list):
        """Requires a list of questions, or a question bank"""
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        guess = input(f"Q.{self.question_number} {question.text} (True or False) ?: ")
        self.check_answer(guess, question.answer)

    def check_answer(self, guess, answer):
        if guess.lower() == answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("Incorrect")
        print(f"Score {self.score}/{self.question_number}")
        print(f"The correct answer is {answer}")
        print("\n")
