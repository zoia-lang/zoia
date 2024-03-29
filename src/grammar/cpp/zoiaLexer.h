
// Generated from grammar/zoia.g4 by ANTLR 4.11.1

#pragma once


#include "antlr4-runtime.h"




class  zoiaLexer : public antlr4::Lexer {
public:
  enum {
    COMMENT = 1, Asterisk = 2, Backslash = 3, Bar = 4, BracketsClose = 5,
    BracketsOpen = 6, Equals = 7, Header = 8, Newline = 9, Semicolon = 10,
    Spaces = 11, Alias = 12, Word = 13
  };

  explicit zoiaLexer(antlr4::CharStream *input);

  ~zoiaLexer() override;


  std::string getGrammarFileName() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const std::vector<std::string>& getChannelNames() const override;

  const std::vector<std::string>& getModeNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;

  const antlr4::atn::ATN& getATN() const override;

  // By default the static state used to implement the lexer is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:

  // Individual action functions triggered by action() above.

  // Individual semantic predicate functions triggered by sempred() above.

};
