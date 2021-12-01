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

// An arbitrary combination of text fragments, aliases and commands.
// Must be ended by a newline, may be marked up with asterisks.
line: lineElements? Newline;
lineElements: (markedUpLineElements | regularLineElements)+;
regularLineElements: lineElement+;
lineElement: textFragment | alias | command;

// One or more line elements, surrounded by 1-3 asterisks.
markedUpLineElements: boldItalicLineElements
                      | boldLineElements
                      | italicLineElements;
boldItalicLineElements: Asterisk Asterisk Asterisk
                        regularLineElements
                        Asterisk Asterisk Asterisk;
boldLineElements: Asterisk Asterisk
                  regularLineElements
                  Asterisk Asterisk;
italicLineElements: Asterisk regularLineElements Asterisk;

// An arbitrary combination of words and spaces.
textFragment: (word | Space)+;

// One or more characters.
word: Char+;

// An at sign followed by a word.
alias: '@' word;

// A backslash and a word, followed optionally by an argument list.
// May optionally be ended by a vertical bar (this is necessary when
// using an argumentless command that you don't want a space after.
// For example, '\atmyHandle' would be parsed as a single command
// named 'atMyHandle', which doesn't exist. '\at|myHandle' would be
// parsed as a command named 'at' and a text fragment 'myHandle'.
command: '\\' word arguments? '|'?;

// One or more arguments. Multiple arguments must be separated by
// semicolons. Trailing semicolons are allowed.
// The whitespace handling here is ugly grammar-wise, but should be
// fairly intuitive when actually using the language.
arguments: '[' whitespace* argument (';' whitespace* argument)*? ';'?
           whitespace* ']';

// Either a text fragment or a word, an equals sign and a text
// fragment.
argument: kwdArgument | stdArgument;
kwdArgument: word Space* '=' Space* lineElements;
stdArgument: lineElements;

// Any kind of whitespace: newlines, spaces, tabs, etc.
whitespace: (Newline | Space)+;

/* ==== LEXER ==== */
// Skip all comments.
COMMENT: '#' ~[\r\n]* -> skip;

// Tokens
Asterisk: '*';
Newline: ('\r\n' | '\r' | '\n');
// See https://unicode.org/reports/tr44/#General_Category_Values
Space: [\p{Z}];
Char: [\p{L}\p{M}\p{N}\p{P}\p{S}\p{C}];
