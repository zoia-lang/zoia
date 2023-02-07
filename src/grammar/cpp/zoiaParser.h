
// Generated from grammar/zoia.g4 by ANTLR 4.11.1

#pragma once


#include "antlr4-runtime.h"




class  zoiaParser : public antlr4::Parser {
public:
  enum {
    COMMENT = 1, Asterisk = 2, Backslash = 3, Bar = 4, BracketsClose = 5,
    BracketsOpen = 6, Equals = 7, Header = 8, Newline = 9, Semicolon = 10,
    Spaces = 11, Alias = 12, Word = 13
  };

  enum {
    RuleZoiaFile = 0, RuleHeader = 1, RuleLine = 2, RuleLineElements = 3,
    RuleLineElementsInner = 4, RuleLineElementsArg = 5, RuleEm3LineElement = 6,
    RuleEm2LineElement = 7, RuleEm1LineElement = 8, RuleTextFragment = 9,
    RuleTextFragmentWord = 10, RuleAlias = 11, RuleCommand = 12, RuleArguments = 13,
    RuleArgument = 14, RuleKwdArgument = 15, RuleStdArgument = 16, RuleWhitespace = 17
  };

  explicit zoiaParser(antlr4::TokenStream *input);

  zoiaParser(antlr4::TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options);

  ~zoiaParser() override;

  std::string getGrammarFileName() const override;

  const antlr4::atn::ATN& getATN() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;


  class ZoiaFileContext;
  class HeaderContext;
  class LineContext;
  class LineElementsContext;
  class LineElementsInnerContext;
  class LineElementsArgContext;
  class Em3LineElementContext;
  class Em2LineElementContext;
  class Em1LineElementContext;
  class TextFragmentContext;
  class TextFragmentWordContext;
  class AliasContext;
  class CommandContext;
  class ArgumentsContext;
  class ArgumentContext;
  class KwdArgumentContext;
  class StdArgumentContext;
  class WhitespaceContext;

  class  ZoiaFileContext : public antlr4::ParserRuleContext {
  public:
    ZoiaFileContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    HeaderContext *header();
    antlr4::tree::TerminalNode *EOF();
    std::vector<LineContext *> line();
    LineContext* line(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  ZoiaFileContext* zoiaFile();

  class  HeaderContext : public antlr4::ParserRuleContext {
  public:
    HeaderContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Header();
    ArgumentsContext *arguments();
    antlr4::tree::TerminalNode *Newline();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  HeaderContext* header();

  class  LineContext : public antlr4::ParserRuleContext {
  public:
    LineContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Newline();
    LineElementsContext *lineElements();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  LineContext* line();

  class  LineElementsContext : public antlr4::ParserRuleContext {
  public:
    LineElementsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<TextFragmentContext *> textFragment();
    TextFragmentContext* textFragment(size_t i);
    std::vector<AliasContext *> alias();
    AliasContext* alias(size_t i);
    std::vector<CommandContext *> command();
    CommandContext* command(size_t i);
    std::vector<Em1LineElementContext *> em1LineElement();
    Em1LineElementContext* em1LineElement(size_t i);
    std::vector<Em2LineElementContext *> em2LineElement();
    Em2LineElementContext* em2LineElement(size_t i);
    std::vector<Em3LineElementContext *> em3LineElement();
    Em3LineElementContext* em3LineElement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  LineElementsContext* lineElements();

  class  LineElementsInnerContext : public antlr4::ParserRuleContext {
  public:
    LineElementsInnerContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    TextFragmentWordContext *textFragmentWord();
    std::vector<AliasContext *> alias();
    AliasContext* alias(size_t i);
    std::vector<CommandContext *> command();
    CommandContext* command(size_t i);
    std::vector<TextFragmentContext *> textFragment();
    TextFragmentContext* textFragment(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  LineElementsInnerContext* lineElementsInner();

  class  LineElementsArgContext : public antlr4::ParserRuleContext {
  public:
    LineElementsArgContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    TextFragmentWordContext *textFragmentWord();
    std::vector<AliasContext *> alias();
    AliasContext* alias(size_t i);
    std::vector<CommandContext *> command();
    CommandContext* command(size_t i);
    std::vector<Em1LineElementContext *> em1LineElement();
    Em1LineElementContext* em1LineElement(size_t i);
    std::vector<Em2LineElementContext *> em2LineElement();
    Em2LineElementContext* em2LineElement(size_t i);
    std::vector<Em3LineElementContext *> em3LineElement();
    Em3LineElementContext* em3LineElement(size_t i);
    std::vector<TextFragmentContext *> textFragment();
    TextFragmentContext* textFragment(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  LineElementsArgContext* lineElementsArg();

  class  Em3LineElementContext : public antlr4::ParserRuleContext {
  public:
    Em3LineElementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Asterisk();
    antlr4::tree::TerminalNode* Asterisk(size_t i);
    LineElementsInnerContext *lineElementsInner();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  Em3LineElementContext* em3LineElement();

  class  Em2LineElementContext : public antlr4::ParserRuleContext {
  public:
    Em2LineElementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Asterisk();
    antlr4::tree::TerminalNode* Asterisk(size_t i);
    LineElementsInnerContext *lineElementsInner();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  Em2LineElementContext* em2LineElement();

  class  Em1LineElementContext : public antlr4::ParserRuleContext {
  public:
    Em1LineElementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Asterisk();
    antlr4::tree::TerminalNode* Asterisk(size_t i);
    LineElementsInnerContext *lineElementsInner();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  Em1LineElementContext* em1LineElement();

  class  TextFragmentContext : public antlr4::ParserRuleContext {
  public:
    TextFragmentContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Word();
    antlr4::tree::TerminalNode *Spaces();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  TextFragmentContext* textFragment();

  class  TextFragmentWordContext : public antlr4::ParserRuleContext {
  public:
    TextFragmentWordContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Word();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  TextFragmentWordContext* textFragmentWord();

  class  AliasContext : public antlr4::ParserRuleContext {
  public:
    AliasContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Alias();
    antlr4::tree::TerminalNode *Bar();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  AliasContext* alias();

  class  CommandContext : public antlr4::ParserRuleContext {
  public:
    CommandContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Backslash();
    antlr4::tree::TerminalNode* Backslash(size_t i);
    antlr4::tree::TerminalNode *Word();
    ArgumentsContext *arguments();
    antlr4::tree::TerminalNode *Bar();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  CommandContext* command();

  class  ArgumentsContext : public antlr4::ParserRuleContext {
  public:
    ArgumentsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *BracketsOpen();
    std::vector<ArgumentContext *> argument();
    ArgumentContext* argument(size_t i);
    antlr4::tree::TerminalNode *BracketsClose();
    std::vector<WhitespaceContext *> whitespace();
    WhitespaceContext* whitespace(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Semicolon();
    antlr4::tree::TerminalNode* Semicolon(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  ArgumentsContext* arguments();

  class  ArgumentContext : public antlr4::ParserRuleContext {
  public:
    ArgumentContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    KwdArgumentContext *kwdArgument();
    StdArgumentContext *stdArgument();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  ArgumentContext* argument();

  class  KwdArgumentContext : public antlr4::ParserRuleContext {
  public:
    KwdArgumentContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Word();
    antlr4::tree::TerminalNode *Equals();
    LineElementsArgContext *lineElementsArg();
    std::vector<antlr4::tree::TerminalNode *> Spaces();
    antlr4::tree::TerminalNode* Spaces(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  KwdArgumentContext* kwdArgument();

  class  StdArgumentContext : public antlr4::ParserRuleContext {
  public:
    StdArgumentContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    LineElementsArgContext *lineElementsArg();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  StdArgumentContext* stdArgument();

  class  WhitespaceContext : public antlr4::ParserRuleContext {
  public:
    WhitespaceContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Newline();
    antlr4::tree::TerminalNode* Newline(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Spaces();
    antlr4::tree::TerminalNode* Spaces(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  WhitespaceContext* whitespace();


  // By default the static state used to implement the parser is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:
};
