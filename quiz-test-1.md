At first glance, it might appear that `get_question` is
difficult to test. Since it is random, it isn't testable...
right? Randomness certainly makes items more difficult to test, but not
impossible.

But we are getting ahead of ourselves. By breaking `get_question` up into
deterministic pieces (as `get_question_weights` does), we can test those
pieces much more easily.

## Basic Functionality Tests

> #### Exercise 1:
> Create unit tests for `get_question_weights` to validate that it works
> as expected. There are two bugs, can you find them?
>
> - Hint 1: try running it with a few questions and a new `Answered` object.
> - Hint 2: try running it with a single question right twice and another
>   right only once

The first thing we want to do is write some very basic tests for our
deterministic components, in this case `get_question_weights`.

The first, most basic test is to input a couple of questions that have
not been asked and expect their weights to both be 1. Create a file at:
`flash/tests/test_quiz.py`:

{%ace edit=false, lang='python'%}
import unittest
from flash.quiz import Answered
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
{%endace%}

Now run the test with: `py.test flash/tests/test_quiz.py`. You should get
a `ZeroDivisionError`.

Whoops! Something in our design wasn't quite right -- we never accounted for
what to do if `total_right` or `total_wrong` was zero!

In `quiz.py`, change these lines:

{%ace edit=false, lang='python'%}
weight -= hist[0] / total_right
weight += hist[1] / total_wrong
{%endace%}

To this:

{%ace edit=false, lang='python'%}
if total_right:
    weight -= hist[0] / total_right
if total_wrong:
    weight += hist[1] / total_wrong
{%endace%}

And try running the test again -- it should pass. Horray! This function
works... or does it? It's hard to say for sure -- after all we only
wrote a single test case. Let's write one more.

This test requires a bit of knowledge about the gotchas of python.
What happens if some of the weights should be floats?

{%ace edit=false, lang='python'%}
def test_weights_right(self):
    """Assert values are correct when you get some answers
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
{%endace%}

After running the tests, you will see that the result is NOT as you expected.
Why is this? The bug is because when you do `int / int` in python the result is an
`int`, not a float as you might expect from algebra.

> note: if you were using python3, you would not hit this bug.
> All division in python3 results in a float.

Go and fix the bug in `get_weights` by multiplying all values by `1.0`
before dividing:

{%ace edit=false, lang='python'%}
if total_right:
    weight -= hist[0] * 1.0 / total_right
if total_wrong:
    weight += hist[1] * 1.0 / total_wrong
{%endace%}

At last, our basic functional tests should pass.

> #### Exercise 2:
> Write two more unit tests to complete the basic functionality testing:
> - `test_weights_wrong` where you assert that the weights are correct
>   if some of the answers were wrong.
> - `test_weights_mixed` where the questions get different amounts right
>   and wrong
>
> Hopefully you won't find any additional bugs, but these tests should
> help give you confidence in your implementation.

Before continuing, remember to run autopep8 and docformatter on your code and
commit the changes. Also run pylint to make sure our code quality has been
good.

## Chapter Conclusion

Hopefully it is starting to be clear how useful, but also difficult,
testing can be. Testing can detect bugs in our functions before other
functions use them, improving the quality of our entire software stack.

But how many tests should we write? How do we know how many is enough?
The answer is, of course, that no amount of tests completely cover all
the possible scenarios that software can be subjected to. However,
if you cover the three categories of unit tests given in the
[Vocabulary Chapter](vocabulary.md), then you can be pretty confident
your unit tests cover as much of the risk as you could hope for.

Further coverage is the job of integration and system tests, and is
the topic of a later chapter.
