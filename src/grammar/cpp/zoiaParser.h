
// Generated from grammar/zoia.g4 by ANTLR 4.9.3

#pragma once


#include "antlr4-runtime.h"




class  zoiaParser : public antlr4::Parser {
public:
  enum {
    T__0 = 1, T__1 = 2, T__2 = 3, T__3 = 4, T__4 = 5, T__5 = 6, T__6 = 7,
    T__7 = 8, COMMENT = 9, Asterisk = 10, Newline = 11, Space = 12, Char = 13
  };

  enum {
    RuleZoiaFile = 0, RuleHeader = 1, RuleLine = 2, RuleLineElements = 3,
    RuleRegularLineElements = 4, RuleLineElement = 5, RuleMarkedUpLineElements = 6,
    RuleBoldItalicLineElements = 7, RuleBoldLineElements = 8, RuleItalicLineElements = 9,
    RuleTextFragment = 10, RuleWord = 11, RuleAlias = 12, RuleCommand = 13,
    RuleArguments = 14, RuleArgument = 15, RuleKwdArgument = 16, RuleStdArgument = 17,
    RuleWhitespace = 18
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
  class WordContext;
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
    std::vector<WordContext *> word();
    WordContext* word(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Space();
    antlr4::tree::TerminalNode* Space(size_t i);


    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  TextFragmentContext* textFragment();

  class  WordContext : public antlr4::ParserRuleContext {
  public:
    WordContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Char();
    antlr4::tree::TerminalNode* Char(size_t i);


    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  WordContext* word();

  class  AliasContext : public antlr4::ParserRuleContext {
  public:
    AliasContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    WordContext *word();


    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  AliasContext* alias();

  class  CommandContext : public antlr4::ParserRuleContext {
  public:
    CommandContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    WordContext *word();
    ArgumentsContext *arguments();


    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  CommandContext* command();

  class  ArgumentsContext : public antlr4::ParserRuleContext {
  public:
    ArgumentsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<ArgumentContext *> argument();
    ArgumentContext* argument(size_t i);
    std::vector<WhitespaceContext *> whitespace();
    WhitespaceContext* whitespace(size_t i);


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
    WordContext *word();
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
