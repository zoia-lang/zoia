
// Generated from grammar/zoia.g4 by ANTLR 4.9.3


#include "zoiaVisitor.h"

#include "zoiaParser.h"


using namespace antlrcpp;
using namespace antlr4;

zoiaParser::zoiaParser(TokenStream *input) : Parser(input) {
  _interpreter = new atn::ParserATNSimulator(this, _atn, _decisionToDFA, _sharedContextCache);
}

zoiaParser::~zoiaParser() {
  delete _interpreter;
}

std::string zoiaParser::getGrammarFileName() const {
  return "zoia.g4";
}

const std::vector<std::string>& zoiaParser::getRuleNames() const {
  return _ruleNames;
}

dfa::Vocabulary& zoiaParser::getVocabulary() const {
  return _vocabulary;
}


//----------------- ZoiaFileContext ------------------------------------------------------------------

zoiaParser::ZoiaFileContext::ZoiaFileContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

zoiaParser::HeaderContext* zoiaParser::ZoiaFileContext::header() {
  return getRuleContext<zoiaParser::HeaderContext>(0);
}

tree::TerminalNode* zoiaParser::ZoiaFileContext::EOF() {
  return getToken(zoiaParser::EOF, 0);
}

std::vector<zoiaParser::LineContext *> zoiaParser::ZoiaFileContext::line() {
  return getRuleContexts<zoiaParser::LineContext>();
}

zoiaParser::LineContext* zoiaParser::ZoiaFileContext::line(size_t i) {
  return getRuleContext<zoiaParser::LineContext>(i);
}


size_t zoiaParser::ZoiaFileContext::getRuleIndex() const {
  return zoiaParser::RuleZoiaFile;
}


antlrcpp::Any zoiaParser::ZoiaFileContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<zoiaVisitor*>(visitor))
    return parserVisitor->visitZoiaFile(this);
  else
    return visitor->visitChildren(this);
}

zoiaParser::ZoiaFileContext* zoiaParser::zoiaFile() {
  ZoiaFileContext *_localctx = _tracker.createInstance<ZoiaFileContext>(_ctx, getState());
  enterRule(_localctx, 0, zoiaParser::RuleZoiaFile);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(38);
    header();
    setState(42);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & ((1ULL << zoiaParser::T__1)
      | (1ULL << zoiaParser::T__2)
      | (1ULL << zoiaParser::Asterisk)
      | (1ULL << zoiaParser::Newline)
      | (1ULL << zoiaParser::Space)
      | (1ULL << zoiaParser::Char))) != 0)) {
      setState(39);
      line();
      setState(44);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(45);
    match(zoiaParser::EOF);

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- HeaderContext ------------------------------------------------------------------

zoiaParser::HeaderContext::HeaderContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

zoiaParser::ArgumentsContext* zoiaParser::HeaderContext::arguments() {
  return getRuleContext<zoiaParser::ArgumentsContext>(0);
}

tree::TerminalNode* zoiaParser::HeaderContext::Newline() {
  return getToken(zoiaParser::Newline, 0);
}


size_t zoiaParser::HeaderContext::getRuleIndex() const {
  return zoiaParser::RuleHeader;
}


antlrcpp::Any zoiaParser::HeaderContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<zoiaVisitor*>(visitor))
    return parserVisitor->visitHeader(this);
  else
    return visitor->visitChildren(this);
}

zoiaParser::HeaderContext* zoiaParser::header() {
  HeaderContext *_localctx = _tracker.createInstance<HeaderContext>(_ctx, getState());
  enterRule(_localctx, 2, zoiaParser::RuleHeader);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(47);
    match(zoiaParser::T__0);
    setState(48);
    arguments();
    setState(49);
    match(zoiaParser::Newline);

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- LineContext ------------------------------------------------------------------

zoiaParser::LineContext::LineContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* zoiaParser::LineContext::Newline() {
  return getToken(zoiaParser::Newline, 0);
}

zoiaParser::LineElementsContext* zoiaParser::LineContext::lineElements() {
  return getRuleContext<zoiaParser::LineElementsContext>(0);
}


size_t zoiaParser::LineContext::getRuleIndex() const {
  return zoiaParser::RuleLine;
}


antlrcpp::Any zoiaParser::LineContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<zoiaVisitor*>(visitor))
    return parserVisitor->visitLine(this);
  else
    return visitor->visitChildren(this);
}

zoiaParser::LineContext* zoiaParser::line() {
  LineContext *_localctx = _tracker.createInstance<LineContext>(_ctx, getState());
  enterRule(_localctx, 4, zoiaParser::RuleLine);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(52);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & ((1ULL << zoiaParser::T__1)
      | (1ULL << zoiaParser::T__2)
      | (1ULL << zoiaParser::Asterisk)
      | (1ULL << zoiaParser::Space)
      | (1ULL << zoiaParser::Char))) != 0)) {
      setState(51);
      lineElements();
    }
    setState(54);
    match(zoiaParser::Newline);

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- LineElementsContext ------------------------------------------------------------------

zoiaParser::LineElementsContext::LineElementsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<zoiaParser::MarkedUpLineElementsContext *> zoiaParser::LineElementsContext::markedUpLineElements() {
  return getRuleContexts<zoiaParser::MarkedUpLineElementsContext>();
}

zoiaParser::MarkedUpLineElementsContext* zoiaParser::LineElementsContext::markedUpLineElements(size_t i) {
  return getRuleContext<zoiaParser::MarkedUpLineElementsContext>(i);
}

std::vector<zoiaParser::RegularLineElementsContext *> zoiaParser::LineElementsContext::regularLineElements() {
  return getRuleContexts<zoiaParser::RegularLineElementsContext>();
}

zoiaParser::RegularLineElementsContext* zoiaParser::LineElementsContext::regularLineElements(size_t i) {
  return getRuleContext<zoiaParser::RegularLineElementsContext>(i);
}


size_t zoiaParser::LineElementsContext::getRuleIndex() const {
  return zoiaParser::RuleLineElements;
}


antlrcpp::Any zoiaParser::LineElementsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<zoiaVisitor*>(visitor))
    return parserVisitor->visitLineElements(this);
  else
    return visitor->visitChildren(this);
}

zoiaParser::LineElementsContext* zoiaParser::lineElements() {
  LineElementsContext *_localctx = _tracker.createInstance<LineElementsContext>(_ctx, getState());
  enterRule(_localctx, 6, zoiaParser::RuleLineElements);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    size_t alt;
    enterOuterAlt(_localctx, 1);
    setState(58);
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(58);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case zoiaParser::Asterisk: {
                  setState(56);
                  markedUpLineElements();
                  break;
                }

                case zoiaParser::T__1:
                case zoiaParser::T__2:
                case zoiaParser::Space:
                case zoiaParser::Char: {
                  setState(57);
                  regularLineElements();
                  break;
                }

              default:
                throw NoViableAltException(this);
              }
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(60);
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 3, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- RegularLineElementsContext ------------------------------------------------------------------

zoiaParser::RegularLineElementsContext::RegularLineElementsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<zoiaParser::LineElementContext *> zoiaParser::RegularLineElementsContext::lineElement() {
  return getRuleContexts<zoiaParser::LineElementContext>();
}

zoiaParser::LineElementContext* zoiaParser::RegularLineElementsContext::lineElement(size_t i) {
  return getRuleContext<zoiaParser::LineElementContext>(i);
}


size_t zoiaParser::RegularLineElementsContext::getRuleIndex() const {
  return zoiaParser::RuleRegularLineElements;
}


antlrcpp::Any zoiaParser::RegularLineElementsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<zoiaVisitor*>(visitor))
    return parserVisitor->visitRegularLineElements(this);
  else
    return visitor->visitChildren(this);
}

zoiaParser::RegularLineElementsContext* zoiaParser::regularLineElements() {
  RegularLineElementsContext *_localctx = _tracker.createInstance<RegularLineElementsContext>(_ctx, getState());
  enterRule(_localctx, 8, zoiaParser::RuleRegularLineElements);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    size_t alt;
    enterOuterAlt(_localctx, 1);
    setState(63);
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(62);
              lineElement();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(65);
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 4, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- LineElementContext ------------------------------------------------------------------

zoiaParser::LineElementContext::LineElementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

zoiaParser::TextFragmentContext* zoiaParser::LineElementContext::textFragment() {
  return getRuleContext<zoiaParser::TextFragmentContext>(0);
}

zoiaParser::AliasContext* zoiaParser::LineElementContext::alias() {
  return getRuleContext<zoiaParser::AliasContext>(0);
}

zoiaParser::CommandContext* zoiaParser::LineElementContext::command() {
  return getRuleContext<zoiaParser::CommandContext>(0);
}


size_t zoiaParser::LineElementContext::getRuleIndex() const {
  return zoiaParser::RuleLineElement;
}


antlrcpp::Any zoiaParser::LineElementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<zoiaVisitor*>(visitor))
    return parserVisitor->visitLineElement(this);
  else
    return visitor->visitChildren(this);
}

zoiaParser::LineElementContext* zoiaParser::lineElement() {
  LineElementContext *_localctx = _tracker.createInstance<LineElementContext>(_ctx, getState());
  enterRule(_localctx, 10, zoiaParser::RuleLineElement);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(70);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case zoiaParser::Space:
      case zoiaParser::Char: {
        enterOuterAlt(_localctx, 1);
        setState(67);
        textFragment();
        break;
      }

      case zoiaParser::T__1: {
        enterOuterAlt(_localctx, 2);
        setState(68);
        alias();
        break;
      }

      case zoiaParser::T__2: {
        enterOuterAlt(_localctx, 3);
        setState(69);
        command();
        break;
      }

    default:
      throw NoViableAltException(this);
    }

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- MarkedUpLineElementsContext ------------------------------------------------------------------

zoiaParser::MarkedUpLineElementsContext::MarkedUpLineElementsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

zoiaParser::BoldItalicLineElementsContext* zoiaParser::MarkedUpLineElementsContext::boldItalicLineElements() {
  return getRuleContext<zoiaParser::BoldItalicLineElementsContext>(0);
}

zoiaParser::BoldLineElementsContext* zoiaParser::MarkedUpLineElementsContext::boldLineElements() {
  return getRuleContext<zoiaParser::BoldLineElementsContext>(0);
}

zoiaParser::ItalicLineElementsContext* zoiaParser::MarkedUpLineElementsContext::italicLineElements() {
  return getRuleContext<zoiaParser::ItalicLineElementsContext>(0);
}


size_t zoiaParser::MarkedUpLineElementsContext::getRuleIndex() const {
  return zoiaParser::RuleMarkedUpLineElements;
}


antlrcpp::Any zoiaParser::MarkedUpLineElementsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<zoiaVisitor*>(visitor))
    return parserVisitor->visitMarkedUpLineElements(this);
  else
    return visitor->visitChildren(this);
}

zoiaParser::MarkedUpLineElementsContext* zoiaParser::markedUpLineElements() {
  MarkedUpLineElementsContext *_localctx = _tracker.createInstance<MarkedUpLineElementsContext>(_ctx, getState());
  enterRule(_localctx, 12, zoiaParser::RuleMarkedUpLineElements);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(75);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 6, _ctx)) {
    case 1: {
      enterOuterAlt(_localctx, 1);
      setState(72);
      boldItalicLineElements();
      break;
    }

    case 2: {
      enterOuterAlt(_localctx, 2);
      setState(73);
      boldLineElements();
      break;
    }

    case 3: {
      enterOuterAlt(_localctx, 3);
      setState(74);
      italicLineElements();
      break;
    }

    default:
      break;
    }

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- BoldItalicLineElementsContext ------------------------------------------------------------------

zoiaParser::BoldItalicLineElementsContext::BoldItalicLineElementsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> zoiaParser::BoldItalicLineElementsContext::Asterisk() {
  return getTokens(zoiaParser::Asterisk);
}

tree::TerminalNode* zoiaParser::BoldItalicLineElementsContext::Asterisk(size_t i) {
  return getToken(zoiaParser::Asterisk, i);
}

zoiaParser::RegularLineElementsContext* zoiaParser::BoldItalicLineElementsContext::regularLineElements() {
  return getRuleContext<zoiaParser::RegularLineElementsContext>(0);
}


size_t zoiaParser::BoldItalicLineElementsContext::getRuleIndex() const {
  return zoiaParser::RuleBoldItalicLineElements;
}


antlrcpp::Any zoiaParser::BoldItalicLineElementsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<zoiaVisitor*>(visitor))
    return parserVisitor->visitBoldItalicLineElements(this);
  else
    return visitor->visitChildren(this);
}

zoiaParser::BoldItalicLineElementsContext* zoiaParser::boldItalicLineElements() {
  BoldItalicLineElementsContext *_localctx = _tracker.createInstance<BoldItalicLineElementsContext>(_ctx, getState());
  enterRule(_localctx, 14, zoiaParser::RuleBoldItalicLineElements);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(77);
    match(zoiaParser::Asterisk);
    setState(78);
    match(zoiaParser::Asterisk);
    setState(79);
    match(zoiaParser::Asterisk);
    setState(80);
    regularLineElements();
    setState(81);
    match(zoiaParser::Asterisk);
    setState(82);
    match(zoiaParser::Asterisk);
    setState(83);
    match(zoiaParser::Asterisk);

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- BoldLineElementsContext ------------------------------------------------------------------

zoiaParser::BoldLineElementsContext::BoldLineElementsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> zoiaParser::BoldLineElementsContext::Asterisk() {
  return getTokens(zoiaParser::Asterisk);
}

tree::TerminalNode* zoiaParser::BoldLineElementsContext::Asterisk(size_t i) {
  return getToken(zoiaParser::Asterisk, i);
}

zoiaParser::RegularLineElementsContext* zoiaParser::BoldLineElementsContext::regularLineElements() {
  return getRuleContext<zoiaParser::RegularLineElementsContext>(0);
}


size_t zoiaParser::BoldLineElementsContext::getRuleIndex() const {
  return zoiaParser::RuleBoldLineElements;
}


antlrcpp::Any zoiaParser::BoldLineElementsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<zoiaVisitor*>(visitor))
    return parserVisitor->visitBoldLineElements(this);
  else
    return visitor->visitChildren(this);
}

zoiaParser::BoldLineElementsContext* zoiaParser::boldLineElements() {
  BoldLineElementsContext *_localctx = _tracker.createInstance<BoldLineElementsContext>(_ctx, getState());
  enterRule(_localctx, 16, zoiaParser::RuleBoldLineElements);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(85);
    match(zoiaParser::Asterisk);
    setState(86);
    match(zoiaParser::Asterisk);
    setState(87);
    regularLineElements();
    setState(88);
    match(zoiaParser::Asterisk);
    setState(89);
    match(zoiaParser::Asterisk);

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ItalicLineElementsContext ------------------------------------------------------------------

zoiaParser::ItalicLineElementsContext::ItalicLineElementsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> zoiaParser::ItalicLineElementsContext::Asterisk() {
  return getTokens(zoiaParser::Asterisk);
}

tree::TerminalNode* zoiaParser::ItalicLineElementsContext::Asterisk(size_t i) {
  return getToken(zoiaParser::Asterisk, i);
}

zoiaParser::RegularLineElementsContext* zoiaParser::ItalicLineElementsContext::regularLineElements() {
  return getRuleContext<zoiaParser::RegularLineElementsContext>(0);
}


size_t zoiaParser::ItalicLineElementsContext::getRuleIndex() const {
  return zoiaParser::RuleItalicLineElements;
}


antlrcpp::Any zoiaParser::ItalicLineElementsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<zoiaVisitor*>(visitor))
    return parserVisitor->visitItalicLineElements(this);
  else
    return visitor->visitChildren(this);
}

zoiaParser::ItalicLineElementsContext* zoiaParser::italicLineElements() {
  ItalicLineElementsContext *_localctx = _tracker.createInstance<ItalicLineElementsContext>(_ctx, getState());
  enterRule(_localctx, 18, zoiaParser::RuleItalicLineElements);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(91);
    match(zoiaParser::Asterisk);
    setState(92);
    regularLineElements();
    setState(93);
    match(zoiaParser::Asterisk);

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- TextFragmentContext ------------------------------------------------------------------

zoiaParser::TextFragmentContext::TextFragmentContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<zoiaParser::WordContext *> zoiaParser::TextFragmentContext::word() {
  return getRuleContexts<zoiaParser::WordContext>();
}

zoiaParser::WordContext* zoiaParser::TextFragmentContext::word(size_t i) {
  return getRuleContext<zoiaParser::WordContext>(i);
}

std::vector<tree::TerminalNode *> zoiaParser::TextFragmentContext::Space() {
  return getTokens(zoiaParser::Space);
}

tree::TerminalNode* zoiaParser::TextFragmentContext::Space(size_t i) {
  return getToken(zoiaParser::Space, i);
}


size_t zoiaParser::TextFragmentContext::getRuleIndex() const {
  return zoiaParser::RuleTextFragment;
}


antlrcpp::Any zoiaParser::TextFragmentContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<zoiaVisitor*>(visitor))
    return parserVisitor->visitTextFragment(this);
  else
    return visitor->visitChildren(this);
}

zoiaParser::TextFragmentContext* zoiaParser::textFragment() {
  TextFragmentContext *_localctx = _tracker.createInstance<TextFragmentContext>(_ctx, getState());
  enterRule(_localctx, 20, zoiaParser::RuleTextFragment);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    size_t alt;
    enterOuterAlt(_localctx, 1);
    setState(97);
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(97);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case zoiaParser::Char: {
                  setState(95);
                  word();
                  break;
                }

                case zoiaParser::Space: {
                  setState(96);
                  match(zoiaParser::Space);
                  break;
                }

              default:
                throw NoViableAltException(this);
              }
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(99);
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 8, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- WordContext ------------------------------------------------------------------

zoiaParser::WordContext::WordContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> zoiaParser::WordContext::Char() {
  return getTokens(zoiaParser::Char);
}

tree::TerminalNode* zoiaParser::WordContext::Char(size_t i) {
  return getToken(zoiaParser::Char, i);
}


size_t zoiaParser::WordContext::getRuleIndex() const {
  return zoiaParser::RuleWord;
}


antlrcpp::Any zoiaParser::WordContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<zoiaVisitor*>(visitor))
    return parserVisitor->visitWord(this);
  else
    return visitor->visitChildren(this);
}

zoiaParser::WordContext* zoiaParser::word() {
  WordContext *_localctx = _tracker.createInstance<WordContext>(_ctx, getState());
  enterRule(_localctx, 22, zoiaParser::RuleWord);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    size_t alt;
    enterOuterAlt(_localctx, 1);
    setState(102);
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(101);
              match(zoiaParser::Char);
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(104);
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 9, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- AliasContext ------------------------------------------------------------------

zoiaParser::AliasContext::AliasContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

zoiaParser::WordContext* zoiaParser::AliasContext::word() {
  return getRuleContext<zoiaParser::WordContext>(0);
}


size_t zoiaParser::AliasContext::getRuleIndex() const {
  return zoiaParser::RuleAlias;
}


antlrcpp::Any zoiaParser::AliasContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<zoiaVisitor*>(visitor))
    return parserVisitor->visitAlias(this);
  else
    return visitor->visitChildren(this);
}

zoiaParser::AliasContext* zoiaParser::alias() {
  AliasContext *_localctx = _tracker.createInstance<AliasContext>(_ctx, getState());
  enterRule(_localctx, 24, zoiaParser::RuleAlias);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(106);
    match(zoiaParser::T__1);
    setState(107);
    word();

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- CommandContext ------------------------------------------------------------------

zoiaParser::CommandContext::CommandContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

zoiaParser::WordContext* zoiaParser::CommandContext::word() {
  return getRuleContext<zoiaParser::WordContext>(0);
}

zoiaParser::ArgumentsContext* zoiaParser::CommandContext::arguments() {
  return getRuleContext<zoiaParser::ArgumentsContext>(0);
}


size_t zoiaParser::CommandContext::getRuleIndex() const {
  return zoiaParser::RuleCommand;
}


antlrcpp::Any zoiaParser::CommandContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<zoiaVisitor*>(visitor))
    return parserVisitor->visitCommand(this);
  else
    return visitor->visitChildren(this);
}

zoiaParser::CommandContext* zoiaParser::command() {
  CommandContext *_localctx = _tracker.createInstance<CommandContext>(_ctx, getState());
  enterRule(_localctx, 26, zoiaParser::RuleCommand);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(109);
    match(zoiaParser::T__2);
    setState(110);
    word();
    setState(112);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == zoiaParser::T__4) {
      setState(111);
      arguments();
    }
    setState(115);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == zoiaParser::T__3) {
      setState(114);
      match(zoiaParser::T__3);
    }

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ArgumentsContext ------------------------------------------------------------------

zoiaParser::ArgumentsContext::ArgumentsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<zoiaParser::ArgumentContext *> zoiaParser::ArgumentsContext::argument() {
  return getRuleContexts<zoiaParser::ArgumentContext>();
}

zoiaParser::ArgumentContext* zoiaParser::ArgumentsContext::argument(size_t i) {
  return getRuleContext<zoiaParser::ArgumentContext>(i);
}

std::vector<zoiaParser::WhitespaceContext *> zoiaParser::ArgumentsContext::whitespace() {
  return getRuleContexts<zoiaParser::WhitespaceContext>();
}

zoiaParser::WhitespaceContext* zoiaParser::ArgumentsContext::whitespace(size_t i) {
  return getRuleContext<zoiaParser::WhitespaceContext>(i);
}


size_t zoiaParser::ArgumentsContext::getRuleIndex() const {
  return zoiaParser::RuleArguments;
}


antlrcpp::Any zoiaParser::ArgumentsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<zoiaVisitor*>(visitor))
    return parserVisitor->visitArguments(this);
  else
    return visitor->visitChildren(this);
}

zoiaParser::ArgumentsContext* zoiaParser::arguments() {
  ArgumentsContext *_localctx = _tracker.createInstance<ArgumentsContext>(_ctx, getState());
  enterRule(_localctx, 28, zoiaParser::RuleArguments);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    size_t alt;
    enterOuterAlt(_localctx, 1);
    setState(117);
    match(zoiaParser::T__4);
    setState(121);
    _errHandler->sync(this);
    alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 12, _ctx);
    while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER) {
      if (alt == 1) {
        setState(118);
        whitespace();
      }
      setState(123);
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 12, _ctx);
    }
    setState(124);
    argument();
    setState(135);
    _errHandler->sync(this);
    alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 14, _ctx);
    while (alt != 1 && alt != atn::ATN::INVALID_ALT_NUMBER) {
      if (alt == 1 + 1) {
        setState(125);
        match(zoiaParser::T__5);
        setState(129);
        _errHandler->sync(this);
        alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 13, _ctx);
        while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER) {
          if (alt == 1) {
            setState(126);
            whitespace();
          }
          setState(131);
          _errHandler->sync(this);
          alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 13, _ctx);
        }
        setState(132);
        argument();
      }
      setState(137);
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 14, _ctx);
    }
    setState(139);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == zoiaParser::T__5) {
      setState(138);
      match(zoiaParser::T__5);
    }
    setState(144);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == zoiaParser::Newline

    || _la == zoiaParser::Space) {
      setState(141);
      whitespace();
      setState(146);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(147);
    match(zoiaParser::T__6);

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ArgumentContext ------------------------------------------------------------------

zoiaParser::ArgumentContext::ArgumentContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

zoiaParser::KwdArgumentContext* zoiaParser::ArgumentContext::kwdArgument() {
  return getRuleContext<zoiaParser::KwdArgumentContext>(0);
}

zoiaParser::StdArgumentContext* zoiaParser::ArgumentContext::stdArgument() {
  return getRuleContext<zoiaParser::StdArgumentContext>(0);
}


size_t zoiaParser::ArgumentContext::getRuleIndex() const {
  return zoiaParser::RuleArgument;
}


antlrcpp::Any zoiaParser::ArgumentContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<zoiaVisitor*>(visitor))
    return parserVisitor->visitArgument(this);
  else
    return visitor->visitChildren(this);
}

zoiaParser::ArgumentContext* zoiaParser::argument() {
  ArgumentContext *_localctx = _tracker.createInstance<ArgumentContext>(_ctx, getState());
  enterRule(_localctx, 30, zoiaParser::RuleArgument);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(151);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 17, _ctx)) {
    case 1: {
      enterOuterAlt(_localctx, 1);
      setState(149);
      kwdArgument();
      break;
    }

    case 2: {
      enterOuterAlt(_localctx, 2);
      setState(150);
      stdArgument();
      break;
    }

    default:
      break;
    }

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- KwdArgumentContext ------------------------------------------------------------------

zoiaParser::KwdArgumentContext::KwdArgumentContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

zoiaParser::WordContext* zoiaParser::KwdArgumentContext::word() {
  return getRuleContext<zoiaParser::WordContext>(0);
}

zoiaParser::LineElementsContext* zoiaParser::KwdArgumentContext::lineElements() {
  return getRuleContext<zoiaParser::LineElementsContext>(0);
}

std::vector<tree::TerminalNode *> zoiaParser::KwdArgumentContext::Space() {
  return getTokens(zoiaParser::Space);
}

tree::TerminalNode* zoiaParser::KwdArgumentContext::Space(size_t i) {
  return getToken(zoiaParser::Space, i);
}


size_t zoiaParser::KwdArgumentContext::getRuleIndex() const {
  return zoiaParser::RuleKwdArgument;
}


antlrcpp::Any zoiaParser::KwdArgumentContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<zoiaVisitor*>(visitor))
    return parserVisitor->visitKwdArgument(this);
  else
    return visitor->visitChildren(this);
}

zoiaParser::KwdArgumentContext* zoiaParser::kwdArgument() {
  KwdArgumentContext *_localctx = _tracker.createInstance<KwdArgumentContext>(_ctx, getState());
  enterRule(_localctx, 32, zoiaParser::RuleKwdArgument);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    size_t alt;
    enterOuterAlt(_localctx, 1);
    setState(153);
    word();
    setState(157);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == zoiaParser::Space) {
      setState(154);
      match(zoiaParser::Space);
      setState(159);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(160);
    match(zoiaParser::T__7);
    setState(164);
    _errHandler->sync(this);
    alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 19, _ctx);
    while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER) {
      if (alt == 1) {
        setState(161);
        match(zoiaParser::Space);
      }
      setState(166);
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 19, _ctx);
    }
    setState(167);
    lineElements();

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- StdArgumentContext ------------------------------------------------------------------

zoiaParser::StdArgumentContext::StdArgumentContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

zoiaParser::LineElementsContext* zoiaParser::StdArgumentContext::lineElements() {
  return getRuleContext<zoiaParser::LineElementsContext>(0);
}


size_t zoiaParser::StdArgumentContext::getRuleIndex() const {
  return zoiaParser::RuleStdArgument;
}


antlrcpp::Any zoiaParser::StdArgumentContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<zoiaVisitor*>(visitor))
    return parserVisitor->visitStdArgument(this);
  else
    return visitor->visitChildren(this);
}

zoiaParser::StdArgumentContext* zoiaParser::stdArgument() {
  StdArgumentContext *_localctx = _tracker.createInstance<StdArgumentContext>(_ctx, getState());
  enterRule(_localctx, 34, zoiaParser::RuleStdArgument);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(169);
    lineElements();

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- WhitespaceContext ------------------------------------------------------------------

zoiaParser::WhitespaceContext::WhitespaceContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> zoiaParser::WhitespaceContext::Newline() {
  return getTokens(zoiaParser::Newline);
}

tree::TerminalNode* zoiaParser::WhitespaceContext::Newline(size_t i) {
  return getToken(zoiaParser::Newline, i);
}

std::vector<tree::TerminalNode *> zoiaParser::WhitespaceContext::Space() {
  return getTokens(zoiaParser::Space);
}

tree::TerminalNode* zoiaParser::WhitespaceContext::Space(size_t i) {
  return getToken(zoiaParser::Space, i);
}


size_t zoiaParser::WhitespaceContext::getRuleIndex() const {
  return zoiaParser::RuleWhitespace;
}


antlrcpp::Any zoiaParser::WhitespaceContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<zoiaVisitor*>(visitor))
    return parserVisitor->visitWhitespace(this);
  else
    return visitor->visitChildren(this);
}

zoiaParser::WhitespaceContext* zoiaParser::whitespace() {
  WhitespaceContext *_localctx = _tracker.createInstance<WhitespaceContext>(_ctx, getState());
  enterRule(_localctx, 36, zoiaParser::RuleWhitespace);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    size_t alt;
    enterOuterAlt(_localctx, 1);
    setState(172);
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(171);
              _la = _input->LA(1);
              if (!(_la == zoiaParser::Newline

              || _la == zoiaParser::Space)) {
              _errHandler->recoverInline(this);
              }
              else {
                _errHandler->reportMatch(this);
                consume();
              }
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(174);
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 20, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

// Static vars and initialization.
std::vector<dfa::DFA> zoiaParser::_decisionToDFA;
atn::PredictionContextCache zoiaParser::_sharedContextCache;

// We own the ATN which in turn owns the ATN states.
atn::ATN zoiaParser::_atn;
std::vector<uint16_t> zoiaParser::_serializedATN;

std::vector<std::string> zoiaParser::_ruleNames = {
  "zoiaFile", "header", "line", "lineElements", "regularLineElements", "lineElement",
  "markedUpLineElements", "boldItalicLineElements", "boldLineElements",
  "italicLineElements", "textFragment", "word", "alias", "command", "arguments",
  "argument", "kwdArgument", "stdArgument", "whitespace"
};

std::vector<std::string> zoiaParser::_literalNames = {
  "", "'\\header'", "'@'", "'\\'", "'|'", "'['", "';'", "']'", "'='", "",
  "'*'"
};

std::vector<std::string> zoiaParser::_symbolicNames = {
  "", "", "", "", "", "", "", "", "", "COMMENT", "Asterisk", "Newline",
  "Space", "Char"
};

dfa::Vocabulary zoiaParser::_vocabulary(_literalNames, _symbolicNames);

std::vector<std::string> zoiaParser::_tokenNames;

zoiaParser::Initializer::Initializer() {
	for (size_t i = 0; i < _symbolicNames.size(); ++i) {
		std::string name = _vocabulary.getLiteralName(i);
		if (name.empty()) {
			name = _vocabulary.getSymbolicName(i);
		}

		if (name.empty()) {
			_tokenNames.push_back("<INVALID>");
		} else {
      _tokenNames.push_back(name);
    }
	}

  static const uint16_t serializedATNSegment0[] = {
    0x3, 0x608b, 0xa72a, 0x8133, 0xb9ed, 0x417c, 0x3be7, 0x7786, 0x5964,
       0x3, 0xf, 0xb3, 0x4, 0x2, 0x9, 0x2, 0x4, 0x3, 0x9, 0x3, 0x4, 0x4,
       0x9, 0x4, 0x4, 0x5, 0x9, 0x5, 0x4, 0x6, 0x9, 0x6, 0x4, 0x7, 0x9,
       0x7, 0x4, 0x8, 0x9, 0x8, 0x4, 0x9, 0x9, 0x9, 0x4, 0xa, 0x9, 0xa,
       0x4, 0xb, 0x9, 0xb, 0x4, 0xc, 0x9, 0xc, 0x4, 0xd, 0x9, 0xd, 0x4,
       0xe, 0x9, 0xe, 0x4, 0xf, 0x9, 0xf, 0x4, 0x10, 0x9, 0x10, 0x4, 0x11,
       0x9, 0x11, 0x4, 0x12, 0x9, 0x12, 0x4, 0x13, 0x9, 0x13, 0x4, 0x14,
       0x9, 0x14, 0x3, 0x2, 0x3, 0x2, 0x7, 0x2, 0x2b, 0xa, 0x2, 0xc, 0x2,
       0xe, 0x2, 0x2e, 0xb, 0x2, 0x3, 0x2, 0x3, 0x2, 0x3, 0x3, 0x3, 0x3,
       0x3, 0x3, 0x3, 0x3, 0x3, 0x4, 0x5, 0x4, 0x37, 0xa, 0x4, 0x3, 0x4,
       0x3, 0x4, 0x3, 0x5, 0x3, 0x5, 0x6, 0x5, 0x3d, 0xa, 0x5, 0xd, 0x5,
       0xe, 0x5, 0x3e, 0x3, 0x6, 0x6, 0x6, 0x42, 0xa, 0x6, 0xd, 0x6, 0xe,
       0x6, 0x43, 0x3, 0x7, 0x3, 0x7, 0x3, 0x7, 0x5, 0x7, 0x49, 0xa, 0x7,
       0x3, 0x8, 0x3, 0x8, 0x3, 0x8, 0x5, 0x8, 0x4e, 0xa, 0x8, 0x3, 0x9,
       0x3, 0x9, 0x3, 0x9, 0x3, 0x9, 0x3, 0x9, 0x3, 0x9, 0x3, 0x9, 0x3,
       0x9, 0x3, 0xa, 0x3, 0xa, 0x3, 0xa, 0x3, 0xa, 0x3, 0xa, 0x3, 0xa,
       0x3, 0xb, 0x3, 0xb, 0x3, 0xb, 0x3, 0xb, 0x3, 0xc, 0x3, 0xc, 0x6,
       0xc, 0x64, 0xa, 0xc, 0xd, 0xc, 0xe, 0xc, 0x65, 0x3, 0xd, 0x6, 0xd,
       0x69, 0xa, 0xd, 0xd, 0xd, 0xe, 0xd, 0x6a, 0x3, 0xe, 0x3, 0xe, 0x3,
       0xe, 0x3, 0xf, 0x3, 0xf, 0x3, 0xf, 0x5, 0xf, 0x73, 0xa, 0xf, 0x3,
       0xf, 0x5, 0xf, 0x76, 0xa, 0xf, 0x3, 0x10, 0x3, 0x10, 0x7, 0x10, 0x7a,
       0xa, 0x10, 0xc, 0x10, 0xe, 0x10, 0x7d, 0xb, 0x10, 0x3, 0x10, 0x3,
       0x10, 0x3, 0x10, 0x7, 0x10, 0x82, 0xa, 0x10, 0xc, 0x10, 0xe, 0x10,
       0x85, 0xb, 0x10, 0x3, 0x10, 0x7, 0x10, 0x88, 0xa, 0x10, 0xc, 0x10,
       0xe, 0x10, 0x8b, 0xb, 0x10, 0x3, 0x10, 0x5, 0x10, 0x8e, 0xa, 0x10,
       0x3, 0x10, 0x7, 0x10, 0x91, 0xa, 0x10, 0xc, 0x10, 0xe, 0x10, 0x94,
       0xb, 0x10, 0x3, 0x10, 0x3, 0x10, 0x3, 0x11, 0x3, 0x11, 0x5, 0x11,
       0x9a, 0xa, 0x11, 0x3, 0x12, 0x3, 0x12, 0x7, 0x12, 0x9e, 0xa, 0x12,
       0xc, 0x12, 0xe, 0x12, 0xa1, 0xb, 0x12, 0x3, 0x12, 0x3, 0x12, 0x7,
       0x12, 0xa5, 0xa, 0x12, 0xc, 0x12, 0xe, 0x12, 0xa8, 0xb, 0x12, 0x3,
       0x12, 0x3, 0x12, 0x3, 0x13, 0x3, 0x13, 0x3, 0x14, 0x6, 0x14, 0xaf,
       0xa, 0x14, 0xd, 0x14, 0xe, 0x14, 0xb0, 0x3, 0x14, 0x3, 0x89, 0x2,
       0x15, 0x2, 0x4, 0x6, 0x8, 0xa, 0xc, 0xe, 0x10, 0x12, 0x14, 0x16,
       0x18, 0x1a, 0x1c, 0x1e, 0x20, 0x22, 0x24, 0x26, 0x2, 0x3, 0x3, 0x2,
       0xd, 0xe, 0x2, 0xb6, 0x2, 0x28, 0x3, 0x2, 0x2, 0x2, 0x4, 0x31, 0x3,
       0x2, 0x2, 0x2, 0x6, 0x36, 0x3, 0x2, 0x2, 0x2, 0x8, 0x3c, 0x3, 0x2,
       0x2, 0x2, 0xa, 0x41, 0x3, 0x2, 0x2, 0x2, 0xc, 0x48, 0x3, 0x2, 0x2,
       0x2, 0xe, 0x4d, 0x3, 0x2, 0x2, 0x2, 0x10, 0x4f, 0x3, 0x2, 0x2, 0x2,
       0x12, 0x57, 0x3, 0x2, 0x2, 0x2, 0x14, 0x5d, 0x3, 0x2, 0x2, 0x2, 0x16,
       0x63, 0x3, 0x2, 0x2, 0x2, 0x18, 0x68, 0x3, 0x2, 0x2, 0x2, 0x1a, 0x6c,
       0x3, 0x2, 0x2, 0x2, 0x1c, 0x6f, 0x3, 0x2, 0x2, 0x2, 0x1e, 0x77, 0x3,
       0x2, 0x2, 0x2, 0x20, 0x99, 0x3, 0x2, 0x2, 0x2, 0x22, 0x9b, 0x3, 0x2,
       0x2, 0x2, 0x24, 0xab, 0x3, 0x2, 0x2, 0x2, 0x26, 0xae, 0x3, 0x2, 0x2,
       0x2, 0x28, 0x2c, 0x5, 0x4, 0x3, 0x2, 0x29, 0x2b, 0x5, 0x6, 0x4, 0x2,
       0x2a, 0x29, 0x3, 0x2, 0x2, 0x2, 0x2b, 0x2e, 0x3, 0x2, 0x2, 0x2, 0x2c,
       0x2a, 0x3, 0x2, 0x2, 0x2, 0x2c, 0x2d, 0x3, 0x2, 0x2, 0x2, 0x2d, 0x2f,
       0x3, 0x2, 0x2, 0x2, 0x2e, 0x2c, 0x3, 0x2, 0x2, 0x2, 0x2f, 0x30, 0x7,
       0x2, 0x2, 0x3, 0x30, 0x3, 0x3, 0x2, 0x2, 0x2, 0x31, 0x32, 0x7, 0x3,
       0x2, 0x2, 0x32, 0x33, 0x5, 0x1e, 0x10, 0x2, 0x33, 0x34, 0x7, 0xd,
       0x2, 0x2, 0x34, 0x5, 0x3, 0x2, 0x2, 0x2, 0x35, 0x37, 0x5, 0x8, 0x5,
       0x2, 0x36, 0x35, 0x3, 0x2, 0x2, 0x2, 0x36, 0x37, 0x3, 0x2, 0x2, 0x2,
       0x37, 0x38, 0x3, 0x2, 0x2, 0x2, 0x38, 0x39, 0x7, 0xd, 0x2, 0x2, 0x39,
       0x7, 0x3, 0x2, 0x2, 0x2, 0x3a, 0x3d, 0x5, 0xe, 0x8, 0x2, 0x3b, 0x3d,
       0x5, 0xa, 0x6, 0x2, 0x3c, 0x3a, 0x3, 0x2, 0x2, 0x2, 0x3c, 0x3b, 0x3,
       0x2, 0x2, 0x2, 0x3d, 0x3e, 0x3, 0x2, 0x2, 0x2, 0x3e, 0x3c, 0x3, 0x2,
       0x2, 0x2, 0x3e, 0x3f, 0x3, 0x2, 0x2, 0x2, 0x3f, 0x9, 0x3, 0x2, 0x2,
       0x2, 0x40, 0x42, 0x5, 0xc, 0x7, 0x2, 0x41, 0x40, 0x3, 0x2, 0x2, 0x2,
       0x42, 0x43, 0x3, 0x2, 0x2, 0x2, 0x43, 0x41, 0x3, 0x2, 0x2, 0x2, 0x43,
       0x44, 0x3, 0x2, 0x2, 0x2, 0x44, 0xb, 0x3, 0x2, 0x2, 0x2, 0x45, 0x49,
       0x5, 0x16, 0xc, 0x2, 0x46, 0x49, 0x5, 0x1a, 0xe, 0x2, 0x47, 0x49,
       0x5, 0x1c, 0xf, 0x2, 0x48, 0x45, 0x3, 0x2, 0x2, 0x2, 0x48, 0x46,
       0x3, 0x2, 0x2, 0x2, 0x48, 0x47, 0x3, 0x2, 0x2, 0x2, 0x49, 0xd, 0x3,
       0x2, 0x2, 0x2, 0x4a, 0x4e, 0x5, 0x10, 0x9, 0x2, 0x4b, 0x4e, 0x5,
       0x12, 0xa, 0x2, 0x4c, 0x4e, 0x5, 0x14, 0xb, 0x2, 0x4d, 0x4a, 0x3,
       0x2, 0x2, 0x2, 0x4d, 0x4b, 0x3, 0x2, 0x2, 0x2, 0x4d, 0x4c, 0x3, 0x2,
       0x2, 0x2, 0x4e, 0xf, 0x3, 0x2, 0x2, 0x2, 0x4f, 0x50, 0x7, 0xc, 0x2,
       0x2, 0x50, 0x51, 0x7, 0xc, 0x2, 0x2, 0x51, 0x52, 0x7, 0xc, 0x2, 0x2,
       0x52, 0x53, 0x5, 0xa, 0x6, 0x2, 0x53, 0x54, 0x7, 0xc, 0x2, 0x2, 0x54,
       0x55, 0x7, 0xc, 0x2, 0x2, 0x55, 0x56, 0x7, 0xc, 0x2, 0x2, 0x56, 0x11,
       0x3, 0x2, 0x2, 0x2, 0x57, 0x58, 0x7, 0xc, 0x2, 0x2, 0x58, 0x59, 0x7,
       0xc, 0x2, 0x2, 0x59, 0x5a, 0x5, 0xa, 0x6, 0x2, 0x5a, 0x5b, 0x7, 0xc,
       0x2, 0x2, 0x5b, 0x5c, 0x7, 0xc, 0x2, 0x2, 0x5c, 0x13, 0x3, 0x2, 0x2,
       0x2, 0x5d, 0x5e, 0x7, 0xc, 0x2, 0x2, 0x5e, 0x5f, 0x5, 0xa, 0x6, 0x2,
       0x5f, 0x60, 0x7, 0xc, 0x2, 0x2, 0x60, 0x15, 0x3, 0x2, 0x2, 0x2, 0x61,
       0x64, 0x5, 0x18, 0xd, 0x2, 0x62, 0x64, 0x7, 0xe, 0x2, 0x2, 0x63,
       0x61, 0x3, 0x2, 0x2, 0x2, 0x63, 0x62, 0x3, 0x2, 0x2, 0x2, 0x64, 0x65,
       0x3, 0x2, 0x2, 0x2, 0x65, 0x63, 0x3, 0x2, 0x2, 0x2, 0x65, 0x66, 0x3,
       0x2, 0x2, 0x2, 0x66, 0x17, 0x3, 0x2, 0x2, 0x2, 0x67, 0x69, 0x7, 0xf,
       0x2, 0x2, 0x68, 0x67, 0x3, 0x2, 0x2, 0x2, 0x69, 0x6a, 0x3, 0x2, 0x2,
       0x2, 0x6a, 0x68, 0x3, 0x2, 0x2, 0x2, 0x6a, 0x6b, 0x3, 0x2, 0x2, 0x2,
       0x6b, 0x19, 0x3, 0x2, 0x2, 0x2, 0x6c, 0x6d, 0x7, 0x4, 0x2, 0x2, 0x6d,
       0x6e, 0x5, 0x18, 0xd, 0x2, 0x6e, 0x1b, 0x3, 0x2, 0x2, 0x2, 0x6f,
       0x70, 0x7, 0x5, 0x2, 0x2, 0x70, 0x72, 0x5, 0x18, 0xd, 0x2, 0x71,
       0x73, 0x5, 0x1e, 0x10, 0x2, 0x72, 0x71, 0x3, 0x2, 0x2, 0x2, 0x72,
       0x73, 0x3, 0x2, 0x2, 0x2, 0x73, 0x75, 0x3, 0x2, 0x2, 0x2, 0x74, 0x76,
       0x7, 0x6, 0x2, 0x2, 0x75, 0x74, 0x3, 0x2, 0x2, 0x2, 0x75, 0x76, 0x3,
       0x2, 0x2, 0x2, 0x76, 0x1d, 0x3, 0x2, 0x2, 0x2, 0x77, 0x7b, 0x7, 0x7,
       0x2, 0x2, 0x78, 0x7a, 0x5, 0x26, 0x14, 0x2, 0x79, 0x78, 0x3, 0x2,
       0x2, 0x2, 0x7a, 0x7d, 0x3, 0x2, 0x2, 0x2, 0x7b, 0x79, 0x3, 0x2, 0x2,
       0x2, 0x7b, 0x7c, 0x3, 0x2, 0x2, 0x2, 0x7c, 0x7e, 0x3, 0x2, 0x2, 0x2,
       0x7d, 0x7b, 0x3, 0x2, 0x2, 0x2, 0x7e, 0x89, 0x5, 0x20, 0x11, 0x2,
       0x7f, 0x83, 0x7, 0x8, 0x2, 0x2, 0x80, 0x82, 0x5, 0x26, 0x14, 0x2,
       0x81, 0x80, 0x3, 0x2, 0x2, 0x2, 0x82, 0x85, 0x3, 0x2, 0x2, 0x2, 0x83,
       0x81, 0x3, 0x2, 0x2, 0x2, 0x83, 0x84, 0x3, 0x2, 0x2, 0x2, 0x84, 0x86,
       0x3, 0x2, 0x2, 0x2, 0x85, 0x83, 0x3, 0x2, 0x2, 0x2, 0x86, 0x88, 0x5,
       0x20, 0x11, 0x2, 0x87, 0x7f, 0x3, 0x2, 0x2, 0x2, 0x88, 0x8b, 0x3,
       0x2, 0x2, 0x2, 0x89, 0x8a, 0x3, 0x2, 0x2, 0x2, 0x89, 0x87, 0x3, 0x2,
       0x2, 0x2, 0x8a, 0x8d, 0x3, 0x2, 0x2, 0x2, 0x8b, 0x89, 0x3, 0x2, 0x2,
       0x2, 0x8c, 0x8e, 0x7, 0x8, 0x2, 0x2, 0x8d, 0x8c, 0x3, 0x2, 0x2, 0x2,
       0x8d, 0x8e, 0x3, 0x2, 0x2, 0x2, 0x8e, 0x92, 0x3, 0x2, 0x2, 0x2, 0x8f,
       0x91, 0x5, 0x26, 0x14, 0x2, 0x90, 0x8f, 0x3, 0x2, 0x2, 0x2, 0x91,
       0x94, 0x3, 0x2, 0x2, 0x2, 0x92, 0x90, 0x3, 0x2, 0x2, 0x2, 0x92, 0x93,
       0x3, 0x2, 0x2, 0x2, 0x93, 0x95, 0x3, 0x2, 0x2, 0x2, 0x94, 0x92, 0x3,
       0x2, 0x2, 0x2, 0x95, 0x96, 0x7, 0x9, 0x2, 0x2, 0x96, 0x1f, 0x3, 0x2,
       0x2, 0x2, 0x97, 0x9a, 0x5, 0x22, 0x12, 0x2, 0x98, 0x9a, 0x5, 0x24,
       0x13, 0x2, 0x99, 0x97, 0x3, 0x2, 0x2, 0x2, 0x99, 0x98, 0x3, 0x2,
       0x2, 0x2, 0x9a, 0x21, 0x3, 0x2, 0x2, 0x2, 0x9b, 0x9f, 0x5, 0x18,
       0xd, 0x2, 0x9c, 0x9e, 0x7, 0xe, 0x2, 0x2, 0x9d, 0x9c, 0x3, 0x2, 0x2,
       0x2, 0x9e, 0xa1, 0x3, 0x2, 0x2, 0x2, 0x9f, 0x9d, 0x3, 0x2, 0x2, 0x2,
       0x9f, 0xa0, 0x3, 0x2, 0x2, 0x2, 0xa0, 0xa2, 0x3, 0x2, 0x2, 0x2, 0xa1,
       0x9f, 0x3, 0x2, 0x2, 0x2, 0xa2, 0xa6, 0x7, 0xa, 0x2, 0x2, 0xa3, 0xa5,
       0x7, 0xe, 0x2, 0x2, 0xa4, 0xa3, 0x3, 0x2, 0x2, 0x2, 0xa5, 0xa8, 0x3,
       0x2, 0x2, 0x2, 0xa6, 0xa4, 0x3, 0x2, 0x2, 0x2, 0xa6, 0xa7, 0x3, 0x2,
       0x2, 0x2, 0xa7, 0xa9, 0x3, 0x2, 0x2, 0x2, 0xa8, 0xa6, 0x3, 0x2, 0x2,
       0x2, 0xa9, 0xaa, 0x5, 0x8, 0x5, 0x2, 0xaa, 0x23, 0x3, 0x2, 0x2, 0x2,
       0xab, 0xac, 0x5, 0x8, 0x5, 0x2, 0xac, 0x25, 0x3, 0x2, 0x2, 0x2, 0xad,
       0xaf, 0x9, 0x2, 0x2, 0x2, 0xae, 0xad, 0x3, 0x2, 0x2, 0x2, 0xaf, 0xb0,
       0x3, 0x2, 0x2, 0x2, 0xb0, 0xae, 0x3, 0x2, 0x2, 0x2, 0xb0, 0xb1, 0x3,
       0x2, 0x2, 0x2, 0xb1, 0x27, 0x3, 0x2, 0x2, 0x2, 0x17, 0x2c, 0x36,
       0x3c, 0x3e, 0x43, 0x48, 0x4d, 0x63, 0x65, 0x6a, 0x72, 0x75, 0x7b,
       0x83, 0x89, 0x8d, 0x92, 0x99, 0x9f, 0xa6, 0xb0,
  };

  _serializedATN.insert(_serializedATN.end(), serializedATNSegment0,
    serializedATNSegment0 + sizeof(serializedATNSegment0) / sizeof(serializedATNSegment0[0]));


  atn::ATNDeserializer deserializer;
  _atn = deserializer.deserialize(_serializedATN);

  size_t count = _atn.getNumberOfDecisions();
  _decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) {
    _decisionToDFA.emplace_back(_atn.getDecisionState(i), i);
  }
}

zoiaParser::Initializer zoiaParser::_init;
