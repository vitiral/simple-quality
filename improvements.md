We have completed our tutorial, but the flash quizzer is far from
finished. There are still many things that can be done before
it should be considered "complete".

## Basic Features That Can Be Added
1. export our design docs with `art export html`
2. host it on github using [github pages][5]
1. Make sure all items in the design are done by running
    `art ls -c '<99'`
2. Try running `art ls -t '<99'` -- this should show you that
    there are several items that we don't consider to be
    completely tested
3. Currently the user exits with `Cntrl+C`, which is fine.
    Try catching the [`KeyboardInterrupt`][1] exception
    and handling it more gracefully.
4. Speaking of exiting, we record how many answers
    a user got right and wrong, but we don't print out
    any kind of report on exiting! Add requirements
    for doing so (can just go in purpose if you want)
    and implement that.
5. Users should also be able to store their report in
    a log file -- add a flag for that.
6. There are several flags designed in `SPC-cmd`
    that were not implemented

## Integration Tests
There are currently no tests designed or implemented
which test the end-to-end functionality of the
application.

Here is one approach to do integration testing this
application:
1. Rather than using `print`, pass in a [`StringIO`][2]
    object into `main` and write to it.
    `flash/bin` then passes in `sys.stdout`.
2. Create method `get_input()` in `flash/__init__.py` that
    just makes a call to `raw_input()`. Use that
    method in `main(...)` instead of `raw_input()`
3. [Mock][3] out `get_input()` using `mock.patch(...)` with
    `side_effect` being a closure that answers in
    an expected way.
4. You now have complete control over the inputs
    and outputs to your program and can record
    the questions asked by modifiying variables inside
    your closure.
5. Keep track of questions asked, make assertions
    for how often items get asked, answer some
    questions incorrectly and assert the format
    is correct, etc.
6. Make sure the closure raises an (expected)
    exception after a certain number of questions
    have been asked it.

Integration test design is typically something that should
go into your `design` folder, as they involve multiple
pieces of disparate code. Make sure *what* you will
test gets added.

## System Tests

You can can create system tests using a library
like [expect][4], but that is probably more complication than
you need for this application.

Any system tests should *definitely* go in your `design` folder.

[1]: https://docs.python.org/2/library/exceptions.html#exceptions.KeyboardInterrupt
[2]: https://docs.python.org/2/library/stringio.html
[3]: https://docs.python.org/dev/library/unittest.mock.html
[4]: https://pexpect.readthedocs.io/en/stable/
[5]: https://github.com/vitiral/artifact/blob/master/docs/ExportingHtml.md

