Before we design and implement the quiz component, let's take stock
of where we are. We have:
- functions that can load from either a path or a stream (file-object)
- a large number of (passing!) unit tests for loading
- high level requirements for our application and the quizzer itself
- a "Question" class that we can build off of

Here are a few rules to good design that the load component followed
well:
- it verified data before passing it to the layer above it
- it converted data into an object. This makes it harder to have
    errors like InvalidKey, etc.

Some things it did not do well:
- it didn't run any linters or formatters

We are going to fix the problems before we continue onto the
next section.

## Code Sanitation
Before continuing, we want our code to be sanitary.

First we need to install the tools:
```
pip install pylint docformatter autopep8
```

Now we will use them. First, run the linter with `pylint flash`,
the top of the output should look something like:
```
No config file found, using default configuration
************* Module flash.load
R: 10, 0: Too few public methods (1/2) (too-few-public-methods)
C: 42, 8: Invalid variable name "q" (invalid-name)
C: 50, 0: Invalid argument name "f" (invalid-name)
C: 69,29: Invalid variable name "f" (invalid-name)
************* Module flash.tests.test_load
C:  1, 0: Missing module docstring (missing-docstring)
C:  7, 0: Invalid constant name "script_dir" (invalid-name)
C: 10, 0: Missing class docstring (missing-docstring)
C: 72, 4: Missing method docstring (missing-docstring)
```

The pylint tool looks at your code an compares it to the
[pep8 style guide][1]. There are multiple reasons to follow your
language's style guide:
- typically the style enforced by the guide is well thought out
	and the most clear method of doing any particular thing
- standardization is good -- it makes your team's code more readable
    and writable by everybody involved
- documentation is good. It allows people who are reading your code to at
    least know what you were *trying to do* (even if you did a bad job
    actually doing it!)

> ### Exercise 1:
> fix all the `missing-docstring` pylint errors by documenting
> what the tests do (read their code first!)
>
> Now fix the invalid-name errors (need to be more than one char)
> and constants need to be `LIKE_THIS`

Now that we have fixed most lint errors, run your unit tests
(making sure none fail) and commit your changes. Doing small
commits is always recommended as you can always edit your commit
history later. Think of them like "savepoints" in a video game.
Keep in mind that you can always re-write your commit history to
be more readable later (as long as you don't push).

Now we are going to auto-format our code. Run
`autopep8 flash -r --in-place` and run `git diff` to see what it changed.
Autoformatters are a great way to remove the pain in having standardized
code.

Commit those changes. Now run `docformatter flash -r --in-place` and then
`git diff`. You will see that your docstrings are now all standardized.

Commit your changes. There is one final thing we should do, and that
is format your requirements. Run `rst fmt -w`. This will format and
alphabetize all your design documents (and remove comments, which
[is a bug][3])

Commit these changes. You are now using industry best practices for
code cleanliness - your future team mates will thank you! Let's continue
onto the next section where we will actually build a component from
scratch.

[1]: https://www.python.org/dev/peps/pep-0008/
[2]: http://pylint-messages.wikidot.com/all-codes
[3]: https://github.com/vitiral/rst/issues/23
