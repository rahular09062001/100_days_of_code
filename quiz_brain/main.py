from data import question_data
from data import question_data2
from question_model import Question
from quiz_brain import QuizBrain

question_bank=[]
for i in question_data2:
    x=Question(i['question'],i['correct_answer'])
    question_bank.append(x)

quiz = QuizBrain(question_bank)
while(quiz.still_has_question()):
    quiz.next_question()
print(f'''
You've completed the quiz
Your final score was : {quiz.score}/{quiz.question_number}
''')


