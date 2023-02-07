
// Generated from grammar/zoia.g4 by ANTLR 4.11.1


#include "zoiaVisitor.h"

#include "zoiaParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct ZoiaParserStaticData final {
  ZoiaParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  ZoiaParserStaticData(const ZoiaParserStaticData&) = delete;
  ZoiaParserStaticData(ZoiaParserStaticData&&) = delete;
  ZoiaParserStaticData& operator=(const ZoiaParserStaticData&) = delete;
  ZoiaParserStaticData& operator=(ZoiaParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag zoiaParserOnceFlag;
ZoiaParserStaticData *zoiaParserStaticData = nullptr;

void zoiaParserInitialize() {
  assert(zoiaParserStaticData == nullptr);
  auto staticData = std::make_unique<ZoiaParserStaticData>(
    std::vector<std::string>{
      "zoiaFile", "header", "line", "lineElements", "lineElementsInner",
      "lineElementsArg", "em3LineElement", "em2LineElement", "em1LineElement",
      "textFragment", "textFragmentWord", "alias", "command", "arguments",
      "argument", "kwdArgument", "stdArgument", "whitespace"
    },
    std::vector<std::string>{
      "", "", "'*'", "'\\'", "'|'", "']'", "'['", "'='", "'\\header'", "",
      "';'"
    },
    std::vector<std::string>{
      "", "COMMENT", "Asterisk", "Backslash", "Bar", "BracketsClose", "BracketsOpen",
      "Equals", "Header", "Newline", "Semicolon", "Spaces", "Alias", "Word"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,13,175,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,
  	7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,2,14,7,
  	14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,1,0,5,0,39,8,0,10,0,12,0,42,9,0,
  	1,0,1,0,1,1,1,1,1,1,1,1,1,2,3,2,51,8,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,
  	3,4,3,61,8,3,11,3,12,3,62,1,4,1,4,1,4,3,4,68,8,4,1,4,1,4,1,4,5,4,73,8,
  	4,10,4,12,4,76,9,4,1,5,1,5,1,5,1,5,1,5,1,5,3,5,84,8,5,1,5,1,5,1,5,1,5,
  	1,5,1,5,5,5,92,8,5,10,5,12,5,95,9,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
  	7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,3,11,
  	121,8,11,1,12,1,12,1,12,3,12,126,8,12,1,12,3,12,129,8,12,1,13,1,13,3,
  	13,133,8,13,1,13,1,13,1,13,3,13,138,8,13,1,13,5,13,141,8,13,10,13,12,
  	13,144,9,13,1,13,3,13,147,8,13,1,13,3,13,150,8,13,1,13,1,13,1,14,1,14,
  	3,14,156,8,14,1,15,1,15,3,15,160,8,15,1,15,1,15,3,15,164,8,15,1,15,1,
  	15,1,16,1,16,1,17,4,17,171,8,17,11,17,12,17,172,1,17,1,142,0,18,0,2,4,
  	6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,0,3,2,0,11,11,13,13,2,0,3,
  	3,13,13,2,0,9,9,11,11,192,0,36,1,0,0,0,2,45,1,0,0,0,4,50,1,0,0,0,6,60,
  	1,0,0,0,8,67,1,0,0,0,10,83,1,0,0,0,12,96,1,0,0,0,14,104,1,0,0,0,16,110,
  	1,0,0,0,18,114,1,0,0,0,20,116,1,0,0,0,22,118,1,0,0,0,24,122,1,0,0,0,26,
  	130,1,0,0,0,28,155,1,0,0,0,30,157,1,0,0,0,32,167,1,0,0,0,34,170,1,0,0,
  	0,36,40,3,2,1,0,37,39,3,4,2,0,38,37,1,0,0,0,39,42,1,0,0,0,40,38,1,0,0,
  	0,40,41,1,0,0,0,41,43,1,0,0,0,42,40,1,0,0,0,43,44,5,0,0,1,44,1,1,0,0,
  	0,45,46,5,8,0,0,46,47,3,26,13,0,47,48,5,9,0,0,48,3,1,0,0,0,49,51,3,6,
  	3,0,50,49,1,0,0,0,50,51,1,0,0,0,51,52,1,0,0,0,52,53,5,9,0,0,53,5,1,0,
  	0,0,54,61,3,18,9,0,55,61,3,22,11,0,56,61,3,24,12,0,57,61,3,16,8,0,58,
  	61,3,14,7,0,59,61,3,12,6,0,60,54,1,0,0,0,60,55,1,0,0,0,60,56,1,0,0,0,
  	60,57,1,0,0,0,60,58,1,0,0,0,60,59,1,0,0,0,61,62,1,0,0,0,62,60,1,0,0,0,
  	62,63,1,0,0,0,63,7,1,0,0,0,64,68,3,20,10,0,65,68,3,22,11,0,66,68,3,24,
  	12,0,67,64,1,0,0,0,67,65,1,0,0,0,67,66,1,0,0,0,68,74,1,0,0,0,69,73,3,
  	18,9,0,70,73,3,22,11,0,71,73,3,24,12,0,72,69,1,0,0,0,72,70,1,0,0,0,72,
  	71,1,0,0,0,73,76,1,0,0,0,74,72,1,0,0,0,74,75,1,0,0,0,75,9,1,0,0,0,76,
  	74,1,0,0,0,77,84,3,20,10,0,78,84,3,22,11,0,79,84,3,24,12,0,80,84,3,16,
  	8,0,81,84,3,14,7,0,82,84,3,12,6,0,83,77,1,0,0,0,83,78,1,0,0,0,83,79,1,
  	0,0,0,83,80,1,0,0,0,83,81,1,0,0,0,83,82,1,0,0,0,84,93,1,0,0,0,85,92,3,
  	18,9,0,86,92,3,22,11,0,87,92,3,24,12,0,88,92,3,16,8,0,89,92,3,14,7,0,
  	90,92,3,12,6,0,91,85,1,0,0,0,91,86,1,0,0,0,91,87,1,0,0,0,91,88,1,0,0,
  	0,91,89,1,0,0,0,91,90,1,0,0,0,92,95,1,0,0,0,93,91,1,0,0,0,93,94,1,0,0,
  	0,94,11,1,0,0,0,95,93,1,0,0,0,96,97,5,2,0,0,97,98,5,2,0,0,98,99,5,2,0,
  	0,99,100,3,8,4,0,100,101,5,2,0,0,101,102,5,2,0,0,102,103,5,2,0,0,103,
  	13,1,0,0,0,104,105,5,2,0,0,105,106,5,2,0,0,106,107,3,8,4,0,107,108,5,
  	2,0,0,108,109,5,2,0,0,109,15,1,0,0,0,110,111,5,2,0,0,111,112,3,8,4,0,
  	112,113,5,2,0,0,113,17,1,0,0,0,114,115,7,0,0,0,115,19,1,0,0,0,116,117,
  	5,13,0,0,117,21,1,0,0,0,118,120,5,12,0,0,119,121,5,4,0,0,120,119,1,0,
  	0,0,120,121,1,0,0,0,121,23,1,0,0,0,122,123,5,3,0,0,123,125,7,1,0,0,124,
  	126,3,26,13,0,125,124,1,0,0,0,125,126,1,0,0,0,126,128,1,0,0,0,127,129,
  	5,4,0,0,128,127,1,0,0,0,128,129,1,0,0,0,129,25,1,0,0,0,130,132,5,6,0,
  	0,131,133,3,34,17,0,132,131,1,0,0,0,132,133,1,0,0,0,133,134,1,0,0,0,134,
  	142,3,28,14,0,135,137,5,10,0,0,136,138,3,34,17,0,137,136,1,0,0,0,137,
  	138,1,0,0,0,138,139,1,0,0,0,139,141,3,28,14,0,140,135,1,0,0,0,141,144,
  	1,0,0,0,142,143,1,0,0,0,142,140,1,0,0,0,143,146,1,0,0,0,144,142,1,0,0,
  	0,145,147,5,10,0,0,146,145,1,0,0,0,146,147,1,0,0,0,147,149,1,0,0,0,148,
  	150,3,34,17,0,149,148,1,0,0,0,149,150,1,0,0,0,150,151,1,0,0,0,151,152,
  	5,5,0,0,152,27,1,0,0,0,153,156,3,30,15,0,154,156,3,32,16,0,155,153,1,
  	0,0,0,155,154,1,0,0,0,156,29,1,0,0,0,157,159,5,13,0,0,158,160,5,11,0,
  	0,159,158,1,0,0,0,159,160,1,0,0,0,160,161,1,0,0,0,161,163,5,7,0,0,162,
  	164,5,11,0,0,163,162,1,0,0,0,163,164,1,0,0,0,164,165,1,0,0,0,165,166,
  	3,10,5,0,166,31,1,0,0,0,167,168,3,10,5,0,168,33,1,0,0,0,169,171,7,2,0,
  	0,170,169,1,0,0,0,171,172,1,0,0,0,172,170,1,0,0,0,172,173,1,0,0,0,173,
  	35,1,0,0,0,22,40,50,60,62,67,72,74,83,91,93,120,125,128,132,137,142,146,
  	149,155,159,163,172
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) {
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  zoiaParserStaticData = staticData.release();
}

}

zoiaParser::zoiaParser(TokenStream *input) : zoiaParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

zoiaParser::zoiaParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  zoiaParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *zoiaParserStaticData->atn, zoiaParserStaticData->decisionToDFA, zoiaParserStaticData->sharedContextCache, options);
}

zoiaParser::~zoiaParser() {
  delete _interpreter;
}

const atn::ATN& zoiaParser::getATN() const {
  return *zoiaParserStaticData->atn;
}

std::string zoiaParser::getGrammarFileName() const {
  return "zoia.g4";
}

const std::vector<std::string>& zoiaParser::getRuleNames() const {
  return zoiaParserStaticData->ruleNames;
}

const dfa::Vocabulary& zoiaParser::getVocabulary() const {
  return zoiaParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView zoiaParser::getSerializedATN() const {
  return zoiaParserStaticData->serializedATN;
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


std::any zoiaParser::ZoiaFileContext::accept(tree::ParseTreeVisitor *visitor) {
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
    setState(36);
    header();
    setState(40);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 14860) != 0) {
      setState(37);
      line();
      setState(42);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(43);
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


std::any zoiaParser::HeaderContext::accept(tree::ParseTreeVisitor *visitor) {
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
    setState(45);
    match(zoiaParser::Header);
    setState(46);
    arguments();
    setState(47);
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


std::any zoiaParser::LineContext::accept(tree::ParseTreeVisitor *visitor) {
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
    setState(50);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 14348) != 0) {
      setState(49);
      lineElements();
    }
    setState(52);
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


std::any zoiaParser::LineElementsContext::accept(tree::ParseTreeVisitor *visitor) {
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
    setState(60);
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(60);
      _errHandler->sync(this);
      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 2, _ctx)) {
      case 1: {
        setState(54);
        textFragment();
        break;
      }

      case 2: {
        setState(55);
        alias();
        break;
      }

      case 3: {
        setState(56);
        command();
        break;
      }

      case 4: {
        setState(57);
        em1LineElement();
        break;
      }

      case 5: {
        setState(58);
        em2LineElement();
        break;
      }

      case 6: {
        setState(59);
        em3LineElement();
        break;
      }

      default:
        break;
      }
      setState(62);
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 14348) != 0);

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

zoiaParser::TextFragmentWordContext* zoiaParser::LineElementsInnerContext::textFragmentWord() {
  return getRuleContext<zoiaParser::TextFragmentWordContext>(0);
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

std::vector<zoiaParser::TextFragmentContext *> zoiaParser::LineElementsInnerContext::textFragment() {
  return getRuleContexts<zoiaParser::TextFragmentContext>();
}

zoiaParser::TextFragmentContext* zoiaParser::LineElementsInnerContext::textFragment(size_t i) {
  return getRuleContext<zoiaParser::TextFragmentContext>(i);
}


size_t zoiaParser::LineElementsInnerContext::getRuleIndex() const {
  return zoiaParser::RuleLineElementsInner;
}


std::any zoiaParser::LineElementsInnerContext::accept(tree::ParseTreeVisitor *visitor) {
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
    setState(67);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case zoiaParser::Word: {
        setState(64);
        textFragmentWord();
        break;
      }

      case zoiaParser::Alias: {
        setState(65);
        alias();
        break;
      }

      case zoiaParser::Backslash: {
        setState(66);
        command();
        break;
      }

    default:
      throw NoViableAltException(this);
    }
    setState(74);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 14344) != 0) {
      setState(72);
      _errHandler->sync(this);
      switch (_input->LA(1)) {
        case zoiaParser::Spaces:
        case zoiaParser::Word: {
          setState(69);
          textFragment();
          break;
        }

        case zoiaParser::Alias: {
          setState(70);
          alias();
          break;
        }

        case zoiaParser::Backslash: {
          setState(71);
          command();
          break;
        }

      default:
        throw NoViableAltException(this);
      }
      setState(76);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }

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


std::any zoiaParser::LineElementsArgContext::accept(tree::ParseTreeVisitor *visitor) {
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
    setState(83);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 7, _ctx)) {
    case 1: {
      setState(77);
      textFragmentWord();
      break;
    }

    case 2: {
      setState(78);
      alias();
      break;
    }

    case 3: {
      setState(79);
      command();
      break;
    }

    case 4: {
      setState(80);
      em1LineElement();
      break;
    }

    case 5: {
      setState(81);
      em2LineElement();
      break;
    }

    case 6: {
      setState(82);
      em3LineElement();
      break;
    }

    default:
      break;
    }
    setState(93);
    _errHandler->sync(this);
    alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 9, _ctx);
    while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER) {
      if (alt == 1) {
        setState(91);
        _errHandler->sync(this);
        switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 8, _ctx)) {
        case 1: {
          setState(85);
          textFragment();
          break;
        }

        case 2: {
          setState(86);
          alias();
          break;
        }

        case 3: {
          setState(87);
          command();
          break;
        }

        case 4: {
          setState(88);
          em1LineElement();
          break;
        }

        case 5: {
          setState(89);
          em2LineElement();
          break;
        }

        case 6: {
          setState(90);
          em3LineElement();
          break;
        }

        default:
          break;
        }
      }
      setState(95);
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 9, _ctx);
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


std::any zoiaParser::Em3LineElementContext::accept(tree::ParseTreeVisitor *visitor) {
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
    setState(96);
    match(zoiaParser::Asterisk);
    setState(97);
    match(zoiaParser::Asterisk);
    setState(98);
    match(zoiaParser::Asterisk);
    setState(99);
    lineElementsInner();
    setState(100);
    match(zoiaParser::Asterisk);
    setState(101);
    match(zoiaParser::Asterisk);
    setState(102);
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


std::any zoiaParser::Em2LineElementContext::accept(tree::ParseTreeVisitor *visitor) {
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
    setState(104);
    match(zoiaParser::Asterisk);
    setState(105);
    match(zoiaParser::Asterisk);
    setState(106);
    lineElementsInner();
    setState(107);
    match(zoiaParser::Asterisk);
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


std::any zoiaParser::Em1LineElementContext::accept(tree::ParseTreeVisitor *visitor) {
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
    setState(110);
    match(zoiaParser::Asterisk);
    setState(111);
    lineElementsInner();
    setState(112);
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


std::any zoiaParser::TextFragmentContext::accept(tree::ParseTreeVisitor *visitor) {
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
    setState(114);
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

//----------------- TextFragmentWordContext ------------------------------------------------------------------

zoiaParser::TextFragmentWordContext::TextFragmentWordContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* zoiaParser::TextFragmentWordContext::Word() {
  return getToken(zoiaParser::Word, 0);
}


size_t zoiaParser::TextFragmentWordContext::getRuleIndex() const {
  return zoiaParser::RuleTextFragmentWord;
}


std::any zoiaParser::TextFragmentWordContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<zoiaVisitor*>(visitor))
    return parserVisitor->visitTextFragmentWord(this);
  else
    return visitor->visitChildren(this);
}

zoiaParser::TextFragmentWordContext* zoiaParser::textFragmentWord() {
  TextFragmentWordContext *_localctx = _tracker.createInstance<TextFragmentWordContext>(_ctx, getState());
  enterRule(_localctx, 20, zoiaParser::RuleTextFragmentWord);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(116);
    match(zoiaParser::Word);

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

tree::TerminalNode* zoiaParser::AliasContext::Alias() {
  return getToken(zoiaParser::Alias, 0);
}

tree::TerminalNode* zoiaParser::AliasContext::Bar() {
  return getToken(zoiaParser::Bar, 0);
}


size_t zoiaParser::AliasContext::getRuleIndex() const {
  return zoiaParser::RuleAlias;
}


std::any zoiaParser::AliasContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<zoiaVisitor*>(visitor))
    return parserVisitor->visitAlias(this);
  else
    return visitor->visitChildren(this);
}

zoiaParser::AliasContext* zoiaParser::alias() {
  AliasContext *_localctx = _tracker.createInstance<AliasContext>(_ctx, getState());
  enterRule(_localctx, 22, zoiaParser::RuleAlias);
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
    setState(118);
    match(zoiaParser::Alias);
    setState(120);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == zoiaParser::Bar) {
      setState(119);
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

std::vector<tree::TerminalNode *> zoiaParser::CommandContext::Backslash() {
  return getTokens(zoiaParser::Backslash);
}

tree::TerminalNode* zoiaParser::CommandContext::Backslash(size_t i) {
  return getToken(zoiaParser::Backslash, i);
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


std::any zoiaParser::CommandContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<zoiaVisitor*>(visitor))
    return parserVisitor->visitCommand(this);
  else
    return visitor->visitChildren(this);
}

zoiaParser::CommandContext* zoiaParser::command() {
  CommandContext *_localctx = _tracker.createInstance<CommandContext>(_ctx, getState());
  enterRule(_localctx, 24, zoiaParser::RuleCommand);
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
    setState(122);
    match(zoiaParser::Backslash);
    setState(123);
    _la = _input->LA(1);
    if (!(_la == zoiaParser::Backslash

    || _la == zoiaParser::Word)) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(125);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == zoiaParser::BracketsOpen) {
      setState(124);
      arguments();
    }
    setState(128);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == zoiaParser::Bar) {
      setState(127);
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


std::any zoiaParser::ArgumentsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<zoiaVisitor*>(visitor))
    return parserVisitor->visitArguments(this);
  else
    return visitor->visitChildren(this);
}

zoiaParser::ArgumentsContext* zoiaParser::arguments() {
  ArgumentsContext *_localctx = _tracker.createInstance<ArgumentsContext>(_ctx, getState());
  enterRule(_localctx, 26, zoiaParser::RuleArguments);
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
    setState(130);
    match(zoiaParser::BracketsOpen);
    setState(132);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == zoiaParser::Newline

    || _la == zoiaParser::Spaces) {
      setState(131);
      whitespace();
    }
    setState(134);
    argument();
    setState(142);
    _errHandler->sync(this);
    alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 15, _ctx);
    while (alt != 1 && alt != atn::ATN::INVALID_ALT_NUMBER) {
      if (alt == 1 + 1) {
        setState(135);
        match(zoiaParser::Semicolon);
        setState(137);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == zoiaParser::Newline

        || _la == zoiaParser::Spaces) {
          setState(136);
          whitespace();
        }
        setState(139);
        argument();
      }
      setState(144);
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 15, _ctx);
    }
    setState(146);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == zoiaParser::Semicolon) {
      setState(145);
      match(zoiaParser::Semicolon);
    }
    setState(149);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == zoiaParser::Newline

    || _la == zoiaParser::Spaces) {
      setState(148);
      whitespace();
    }
    setState(151);
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


std::any zoiaParser::ArgumentContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<zoiaVisitor*>(visitor))
    return parserVisitor->visitArgument(this);
  else
    return visitor->visitChildren(this);
}

zoiaParser::ArgumentContext* zoiaParser::argument() {
  ArgumentContext *_localctx = _tracker.createInstance<ArgumentContext>(_ctx, getState());
  enterRule(_localctx, 28, zoiaParser::RuleArgument);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(155);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 18, _ctx)) {
    case 1: {
      enterOuterAlt(_localctx, 1);
      setState(153);
      kwdArgument();
      break;
    }

    case 2: {
      enterOuterAlt(_localctx, 2);
      setState(154);
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


std::any zoiaParser::KwdArgumentContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<zoiaVisitor*>(visitor))
    return parserVisitor->visitKwdArgument(this);
  else
    return visitor->visitChildren(this);
}

zoiaParser::KwdArgumentContext* zoiaParser::kwdArgument() {
  KwdArgumentContext *_localctx = _tracker.createInstance<KwdArgumentContext>(_ctx, getState());
  enterRule(_localctx, 30, zoiaParser::RuleKwdArgument);
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
    setState(157);
    match(zoiaParser::Word);
    setState(159);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == zoiaParser::Spaces) {
      setState(158);
      match(zoiaParser::Spaces);
    }
    setState(161);
    match(zoiaParser::Equals);
    setState(163);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == zoiaParser::Spaces) {
      setState(162);
      match(zoiaParser::Spaces);
    }
    setState(165);
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


std::any zoiaParser::StdArgumentContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<zoiaVisitor*>(visitor))
    return parserVisitor->visitStdArgument(this);
  else
    return visitor->visitChildren(this);
}

zoiaParser::StdArgumentContext* zoiaParser::stdArgument() {
  StdArgumentContext *_localctx = _tracker.createInstance<StdArgumentContext>(_ctx, getState());
  enterRule(_localctx, 32, zoiaParser::RuleStdArgument);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(167);
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


std::any zoiaParser::WhitespaceContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<zoiaVisitor*>(visitor))
    return parserVisitor->visitWhitespace(this);
  else
    return visitor->visitChildren(this);
}

zoiaParser::WhitespaceContext* zoiaParser::whitespace() {
  WhitespaceContext *_localctx = _tracker.createInstance<WhitespaceContext>(_ctx, getState());
  enterRule(_localctx, 34, zoiaParser::RuleWhitespace);
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
    setState(170);
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(169);
      _la = _input->LA(1);
      if (!(_la == zoiaParser::Newline

      || _la == zoiaParser::Spaces)) {
      _errHandler->recoverInline(this);
      }
      else {
        _errHandler->reportMatch(this);
        consume();
      }
      setState(172);
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

void zoiaParser::initialize() {
  ::antlr4::internal::call_once(zoiaParserOnceFlag, zoiaParserInitialize);
}
