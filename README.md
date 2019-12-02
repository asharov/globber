# Globber

[![Build Status](https://travis-ci.com/asharov/globber.svg?branch=master)](https://travis-ci.com/asharov/globber)
[![codecov](https://codecov.io/gh/asharov/globber/branch/master/graph/badge.svg)](https://codecov.io/gh/asharov/globber)
![PyPI](https://img.shields.io/pypi/v/globber)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Globber is a Python library for matching file names against
glob patterns. In contrast to other glob-matching libraries,
it matches arbitrary strings and doesn't require the matched
names to be existing files. In addition, it supports the
globstar `**` operator to match an arbitrary number of path
components.

I have been working with Git repositories, specifically trying
to process files classified as source. Picking the source files
is much easier with globstar expressions, and since old files
might no longer exist on the file system, the matching cannot
be based on actual files. I couldn't find anything that had
support for both, so I wrote this library.

## Patterns

The syntax of a pattern is a sequence of components, separated
by slashes `/`. Each component may include the following
special characters:

Character | Meaning
----------|--------
?         | Match any single character (not a path separator)
\*        | Match any sequence of characters, possibly empty (except path separators)
\**       | Must appear alone inside a component. Match any sequence of components, possibly empty
\         | Match the following character literally. This is intended to escape the special characters

## Contributing

I may occasionally keep working on this library if I have a need
for new functionality, but for the moment it is good enough for
my current needs. If you're using it, and find bugs or want
some new functionality, you're welcome to open an issue. Pull
requests are also appreciated but not necessary to get your
concerns heard.

## License

Globber is licensed under the Apache Software License, version
2.0. See the LICENSE file for precise license terms and
conditions.
