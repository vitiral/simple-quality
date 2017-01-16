# Shiny New Tools
Just like revision control best practices would be meaningless without
a revision control tool like git, design best practices are
meaningless without the associated tools.

Okay, that isn't *quite* accurate, but it's inaccuracy is the root of why
design tools have languished so much in the history of software
development. It is easy to think that your requirements can be
completely captured in your README, or in your code documentation,
or in your unit tests -- but in the end they get captured everywhere
and nowhere. You end up either repeating intention or forgetting to
specify it all together.

Let's get this out of the way first: except for some of the
simplest possible libraries, user/developer documents
should **not** be your only design documents! The things your users are concerned
about should almost never be the implementation details of your project,
and unless your library is so simple that all design decisions fit in
a few sentences, your code documentation won't cut it for preserving
intent or pointing out relationships between components.

This is not to say that user (guide/README) and developer (code) documentation
are not critical to a project's quality: they absolutely are. But they
should not replace your requirements, design specification or
testing overview documentation for any but the simplest projects.

So, here are the primary tools that every developer should have
under their belt to increase the quality of their software and
their productivity.

## revision control
This is probably the most essential tool to learn how to use,
as it allows you to code fearlessly without worrying that past code will
be "lost." We will be using [git](1) to track our progress at each stage.

## developer ready inline documentation
[Most languages](2) at least have a library that can take inline
documentation on your functions, classes, etc and translate
them into rendered and beautiful user docs. Some languages
support it natively. [rust](3) is a great example, where the
language-defined syntax will create beautiful developer docs.
We will be writing python documentation that *could* be converted using
[Spinx](4) and can be natively viewed when importing our package
from python REPL by calling `help(obj)`.

## unit testing
Almost every language has a unit testing framework. Get
to know yours intimately. We will be using python's [unittest](5)
package to write tests in this tutorial and [pytest](6) to run
them.

## custom tooling, build systems and scripting languages
Some people believe that the primary responsibility of Software Engineers
in Test (my job title) is to design test cases. I think this is
incorrect. In my opinion, the primary job of an SET should be to develop
processes, tools and frameworks that make the entire organization run
more efficiently and with higher quality.

This section will be one of the least discussed in this book, but
it is the most important for your future development. The problem is
that it can't really be taught except to say: always look for ways
you can automate pain points and increase quality. Develop tools that
make it easy to interface with your product, or hook into annoying legacy test
software, or develop tests in a simpler way, etc.

## [rst](7): the requirements tracking tool made for developers
rst will be our bread and butter for writing
and linking components in our design, and then linking it with our code to track
how much of our project is implemented and tested. This tool was
designed specifically to facilitate the philosophy of software quality
presented in this book.

[1]: https://git-scm.com/
[2]: http://rosettacode.org/wiki/Documentation
[3]: https://doc.rust-lang.org/std/
[4]: http://www.sphinx-doc.org/en/1.5.1/
[5]: https://docs.python.org/3.6/library/unittest.html
[6]: http://doc.pytest.org/en/latest/
[7]: https://github.com/vitiral/rst

[30]: http://dpc.pw/cbuf-rs/cbuf/index.html
[31]: https://github.com/rust-lang-nursery/lazy-static.rs
