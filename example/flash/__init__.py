from __future__ import print_function

import argparse

from flash import quiz
from flash import load

def ask_question(question):
    """ask a question of the user.

    returns True if the answer is correct

    partof: #SPC-quiz-ask
    """
    answer = raw_input("{}?: ".format(question.question)).strip().lower()
    return answer == question.answer

def main(cwd, argv):
    """The executable that is called by the binary.

    partof: #SPC-cmd
    """
    parser = argparse.ArgumentParser(
        prog='flash',
        description='flash card quizzer')
    parser.add_argument('file', help='csv file to get quiz questions from')
    args = parser.parse_args(argv[1:])

    questions = load.load_path(args.file)
    answered = quiz.Answered()
    print("Starting Quiz {}. Press Ctrl+C to quit.".format(args.file))
    while True:
        question = quiz.get_question(questions, answered)
        result = ask_question(question)
        # see: #SPC-response
        if result:
            print("* Correct! Good job\n")
        else:
            print("X Incorrect. The correct answer is: ", question.answer, "\n")
        answered.record(question, result)
