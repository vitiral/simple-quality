With the paradigm of design in hand (functional programming), let's begin
designing the quiz component

## Quiz Module Design

Let's start by turning our brainstorming from the last chapter into
actual design specifications. Create a new file, at
`design/quiz.toml` and write the following:

```
[SPC-quiz]
partof = "REQ-purpose"
text = '''
the quiz component is broken down into the following parts
'''

[SPC-quiz-ask]
text = '''
There shall be an `ask_question(question)` function which
takes the question to ask and returns whether the user got
it wrong or right
'''

[SPC-quiz-get]
text = '''
There shall be a `get_question(questions, answered)`
function which takes a list of questions and the answers
which the user previously gave and returns the question to
ask.
'''
```

## Answered Component

There is still a major component we are missing to our design, and that
is the `Answered` object.

Let's look at the basics, what does the Answered object do?
- given a question, it returns how many times the question has
    been answered correctly and incorrectly
- given a question and an answer, it records that question's answer
    internally

Now wait, you might be saying -- if it is recording state isn't that
not a functional style? And you would be right, it's not! But what we
have managed to do is keep all state at our *top layer*. As long as the
`Answered` object never gets mutated in a lower layer only, then all our lower
layers remain simple and easy to reason about.

One of the first things to notice is that `Answered` is going to have
to perform an internal lookup from `Question` -> `Answer`. Normally,
this is best done by an object called a `dict` in python or a `HashMap`
in other languages. `dict`s offer `O(1)` lookup time, or lookup
time that does not depend on the number of items in the `dict`.

Can we use our Question objects as keys in a dictionary? No, we can't -- only
[immutable data types][1] can be used as keys. Drat.

But wait... does our `Answered` object really need to know the *answers* to the
questions, or does it only need to know the question itself? The
`Question.question` attribute *is* immutable (it is a `str` type) and so
*can* be the keys for our `dict`!

With this knowledge in hand, let's create our specification. Add the
following to `design/quiz.toml`

```
[SPC-answered]
partof = "SPC-quiz"
text = '''
There shall be an `Answered` object which has the following methods:
- `record(question, correct)`: records the answer to a question internally
- `get_hist(question)`: return `(num_right, num_wrong)` answers to a question

If the user requests a question that hasn't been asked, the output shall be
`(0, 0)`

Internally, the `Answered` object will have an `_hist` dict
which uses `question.question` as the keys and has
`(num_right, num_wrong)` as the values.
```

> #### Exercise 1:
> Using the specification above, write the `Answered` class in your
> source code and link it to the #SPC-answered specification
>
> Were there things that you think should have been added to the
> design specification? If so, feel free to add them.

If you are having trouble with the above exercise, here is my code in
`flash/quiz.py`:

```
class Answered(object):
    """keeps track of question and answer history.

    partof: #SPC-answered
    """

    def __init__(self):
        self._hist = {}

    def get_hist(self, question):
        """Return (num_right, num_wrong) of the question."""
        self._hist.get(question.question, (0, 0))

    def record(self, question, correct):
        """Record question history."""
        before = self.get_hist(question)
        if correct:
            after = (before[0] + 1, before[1])
        else:
            after = (before[0], before[1] + 1)
        self._hist[question.question] = after
```

## Implementing `get_question`

`get_question` requires that we get a question at random, but weight
questions which the user has gotten incorrect.

We want to try and incorporate right and wrong answers into the weight.
We want right answers to decrease weight and wrong answers to increase
weight.

Let's take a first stab at something like this
```
weight = 1
weight -= num_correct / total_correct
weight += num_incorrect / total_incorrect
```

In other words, the weight is going to be lower (less likely to ask again)
if the question has been gotten correct many times and higher (more likely
to ask again) if the question has been gotten incorrect many times.

This is just a first stab, we may want to tweak this later.

> #### Exercise 2:
> Using the weight formula above, write the `get_question` method.
>
> HINT: check out Python's [`random`][2] module.
>
> DOUBLE HINT: check out `random.choices`

Here is my initial implementation:

```
def get_question(questions, answered):
    """Get a random question weighted by previous answers.

    partof: #SPC-quiz-get
    """
    weights = answered.get_weights(questions)
    return weighted_choice(weights, choices)


def weighted_choice(weights, choices):
    """Get a choice randomly based on the weights.

    taken from:
        http://stackoverflow.com/questions/3679694

    partof: #SPC-random
    """
    total = sum(weights)
    r = random.uniform(0, total)
    upto = 0
    for c, w in zip(choices, weights):
        if upto + w >= r:
            return c
        upto += w
    assert False, "Shouldn't get here"
```

And add the following method to `Answered`:
```
def get_weights(self, questions):
    """Get the question weights based on answers."""
    total_right = sum(h[0] for h in self._hist.values())
    total_wrong = sum(h[1] for h in self._hist.values())

    weights = []
    for question in questions:
        hist = self.get_hist(question)
        weight = 1
        weight -= hist[0] / total_right
        weight += hist[1] / total_wrong
        weights.append(weight)

    return weights
```

If you are clever or used to floating point and python gotchas
you may notice a couple of mistakes in the above code. Rather than try and
analyze the code for errors, we are going to find the mistakes
through unit testing, the subject of the next chapter.

[1]: https://docs.python.org/2/reference/datamodel.html
[2]: https://docs.python.org/3/library/random.html#module-random
