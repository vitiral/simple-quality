Now that we have all our tooling set up for running tests
and writing clean code, we are ready to continue with the
design of our application. The next component that we
should develop is the quiz component.

> ##### Exercise 1:
> What should the "quiz component" do?
>
> Using rst, write down the high level design docs of the quiz component

## Designing To Test

Before we continue too far, let's review what the quiz component does:
- it is given a list of questions
- it chooses a question at random
- it keeps track of right/wrong answers and assigns
	greater weight to the ones the user is getting wrong.

There are two common design patterns in software development:
1. **Object Oriented**: the `Quiz` component is an **object** which exposes a
    **method** like `ask_question()`, which returns a random
	`Question`. Each time a question is answered it records
	it in it's internal `Answered` object (it holds state)
2. **Functional**: the quiz component is composed of two **functions** -- one
    for getting a question and one for asking a question.
	- `get_question(questions, answered)` takes the list of
	    `Question` objects and the `Answered` object and outputs
	    a `Question` randomly based on the weights.
	- The `ask_question(question)` takes in the `Question`
	    and outputs true if it was answered correctly
	    and false otherwise (interfacing with the user).
	- the caller then updates the `Answered` object
	    with the result before it asks another question.

These represent two design paradigms called "object oriented
programming" and "functional programming". Let's take some
observations:
1. The Object oriented approach seems simpler -- all the caller has to
	do is call `Quiz.ask_question()` over and over again.
2. The functional approach seems easier to test -- if you have the
	same inputs you will always have the same outputs
	(except when talking to the user!)
3. The functional approach is easier to reason about -- there
	is no hidden state, everything happens in the open.

We will be using the functional programming style in this
guide. In general, it is always good practice to think of
ways in which you can use functional programming in your
software. Most find that as applications get large, functional
programming is much easier to test and reason about.

> ### Exercise 2:
> Spend some time researching the differences between functional
> and object-oriented programming. What things strike you as
> useful to each style?
