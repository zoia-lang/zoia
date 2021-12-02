# Zoia

[![CI](https://github.com/Infernio/zoia/actions/workflows/ci.yaml/badge.svg)](https://github.com/Infernio/zoia/actions/workflows/ci.yaml)
[![Coverage Status](https://coveralls.io/repos/github/Infernio/zoia/badge.svg?branch=dev)](https://coveralls.io/github/Infernio/zoia?branch=dev)
[![License: GPLv3](https://img.shields.io/badge/license-GPLv3-blue.svg)](LICENSE)

A language for writing fiction.

## Status & Agenda
- [x] Write a grammar
- [x] Create a functional lexer/parser via ANTLR
- [x] Implement AST node classes
- [x] Write a converter (parse tree -> AST)
- [x] Implement canonical reprs for all AST nodes
- [x] Come up with some tests for the lexer, parser and canonical repr
- [x] Experiment with AO3 (the primary output target) drafts:
  - [x] What's the nicest output format? One file, multiple files? -> multiple HTML files
  - [x] What about summaries and author notes? -> separate files per chapter
  - [x] And all the other stuff (warnings, tags, etc.)? -> not useful (esp. for warnings, which are radio buttons)
  - [ ] Revisit later: What about work summaries/notes? E.g. [this fic](https://archiveofourown.org/works/24293356/chapters/58558123) has:
    - A work summary
    - Author notes at the beginning of the work
    - Author notes at the end of the work
    - A summary on the first chapter
    - Author notes at the end of the first chapter
  - But the AO3 form only has three boxes for entering a summary and 2x notes
  - Probably can't figure this out without actually posting a fic, hence revisit later
  - Work off the assumption that we'll potentially put out three extra files for work summaries and notes
- [x] Come up with a mockup for a project layout (src, build, config, etc.)
- [ ] Come up with mockup classes to model this (series, story, chapter)
- [ ] Model how we want the whole system to process our nodes (rough draft):
  - [ ] 1. Parse aliases
  - [ ] 2. Parse dict
  - [ ] 3. Insert fragments
  - [ ] 4. Resolve aliases (repeat until no more alias nodes left)
  - [ ] 5. Evaluate lines top to bottom, left to right.
           Commands get executed here, resolving either to text fragments
           or to nothing at all (in which case they probably have side effects).
  - [ ] 6. Once a line is evaluated, combine all text fragments
  - [ ] 7. Keep combining fragments together (newlines become spaces, similar
           to HTML) until we hit a double newline or a breaking command - that
           marks the end of a paragraph
- [ ] Consider other types of HTML markup and how to integrate those
- [ ] Write a user-friendly CLI for setting up a new project, creating new
      chapters, etc.
- [ ] Come up with a good way to deploy this on Linux
- [ ] Bonus credit: same thing, but on Windows (ugh)

## Name
Named after [Zoia Markovna Horn](https://en.wikipedia.org/wiki/Zoia_Horn),
an American librarian and advocate for intellectual freedom.

## License
Zoia itself is licensed [under the GPLv3](LICENSE).

This does not extend to fiction you write using it, nor does it extend to
the output generated from such fiction once Zoia compiles it. You may
license such data however you like.
