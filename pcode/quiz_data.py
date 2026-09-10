"""Data"""

import csv
import os
from datetime import datetime

from pcode.questions import Question


class QuizData:
    """Data"""

    def __init__(self, questions_file, results_file):
        """Set up file path"""
        self.questions_file = questions_file
        self.results_file = results_file

    def load_questions(self):
        """Load the questiosn"""
        loaded_questions = []

        try:
            with open(self.questions_file, newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    options = {}

                    for letter in ["a", "b", "c", "d"]:
                        option = row.get("option_" + letter, "")
                        option = option.strip()

                        if option != "":
                            options[letter] = option

                    question = Question(
                        int(row["id"]),
                        row["question"],
                        options,
                        row["correct_answer"].strip(),
                    )
                    loaded_questions.append(question)

        except FileNotFoundError:
            raise FileNotFoundError("Could not find this  file: " + self.questions_file)

        return loaded_questions

    def save_attempt(self, name, score, total):
        """Savesquiz attempt"""
        file_exists = os.path.isfile(self.results_file)

        with open(self.results_file, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(["name", "score", "total", "date"])

            writer.writerow(
                [
                    name,
                    score,
                    total,
                    datetime.now(),
                ]
            )


    def load_attempts(self):
        """Loads past attempt"""
        attempts = []

        if not os.path.isfile(self.results_file):
            return attempts

        with open(self.results_file, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                attempts.append(row)

        return attempts