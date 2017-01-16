# Vocabulary

It is time we briefly get the vocabulary of design out of the way. Rather than
just throwing words+definitions at you (I'll leave our flash program to do
that!), I will try and give a rough history of words and why they come in handy.

## Specifying meaning
It is very important that your design documents have clear meaning. Without
clear meaning, it is easy to not know what the [definition of done](1) of a
specific requirement or specification is.

This is where the three "words with teeth" come in, and will be used throughout
this book. These definitions are edited versions of the excellent article at
[reqexperts.com](5):
- **Shall – Requirement:**  Shall is used to indicate a requirement that is contractually
	  binding, meaning it must be implemented, and its implementation verified.
	  Period!  Don’t think of “shall” as a word, but rather as an icon that SCREAMS:
	  “This is a requirement.”  If a statement does not contain the word “shall” it
	  is not a requirement.
- **Will - Facts or Declaration of Purpose:** Will is used to indicate a
	  statement of fact.  Will statements are not subject to verification.  For
	  example:  if I want to tell you something about another system I will use
	  will.  "The application will be written in python" is an example.
    **Will** statements are meant to be notes to inform lower layers
    of design or note implementation details
- **Should – Goals, non-mandatory provisions:** Should is used to indicate a
	goal which must be addressed by the design team but is not formally
	verified. Why include should (goal) statements? Because you may have a very
	important issue that you want to communicate to the developers, but can’t
	think of a way to do so in the form of a verifiable requirement. We have
	already seen an example in our purpose statement: "the [flash-quizzer]
	**should** use methodologies that uses effective memorization techniques".
	There is no way to validate that we are using the best methodlogies, but
	we should aim for that goal.

> ### Exercise 1:
> Review the documentation we've written so far. When did we use "shall",
> "will" and "should"? Did we use them correctly?

## Testing your software
There are three kinds of testing this book will cover:
- [unit testing](2), which is testing isolated pieces of code
- [integration testing](3), which is testing modules of your code integrated
	together, but not the entire system
- [system testing](3), also known as end-to-end testing.

There are other testing phases and other schools of thought, but these three
will get you a long way no matter what your job.

> ### Exercise 2:
> Read at least the intro for all three wikipedia links above.
> These are the three testing methodologies that will be used in this
> tutorial.

[1]: https://www.agilealliance.org/glossary/definition-of-done/

[5]: http://reqexperts.com/blog/2012/10/using-the-correct-terms-shall-will-should/

[2]: https://en.wikipedia.org/wiki/Unit_testing
[3]: https://en.wikipedia.org/wiki/Integration_testing
[4]: https://en.wikipedia.org/wiki/System_testing
