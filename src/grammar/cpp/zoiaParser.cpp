
// Generated from grammar/zoia.g4 by ANTLR 4.10.1


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

std::once_flag zoiaParserOnceFlag;
ZoiaParserStaticData *zoiaParserStaticData = nullptr;

void zoiaParserInitialize() {
  assert(zoiaParserStaticData == nullptr);
  auto staticData = std::make_unique<ZoiaParserStaticData>(
    std::vector<std::string>{
      "zoiaFile", "header", "line", "lineElements", "lineElementsInner",
      "lineElementsArg", "em3LineElement", "em2LineElement", "em1LineElement",
      "textFragment", "textFragmentReq", "textFragmentWord", "alias", "command",
      "arguments", "argument", "kwdArgument", "stdArgument", "whitespace"
    },
    std::vector<std::string>{
      "", "", "'*'", "'@'", "'\\'", "'|'", "']'", "'['", "'='", "'\\header'",
      "", "';'"
    },
    std::vector<std::string>{
      "", "COMMENT", "Asterisk", "At", "Backslash", "Bar", "BracketsClose",
      "BracketsOpen", "Equals", "Header", "Newline", "Semicolon", "Spaces",
      "Word"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,13,181,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,
  	7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,2,14,7,
  	14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,1,0,5,0,41,8,0,10,0,12,
  	0,44,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,2,3,2,53,8,2,1,2,1,2,1,3,1,3,1,3,1,
  	3,1,3,1,3,4,3,63,8,3,11,3,12,3,64,1,4,1,4,1,4,4,4,70,8,4,11,4,12,4,71,
  	1,5,1,5,1,5,1,5,1,5,1,5,3,5,80,8,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,88,8,5,
  	10,5,12,5,91,9,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,
  	1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,10,3,10,114,8,10,1,10,1,10,3,10,118,8,10,
  	1,11,1,11,3,11,122,8,11,1,12,1,12,1,12,3,12,127,8,12,1,13,1,13,1,13,3,
  	13,132,8,13,1,13,3,13,135,8,13,1,14,1,14,3,14,139,8,14,1,14,1,14,1,14,
  	3,14,144,8,14,1,14,5,14,147,8,14,10,14,12,14,150,9,14,1,14,3,14,153,8,
  	14,1,14,3,14,156,8,14,1,14,1,14,1,15,1,15,3,15,162,8,15,1,16,1,16,3,16,
  	166,8,16,1,16,1,16,3,16,170,8,16,1,16,1,16,1,17,1,17,1,18,4,18,177,8,
  	18,11,18,12,18,178,1,18,1,148,0,19,0,2,4,6,8,10,12,14,16,18,20,22,24,
  	26,28,30,32,34,36,0,3,1,0,12,13,2,0,4,4,13,13,2,0,10,10,12,12,198,0,38,
  	1,0,0,0,2,47,1,0,0,0,4,52,1,0,0,0,6,62,1,0,0,0,8,69,1,0,0,0,10,79,1,0,
  	0,0,12,92,1,0,0,0,14,100,1,0,0,0,16,106,1,0,0,0,18,110,1,0,0,0,20,113,
  	1,0,0,0,22,119,1,0,0,0,24,123,1,0,0,0,26,128,1,0,0,0,28,136,1,0,0,0,30,
  	161,1,0,0,0,32,163,1,0,0,0,34,173,1,0,0,0,36,176,1,0,0,0,38,42,3,2,1,
  	0,39,41,3,4,2,0,40,39,1,0,0,0,41,44,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,
  	0,43,45,1,0,0,0,44,42,1,0,0,0,45,46,5,0,0,1,46,1,1,0,0,0,47,48,5,9,0,
  	0,48,49,3,28,14,0,49,50,5,10,0,0,50,3,1,0,0,0,51,53,3,6,3,0,52,51,1,0,
  	0,0,52,53,1,0,0,0,53,54,1,0,0,0,54,55,5,10,0,0,55,5,1,0,0,0,56,63,3,18,
  	9,0,57,63,3,24,12,0,58,63,3,26,13,0,59,63,3,16,8,0,60,63,3,14,7,0,61,
  	63,3,12,6,0,62,56,1,0,0,0,62,57,1,0,0,0,62,58,1,0,0,0,62,59,1,0,0,0,62,
  	60,1,0,0,0,62,61,1,0,0,0,63,64,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,
  	7,1,0,0,0,66,70,3,20,10,0,67,70,3,24,12,0,68,70,3,26,13,0,69,66,1,0,0,
  	0,69,67,1,0,0,0,69,68,1,0,0,0,70,71,1,0,0,0,71,69,1,0,0,0,71,72,1,0,0,
  	0,72,9,1,0,0,0,73,80,3,22,11,0,74,80,3,24,12,0,75,80,3,26,13,0,76,80,
  	3,16,8,0,77,80,3,14,7,0,78,80,3,12,6,0,79,73,1,0,0,0,79,74,1,0,0,0,79,
  	75,1,0,0,0,79,76,1,0,0,0,79,77,1,0,0,0,79,78,1,0,0,0,80,89,1,0,0,0,81,
  	88,3,18,9,0,82,88,3,24,12,0,83,88,3,26,13,0,84,88,3,16,8,0,85,88,3,14,
  	7,0,86,88,3,12,6,0,87,81,1,0,0,0,87,82,1,0,0,0,87,83,1,0,0,0,87,84,1,
  	0,0,0,87,85,1,0,0,0,87,86,1,0,0,0,88,91,1,0,0,0,89,87,1,0,0,0,89,90,1,
  	0,0,0,90,11,1,0,0,0,91,89,1,0,0,0,92,93,5,2,0,0,93,94,5,2,0,0,94,95,5,
  	2,0,0,95,96,3,8,4,0,96,97,5,2,0,0,97,98,5,2,0,0,98,99,5,2,0,0,99,13,1,
  	0,0,0,100,101,5,2,0,0,101,102,5,2,0,0,102,103,3,8,4,0,103,104,5,2,0,0,
  	104,105,5,2,0,0,105,15,1,0,0,0,106,107,5,2,0,0,107,108,3,8,4,0,108,109,
  	5,2,0,0,109,17,1,0,0,0,110,111,7,0,0,0,111,19,1,0,0,0,112,114,5,12,0,
  	0,113,112,1,0,0,0,113,114,1,0,0,0,114,115,1,0,0,0,115,117,5,13,0,0,116,
  	118,5,12,0,0,117,116,1,0,0,0,117,118,1,0,0,0,118,21,1,0,0,0,119,121,5,
  	13,0,0,120,122,5,12,0,0,121,120,1,0,0,0,121,122,1,0,0,0,122,23,1,0,0,
  	0,123,124,5,3,0,0,124,126,5,13,0,0,125,127,5,5,0,0,126,125,1,0,0,0,126,
  	127,1,0,0,0,127,25,1,0,0,0,128,129,5,4,0,0,129,131,7,1,0,0,130,132,3,
  	28,14,0,131,130,1,0,0,0,131,132,1,0,0,0,132,134,1,0,0,0,133,135,5,5,0,
  	0,134,133,1,0,0,0,134,135,1,0,0,0,135,27,1,0,0,0,136,138,5,7,0,0,137,
  	139,3,36,18,0,138,137,1,0,0,0,138,139,1,0,0,0,139,140,1,0,0,0,140,148,
  	3,30,15,0,141,143,5,11,0,0,142,144,3,36,18,0,143,142,1,0,0,0,143,144,
  	1,0,0,0,144,145,1,0,0,0,145,147,3,30,15,0,146,141,1,0,0,0,147,150,1,0,
  	0,0,148,149,1,0,0,0,148,146,1,0,0,0,149,152,1,0,0,0,150,148,1,0,0,0,151,
  	153,5,11,0,0,152,151,1,0,0,0,152,153,1,0,0,0,153,155,1,0,0,0,154,156,
  	3,36,18,0,155,154,1,0,0,0,155,156,1,0,0,0,156,157,1,0,0,0,157,158,5,6,
  	0,0,158,29,1,0,0,0,159,162,3,32,16,0,160,162,3,34,17,0,161,159,1,0,0,
  	0,161,160,1,0,0,0,162,31,1,0,0,0,163,165,5,13,0,0,164,166,5,12,0,0,165,
  	164,1,0,0,0,165,166,1,0,0,0,166,167,1,0,0,0,167,169,5,8,0,0,168,170,5,
  	12,0,0,169,168,1,0,0,0,169,170,1,0,0,0,170,171,1,0,0,0,171,172,3,10,5,
  	0,172,33,1,0,0,0,173,174,3,10,5,0,174,35,1,0,0,0,175,177,7,2,0,0,176,
  	175,1,0,0,0,177,178,1,0,0,0,178,176,1,0,0,0,178,179,1,0,0,0,179,37,1,
  	0,0,0,24,42,52,62,64,69,71,79,87,89,113,117,121,126,131,134,138,143,148,
  	152,155,161,165,169,178
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


std::any zoiaParser::TextFragmentReqContext::accept(tree::ParseTreeVisitor *visitor) {
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


std::any zoiaParser::TextFragmentWordContext::accept(tree::ParseTreeVisitor *visitor) {
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


std::any zoiaParser::AliasContext::accept(tree::ParseTreeVisitor *visitor) {
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
    _la = _input->LA(1);
    if (!(_la == zoiaParser::Backslash

    || _la == zoiaParser::Word)) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
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


std::any zoiaParser::ArgumentsContext::accept(tree::ParseTreeVisitor *visitor) {
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


std::any zoiaParser::ArgumentContext::accept(tree::ParseTreeVisitor *visitor) {
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


std::any zoiaParser::KwdArgumentContext::accept(tree::ParseTreeVisitor *visitor) {
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


std::any zoiaParser::StdArgumentContext::accept(tree::ParseTreeVisitor *visitor) {
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


std::any zoiaParser::WhitespaceContext::accept(tree::ParseTreeVisitor *visitor) {
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

void zoiaParser::initialize() {
  std::call_once(zoiaParserOnceFlag, zoiaParserInitialize);
}
