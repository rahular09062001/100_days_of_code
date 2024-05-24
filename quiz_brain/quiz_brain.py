class QuizBrain:
    def __init__(self,quiz_list):
        self.question_number = 0
        self.question_list = quiz_list
        self.score = 0

    def still_has_question(self):
        return (self.question_number<len(self.question_list))

    def next_question(self):
        current_question=self.question_list[self.question_number].text
        correct_answer = self.question_list[self.question_number].answer
        self.question_number += 1
        user_answer=input(f"Q.{self.question_number}: {current_question} (True/False).")
        self.check(user_answer,correct_answer)

    def check(self,user_answer,correct_answer):
        if(user_answer.lower()==correct_answer.lower()):
            print('You got it correct.')
            self.score += 1
        else:
            print('You got it wrong.')
        print(f'The correct answer is {correct_answer}')
        print(f'Your current score is {self.score}/{self.question_number}')
        print("\n")
