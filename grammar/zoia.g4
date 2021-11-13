// TODO Do we need line continuations?

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
header: '\\header' arguments;

// An arbitrary combination of text fragments and commands. Must be
// ended by a newline.
line: (textFragment | command)* Newline;

// Anything but a command.
textFragment: 'foo'; // TODO

// A backslash, followed optionally by an argument list.
// May optionally be ended by a vertical bar (this is necessary when
// using an argumentless command that you don't want a space after.
// For example, '\atmyHandle' would be parsed as a single command
// named 'atMyHandle', which doesn't exist. '\at|myHandle' would be
// parsed as a command named 'at' and a text fragment 'myHandle'.
command: '\\' identifier arguments? '|'?;

// One or more arguments. Multiple arguments must be separated by
// commas. Trailing commas are allowed.
arguments: '[' argument (',' argument)* ','? ']';
argument: 'bar'; // TODO

identifier: 'qux'; // TODO

/* ==== LEXER ==== */
// Skip all comments.
COMMENT: '#' ~[\r\n]* -> skip;

// Tokens
Newline: ('\r\n'|'\r'|'\n');
// Asterisk: '*';
// At: '@';
// Equals: '=';

// Ignore whitespace.
WHITESPACE: [ \t]+ -> skip;
