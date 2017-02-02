
We will now put what we have built together into an actual
command line application.

The design is already laid out for us, all we need is
the implementation.

> ##### Exercise 1:
> Implement an MVP of the  command line interface using python's
> [argparse][1] library. You don't need to implement all the flags.
>
> Remember that it is defined in `SPC-cmd`.

Here is one implementation.

Add the following to `flash/__init__.py`
```
from __future__ import print_function

import argparse

from flash import quiz
from flash import load


def ask_question(question):
    """ask a question of the user, returning True if the answer is
    correct."""
    answer = raw_input("{}?: ".format(question.question)).strip().lower()
    return answer == question.answer


def main(cwd, argv):
    parser = argparse.ArgumentParser(
        prog='flash',
        description='flash card quizzer')
    parser.add_argument('file', help='csv file to get quiz questions from')
    args = parser.parse_args(argv[1:])

    questions = load.load_path(args.file)
    answered = quiz.Answered()
    print("Starting Quiz {}. Press Ctrl+C to quit.".format(args.file))
    while True:
        question = quiz.get_question(questions, answered)
        result = ask_question(question)
        if result:
            print("* Correct! Good job\n")
        else:
            print("X Incorrect. The correct answer is: ", question.answer, "\n")
        answered.record(question, result)
```

Now create a file at `bin/flash` and write the following:
```
#!/usr/bin/python2

import os
import sys
import flash

if __name__ == '__main__':
    flash.main(os.getcwd(), sys.argv)
```

Then run the following:

> note: `export` won't work on Windows. Instead run the following
> or see [this guide][2]:
> ```
set PYTHONPATH=%PYTHONPATH%;%cd%
```

```
export PYTHONPATH=$(pwd)
python bin/flash capitols.csv
```

> note: for linux you can also make `bin/flash` executable with
> `chmod a+x bin/flash` and then you don't need `python` in
> front of it.

Congratulations! You have designed, developed and tested a full blown
application.

[1]: https://docs.python.org/2.7/library/argparse.html
[2]: http://stackoverflow.com/questions/3701646
