import os
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_list = [
    Question(question["text"], question["answer"]) for question in question_data
]

quiz = QuizBrain(question_list)

while quiz.more_questions() and quiz.keep_playing:
    quiz.next_question()

    if quiz.more_questions():
        next = input("Press X to exit quiz or any character to continue: \n").lower()
        if next == "x" or next == "X":
            quiz.keep_playing = 0
else:
    clear = lambda: os.system("clear")
    clear()
    print(
        f"Thank you. \n You've completed the quiz \n Your final score is {quiz.score} / {len(quiz.question_list)}"
    )
