## How and Why Do We Test Random Values?

A significant part of the quiz component relies on randomness. How can we
possibly test something that is random?

We should switch gears. What we are testing will not be an implementation,
but rather a *specification*. "If I get X number of answers wrong I will
have at least N% chance of getting asked it".

To kick things off, which of the following are valid tests?
1. with a set of 5 questions, if `get_question` is called 1000 times
    it will return *at least* one of each question.
2. In scenario 1: the same is true even if one question has been gotten
    wrong 5 times
3. In scenario 1: if one question has been gotten wrong 5 times and the
    others right 5 times, the wrong answer should be selected
    *at least* 3x more often than the others.

The answer: all of these can be valid tests! By using large sample sizes, we
can reduce the chances of random failures substantially. We can also use our
tests to tune our specification. The requirement simply says to do "missed
items more often", but it wasn't very clear on how MUCH higher.

Come to think of it, this should have been called out in the requirements,
so let's modify that. Add the following to the end of
`REQ-purpose-learning`:

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
of your project and to always update specifications and tests accordingly.
Notice that we did not create `SPC` or `TST` artifacts for
`get_weights`. Although we certainly could have, that method and it's
associated tests were pretty self explanatory. This follows the general
rule of "keep your design docs simple and short". This means not
over-specifying your design as this will only convolute your project.


