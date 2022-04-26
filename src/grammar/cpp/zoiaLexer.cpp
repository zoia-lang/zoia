
// Generated from grammar/zoia.g4 by ANTLR 4.10.1


#include "zoiaLexer.h"


using namespace antlr4;



using namespace antlr4;

namespace {

struct ZoiaLexerStaticData final {
  ZoiaLexerStaticData(std::vector<std::string> ruleNames,
                          std::vector<std::string> channelNames,
                          std::vector<std::string> modeNames,
                          std::vector<std::string> literalNames,
                          std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), channelNames(std::move(channelNames)),
        modeNames(std::move(modeNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  ZoiaLexerStaticData(const ZoiaLexerStaticData&) = delete;
  ZoiaLexerStaticData(ZoiaLexerStaticData&&) = delete;
  ZoiaLexerStaticData& operator=(const ZoiaLexerStaticData&) = delete;
  ZoiaLexerStaticData& operator=(ZoiaLexerStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> channelNames;
  const std::vector<std::string> modeNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

std::once_flag zoialexerLexerOnceFlag;
ZoiaLexerStaticData *zoialexerLexerStaticData = nullptr;

void zoialexerLexerInitialize() {
  assert(zoialexerLexerStaticData == nullptr);
  auto staticData = std::make_unique<ZoiaLexerStaticData>(
    std::vector<std::string>{
      "COMMENT", "Asterisk", "At", "Backslash", "Bar", "BracketsClose",
      "BracketsOpen", "Equals", "Header", "Newline", "Semicolon", "Spaces",
      "Word"
    },
    std::vector<std::string>{
      "DEFAULT_TOKEN_CHANNEL", "HIDDEN"
    },
    std::vector<std::string>{
      "DEFAULT_MODE"
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
  	4,0,13,75,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
  	6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,5,0,30,
  	8,0,10,0,12,0,33,9,0,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,
  	1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,3,9,62,8,
  	9,1,10,1,10,1,11,4,11,67,8,11,11,11,12,11,68,1,12,4,12,72,8,12,11,12,
  	12,12,73,0,0,13,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,
  	12,25,13,1,0,3,2,0,10,10,13,13,8,0,32,32,160,160,5760,5760,8192,8202,
  	8232,8233,8239,8239,8287,8287,12288,12288,17,0,10,10,13,13,32,32,35,35,
  	42,42,59,59,61,61,64,64,91,93,124,124,160,160,5760,5760,8192,8202,8232,
  	8233,8239,8239,8287,8287,12288,12288,78,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,
  	0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,
  	0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,1,27,
  	1,0,0,0,3,36,1,0,0,0,5,38,1,0,0,0,7,40,1,0,0,0,9,42,1,0,0,0,11,44,1,0,
  	0,0,13,46,1,0,0,0,15,48,1,0,0,0,17,50,1,0,0,0,19,61,1,0,0,0,21,63,1,0,
  	0,0,23,66,1,0,0,0,25,71,1,0,0,0,27,31,5,35,0,0,28,30,8,0,0,0,29,28,1,
  	0,0,0,30,33,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,34,1,0,0,0,33,31,1,
  	0,0,0,34,35,6,0,0,0,35,2,1,0,0,0,36,37,5,42,0,0,37,4,1,0,0,0,38,39,5,
  	64,0,0,39,6,1,0,0,0,40,41,5,92,0,0,41,8,1,0,0,0,42,43,5,124,0,0,43,10,
  	1,0,0,0,44,45,5,93,0,0,45,12,1,0,0,0,46,47,5,91,0,0,47,14,1,0,0,0,48,
  	49,5,61,0,0,49,16,1,0,0,0,50,51,5,92,0,0,51,52,5,104,0,0,52,53,5,101,
  	0,0,53,54,5,97,0,0,54,55,5,100,0,0,55,56,5,101,0,0,56,57,5,114,0,0,57,
  	18,1,0,0,0,58,59,5,13,0,0,59,62,5,10,0,0,60,62,7,0,0,0,61,58,1,0,0,0,
  	61,60,1,0,0,0,62,20,1,0,0,0,63,64,5,59,0,0,64,22,1,0,0,0,65,67,7,1,0,
  	0,66,65,1,0,0,0,67,68,1,0,0,0,68,66,1,0,0,0,68,69,1,0,0,0,69,24,1,0,0,
  	0,70,72,8,2,0,0,71,70,1,0,0,0,72,73,1,0,0,0,73,71,1,0,0,0,73,74,1,0,0,
  	0,74,26,1,0,0,0,5,0,31,61,68,73,1,6,0,0
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) {
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  zoialexerLexerStaticData = staticData.release();
}

}

zoiaLexer::zoiaLexer(CharStream *input) : Lexer(input) {
  zoiaLexer::initialize();
  _interpreter = new atn::LexerATNSimulator(this, *zoialexerLexerStaticData->atn, zoialexerLexerStaticData->decisionToDFA, zoialexerLexerStaticData->sharedContextCache);
}

zoiaLexer::~zoiaLexer() {
  delete _interpreter;
}

std::string zoiaLexer::getGrammarFileName() const {
  return "zoia.g4";
}

const std::vector<std::string>& zoiaLexer::getRuleNames() const {
  return zoialexerLexerStaticData->ruleNames;
}

const std::vector<std::string>& zoiaLexer::getChannelNames() const {
  return zoialexerLexerStaticData->channelNames;
}

const std::vector<std::string>& zoiaLexer::getModeNames() const {
  return zoialexerLexerStaticData->modeNames;
}

const dfa::Vocabulary& zoiaLexer::getVocabulary() const {
  return zoialexerLexerStaticData->vocabulary;
}

antlr4::atn::SerializedATNView zoiaLexer::getSerializedATN() const {
  return zoialexerLexerStaticData->serializedATN;
}

const atn::ATN& zoiaLexer::getATN() const {
  return *zoialexerLexerStaticData->atn;
}




void zoiaLexer::initialize() {
  std::call_once(zoialexerLexerOnceFlag, zoialexerLexerInitialize);
}
