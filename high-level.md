# High Level Requirements and Specifications
Once you know the purpose of your project, it is important for you to write
down the approach you plan to take, as well as list a few alternative
approaches. This is important because:
- There may be gaps of when you work on your project. If you go on vacation
    for a month, having a reference of your thoughts at the time you were
    focused can jumpstart your productivity when you return.
- It is important to be able to reference a design doc for new contributors
    and newbie developers, it helps them understand the design process
    as a whole.

Your high level requirements should go in "README.md", just below your purpose
section:

```
## High Level Design

### Execution Method

The minimum viable product shall be a command line utility that is given the
path to one or more question files, as detailed in "User Configuration", as
arguments.

Additional arguments will include:
- `-t`: specify the time allowed for each question
- `-T`: specify the total time allowed for the whole quiz
- `-r NUM`: repeat questions only a certain number of times.
    By default there is no limits.

The program will ask one question at a time, recording how many answers
the user got correct/incorrect.

When the program is complete:
- time taken, broken up by whole quiz and each question
- the user's score

### Question File Format
The user shall be able to easily configure the quiz questions through a simple
csv format consisting of two columns: the question and the answer.
```

Again, just like the purpose documentation, this documentation aims to be
brief and help you during your design process. By writing documentation

