
import unittest
from flash.quiz import Answered, get_question
from flash.load import Question

class TestGetWeights(unittest.TestCase):
    def test_weights_empty(self):
        questions = [
            Question("who", "correct"),
            Question("what", "correct"),
        ]

        answered = Answered()
        weights = answered.get_weights(questions)
        assert weights == [1, 1]

    def test_weights_right(self):
        """assert values are correct when you get some answers
        right more than others."""
        questions = [
            Question("who", "correct"),
            Question("what", "correct"),
        ]

        answered = Answered()
        ask = questions[0]
        answered.record(ask, True)
        answered.record(ask, True)
        ask = questions[1]
        answered.record(ask, True)

        expected = [
            1 - 2.0 / 3,
            1 - 1.0 / 3,
        ]

        weights = answered.get_weights(questions)
        assert weights == expected

    def test_weights_wrong(self):
        """assert values are correct when you get some answers
        wrong more than others."""
        questions = [
            Question("who", "correct"),
            Question("what", "correct"),
        ]

        answered = Answered()
        ask = questions[0]
        answered.record(ask, False)
        answered.record(ask, False)
        ask = questions[1]
        answered.record(ask, False)

        expected = [
            1 + 2.0 / 3,
            1 + 1.0 / 3,
        ]

        weights = answered.get_weights(questions)
        assert weights == expected

    def test_weights_mixed(self):
        """assert values are correct when you have mixed answers"""
        questions = [
            Question("who", "correct"),
            Question("what", "correct"),
        ]

        answered = Answered()
        ask = questions[0]
        answered.record(ask, False)
        answered.record(ask, False)
        answered.record(ask, True)
        ask = questions[1]
        answered.record(ask, False)
        answered.record(ask, True)
        answered.record(ask, True)
        answered.record(ask, True)

        expected = [
            1 - 1.0 / 4 + 2.0 / 3,
            1 - 3.0 / 4 + 1.0 / 3,
        ]

        weights = answered.get_weights(questions)
        assert weights == expected

# a list of questions to be used in the tests
questions = [
    Question("one", "correct"),
    Question("two", "correct"),
    Question("three", "correct"),
    Question("four", "correct"),
    Question("five", "correct"),
]

questions_index = {q.question: i for (i, q) in enumerate(questions)}

class TestGetQuestion(unittest.TestCase):
    """Tests to validate get_question behaves as expected.

    partof: #TST-quiz-get
    """
    def test_coverage(self):
        """make sure all questions are hit when called randomly."""
        asked_count = [0 for _ in questions]
        answered = Answered()
        for _ in range(1000):
            q = get_question(questions, answered)
            index = questions_index[q.question]
            asked_count[index] += 1

        assert min(asked_count) >= 1

    def test_coverage_2(self):
        """Still have coverage even if one answer is wrong several times"""
        asked_count = [0 for _ in questions]
        answered = Answered()
        for _ in range(5):
            answered.record(questions[2], False)

        for _ in range(1000):
            q = get_question(questions, answered)
            index = questions_index[q.question]
            asked_count[index] += 1

        assert min(asked_count) >= 1

    def test_more_wrong(self):
        """Test that getting an answer wrong will increase the
        likihood that it gets asked"""
        asked_count = [0 for _ in questions]
        answered = Answered()
        # answer the first one wrong 5 times and the
        # others right 5 times
        for _ in range(5):
            answered.record(questions[0], False)
            for q in questions[1:]:
                answered.record(q, True)

        for _ in range(1000):
            q = get_question(questions, answered)
            index = questions_index[q.question]
            asked_count[index] += 1

        assert min(asked_count) >= 1
        max_asked_right = max(asked_count[1:])
        assert asked_count[0] >= 1.1 * max_asked_right
