### ANTLR Python 3 Runtime
This is a vendored copy of the ANTLR Python 3 runtime. You can find
the [upstream copy here](https://github.com/antlr/antlr4/tree/master/runtime/Python3).

Modifications have been made for performance improvements and to remove
the XPath API, since Zoia doesn't need it. You can find all commits that
affect this vendored copy by opening `gitk` and searching for
`[antlr-change]`. The reason none of these changes got upstreamed is that
ANTLR requires contributors to sign a CLA with their full legal name. I don't
want to doxx myself, so that's not happening.

You can simply delete this directory to use the site-packages version of the
ANTLR runtime, but Zoia's performance will drop by about 20% if you do.
