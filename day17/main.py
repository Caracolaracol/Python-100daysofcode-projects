from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

for question in question_data:
    text_bank = question["question"]
    answer_bank = question["correct_answer"]   
    question_bank.append(Question(text_bank, answer_bank)) # list of Question objects

my_quiz_game = QuizBrain(question_bank)
while my_quiz_game.still_has_questions():
    my_quiz_game.next_question()
my_quiz_game.final_score()
