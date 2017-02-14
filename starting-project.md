The primary teaching method that this book will employ is "learning by doing".
This is an approach that many developers are familiar with and is used in some
of the most effective tutorials on software development.

The example project used will be the same as the one used in the [artifact][1] tutorial.
This makes sense because I am also the author of that tool and it was designed
*specifically* to address the approach to quality defined in this book. We will
install artifact in a later chapter, but just know that while there is definitely
overlap between the two tutorials, they have very different purposes: artifact's
tutorial is designed to teach the tool, while this is an in-depth tutorial
to unifying quality best practices.

The project we will be implementing is the [flash card challenge][2] created
by open hatch. There are several reasons this project was chosen:
- It has a clear goal with targeted users
- It is simple to define and yet can be extremely broad
- The guide is written in python, a language who's syntax reads largely
    like psuedo code. You should be able to follow along in any language

One of the best tutorials on C, [learn C the hard way][3] has this to
say about itself:

> [This tutorial] teaches real robust C coding and defensive programming tactics on real
> hardware rather than abstract machines and pedantic theory. The book
> emphasizes breaking your code on purpose, and in the process teaches a
> plethora of important topics.

There are three important aspects to the "Learn The Hard Way" method that
this tutorial will use:
1. It is designed for absolute beginners: you should know the basics of a
    programming language and revision control, and that's all you need.
2. It focuses on teaching concepts and tools which are simple and deliver
    immediate real-world value.
3. It uses exercises as the primary method that you learn. Only by actually
    doing them will you understand how the tools and processes you are reading
    are useful.

## Before we start

Before we start, install the following tools:
- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [artifact](https://github.com/vitiral/artifact/wiki/User-Guide)

Now run the following:
```
mkdir ~/quality # or whatever directory you want
cd ~/quality
art tutorial
git init
```

This will set up your project as a art tutorial project and initialize git.

> ##### Exercise 1:
> Create a `README.md` file and take notes while you read the
> [flash card challenge][2] webpage. Pay close attention to:
> - what is the use case (how will this software be used)?
> - what are the inputs/outputs as presented?
>
> Then write a paragraph answering the question "how would I develop
> this application, knowing only what I know now?"

[1]: https://github.com/vitiral/artifact
[2]: http://wiki.openhatch.org/Flash_card_challenge
[3]: https://learncodethehardway.org/c/
