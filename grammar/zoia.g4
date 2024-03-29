// Style guide:
//  - Parser rules are camelCase
//  - Lexer rules are PascalCase
//    - Exception: fragments and skips (i.e. ones that users will
//      _never_ see) are entirely uppercase.
//  - Wrap to 70 characters
//  - If a token has a single usage, move it up to its usage in the
//    parser. Saves a line. Exception is if the definition is long or
//    complex.

grammar zoia;

/* ==== PARSER ==== */
/* === BASICS === */
// The main entry point.
// A header, followed by any number of lines.
zoiaFile: header line* EOF;

// The special 'header' command. Must come first (barring whitespace
// and comments).
header: Header arguments Newline;

// An arbitrary combination of text fragments, aliases and commands.
// Must be ended by a newline, may be marked up with asterisks.
line: lineElements? Newline;
lineElements: (textFragment | alias | command | em1LineElement |
               em2LineElement | em3LineElement)+;
// The lineElements that may occur inside em*LineElements
// This prevents nested em*LineElements
lineElementsInner: (textFragmentWord | alias | command) (textFragment | alias | command)*;
// The lineElements that may occur inside *Arguments
// This resolves an ambiguity/context sensitivity by requiring that
// the first text fragment not start with spaces.
lineElementsArg: (textFragmentWord | alias | command |
                  em1LineElement | em2LineElement | em3LineElement)
                 (textFragment | alias | command |
                  em1LineElement | em2LineElement | em3LineElement)*;

// One or more line elements, surrounded by 1-3 asterisks.
em3LineElement: Asterisk Asterisk Asterisk
                lineElementsInner
                Asterisk Asterisk Asterisk;
em2LineElement: Asterisk Asterisk lineElementsInner Asterisk Asterisk;
em1LineElement: Asterisk lineElementsInner Asterisk;

// Either a word or any number of spaces
textFragment: Word | Spaces;
// Version of textFragment that can only resolve to a word.
textFragmentWord: Word;

// An alias is an at sign followed by (potentially Unicode) letters
// and/or numbers (but no punctuation). May optionally be ended by a
// vertical bar (this is necessary when an alias is directly followed
// by letters, e.g. @A|s).
alias: Alias Bar?;

// A backslash and a word or backslash, followed optionally by an
// argument list. May optionally be ended by a vertical bar (this is
// necessary when using an argumentless command that you don't want a
// space after. For example, '\atmyHandle' would be parsed as a
// single command named 'atMyHandle', which doesn't exist.
// '\at|myHandle' would be parsed as a command named 'at' and a text
// fragment 'myHandle'.
command: Backslash (Word | Backslash) arguments? Bar?;

// One or more arguments. Multiple arguments must be separated by
// semicolons. Trailing semicolons are allowed.
// The whitespace handling here is ugly grammar-wise, but should be
// fairly intuitive when actually using the language.
arguments: BracketsOpen whitespace? argument
           (Semicolon whitespace? argument)*? Semicolon?
           whitespace? BracketsClose;

// Either a text fragment or a word, an equals sign and a text
// fragment.
argument: kwdArgument | stdArgument;
kwdArgument: Word Spaces? Equals Spaces? lineElementsArg;
stdArgument: lineElementsArg;

// Any kind of whitespace: newlines, spaces, tabs, etc.
whitespace: (Newline | Spaces)+;

/* ==== LEXER ==== */
// Skip all comments.
COMMENT: '#' ~[\r\n]* -> skip;

// Regular tokens
Asterisk: '*';
Backslash: '\\';
Bar: '|';
BracketsClose: ']';
BracketsOpen: '[';
Equals: '=';
Header: '\\header';
Newline: ('\r\n' | '\r' | '\n');
Semicolon: ';';

// See https://unicode.org/reports/tr44/#General_Category_Values
Spaces: [\p{Z}]+;
// Put aliases before words, so that ANTLR prefers a full alias
Alias: '@' [\p{L}\p{N}]+;
// Everything that isn't one of the tokens above.
Word: ~[\r\n@\\|[\];=*#\p{Z}]+;
