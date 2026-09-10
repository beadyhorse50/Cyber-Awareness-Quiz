"""Quiz class"""


class Quiz:
    """Holds questions and users answers"""

    def __init__(self, cyber_questions):
        """Creates quiz"""
        self.cyber_questions = cyber_questions
        self.user_answers = {}

    def total_questions(self):
        """Total number of questions"""
        return len(self.cyber_questions)

    def record_answer(self, question_no, answer):
        """Saves answer"""
        self.user_answers[question_no] = answer

    def is_complete(self):
        """Checks all questions are answered"""
        return len(self.user_answers) == len(self.cyber_questions)

    def score(self):
        """Works out final scored"""
        total = 0

        for question in self.cyber_questions:
            user_answer = self.user_answers.get(question.question_no)

            if user_answer is not None:
                if question.is_right(user_answer):
                    total += 1

        return total

    def wrong_answers(self):
        """Collate list of wrong questions"""
        incorrect_questions = []

        for question in self.cyber_questions:
            user_answer = self.user_answers.get(question.question_no)

            if user_answer is None or not question.is_right(user_answer):
                incorrect_questions.append(question)

        return incorrect_questions