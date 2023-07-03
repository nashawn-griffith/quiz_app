class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        self.keep_playing = 1

    def more_questions(self):
        return self.question_number < len(self.question_list)

    def validate_response(self, question, response):
        if question.answer.lower() != response.lower():
            return False
        return True

    def next_question(self):
        current_item = self.question_list[self.question_number]
        answer = input(
            f"Q. {self.question_number + 1}: {current_item.text} (True/False): "
        )

        self.question_number += 1

        if self.validate_response(current_item, answer):
            self.score += 1
            print(
                f"\n You got it right ! \n The correct answer was: {current_item.answer} \n Your current score is {self.score} / {self.question_number} \n"
            )
        else:
            print(
                f"You got it Incorrect ! \n The correct answer was: {current_item.answer} \n Your current score is {self.score} / {self.question_number} \n"
            )
