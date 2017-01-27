With the paradigm of design in hand (functional programming), let's begin
designing the quiz component

### get_question() function

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
- `record(question, answer)`: records the answer to a question internally
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


[1]: https://docs.python.org/2/reference/datamodel.html
