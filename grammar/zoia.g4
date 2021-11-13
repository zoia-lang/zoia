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

zoiaFile: EOF;

/* ==== LEXER ==== */
// Skip all comments.
COMMENT: '#' ~[\r\n]* -> skip;

// Tokens
Asterisk: '*';
At: '@';
Backslash: '\\';
Comma: ',';
Equals: '=';
LeftBracket: '[';
RightBracket: ']';

// Ignore whitespace.
WHITESPACE: [ \t\n\r]+ -> skip;
