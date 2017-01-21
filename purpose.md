# Purpose Documentation
One of the most critical pieces of documentation that you can write is
your purpose documentation. Without purpose documentation, it is easy
to get lost in the web of your project and forget what you were trying
to accomplish in the first place. Also, purpose documentation that is
revision controlled will give you a handy reference for why you did certain
things in the past. As your project adapts and changes (and it will), so
should your purpose documentation.

Open up your README.md in your favorite plain-text editor and write
out the following by hand (don't copy paste):

```
## Purpose:
Write a flash card quizzer from scratch and learn about quality best
practices while doing so.

The example tutorial can be found here:
    http://wiki.openhatch.org/Flash_card_challenge

It should be easy for users to input questions to the quizzer in a
simple and open format. Additionally, the program should use
methodologies that uses effective memorization techniques. Some
possible ideas include:
- doing items in a random order
- doing missed items more often
- telling the answer after a guess is missed
- allowing users to configure time limits, so they can compare
    results between quizzes.
```

Notice that we try to keep our purpose documentation as brief and simple
as possible. This is important for all documents, but is especially important
for high level. There is a basic rule: documentation that is not brief
and clear will not be read -- it will be skimmed. Skimmed documentation will
not get it's meaning across and will hamper your project
instead of help it. Make sure to always go back to your docs and try to make
them simpler and reflect the purpose of the project more plainly. You will
thank yourself for it in the future.

> ### Exercise 1:
> break down the purpose documentation above into some high level
> requirements. Then give a high level specification for how you
> would approach those requirements. What programming language would you use?
> What libraries would you use? What would be your overall approach to
> each problem?

> ### Exercise 2:
> Assume your program ui would be over the command line. What kind of arguments
> and user configuration would you accept? Would you let the user use only
> one quiz file at a time, or use multiple of them? Write down your answers.

> ### Exercise 3:
> Skim through the [markdown format][1] specification. Markdown is a great
> format for keeping docs, since it allows you to write docs in plain text
> (so they can be revision controlled) but the simple formatting rules
> render beautifully on sites like github.
>
> Markdown is easy to learn, easy to read and has become the defacto standard
> for writing docs among open source projects.

[1]: https://gitbookio.gitbooks.io/markdown/content/
