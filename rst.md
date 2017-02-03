
Before we do anything else, let's start using git to track
our progress. Since rst tracks design docs which are written
in plain text, you can (and should) use revision control to
track the evolution of your design documents.

> Note: you should have already [set up your project](starting-project.md)

```
git add README.md
git commit -m "add README.md"
```

This will add the progress you have made so far to git and allow
us to track our progress.

> ### Exercise 1:
> git is a fantastic tool, but it is beyond the scope of this guide
> to give a full tutorial on git or revision control in general.
> Before proceeding with this guide any further, it is recommended
> you go through the [git tutorial][1]
>
> you can always type `git COMMAND -h` to get help on any command
>
> The rest of the tutorial will assume you have a working knowledge
> of git commands and what their purpose is

## rst tutorial
The rst tutorial and this book have been developed together to
work off of each other. Therefore, we are going to use the
interactive tutorial provided by rst and then build off of it.

There are a few modifications you will want to make to the tutorial:
- before continuing onto the next stage, always commit the changes
    you've made to git.
- take notes during the process at the top of your README and be
    sure to include them in your repository.

If you have already completed the rst tutorial, it is safe for you
to just run `rst tutorial 4` and continue from there. If you have
not gone through it, it is very short and was specifically crafted
to fit into this guide. Therefore it is essential that you go through rst's
tutorial in full before continuing.

> ### Exercise 1:
> when you ran `rst tutorial` in the [Starting Project](starting-project.md)
> section, rst launched a `tutorial.toml` file which is a self-documenting
> design file. Read through it and follow the instructions.
>
> The next stage, `rst tutorial 2`, will launch a `tutorial.md` file
> which can also be [viewed on the web][2]. Read through it and
> follow the instructions until you have completed through part 5 (all of it)

## running your tests

Roll back the tutorial and commit your changes.
```
rst tutorial 4
git add *
git commit -m "continuing quality book tutorial"
```

Also, add `*.pyc` to your `.gitignore` file to ignore the python compiled files.

We are running the tutorial in part 4 so that there are no
errors when we are starting out (part 5 is about debugging errors).

If you followed along with the rst interactive tutorial, you should
feel pretty confident by now that our load component is well designed
and *should* be implemented and tested. However, you haven't actually run any
code yet, so you can't be sure! We are going to change that.

The first thing you need to do is make sure you are running python2.7. Running:
```
python --version
pip --version
```

Should return something like:
```
Python 2.7.13
pip 9.0.1 from /usr/lib/python2.7/site-packages (python 2.7)
```

As long as they are both python2.7.X (but not python3.X), you are good to go.

> If not... python can be very difficult to configure.
> Search on google for how to have both python2 and python3 installed. You will
> have to do a similar exercise for `pip`.

> If it is too much of a pain, you can also just use python3 (or any other language),
> it shouldn't be difficult -- you will just have to fix any errors that come up.
>
> If you are using another language, refer to that language's unit testing guide.

Now install py.test:
```
pip install pytest
```
> you may need to use `sudo`

And run your unit tests:
```
py.test flash
```

Congratulations, you've run unit tests!

[1]: https://git-scm.com/doc
[2]: https://github.com/vitiral/rst/blob/master/src/cmd/data/tutorial.md
