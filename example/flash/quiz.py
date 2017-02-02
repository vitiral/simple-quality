"""The quiz module."""
import random


class Answered(object):
    """keeps track of question and answer history.

    partof: #SPC-answered

    """

    def __init__(self):
        self._hist = {}

    def get_hist(self, question):
        """Return (num_right, num_wrong) of the question."""
        return self._hist.get(question.question, (0, 0))

    def record(self, question, correct):
        """Record question history."""
        before = self.get_hist(question)
        if correct:
            after = (before[0] + 1, before[1])
        else:
            after = (before[0], before[1] + 1)
        self._hist[question.question] = after

    def get_weights(self, questions):
        """Get the question weights based on answers."""
        total_right = sum(h[0] for h in self._hist.values())
        total_wrong = sum(h[1] for h in self._hist.values())

        weights = []
        for question in questions:
            hist = self.get_hist(question)
            weight = 1
            if total_right:
                weight -= hist[0] * 1.0 / total_right
            if total_wrong:
                weight += hist[1] * 1.0 / total_wrong
            weights.append(weight)

        return weights


def get_question(questions, answered):
    """Get a random question weighted by previous answers.

    partof: #SPC-quiz-get
    """
    weights = answered.get_weights(questions)
    return weighted_choice(weights, questions)


def weighted_choice(weights, choices):
    """Get a choice randomly based on the weights.

    taken from:
        http://stackoverflow.com/questions/3679694
    """
    total = sum(weights)
    r = random.uniform(0, total)
    upto = 0
    for c, w in zip(choices, weights):
        if upto + w >= r:
            return c
        upto += w
    assert False, "Shouldn't get here"
