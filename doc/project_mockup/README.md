# Zoia Project Mockup
This is a mockup for what the layout of a typical Zoia project would look like.

## Full Layout
<pre>
├── <a href="#build">build</a>
│   └── work1
│       ├── ch1
│       │   ├── <a href="#notes_beginninghtml">notes_beginning.html</a>
│       │   ├── <a href="#notes_endhtml">notes_end.html</a>
│       │   ├── <a href="#summaryhtml">summary.html</a>
│       │   └── <a href="#texthtml">text.html</a>
│       ├── ch2
│       │   ├── <a href="#summaryhtml">summary.html</a>
│       │   └── <a href="#texthtml">text.html</a>
│       ├── <a href="#notes_beginninghtml">notes_beginning.html</a>
│       ├── <a href="#notes_endhtml">notes_end.html</a>
│       └── <a href="#summaryhtml">summary.html</a>
├── <a href="#src">src</a>
│   └── work1
│       ├── ch1
│       │   └── <a href="#mainzoia">main.zoia</a>
│       └── ch2
│           ├── <a href="#mainzoia">fight.zoia</a>
│           ├── <a href="#mainzoia">kiss.zoia</a>
│           └── <a href="#mainzoia">main.zoia</a>
├── <a href="#aliaseszoia">aliases.zoia</a>
├── <a href="#dictzoia">dict.zoia</a>
└── <a href="#zoiatoml">zoia.toml</a>
</pre>

## `src`
Contains the `.zoia` source files.

We always think in terms of series -> works -> chapters, even if we only have
one work and that work does not have multiple chapters. That way we simplify
the implementation and make it possible to change your mind at any time with
zero headaches.

### `main.zoia`
Each chapter contains one `main.zoia` file. That's the entry point. It's
evaluated from top to bottom and used to generate the output. It may make use
of other `.zoia` files, called 'fragments', to better split up a long chapter
(e.g. into scenes - chapter 2 here consists of two scenes, a fight
(`fight.zoia`) and a kiss (`kiss.zoia`), which the main file would link
together).

## `build`
This is where the generated output goes.

Output consists of between one and four HTML files per chapter. These contain
the HTML code that you then copy-paste into the AO3 post form. The files are
as follows:

### `notes_beginning.html`
The author notes for the start of the chapter. Only present if you entered
author notes via `\begin_notes_b`.

If the work itself has notes too (added via `\begin_work_notes_e`) then such
a file will also appear directly in the `workX` folder. See `work1` above.

### `notes_end.html`
The author notes for the end of the chapter. Only present if you entered
author notes via `\begin_notes_e`.

If the work itself has notes too (added via `\begin_work_notes_b`) then such a
file will also appear directly in the `workX` folder. See `work1` above.

### `summary.html`
The summary for this chapter. Only present if you entered a summary via
`\begin_summary`.

If the work itself has a summary too (added via `\begin_work_summary`) then
such a file will also appear directly in the `workX` folder. See `work1` above.

### `text.html`
The actual text of the chapter. What people will be reading, as opposed to the
metadata in the notes and summary files above.

## `aliases.zoia`
This file defines aliases and may not contain anything except alias
definitions (`\def_alias` commands). You can change the name using
[`zoia.toml`](#zoiatoml).

## `dict.zoia`
This file can be used to add words to the spellcheck dictionary and may not
contain anything except word additions (`\dict_add` commands). You can change
the name using [`zoia.toml`](#zoiatoml).

## `zoia.toml`
The config file for this Zoia project. Not sure what exactly this will include,
but at the very least this is where the names for the special aliases and dict
files can be customized.
