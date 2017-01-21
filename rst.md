# Using rst

Before we do anything else, let's start using git to track
our progress. Since rst tracks design docs which are written
in plain text, you can (and should) use revision control to
track the evolution of your design documents.

[Install git][1] and type:
```
git init
git add README.md
git commit -m "add README.md"
```

This will add the progress you have made so far to git and allow
us to track our progress.

> ### Exercise 1:
> git is a fantastic tool, but it is beyond the scope of this guide
> to give a full tutorial on git or revision control in general.
> Before proceeding with this guide any further, it is recommended
> you go through the [git documentation][2]
>
> you can always type `git COMMAND -h` to get help on any command
>
> The rest of the tutorial will assume you have a working knowledge
> of git commands and what their purpose is

## rst tutorial

Head over to rst's [User Guide][3] and install rst. Read through
the "hello world" introduction to get a basic overview of what
the tool allows you to do, and then head over to the
[In Depth Guide][4].

The rst tutorial and this book have been developed together to
work off of eachother. Therefore, we are going to use the
interactive tutorial provided by rst and then build off of it.

There are a few modifications you will want to make to the tutorial:
- before continuing onto the next stage, always commit the changes
    to git.
- take notes during the process at the top of your README and be
    sure to include them in your repository.

If you have already completed the rst tutorial, it is safe for you
to just type `rst tutorial 5` and continue from there. If you have
not gone through it, it is very short and was specifically crafted
to fit into this guide and covers:
- starting a project with rst, enabling design to be a trackable
    and scalable first class citizen throughout the entire
    project.
- how to write high level requirements which link to your purpose
    requirements
- how to write high level specifications which link to your
    requriements
- writing detailed design specifications which link to your
    requirements, and then linking your specifications to your
    actual implementation (your code) -- which also tracks your
    progress (% done).
- writing test design which links to your specifications, and then
    linking them to the tests you have written in code. This also
    tracks your progress (% tested)

Therefore it is essential that you go through rst's tutorial in full
before continuing.

> ### Exercise 1:
> commit your changes and then run run `rst tutorial`.
>
> rst will launch a `tutorial.toml` file which is a self-documenting
> design file. Read through it and follow the instructions.
>
> The next stage, `rst tutorial 2`, will launch a `tutorial.md` file
> which can also be [viewed on the web][5]. Read through it and
> follow the instructions

[1]: https://git-scm.com/
[2]: https://git-scm.com/doc
[3]: https://github.com/vitiral/rst/wiki/User-Guide
[4]: https://github.com/vitiral/rst/wiki/In-Depth-Guide
[5]: https://github.com/vitiral/rst/blob/master/src/cmd/data/tutorial.md
