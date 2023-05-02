
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        user_answer = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} (True/False)?:")
        self.question_number += 1
        self.check_answer(user_answer, self.question_list[self.question_number].answer)
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self, user_anser, correct_answer):
        if user_anser.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
            print(f"Your current score is {self.score}/{self.question_number}")
        else:
            print("That's Wrong")
        print(f"The correct answer was: {correct_answer}")
    def final_score(self):
        print(f"You've completed the test your final score was: {self.score}/{self.question_number}")
