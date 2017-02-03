A significant part of the quiz component relies on randomness. How can we
possibly test something that is random?

In order to answer this, it is helpful to ask the question a different way.
Instead of asking how we test the internals, we should ask how we test to
the specification.

Which of the following do you think are valid unit tests?
1. with a set of 5 questions, if `get_question` is called 1000 times
    it will return *at least* one of each question.
2. In scenario 1: the same is true even if one question has been gotten
    wrong 5 times
3. In scenario 1: if one question has been gotten wrong 5 times and the
    others right 5 times, the wrong answer should be selected
    *at least* 3x more often than the others.

The answer: all of these *could* be valid unit tests (one isn't for
our current implementation). By using large sample
sizes, we can reduce the chances of random failures substantially. We can also
use our tests to tune our specification. The requirement simply says to do
"missed items more often", but it wasn't very clear on how MUCH higher.

## Updating Requirements

Come to think of it, this should have been called out in the requirements.
Add the following to the end of `REQ-purpose-learning`:

```
The actual weights given to missed items should be
determined by conducting user studies using an MVP of the
flash application.
```

And let's add the following test designs to `design/quiz.toml`:

```
[TST-quiz-get]
text = '''
The unit tests for getting questions should validate that
the requirements in `REQ-purpose-learning` are being roughly
followed.
'''
```

It is important to keep your requirements up-to-date with the intentions
of your project. Notice that we did not create `SPC` or `TST` artifacts for
`get_weights`. Although we could have, the code we wrote was
pretty self explanatory. By choosing to *not* write design docs, we can keep
everything a little less wordy. If at a later time the implementation
starts to get more complicated than you anticipated, you can always go
back to the drawing board and write docs.

This is a hard balance to strike -- but a simple rule is that if your
function isn't calling any other functions you probably don't need design
docs for it.

## Writing the Tests

For our unit tests, we will be testing that randomness is working
*at all*. It would be very, very bad if all our application did was ask the
same question over and over again -- we want to make sure that doesn't happen
for any normal use case.

Add this to `flash/tests/test_quiz.py`
{%ace edit=false, lang='python'%}
# a list of questions to be used in the tests
questions = [
    Question("one", "correct"),
    Question("two", "correct"),
    Question("three", "correct"),
    Question("four", "correct"),
    Question("five", "correct"),
]

# the index for each question
questions_index = {
    q.question: i for (i, q) in
        enumerate(questions)
}

class TestGetQuestion(unittest.TestCase):
    """Tests to validate get_question behaves
    as expected.

    partof: #TST-quiz-get
    """
    def test_coverage(self):
        """make sure all questions are asked."""
        asked_count = [0 for _ in questions]
        answered = Answered()
        for _ in range(1000):
            q = get_question(questions, answered)
            index = questions_index[q.question]
            asked_count[index] += 1

        assert min(asked_count) >= 1
{%endace%}

> #### Exercise 1:
> Create the additional cases for scenario 2 and 3 at the top
> of this chapter

Here are my answers to exercise 1 (methods of `TestGetQuestion`):
{%ace edit=false, lang='python'%}
def test_coverage_2(self):
    """Still have coverage even if one answer is wrong
        several times.
    """
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
        likihood that it gets asked.
    """
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
    assert asked_count[0] >= 3 * max_asked_right
{%endace%}

> #### Exercise 2:
> run your unit tests and fix any bugs. What did we get wrong?
>
> Answer: with our current design the "wrong question" will *not* be
> asked 3x more than the others. The solution is to lessen the assertion.
>
> I chose `assert asked_count[0] >= 1.1 * max_asked_right`

## Unit Tests Conclusion
The tests we have written so far only cover the absolute basics
of the quiz module, however even the tests we *do* have are very helpful
for feeling confident enough to try and create an minimum viable
product.

It is a good idea at this point to stop and document a few more
tests you might make in the future. You can put them in your
design files or as `TODO`s in your source code -- whatever makes
sense. It is always a good idea to design tests when you are
familiar with the source code.

Make sure to commit your changes before continuing to the next
chapter.
