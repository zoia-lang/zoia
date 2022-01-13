
// Generated from grammar/zoia.g4 by ANTLR 4.9.3

#pragma once


#include "antlr4-runtime.h"




class  zoiaParser : public antlr4::Parser {
public:
  enum {
    COMMENT = 1, Asterisk = 2, At = 3, Backslash = 4, Bar = 5, BracketsClose = 6,
    BracketsOpen = 7, Equals = 8, Header = 9, Newline = 10, Semicolon = 11,
    Space = 12, Word = 13
  };

  enum {
    RuleZoiaFile = 0, RuleHeader = 1, RuleLine = 2, RuleLineElements = 3,
    RuleRegularLineElements = 4, RuleLineElement = 5, RuleMarkedUpLineElements = 6,
    RuleBoldItalicLineElements = 7, RuleBoldLineElements = 8, RuleItalicLineElements = 9,
    RuleTextFragment = 10, RuleAlias = 11, RuleCommand = 12, RuleArguments = 13,
    RuleArgument = 14, RuleKwdArgument = 15, RuleStdArgument = 16, RuleWhitespace = 17
  };

  explicit zoiaParser(antlr4::TokenStream *input);
  ~zoiaParser();

  virtual std::string getGrammarFileName() const override;
  virtual const antlr4::atn::ATN& getATN() const override { return _atn; };
  virtual const std::vector<std::string>& getTokenNames() const override { return _tokenNames; }; // deprecated: use vocabulary instead.
  virtual const std::vector<std::string>& getRuleNames() const override;
  virtual antlr4::dfa::Vocabulary& getVocabulary() const override;


  class ZoiaFileContext;
  class HeaderContext;
  class LineContext;
  class LineElementsContext;
  class RegularLineElementsContext;
  class LineElementContext;
  class MarkedUpLineElementsContext;
  class BoldItalicLineElementsContext;
  class BoldLineElementsContext;
  class ItalicLineElementsContext;
  class TextFragmentContext;
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


    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  ZoiaFileContext* zoiaFile();

  class  HeaderContext : public antlr4::ParserRuleContext {
  public:
    HeaderContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Header();
    ArgumentsContext *arguments();
    antlr4::tree::TerminalNode *Newline();


    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  HeaderContext* header();

  class  LineContext : public antlr4::ParserRuleContext {
  public:
    LineContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Newline();
    LineElementsContext *lineElements();


    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  LineContext* line();

  class  LineElementsContext : public antlr4::ParserRuleContext {
  public:
    LineElementsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<MarkedUpLineElementsContext *> markedUpLineElements();
    MarkedUpLineElementsContext* markedUpLineElements(size_t i);
    std::vector<RegularLineElementsContext *> regularLineElements();
    RegularLineElementsContext* regularLineElements(size_t i);


    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  LineElementsContext* lineElements();

  class  RegularLineElementsContext : public antlr4::ParserRuleContext {
  public:
    RegularLineElementsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<LineElementContext *> lineElement();
    LineElementContext* lineElement(size_t i);


    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  RegularLineElementsContext* regularLineElements();

  class  LineElementContext : public antlr4::ParserRuleContext {
  public:
    LineElementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    TextFragmentContext *textFragment();
    AliasContext *alias();
    CommandContext *command();


    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  LineElementContext* lineElement();

  class  MarkedUpLineElementsContext : public antlr4::ParserRuleContext {
  public:
    MarkedUpLineElementsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    BoldItalicLineElementsContext *boldItalicLineElements();
    BoldLineElementsContext *boldLineElements();
    ItalicLineElementsContext *italicLineElements();


    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  MarkedUpLineElementsContext* markedUpLineElements();

  class  BoldItalicLineElementsContext : public antlr4::ParserRuleContext {
  public:
    BoldItalicLineElementsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Asterisk();
    antlr4::tree::TerminalNode* Asterisk(size_t i);
    RegularLineElementsContext *regularLineElements();


    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  BoldItalicLineElementsContext* boldItalicLineElements();

  class  BoldLineElementsContext : public antlr4::ParserRuleContext {
  public:
    BoldLineElementsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Asterisk();
    antlr4::tree::TerminalNode* Asterisk(size_t i);
    RegularLineElementsContext *regularLineElements();


    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  BoldLineElementsContext* boldLineElements();

  class  ItalicLineElementsContext : public antlr4::ParserRuleContext {
  public:
    ItalicLineElementsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Asterisk();
    antlr4::tree::TerminalNode* Asterisk(size_t i);
    RegularLineElementsContext *regularLineElements();


    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  ItalicLineElementsContext* italicLineElements();

  class  TextFragmentContext : public antlr4::ParserRuleContext {
  public:
    TextFragmentContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Word();
    antlr4::tree::TerminalNode* Word(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Space();
    antlr4::tree::TerminalNode* Space(size_t i);


    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  TextFragmentContext* textFragment();

  class  AliasContext : public antlr4::ParserRuleContext {
  public:
    AliasContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *At();
    antlr4::tree::TerminalNode *Word();


    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  AliasContext* alias();

  class  CommandContext : public antlr4::ParserRuleContext {
  public:
    CommandContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Backslash();
    antlr4::tree::TerminalNode *Word();
    ArgumentsContext *arguments();
    antlr4::tree::TerminalNode *Bar();


    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

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


    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  ArgumentsContext* arguments();

  class  ArgumentContext : public antlr4::ParserRuleContext {
  public:
    ArgumentContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    KwdArgumentContext *kwdArgument();
    StdArgumentContext *stdArgument();


    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  ArgumentContext* argument();

  class  KwdArgumentContext : public antlr4::ParserRuleContext {
  public:
    KwdArgumentContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Word();
    antlr4::tree::TerminalNode *Equals();
    LineElementsContext *lineElements();
    std::vector<antlr4::tree::TerminalNode *> Space();
    antlr4::tree::TerminalNode* Space(size_t i);


    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  KwdArgumentContext* kwdArgument();

  class  StdArgumentContext : public antlr4::ParserRuleContext {
  public:
    StdArgumentContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    LineElementsContext *lineElements();


    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  StdArgumentContext* stdArgument();

  class  WhitespaceContext : public antlr4::ParserRuleContext {
  public:
    WhitespaceContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Newline();
    antlr4::tree::TerminalNode* Newline(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Space();
    antlr4::tree::TerminalNode* Space(size_t i);


    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  WhitespaceContext* whitespace();


private:
  static std::vector<antlr4::dfa::DFA> _decisionToDFA;
  static antlr4::atn::PredictionContextCache _sharedContextCache;
  static std::vector<std::string> _ruleNames;
  static std::vector<std::string> _tokenNames;

  static std::vector<std::string> _literalNames;
  static std::vector<std::string> _symbolicNames;
  static antlr4::dfa::Vocabulary _vocabulary;
  static antlr4::atn::ATN _atn;
  static std::vector<uint16_t> _serializedATN;


  struct Initializer {
    Initializer();
  };
  static Initializer _init;
};
