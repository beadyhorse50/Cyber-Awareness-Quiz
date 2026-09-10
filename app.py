"""Streamlit Interface"""

import streamlit as st

from pcode.quiz import Quiz
from pcode.quiz_data import QuizData
from pcode.validation import validate_name, calculate_percentage

QUESTIONS_FILE = "data/questions.csv"
RESULTS_FILE = "data/results.csv"


def start_screen():
    """Show name entry screen"""
    st.title("Cyber Awareness Quiz")
    name = st.text_input("Enter your name")

    if st.button("Start Quiz"):
        valid, message = validate_name(name)

        if valid:
            try:
                data = QuizData(QUESTIONS_FILE, RESULTS_FILE)
                questions = data.load_questions()
            except (FileNotFoundError, ValueError) as error:
                st.error(str(error))
                return

            st.session_state.name = name
            st.session_state.quiz = Quiz(questions)
            st.session_state.page = "quiz"
            st.session_state.question_index = 0
            st.rerun()
        else:
            st.error(message)


def quiz_screen():
    """Only show one question at a time"""
    quiz = st.session_state.quiz
    current = st.session_state.question_index
    question = quiz.cyber_questions[current]

    st.write(
        "Question "
        + str(current + 1)
        + " of "
        + str(quiz.total_questions())
    )

    options = []

    for letter in question.options:
        options.append(letter + ". " + question.options[letter])

    answer = st.radio(
        question.question_txt,
        options,
        index=None
    )

    if st.button("Next"):
        if answer is None:
            st.error("Please select an answer")
        else:
            selected_letter = answer[0]
            quiz.record_answer(
                question.question_no,
                selected_letter
            )

            if current + 1 < quiz.total_questions():
                st.session_state.question_index = current + 1
            else:
                data = QuizData(
                    QUESTIONS_FILE,
                    RESULTS_FILE
                )
                data.save_attempt(
                    st.session_state.name,
                    quiz.score(),
                    quiz.total_questions()
                )
                st.session_state.page = "results"

            st.rerun()


def results_screen():
    """Show the score and questions answered wrong"""
    quiz = st.session_state.quiz
    score = quiz.score()
    total = quiz.total_questions()

    st.title("Quiz Complete")
    st.write("Score: " + str(score) + "/" + str(total))
    st.write(str(calculate_percentage(score, total)) + "%")

    wrong = quiz.wrong_answers()

    if len(wrong) > 0:
        st.subheader("Questions you got wrong")

        for question in wrong:
            st.write(question.question_txt)
            st.write(
                "Correct answer: "
                + question.right_answer_txt()
            )
    else:
        st.success("You got got all the questions right!")

    if st.button("Try Again"):
        st.session_state.page = "start"
        st.rerun()


if "page" not in st.session_state:
    st.session_state.page = "start"

if st.session_state.page == "start":
    start_screen()
elif st.session_state.page == "quiz":
    quiz_screen()
else:
    results_screen()