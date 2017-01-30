It is time we briefly discuss design vocabulary.

## Specifying meaning
It is very important that your design documents have clear meaning. Without
clear meaning, it is difficult to know your [definition of done][1].

We want to stay as simple as possible, so I prefer to use only three words to
have meaning in requirements docs:
- **Shall – Requirement:**  Shall is used to indicate a requirement that is contractually
	binding, meaning it must be implemented and its implementation verified.
	Period!  Don’t think of “shall” as a word, but rather as an icon that SCREAMS:
	“This is a requirement.”  If a statement does not contain the word “shall” it
	is not a requirement.
- **Will - Facts or Declaration of Purpose:** Will is used to indicate a
	statement of fact.  Will statements are not subject to verification.
	"The application **will** be written in python" is an example.
    **Will** statements are meant to be notes to inform lower layers
    of design or note implementation details about a component.
- **Should – Goals, non-mandatory provisions:** Should is used to indicate a
    goal which must be addressed by the design team but is not formally
    verified. Why include should (goal) statements? Because you may have a very
    important issue that you want to communicate to the developers, but can’t
    think of a way to do so in the form of a verifiable requirement. We have
    already seen an example in our purpose statement: "the [flash-quizzer]
    **should** use methodologies that uses effective memorization techniques".
    There is no way to validate that we are using the best methodlogies, but
    we should aim for that goal.

> Reference: these definitions modified from an article at [reqexperts.com][2]
> (October 9th, 2012. Lou Wheatcraft)

> ### Exercise 1:
> Review the documentation we've written so far. When did we use "shall",
> "will" and "should"? Did we use them correctly?

## Testing your software
There are three kinds of testing this book will cover:
- [unit testing][3] which is testing isolated pieces of code
- [integration testing][4] which is testing modules of your code integrated
	together, but not the entire system
- [system testing][5] also known as end-to-end testing.

There are other testing phases and other schools of thought, but these three
will get you a long way no matter what your job.

> ### Exercise 2:
> Read at least the intro for all three wikipedia links above.
> These are the three testing methodologies that will be used in this
> tutorial, it is good to be familiar with what they mean.

### Kinds of Unit Testing

### [Functional Testing][5]
What is the functionality we are programming for? It is important that
we test at least the basics. This includes the:
- [boundary conditions][6]: test the extreme inputs and outputs of your
    function
- typical use cases: test how the function will typically be used
    (i.e. a few values in the middle of the boundary conditions)
- error cases: make sure it throws exception/returns an error when invalid
    inputs are used. This doesn't have to cover everything -- don't test for
    invalid types, let integration tests (or better yet, your language's type
    checker) handle that.

### [White Box Testing][7]
Look at your code. As the programmer, what kind of inputs are YOU concerned
about? Spend some time focusing on these.

You as the developer have the most insight into your function, so you are
probably the most qualified individual for trying to break it. Always observe
Murphey's law: what can go wrong *will* go wrong. If you can *see* something
that might break, even if the scenario seems impossible for a user to hit,
make sure it doesn't break anyway -- because if you can see it it almost
certainly will happen eventually.

### [Risk Based Testing][8]
What is the worst thing that your function could do. Can it segfault
or recurse infinitely? Can it delete user data? Could it crash the whole
operating system? Can it introduce security vulnerabilities?

It's important to ask what the worst case scenarios are and test for them.
This is especially true if your program overwrites files or exposes a port
to the internet -- data loss and security vulnerabilities are serious
problems that can be introduced in the most simple software

Some of these kind of tests are outside the scope of unit tests -- but if
you *can* write a unit test for them, or part of them, then you should.
Otherwise you should try and cover these risks in your integration
or system tests.


[1]: https://www.agilealliance.org/glossary/definition-of-done/
[2]: http://reqexperts.com/blog/2012/10/using-the-correct-terms-shall-will-should/
[2]: https://en.wikipedia.org/wiki/Unit_testing
[3]: https://en.wikipedia.org/wiki/Integration_testing
[4]: https://en.wikipedia.org/wiki/System_testing
[5]: https://en.wikipedia.org/wiki/Functional_testing
[6]: https://en.wikipedia.org/wiki/Boundary_testing
[7]: https://en.wikipedia.org/wiki/White-box_testing
[8]: https://en.wikipedia.org/wiki/Risk-based_testing
