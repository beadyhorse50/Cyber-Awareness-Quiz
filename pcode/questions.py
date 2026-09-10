"""Questions."""


class Question:
    """Quiz Question."""

    def __init__(self, question_no, question_txt, options, right_answer):
        """Sets the initial question up"""
        self.question_no = question_no
        self.question_txt = question_txt
        self.options = options
        self.right_answer = right_answer

    def is_right(self, answer):
        """Checks if the answer is correct"""
        return answer == self.right_answer

    def right_answer_txt(self):
        """Collects the correct answer"""
        return self.options.get(self.right_answer, "")