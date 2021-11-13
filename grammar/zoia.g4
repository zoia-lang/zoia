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
header: '\\header' arguments Newline;

// An arbitrary combination of text fragments, commands and
// spaces. Must be ended by a newline.
line: (textFragment | command | Space)* Newline;

// An arbitrary combination of words and aliases.
textFragment: (Word | alias)+;

// An at sign followed by a word.
alias: '@' Word;

// A backslash and a word, followed optionally by an argument list.
// May optionally be ended by a vertical bar (this is necessary when
// using an argumentless command that you don't want a space after.
// For example, '\atmyHandle' would be parsed as a single command
// named 'atMyHandle', which doesn't exist. '\at|myHandle' would be
// parsed as a command named 'at' and a text fragment 'myHandle'.
command: '\\' Word arguments? '|'?;

// One or more arguments. Multiple arguments must be separated by
// commas. Trailing commas are allowed.
// The whitespace handling here is ugly grammar-wise, but should be
// fairly intuitive when actually using the language.
arguments: '[' whitespace* argument Space* (',' whitespace* argument)* Space* ','? whitespace* ']';

// Either a text fragment or a word, an equals sign and a text
// fragment.
argument: kwdArgument | stdArgument;
kwdArgument: Word Space* '=' Space* textFragment;
stdArgument: textFragment; // TODO unnecessary?

whitespace: (Newline | Space)+;

/* ==== LEXER ==== */
// Skip all comments.
COMMENT: '#' ~[\r\n]* -> skip;

// Tokens
Newline: ('\r\n' | '\r' | '\n');
Space: (' ' | '\t');
Word: [A-Za-z0-9]+; // TODO unicode
// Asterisk: '*';
