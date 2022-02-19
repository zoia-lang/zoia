
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
      ((1ULL << _la) & ((1ULL << zoiaParser::Asterisk)
      | (1ULL << zoiaParser::At)
      | (1ULL << zoiaParser::Backslash)
      | (1ULL << zoiaParser::Newline)
      | (1ULL << zoiaParser::Spaces)
      | (1ULL << zoiaParser::Word))) != 0)) {
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

tree::TerminalNode* zoiaParser::HeaderContext::Header() {
  return getToken(zoiaParser::Header, 0);
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
    match(zoiaParser::Header);
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
      ((1ULL << _la) & ((1ULL << zoiaParser::Asterisk)
      | (1ULL << zoiaParser::At)
      | (1ULL << zoiaParser::Backslash)
      | (1ULL << zoiaParser::Spaces)
      | (1ULL << zoiaParser::Word))) != 0)) {
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

std::vector<zoiaParser::TextFragmentContext *> zoiaParser::LineElementsContext::textFragment() {
  return getRuleContexts<zoiaParser::TextFragmentContext>();
}

zoiaParser::TextFragmentContext* zoiaParser::LineElementsContext::textFragment(size_t i) {
  return getRuleContext<zoiaParser::TextFragmentContext>(i);
}

std::vector<zoiaParser::AliasContext *> zoiaParser::LineElementsContext::alias() {
  return getRuleContexts<zoiaParser::AliasContext>();
}

zoiaParser::AliasContext* zoiaParser::LineElementsContext::alias(size_t i) {
  return getRuleContext<zoiaParser::AliasContext>(i);
}

std::vector<zoiaParser::CommandContext *> zoiaParser::LineElementsContext::command() {
  return getRuleContexts<zoiaParser::CommandContext>();
}

zoiaParser::CommandContext* zoiaParser::LineElementsContext::command(size_t i) {
  return getRuleContext<zoiaParser::CommandContext>(i);
}

std::vector<zoiaParser::Em1LineElementContext *> zoiaParser::LineElementsContext::em1LineElement() {
  return getRuleContexts<zoiaParser::Em1LineElementContext>();
}

zoiaParser::Em1LineElementContext* zoiaParser::LineElementsContext::em1LineElement(size_t i) {
  return getRuleContext<zoiaParser::Em1LineElementContext>(i);
}

std::vector<zoiaParser::Em2LineElementContext *> zoiaParser::LineElementsContext::em2LineElement() {
  return getRuleContexts<zoiaParser::Em2LineElementContext>();
}

zoiaParser::Em2LineElementContext* zoiaParser::LineElementsContext::em2LineElement(size_t i) {
  return getRuleContext<zoiaParser::Em2LineElementContext>(i);
}

std::vector<zoiaParser::Em3LineElementContext *> zoiaParser::LineElementsContext::em3LineElement() {
  return getRuleContexts<zoiaParser::Em3LineElementContext>();
}

zoiaParser::Em3LineElementContext* zoiaParser::LineElementsContext::em3LineElement(size_t i) {
  return getRuleContext<zoiaParser::Em3LineElementContext>(i);
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
    setState(62);
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(62);
      _errHandler->sync(this);
      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 2, _ctx)) {
      case 1: {
        setState(56);
        textFragment();
        break;
      }

      case 2: {
        setState(57);
        alias();
        break;
      }

      case 3: {
        setState(58);
        command();
        break;
      }

      case 4: {
        setState(59);
        em1LineElement();
        break;
      }

      case 5: {
        setState(60);
        em2LineElement();
        break;
      }

      case 6: {
        setState(61);
        em3LineElement();
        break;
      }

      default:
        break;
      }
      setState(64);
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & ((1ULL << zoiaParser::Asterisk)
      | (1ULL << zoiaParser::At)
      | (1ULL << zoiaParser::Backslash)
      | (1ULL << zoiaParser::Spaces)
      | (1ULL << zoiaParser::Word))) != 0));

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- LineElementsInnerContext ------------------------------------------------------------------

zoiaParser::LineElementsInnerContext::LineElementsInnerContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<zoiaParser::TextFragmentReqContext *> zoiaParser::LineElementsInnerContext::textFragmentReq() {
  return getRuleContexts<zoiaParser::TextFragmentReqContext>();
}

zoiaParser::TextFragmentReqContext* zoiaParser::LineElementsInnerContext::textFragmentReq(size_t i) {
  return getRuleContext<zoiaParser::TextFragmentReqContext>(i);
}

std::vector<zoiaParser::AliasContext *> zoiaParser::LineElementsInnerContext::alias() {
  return getRuleContexts<zoiaParser::AliasContext>();
}

zoiaParser::AliasContext* zoiaParser::LineElementsInnerContext::alias(size_t i) {
  return getRuleContext<zoiaParser::AliasContext>(i);
}

std::vector<zoiaParser::CommandContext *> zoiaParser::LineElementsInnerContext::command() {
  return getRuleContexts<zoiaParser::CommandContext>();
}

zoiaParser::CommandContext* zoiaParser::LineElementsInnerContext::command(size_t i) {
  return getRuleContext<zoiaParser::CommandContext>(i);
}


size_t zoiaParser::LineElementsInnerContext::getRuleIndex() const {
  return zoiaParser::RuleLineElementsInner;
}


antlrcpp::Any zoiaParser::LineElementsInnerContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<zoiaVisitor*>(visitor))
    return parserVisitor->visitLineElementsInner(this);
  else
    return visitor->visitChildren(this);
}

zoiaParser::LineElementsInnerContext* zoiaParser::lineElementsInner() {
  LineElementsInnerContext *_localctx = _tracker.createInstance<LineElementsInnerContext>(_ctx, getState());
  enterRule(_localctx, 8, zoiaParser::RuleLineElementsInner);
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
    setState(69);
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(69);
      _errHandler->sync(this);
      switch (_input->LA(1)) {
        case zoiaParser::Spaces:
        case zoiaParser::Word: {
          setState(66);
          textFragmentReq();
          break;
        }

        case zoiaParser::At: {
          setState(67);
          alias();
          break;
        }

        case zoiaParser::Backslash: {
          setState(68);
          command();
          break;
        }

      default:
        throw NoViableAltException(this);
      }
      setState(71);
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & ((1ULL << zoiaParser::At)
      | (1ULL << zoiaParser::Backslash)
      | (1ULL << zoiaParser::Spaces)
      | (1ULL << zoiaParser::Word))) != 0));

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- LineElementsArgContext ------------------------------------------------------------------

zoiaParser::LineElementsArgContext::LineElementsArgContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

zoiaParser::TextFragmentWordContext* zoiaParser::LineElementsArgContext::textFragmentWord() {
  return getRuleContext<zoiaParser::TextFragmentWordContext>(0);
}

std::vector<zoiaParser::AliasContext *> zoiaParser::LineElementsArgContext::alias() {
  return getRuleContexts<zoiaParser::AliasContext>();
}

zoiaParser::AliasContext* zoiaParser::LineElementsArgContext::alias(size_t i) {
  return getRuleContext<zoiaParser::AliasContext>(i);
}

std::vector<zoiaParser::CommandContext *> zoiaParser::LineElementsArgContext::command() {
  return getRuleContexts<zoiaParser::CommandContext>();
}

zoiaParser::CommandContext* zoiaParser::LineElementsArgContext::command(size_t i) {
  return getRuleContext<zoiaParser::CommandContext>(i);
}

std::vector<zoiaParser::Em1LineElementContext *> zoiaParser::LineElementsArgContext::em1LineElement() {
  return getRuleContexts<zoiaParser::Em1LineElementContext>();
}

zoiaParser::Em1LineElementContext* zoiaParser::LineElementsArgContext::em1LineElement(size_t i) {
  return getRuleContext<zoiaParser::Em1LineElementContext>(i);
}

std::vector<zoiaParser::Em2LineElementContext *> zoiaParser::LineElementsArgContext::em2LineElement() {
  return getRuleContexts<zoiaParser::Em2LineElementContext>();
}

zoiaParser::Em2LineElementContext* zoiaParser::LineElementsArgContext::em2LineElement(size_t i) {
  return getRuleContext<zoiaParser::Em2LineElementContext>(i);
}

std::vector<zoiaParser::Em3LineElementContext *> zoiaParser::LineElementsArgContext::em3LineElement() {
  return getRuleContexts<zoiaParser::Em3LineElementContext>();
}

zoiaParser::Em3LineElementContext* zoiaParser::LineElementsArgContext::em3LineElement(size_t i) {
  return getRuleContext<zoiaParser::Em3LineElementContext>(i);
}

std::vector<zoiaParser::TextFragmentContext *> zoiaParser::LineElementsArgContext::textFragment() {
  return getRuleContexts<zoiaParser::TextFragmentContext>();
}

zoiaParser::TextFragmentContext* zoiaParser::LineElementsArgContext::textFragment(size_t i) {
  return getRuleContext<zoiaParser::TextFragmentContext>(i);
}


size_t zoiaParser::LineElementsArgContext::getRuleIndex() const {
  return zoiaParser::RuleLineElementsArg;
}


antlrcpp::Any zoiaParser::LineElementsArgContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<zoiaVisitor*>(visitor))
    return parserVisitor->visitLineElementsArg(this);
  else
    return visitor->visitChildren(this);
}

zoiaParser::LineElementsArgContext* zoiaParser::lineElementsArg() {
  LineElementsArgContext *_localctx = _tracker.createInstance<LineElementsArgContext>(_ctx, getState());
  enterRule(_localctx, 10, zoiaParser::RuleLineElementsArg);

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
    setState(79);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 6, _ctx)) {
    case 1: {
      setState(73);
      textFragmentWord();
      break;
    }

    case 2: {
      setState(74);
      alias();
      break;
    }

    case 3: {
      setState(75);
      command();
      break;
    }

    case 4: {
      setState(76);
      em1LineElement();
      break;
    }

    case 5: {
      setState(77);
      em2LineElement();
      break;
    }

    case 6: {
      setState(78);
      em3LineElement();
      break;
    }

    default:
      break;
    }
    setState(89);
    _errHandler->sync(this);
    alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 8, _ctx);
    while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER) {
      if (alt == 1) {
        setState(87);
        _errHandler->sync(this);
        switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 7, _ctx)) {
        case 1: {
          setState(81);
          textFragment();
          break;
        }

        case 2: {
          setState(82);
          alias();
          break;
        }

        case 3: {
          setState(83);
          command();
          break;
        }

        case 4: {
          setState(84);
          em1LineElement();
          break;
        }

        case 5: {
          setState(85);
          em2LineElement();
          break;
        }

        case 6: {
          setState(86);
          em3LineElement();
          break;
        }

        default:
          break;
        }
      }
      setState(91);
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 8, _ctx);
    }

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Em3LineElementContext ------------------------------------------------------------------

zoiaParser::Em3LineElementContext::Em3LineElementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> zoiaParser::Em3LineElementContext::Asterisk() {
  return getTokens(zoiaParser::Asterisk);
}

tree::TerminalNode* zoiaParser::Em3LineElementContext::Asterisk(size_t i) {
  return getToken(zoiaParser::Asterisk, i);
}

zoiaParser::LineElementsInnerContext* zoiaParser::Em3LineElementContext::lineElementsInner() {
  return getRuleContext<zoiaParser::LineElementsInnerContext>(0);
}


size_t zoiaParser::Em3LineElementContext::getRuleIndex() const {
  return zoiaParser::RuleEm3LineElement;
}


antlrcpp::Any zoiaParser::Em3LineElementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<zoiaVisitor*>(visitor))
    return parserVisitor->visitEm3LineElement(this);
  else
    return visitor->visitChildren(this);
}

zoiaParser::Em3LineElementContext* zoiaParser::em3LineElement() {
  Em3LineElementContext *_localctx = _tracker.createInstance<Em3LineElementContext>(_ctx, getState());
  enterRule(_localctx, 12, zoiaParser::RuleEm3LineElement);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(92);
    match(zoiaParser::Asterisk);
    setState(93);
    match(zoiaParser::Asterisk);
    setState(94);
    match(zoiaParser::Asterisk);
    setState(95);
    lineElementsInner();
    setState(96);
    match(zoiaParser::Asterisk);
    setState(97);
    match(zoiaParser::Asterisk);
    setState(98);
    match(zoiaParser::Asterisk);

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Em2LineElementContext ------------------------------------------------------------------

zoiaParser::Em2LineElementContext::Em2LineElementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> zoiaParser::Em2LineElementContext::Asterisk() {
  return getTokens(zoiaParser::Asterisk);
}

tree::TerminalNode* zoiaParser::Em2LineElementContext::Asterisk(size_t i) {
  return getToken(zoiaParser::Asterisk, i);
}

zoiaParser::LineElementsInnerContext* zoiaParser::Em2LineElementContext::lineElementsInner() {
  return getRuleContext<zoiaParser::LineElementsInnerContext>(0);
}


size_t zoiaParser::Em2LineElementContext::getRuleIndex() const {
  return zoiaParser::RuleEm2LineElement;
}


antlrcpp::Any zoiaParser::Em2LineElementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<zoiaVisitor*>(visitor))
    return parserVisitor->visitEm2LineElement(this);
  else
    return visitor->visitChildren(this);
}

zoiaParser::Em2LineElementContext* zoiaParser::em2LineElement() {
  Em2LineElementContext *_localctx = _tracker.createInstance<Em2LineElementContext>(_ctx, getState());
  enterRule(_localctx, 14, zoiaParser::RuleEm2LineElement);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(100);
    match(zoiaParser::Asterisk);
    setState(101);
    match(zoiaParser::Asterisk);
    setState(102);
    lineElementsInner();
    setState(103);
    match(zoiaParser::Asterisk);
    setState(104);
    match(zoiaParser::Asterisk);

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Em1LineElementContext ------------------------------------------------------------------

zoiaParser::Em1LineElementContext::Em1LineElementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> zoiaParser::Em1LineElementContext::Asterisk() {
  return getTokens(zoiaParser::Asterisk);
}

tree::TerminalNode* zoiaParser::Em1LineElementContext::Asterisk(size_t i) {
  return getToken(zoiaParser::Asterisk, i);
}

zoiaParser::LineElementsInnerContext* zoiaParser::Em1LineElementContext::lineElementsInner() {
  return getRuleContext<zoiaParser::LineElementsInnerContext>(0);
}


size_t zoiaParser::Em1LineElementContext::getRuleIndex() const {
  return zoiaParser::RuleEm1LineElement;
}


antlrcpp::Any zoiaParser::Em1LineElementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<zoiaVisitor*>(visitor))
    return parserVisitor->visitEm1LineElement(this);
  else
    return visitor->visitChildren(this);
}

zoiaParser::Em1LineElementContext* zoiaParser::em1LineElement() {
  Em1LineElementContext *_localctx = _tracker.createInstance<Em1LineElementContext>(_ctx, getState());
  enterRule(_localctx, 16, zoiaParser::RuleEm1LineElement);

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
    match(zoiaParser::Asterisk);
    setState(107);
    lineElementsInner();
    setState(108);
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

tree::TerminalNode* zoiaParser::TextFragmentContext::Word() {
  return getToken(zoiaParser::Word, 0);
}

tree::TerminalNode* zoiaParser::TextFragmentContext::Spaces() {
  return getToken(zoiaParser::Spaces, 0);
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
  enterRule(_localctx, 18, zoiaParser::RuleTextFragment);
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
    setState(110);
    _la = _input->LA(1);
    if (!(_la == zoiaParser::Spaces

    || _la == zoiaParser::Word)) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- TextFragmentReqContext ------------------------------------------------------------------

zoiaParser::TextFragmentReqContext::TextFragmentReqContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* zoiaParser::TextFragmentReqContext::Word() {
  return getToken(zoiaParser::Word, 0);
}

std::vector<tree::TerminalNode *> zoiaParser::TextFragmentReqContext::Spaces() {
  return getTokens(zoiaParser::Spaces);
}

tree::TerminalNode* zoiaParser::TextFragmentReqContext::Spaces(size_t i) {
  return getToken(zoiaParser::Spaces, i);
}


size_t zoiaParser::TextFragmentReqContext::getRuleIndex() const {
  return zoiaParser::RuleTextFragmentReq;
}


antlrcpp::Any zoiaParser::TextFragmentReqContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<zoiaVisitor*>(visitor))
    return parserVisitor->visitTextFragmentReq(this);
  else
    return visitor->visitChildren(this);
}

zoiaParser::TextFragmentReqContext* zoiaParser::textFragmentReq() {
  TextFragmentReqContext *_localctx = _tracker.createInstance<TextFragmentReqContext>(_ctx, getState());
  enterRule(_localctx, 20, zoiaParser::RuleTextFragmentReq);
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
    setState(113);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == zoiaParser::Spaces) {
      setState(112);
      match(zoiaParser::Spaces);
    }
    setState(115);
    match(zoiaParser::Word);
    setState(117);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 10, _ctx)) {
    case 1: {
      setState(116);
      match(zoiaParser::Spaces);
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

//----------------- TextFragmentWordContext ------------------------------------------------------------------

zoiaParser::TextFragmentWordContext::TextFragmentWordContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* zoiaParser::TextFragmentWordContext::Word() {
  return getToken(zoiaParser::Word, 0);
}

tree::TerminalNode* zoiaParser::TextFragmentWordContext::Spaces() {
  return getToken(zoiaParser::Spaces, 0);
}


size_t zoiaParser::TextFragmentWordContext::getRuleIndex() const {
  return zoiaParser::RuleTextFragmentWord;
}


antlrcpp::Any zoiaParser::TextFragmentWordContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<zoiaVisitor*>(visitor))
    return parserVisitor->visitTextFragmentWord(this);
  else
    return visitor->visitChildren(this);
}

zoiaParser::TextFragmentWordContext* zoiaParser::textFragmentWord() {
  TextFragmentWordContext *_localctx = _tracker.createInstance<TextFragmentWordContext>(_ctx, getState());
  enterRule(_localctx, 22, zoiaParser::RuleTextFragmentWord);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(119);
    match(zoiaParser::Word);
    setState(121);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 11, _ctx)) {
    case 1: {
      setState(120);
      match(zoiaParser::Spaces);
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

//----------------- AliasContext ------------------------------------------------------------------

zoiaParser::AliasContext::AliasContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* zoiaParser::AliasContext::At() {
  return getToken(zoiaParser::At, 0);
}

tree::TerminalNode* zoiaParser::AliasContext::Word() {
  return getToken(zoiaParser::Word, 0);
}

tree::TerminalNode* zoiaParser::AliasContext::Bar() {
  return getToken(zoiaParser::Bar, 0);
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
    setState(123);
    match(zoiaParser::At);
    setState(124);
    match(zoiaParser::Word);
    setState(126);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == zoiaParser::Bar) {
      setState(125);
      match(zoiaParser::Bar);
    }

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

tree::TerminalNode* zoiaParser::CommandContext::Backslash() {
  return getToken(zoiaParser::Backslash, 0);
}

tree::TerminalNode* zoiaParser::CommandContext::Word() {
  return getToken(zoiaParser::Word, 0);
}

zoiaParser::ArgumentsContext* zoiaParser::CommandContext::arguments() {
  return getRuleContext<zoiaParser::ArgumentsContext>(0);
}

tree::TerminalNode* zoiaParser::CommandContext::Bar() {
  return getToken(zoiaParser::Bar, 0);
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
    setState(128);
    match(zoiaParser::Backslash);
    setState(129);
    match(zoiaParser::Word);
    setState(131);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == zoiaParser::BracketsOpen) {
      setState(130);
      arguments();
    }
    setState(134);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == zoiaParser::Bar) {
      setState(133);
      match(zoiaParser::Bar);
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

tree::TerminalNode* zoiaParser::ArgumentsContext::BracketsOpen() {
  return getToken(zoiaParser::BracketsOpen, 0);
}

std::vector<zoiaParser::ArgumentContext *> zoiaParser::ArgumentsContext::argument() {
  return getRuleContexts<zoiaParser::ArgumentContext>();
}

zoiaParser::ArgumentContext* zoiaParser::ArgumentsContext::argument(size_t i) {
  return getRuleContext<zoiaParser::ArgumentContext>(i);
}

tree::TerminalNode* zoiaParser::ArgumentsContext::BracketsClose() {
  return getToken(zoiaParser::BracketsClose, 0);
}

std::vector<zoiaParser::WhitespaceContext *> zoiaParser::ArgumentsContext::whitespace() {
  return getRuleContexts<zoiaParser::WhitespaceContext>();
}

zoiaParser::WhitespaceContext* zoiaParser::ArgumentsContext::whitespace(size_t i) {
  return getRuleContext<zoiaParser::WhitespaceContext>(i);
}

std::vector<tree::TerminalNode *> zoiaParser::ArgumentsContext::Semicolon() {
  return getTokens(zoiaParser::Semicolon);
}

tree::TerminalNode* zoiaParser::ArgumentsContext::Semicolon(size_t i) {
  return getToken(zoiaParser::Semicolon, i);
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
    setState(136);
    match(zoiaParser::BracketsOpen);
    setState(138);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == zoiaParser::Newline

    || _la == zoiaParser::Spaces) {
      setState(137);
      whitespace();
    }
    setState(140);
    argument();
    setState(148);
    _errHandler->sync(this);
    alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 17, _ctx);
    while (alt != 1 && alt != atn::ATN::INVALID_ALT_NUMBER) {
      if (alt == 1 + 1) {
        setState(141);
        match(zoiaParser::Semicolon);
        setState(143);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == zoiaParser::Newline

        || _la == zoiaParser::Spaces) {
          setState(142);
          whitespace();
        }
        setState(145);
        argument();
      }
      setState(150);
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 17, _ctx);
    }
    setState(152);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == zoiaParser::Semicolon) {
      setState(151);
      match(zoiaParser::Semicolon);
    }
    setState(155);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == zoiaParser::Newline

    || _la == zoiaParser::Spaces) {
      setState(154);
      whitespace();
    }
    setState(157);
    match(zoiaParser::BracketsClose);

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
    setState(161);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 20, _ctx)) {
    case 1: {
      enterOuterAlt(_localctx, 1);
      setState(159);
      kwdArgument();
      break;
    }

    case 2: {
      enterOuterAlt(_localctx, 2);
      setState(160);
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

tree::TerminalNode* zoiaParser::KwdArgumentContext::Word() {
  return getToken(zoiaParser::Word, 0);
}

tree::TerminalNode* zoiaParser::KwdArgumentContext::Equals() {
  return getToken(zoiaParser::Equals, 0);
}

zoiaParser::LineElementsArgContext* zoiaParser::KwdArgumentContext::lineElementsArg() {
  return getRuleContext<zoiaParser::LineElementsArgContext>(0);
}

std::vector<tree::TerminalNode *> zoiaParser::KwdArgumentContext::Spaces() {
  return getTokens(zoiaParser::Spaces);
}

tree::TerminalNode* zoiaParser::KwdArgumentContext::Spaces(size_t i) {
  return getToken(zoiaParser::Spaces, i);
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
    enterOuterAlt(_localctx, 1);
    setState(163);
    match(zoiaParser::Word);
    setState(165);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == zoiaParser::Spaces) {
      setState(164);
      match(zoiaParser::Spaces);
    }
    setState(167);
    match(zoiaParser::Equals);
    setState(169);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == zoiaParser::Spaces) {
      setState(168);
      match(zoiaParser::Spaces);
    }
    setState(171);
    lineElementsArg();

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

zoiaParser::LineElementsArgContext* zoiaParser::StdArgumentContext::lineElementsArg() {
  return getRuleContext<zoiaParser::LineElementsArgContext>(0);
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
    setState(173);
    lineElementsArg();

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

std::vector<tree::TerminalNode *> zoiaParser::WhitespaceContext::Spaces() {
  return getTokens(zoiaParser::Spaces);
}

tree::TerminalNode* zoiaParser::WhitespaceContext::Spaces(size_t i) {
  return getToken(zoiaParser::Spaces, i);
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
    enterOuterAlt(_localctx, 1);
    setState(176);
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(175);
      _la = _input->LA(1);
      if (!(_la == zoiaParser::Newline

      || _la == zoiaParser::Spaces)) {
      _errHandler->recoverInline(this);
      }
      else {
        _errHandler->reportMatch(this);
        consume();
      }
      setState(178);
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == zoiaParser::Newline

    || _la == zoiaParser::Spaces);

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
  "zoiaFile", "header", "line", "lineElements", "lineElementsInner", "lineElementsArg",
  "em3LineElement", "em2LineElement", "em1LineElement", "textFragment",
  "textFragmentReq", "textFragmentWord", "alias", "command", "arguments",
  "argument", "kwdArgument", "stdArgument", "whitespace"
};

std::vector<std::string> zoiaParser::_literalNames = {
  "", "", "'*'", "'@'", "'\\'", "'|'", "']'", "'['", "'='", "'\\header'",
  "", "';'"
};

std::vector<std::string> zoiaParser::_symbolicNames = {
  "", "COMMENT", "Asterisk", "At", "Backslash", "Bar", "BracketsClose",
  "BracketsOpen", "Equals", "Header", "Newline", "Semicolon", "Spaces",
  "Word"
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
       0x3, 0xf, 0xb7, 0x4, 0x2, 0x9, 0x2, 0x4, 0x3, 0x9, 0x3, 0x4, 0x4,
       0x9, 0x4, 0x4, 0x5, 0x9, 0x5, 0x4, 0x6, 0x9, 0x6, 0x4, 0x7, 0x9,
       0x7, 0x4, 0x8, 0x9, 0x8, 0x4, 0x9, 0x9, 0x9, 0x4, 0xa, 0x9, 0xa,
       0x4, 0xb, 0x9, 0xb, 0x4, 0xc, 0x9, 0xc, 0x4, 0xd, 0x9, 0xd, 0x4,
       0xe, 0x9, 0xe, 0x4, 0xf, 0x9, 0xf, 0x4, 0x10, 0x9, 0x10, 0x4, 0x11,
       0x9, 0x11, 0x4, 0x12, 0x9, 0x12, 0x4, 0x13, 0x9, 0x13, 0x4, 0x14,
       0x9, 0x14, 0x3, 0x2, 0x3, 0x2, 0x7, 0x2, 0x2b, 0xa, 0x2, 0xc, 0x2,
       0xe, 0x2, 0x2e, 0xb, 0x2, 0x3, 0x2, 0x3, 0x2, 0x3, 0x3, 0x3, 0x3,
       0x3, 0x3, 0x3, 0x3, 0x3, 0x4, 0x5, 0x4, 0x37, 0xa, 0x4, 0x3, 0x4,
       0x3, 0x4, 0x3, 0x5, 0x3, 0x5, 0x3, 0x5, 0x3, 0x5, 0x3, 0x5, 0x3,
       0x5, 0x6, 0x5, 0x41, 0xa, 0x5, 0xd, 0x5, 0xe, 0x5, 0x42, 0x3, 0x6,
       0x3, 0x6, 0x3, 0x6, 0x6, 0x6, 0x48, 0xa, 0x6, 0xd, 0x6, 0xe, 0x6,
       0x49, 0x3, 0x7, 0x3, 0x7, 0x3, 0x7, 0x3, 0x7, 0x3, 0x7, 0x3, 0x7,
       0x5, 0x7, 0x52, 0xa, 0x7, 0x3, 0x7, 0x3, 0x7, 0x3, 0x7, 0x3, 0x7,
       0x3, 0x7, 0x3, 0x7, 0x7, 0x7, 0x5a, 0xa, 0x7, 0xc, 0x7, 0xe, 0x7,
       0x5d, 0xb, 0x7, 0x3, 0x8, 0x3, 0x8, 0x3, 0x8, 0x3, 0x8, 0x3, 0x8,
       0x3, 0x8, 0x3, 0x8, 0x3, 0x8, 0x3, 0x9, 0x3, 0x9, 0x3, 0x9, 0x3,
       0x9, 0x3, 0x9, 0x3, 0x9, 0x3, 0xa, 0x3, 0xa, 0x3, 0xa, 0x3, 0xa,
       0x3, 0xb, 0x3, 0xb, 0x3, 0xc, 0x5, 0xc, 0x74, 0xa, 0xc, 0x3, 0xc,
       0x3, 0xc, 0x5, 0xc, 0x78, 0xa, 0xc, 0x3, 0xd, 0x3, 0xd, 0x5, 0xd,
       0x7c, 0xa, 0xd, 0x3, 0xe, 0x3, 0xe, 0x3, 0xe, 0x5, 0xe, 0x81, 0xa,
       0xe, 0x3, 0xf, 0x3, 0xf, 0x3, 0xf, 0x5, 0xf, 0x86, 0xa, 0xf, 0x3,
       0xf, 0x5, 0xf, 0x89, 0xa, 0xf, 0x3, 0x10, 0x3, 0x10, 0x5, 0x10, 0x8d,
       0xa, 0x10, 0x3, 0x10, 0x3, 0x10, 0x3, 0x10, 0x5, 0x10, 0x92, 0xa,
       0x10, 0x3, 0x10, 0x7, 0x10, 0x95, 0xa, 0x10, 0xc, 0x10, 0xe, 0x10,
       0x98, 0xb, 0x10, 0x3, 0x10, 0x5, 0x10, 0x9b, 0xa, 0x10, 0x3, 0x10,
       0x5, 0x10, 0x9e, 0xa, 0x10, 0x3, 0x10, 0x3, 0x10, 0x3, 0x11, 0x3,
       0x11, 0x5, 0x11, 0xa4, 0xa, 0x11, 0x3, 0x12, 0x3, 0x12, 0x5, 0x12,
       0xa8, 0xa, 0x12, 0x3, 0x12, 0x3, 0x12, 0x5, 0x12, 0xac, 0xa, 0x12,
       0x3, 0x12, 0x3, 0x12, 0x3, 0x13, 0x3, 0x13, 0x3, 0x14, 0x6, 0x14,
       0xb3, 0xa, 0x14, 0xd, 0x14, 0xe, 0x14, 0xb4, 0x3, 0x14, 0x3, 0x96,
       0x2, 0x15, 0x2, 0x4, 0x6, 0x8, 0xa, 0xc, 0xe, 0x10, 0x12, 0x14, 0x16,
       0x18, 0x1a, 0x1c, 0x1e, 0x20, 0x22, 0x24, 0x26, 0x2, 0x4, 0x3, 0x2,
       0xe, 0xf, 0x4, 0x2, 0xc, 0xc, 0xe, 0xe, 0x2, 0xc8, 0x2, 0x28, 0x3,
       0x2, 0x2, 0x2, 0x4, 0x31, 0x3, 0x2, 0x2, 0x2, 0x6, 0x36, 0x3, 0x2,
       0x2, 0x2, 0x8, 0x40, 0x3, 0x2, 0x2, 0x2, 0xa, 0x47, 0x3, 0x2, 0x2,
       0x2, 0xc, 0x51, 0x3, 0x2, 0x2, 0x2, 0xe, 0x5e, 0x3, 0x2, 0x2, 0x2,
       0x10, 0x66, 0x3, 0x2, 0x2, 0x2, 0x12, 0x6c, 0x3, 0x2, 0x2, 0x2, 0x14,
       0x70, 0x3, 0x2, 0x2, 0x2, 0x16, 0x73, 0x3, 0x2, 0x2, 0x2, 0x18, 0x79,
       0x3, 0x2, 0x2, 0x2, 0x1a, 0x7d, 0x3, 0x2, 0x2, 0x2, 0x1c, 0x82, 0x3,
       0x2, 0x2, 0x2, 0x1e, 0x8a, 0x3, 0x2, 0x2, 0x2, 0x20, 0xa3, 0x3, 0x2,
       0x2, 0x2, 0x22, 0xa5, 0x3, 0x2, 0x2, 0x2, 0x24, 0xaf, 0x3, 0x2, 0x2,
       0x2, 0x26, 0xb2, 0x3, 0x2, 0x2, 0x2, 0x28, 0x2c, 0x5, 0x4, 0x3, 0x2,
       0x29, 0x2b, 0x5, 0x6, 0x4, 0x2, 0x2a, 0x29, 0x3, 0x2, 0x2, 0x2, 0x2b,
       0x2e, 0x3, 0x2, 0x2, 0x2, 0x2c, 0x2a, 0x3, 0x2, 0x2, 0x2, 0x2c, 0x2d,
       0x3, 0x2, 0x2, 0x2, 0x2d, 0x2f, 0x3, 0x2, 0x2, 0x2, 0x2e, 0x2c, 0x3,
       0x2, 0x2, 0x2, 0x2f, 0x30, 0x7, 0x2, 0x2, 0x3, 0x30, 0x3, 0x3, 0x2,
       0x2, 0x2, 0x31, 0x32, 0x7, 0xb, 0x2, 0x2, 0x32, 0x33, 0x5, 0x1e,
       0x10, 0x2, 0x33, 0x34, 0x7, 0xc, 0x2, 0x2, 0x34, 0x5, 0x3, 0x2, 0x2,
       0x2, 0x35, 0x37, 0x5, 0x8, 0x5, 0x2, 0x36, 0x35, 0x3, 0x2, 0x2, 0x2,
       0x36, 0x37, 0x3, 0x2, 0x2, 0x2, 0x37, 0x38, 0x3, 0x2, 0x2, 0x2, 0x38,
       0x39, 0x7, 0xc, 0x2, 0x2, 0x39, 0x7, 0x3, 0x2, 0x2, 0x2, 0x3a, 0x41,
       0x5, 0x14, 0xb, 0x2, 0x3b, 0x41, 0x5, 0x1a, 0xe, 0x2, 0x3c, 0x41,
       0x5, 0x1c, 0xf, 0x2, 0x3d, 0x41, 0x5, 0x12, 0xa, 0x2, 0x3e, 0x41,
       0x5, 0x10, 0x9, 0x2, 0x3f, 0x41, 0x5, 0xe, 0x8, 0x2, 0x40, 0x3a,
       0x3, 0x2, 0x2, 0x2, 0x40, 0x3b, 0x3, 0x2, 0x2, 0x2, 0x40, 0x3c, 0x3,
       0x2, 0x2, 0x2, 0x40, 0x3d, 0x3, 0x2, 0x2, 0x2, 0x40, 0x3e, 0x3, 0x2,
       0x2, 0x2, 0x40, 0x3f, 0x3, 0x2, 0x2, 0x2, 0x41, 0x42, 0x3, 0x2, 0x2,
       0x2, 0x42, 0x40, 0x3, 0x2, 0x2, 0x2, 0x42, 0x43, 0x3, 0x2, 0x2, 0x2,
       0x43, 0x9, 0x3, 0x2, 0x2, 0x2, 0x44, 0x48, 0x5, 0x16, 0xc, 0x2, 0x45,
       0x48, 0x5, 0x1a, 0xe, 0x2, 0x46, 0x48, 0x5, 0x1c, 0xf, 0x2, 0x47,
       0x44, 0x3, 0x2, 0x2, 0x2, 0x47, 0x45, 0x3, 0x2, 0x2, 0x2, 0x47, 0x46,
       0x3, 0x2, 0x2, 0x2, 0x48, 0x49, 0x3, 0x2, 0x2, 0x2, 0x49, 0x47, 0x3,
       0x2, 0x2, 0x2, 0x49, 0x4a, 0x3, 0x2, 0x2, 0x2, 0x4a, 0xb, 0x3, 0x2,
       0x2, 0x2, 0x4b, 0x52, 0x5, 0x18, 0xd, 0x2, 0x4c, 0x52, 0x5, 0x1a,
       0xe, 0x2, 0x4d, 0x52, 0x5, 0x1c, 0xf, 0x2, 0x4e, 0x52, 0x5, 0x12,
       0xa, 0x2, 0x4f, 0x52, 0x5, 0x10, 0x9, 0x2, 0x50, 0x52, 0x5, 0xe,
       0x8, 0x2, 0x51, 0x4b, 0x3, 0x2, 0x2, 0x2, 0x51, 0x4c, 0x3, 0x2, 0x2,
       0x2, 0x51, 0x4d, 0x3, 0x2, 0x2, 0x2, 0x51, 0x4e, 0x3, 0x2, 0x2, 0x2,
       0x51, 0x4f, 0x3, 0x2, 0x2, 0x2, 0x51, 0x50, 0x3, 0x2, 0x2, 0x2, 0x52,
       0x5b, 0x3, 0x2, 0x2, 0x2, 0x53, 0x5a, 0x5, 0x14, 0xb, 0x2, 0x54,
       0x5a, 0x5, 0x1a, 0xe, 0x2, 0x55, 0x5a, 0x5, 0x1c, 0xf, 0x2, 0x56,
       0x5a, 0x5, 0x12, 0xa, 0x2, 0x57, 0x5a, 0x5, 0x10, 0x9, 0x2, 0x58,
       0x5a, 0x5, 0xe, 0x8, 0x2, 0x59, 0x53, 0x3, 0x2, 0x2, 0x2, 0x59, 0x54,
       0x3, 0x2, 0x2, 0x2, 0x59, 0x55, 0x3, 0x2, 0x2, 0x2, 0x59, 0x56, 0x3,
       0x2, 0x2, 0x2, 0x59, 0x57, 0x3, 0x2, 0x2, 0x2, 0x59, 0x58, 0x3, 0x2,
       0x2, 0x2, 0x5a, 0x5d, 0x3, 0x2, 0x2, 0x2, 0x5b, 0x59, 0x3, 0x2, 0x2,
       0x2, 0x5b, 0x5c, 0x3, 0x2, 0x2, 0x2, 0x5c, 0xd, 0x3, 0x2, 0x2, 0x2,
       0x5d, 0x5b, 0x3, 0x2, 0x2, 0x2, 0x5e, 0x5f, 0x7, 0x4, 0x2, 0x2, 0x5f,
       0x60, 0x7, 0x4, 0x2, 0x2, 0x60, 0x61, 0x7, 0x4, 0x2, 0x2, 0x61, 0x62,
       0x5, 0xa, 0x6, 0x2, 0x62, 0x63, 0x7, 0x4, 0x2, 0x2, 0x63, 0x64, 0x7,
       0x4, 0x2, 0x2, 0x64, 0x65, 0x7, 0x4, 0x2, 0x2, 0x65, 0xf, 0x3, 0x2,
       0x2, 0x2, 0x66, 0x67, 0x7, 0x4, 0x2, 0x2, 0x67, 0x68, 0x7, 0x4, 0x2,
       0x2, 0x68, 0x69, 0x5, 0xa, 0x6, 0x2, 0x69, 0x6a, 0x7, 0x4, 0x2, 0x2,
       0x6a, 0x6b, 0x7, 0x4, 0x2, 0x2, 0x6b, 0x11, 0x3, 0x2, 0x2, 0x2, 0x6c,
       0x6d, 0x7, 0x4, 0x2, 0x2, 0x6d, 0x6e, 0x5, 0xa, 0x6, 0x2, 0x6e, 0x6f,
       0x7, 0x4, 0x2, 0x2, 0x6f, 0x13, 0x3, 0x2, 0x2, 0x2, 0x70, 0x71, 0x9,
       0x2, 0x2, 0x2, 0x71, 0x15, 0x3, 0x2, 0x2, 0x2, 0x72, 0x74, 0x7, 0xe,
       0x2, 0x2, 0x73, 0x72, 0x3, 0x2, 0x2, 0x2, 0x73, 0x74, 0x3, 0x2, 0x2,
       0x2, 0x74, 0x75, 0x3, 0x2, 0x2, 0x2, 0x75, 0x77, 0x7, 0xf, 0x2, 0x2,
       0x76, 0x78, 0x7, 0xe, 0x2, 0x2, 0x77, 0x76, 0x3, 0x2, 0x2, 0x2, 0x77,
       0x78, 0x3, 0x2, 0x2, 0x2, 0x78, 0x17, 0x3, 0x2, 0x2, 0x2, 0x79, 0x7b,
       0x7, 0xf, 0x2, 0x2, 0x7a, 0x7c, 0x7, 0xe, 0x2, 0x2, 0x7b, 0x7a, 0x3,
       0x2, 0x2, 0x2, 0x7b, 0x7c, 0x3, 0x2, 0x2, 0x2, 0x7c, 0x19, 0x3, 0x2,
       0x2, 0x2, 0x7d, 0x7e, 0x7, 0x5, 0x2, 0x2, 0x7e, 0x80, 0x7, 0xf, 0x2,
       0x2, 0x7f, 0x81, 0x7, 0x7, 0x2, 0x2, 0x80, 0x7f, 0x3, 0x2, 0x2, 0x2,
       0x80, 0x81, 0x3, 0x2, 0x2, 0x2, 0x81, 0x1b, 0x3, 0x2, 0x2, 0x2, 0x82,
       0x83, 0x7, 0x6, 0x2, 0x2, 0x83, 0x85, 0x7, 0xf, 0x2, 0x2, 0x84, 0x86,
       0x5, 0x1e, 0x10, 0x2, 0x85, 0x84, 0x3, 0x2, 0x2, 0x2, 0x85, 0x86,
       0x3, 0x2, 0x2, 0x2, 0x86, 0x88, 0x3, 0x2, 0x2, 0x2, 0x87, 0x89, 0x7,
       0x7, 0x2, 0x2, 0x88, 0x87, 0x3, 0x2, 0x2, 0x2, 0x88, 0x89, 0x3, 0x2,
       0x2, 0x2, 0x89, 0x1d, 0x3, 0x2, 0x2, 0x2, 0x8a, 0x8c, 0x7, 0x9, 0x2,
       0x2, 0x8b, 0x8d, 0x5, 0x26, 0x14, 0x2, 0x8c, 0x8b, 0x3, 0x2, 0x2,
       0x2, 0x8c, 0x8d, 0x3, 0x2, 0x2, 0x2, 0x8d, 0x8e, 0x3, 0x2, 0x2, 0x2,
       0x8e, 0x96, 0x5, 0x20, 0x11, 0x2, 0x8f, 0x91, 0x7, 0xd, 0x2, 0x2,
       0x90, 0x92, 0x5, 0x26, 0x14, 0x2, 0x91, 0x90, 0x3, 0x2, 0x2, 0x2,
       0x91, 0x92, 0x3, 0x2, 0x2, 0x2, 0x92, 0x93, 0x3, 0x2, 0x2, 0x2, 0x93,
       0x95, 0x5, 0x20, 0x11, 0x2, 0x94, 0x8f, 0x3, 0x2, 0x2, 0x2, 0x95,
       0x98, 0x3, 0x2, 0x2, 0x2, 0x96, 0x97, 0x3, 0x2, 0x2, 0x2, 0x96, 0x94,
       0x3, 0x2, 0x2, 0x2, 0x97, 0x9a, 0x3, 0x2, 0x2, 0x2, 0x98, 0x96, 0x3,
       0x2, 0x2, 0x2, 0x99, 0x9b, 0x7, 0xd, 0x2, 0x2, 0x9a, 0x99, 0x3, 0x2,
       0x2, 0x2, 0x9a, 0x9b, 0x3, 0x2, 0x2, 0x2, 0x9b, 0x9d, 0x3, 0x2, 0x2,
       0x2, 0x9c, 0x9e, 0x5, 0x26, 0x14, 0x2, 0x9d, 0x9c, 0x3, 0x2, 0x2,
       0x2, 0x9d, 0x9e, 0x3, 0x2, 0x2, 0x2, 0x9e, 0x9f, 0x3, 0x2, 0x2, 0x2,
       0x9f, 0xa0, 0x7, 0x8, 0x2, 0x2, 0xa0, 0x1f, 0x3, 0x2, 0x2, 0x2, 0xa1,
       0xa4, 0x5, 0x22, 0x12, 0x2, 0xa2, 0xa4, 0x5, 0x24, 0x13, 0x2, 0xa3,
       0xa1, 0x3, 0x2, 0x2, 0x2, 0xa3, 0xa2, 0x3, 0x2, 0x2, 0x2, 0xa4, 0x21,
       0x3, 0x2, 0x2, 0x2, 0xa5, 0xa7, 0x7, 0xf, 0x2, 0x2, 0xa6, 0xa8, 0x7,
       0xe, 0x2, 0x2, 0xa7, 0xa6, 0x3, 0x2, 0x2, 0x2, 0xa7, 0xa8, 0x3, 0x2,
       0x2, 0x2, 0xa8, 0xa9, 0x3, 0x2, 0x2, 0x2, 0xa9, 0xab, 0x7, 0xa, 0x2,
       0x2, 0xaa, 0xac, 0x7, 0xe, 0x2, 0x2, 0xab, 0xaa, 0x3, 0x2, 0x2, 0x2,
       0xab, 0xac, 0x3, 0x2, 0x2, 0x2, 0xac, 0xad, 0x3, 0x2, 0x2, 0x2, 0xad,
       0xae, 0x5, 0xc, 0x7, 0x2, 0xae, 0x23, 0x3, 0x2, 0x2, 0x2, 0xaf, 0xb0,
       0x5, 0xc, 0x7, 0x2, 0xb0, 0x25, 0x3, 0x2, 0x2, 0x2, 0xb1, 0xb3, 0x9,
       0x3, 0x2, 0x2, 0xb2, 0xb1, 0x3, 0x2, 0x2, 0x2, 0xb3, 0xb4, 0x3, 0x2,
       0x2, 0x2, 0xb4, 0xb2, 0x3, 0x2, 0x2, 0x2, 0xb4, 0xb5, 0x3, 0x2, 0x2,
       0x2, 0xb5, 0x27, 0x3, 0x2, 0x2, 0x2, 0x1a, 0x2c, 0x36, 0x40, 0x42,
       0x47, 0x49, 0x51, 0x59, 0x5b, 0x73, 0x77, 0x7b, 0x80, 0x85, 0x88,
       0x8c, 0x91, 0x96, 0x9a, 0x9d, 0xa3, 0xa7, 0xab, 0xb4,
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
